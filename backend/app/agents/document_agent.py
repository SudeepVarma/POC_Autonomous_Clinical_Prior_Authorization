"""
DocumentAgent class that processes uploaded documents inside a workflow context, updating the workflow state and handling errors if a document is missing or fails to process.

Created on: 2026-08-05
Author: Sudeep Varma K
"""

from __future__ import annotations
from app.agents.base import BaseAgent
from app.document.service import DocumentService
from app.workflow.context import WorkflowContext
from app.workflow.state import WorkflowState

class DocumentAgent(BaseAgent):
    """
    Loads and prepares an uploaded document.
    """

    name = "document"

    def __init__(self) -> None:
        self.document_service = DocumentService()

    def run(self, context: WorkflowContext) -> WorkflowContext:

        if context.document is None:
            context.add_error("No document supplied.")
            return context

        try:
            context.document = self.document_service.process(
                context.document.path
            )

            context.state = WorkflowState.DOCUMENT_PROCESSED

            context.add_event("document_processed")

        except Exception as exc:
            context.add_error(str(exc))

        return context