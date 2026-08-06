"""
A workflow agent that uses a policy engine to evaluate extracted document data, updating the workflow state and recording a governance decision or error.

Created on: 2026-08-05
Author: Sudeep Varma K
"""

from __future__ import annotations
from app.agents.base import BaseAgent
from app.governance.policy import PolicyEngine
from app.workflow.context import WorkflowContext
from app.workflow.state import WorkflowState


class GovernanceAgent(BaseAgent):

    name = "governance"

    def __init__(self) -> None:

        self.policy = PolicyEngine()

    def run(
        self,
        context: WorkflowContext,
    ) -> WorkflowContext:

        if context.extraction is None:

            context.add_error(
                "Nothing to evaluate."
            )

            return context

        context.state = WorkflowState.GOVERNANCE

        try:

            context.decision = self.policy.evaluate(
                context.extraction
            )

            context.add_event(
                "governance_completed"
            )

        except Exception as exc:

            context.add_error(str(exc))

            return context

        return context