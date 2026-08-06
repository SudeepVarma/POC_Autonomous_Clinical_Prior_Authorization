"""
A base agent class for workflow agents.

Created on: 2026-08-05
Author: Sudeep Varma K
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from app.workflow.context import WorkflowContext


class BaseAgent(ABC):
    """
    Base class for all workflow agents.
    """

    name: str = "base"

    @abstractmethod
    def run(self, context: WorkflowContext) -> WorkflowContext:
        """
        Execute the agent.

        Args:
            context: Current workflow context.

        Returns:
            Updated workflow context.
        """
        raise NotImplementedError