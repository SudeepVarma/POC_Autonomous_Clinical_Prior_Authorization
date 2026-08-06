"""
A specialized workflow agent that validates and processes uploaded documents using a dedicated document service, updating the workflow state upon success or logging errors upon failure

Created on: 2026-08-05
Author: Sudeep Varma K
"""
from __future__ import annotations
from app.agents.base import BaseAgent
from app.tools.registry import tool_registry
from app.workflow.context import WorkflowContext
from app.workflow.state import WorkflowState


class ExtractionAgent(BaseAgent):
    """
    Uses the LLM to extract structured prior authorization
    information from the processed document.

    Performs one retry when extraction confidence is low.
    Escalates to human review if confidence remains low.
    """

    name = "extraction"

    MIN_CONFIDENCE = 0.80

    MAX_RETRIES = 1

    def __init__(self) -> None:
        self.llm = tool_registry.llm

    def run(self, context: WorkflowContext) -> WorkflowContext:

        if context.document is None:
            context.add_error("Document has not been processed.")
            return context

        context.state = WorkflowState.EXTRACTING

        while True:

            try:

                result = self.llm.extract_prior_authorization(
                    context.document.text
                )

                context.extraction = result

                # Extraction confidence is acceptable
                if result.confidence >= self.MIN_CONFIDENCE:

                    context.state = WorkflowState.EXTRACTION_COMPLETE

                    context.add_event(
                        f"clinical_information_extracted "
                        f"(confidence={result.confidence:.2f})"
                    )

                    return context

                # Retry once
                if context.retry_count < self.MAX_RETRIES:

                    context.retry_count += 1

                    context.add_event(
                        f"low_confidence_retry_{context.retry_count} "
                        f"(confidence={result.confidence:.2f})"
                    )

                    continue

                # Retry exhausted -> Human review
                context.requires_human_review = True
                context.review_reason = (
                    f"Low extraction confidence ({result.confidence:.2f}) "
                    f"after {context.retry_count} retry."
                )
                context.state = WorkflowState.HUMAN_REVIEW
                context.add_event("human_review_requested")

                return context

            except Exception as exc:

                context.add_error(str(exc))

                return context