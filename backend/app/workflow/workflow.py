"""
Central logic for registering and running agents.

Created on: 2026-08-05
Author: Sudeep Varma K
"""

from app.workflow.context import WorkflowContext
from app.workflow.state import WorkflowState
from app.healing import healing_service


class Workflow:
    """
    Coordinates the execution of registered agents.
    """

    def __init__(self) -> None:
        self._agents = []

    def register(self, agent) -> None:
        self._agents.append(agent)

    def run(self, context: WorkflowContext) -> WorkflowContext:
        for agent in self._agents:

            context = agent.run(context)

            if context.state == WorkflowState.FAILED:
                return context

            if context.requires_human_review:
                return context

        context.state = WorkflowState.COMPLETED
        return context
