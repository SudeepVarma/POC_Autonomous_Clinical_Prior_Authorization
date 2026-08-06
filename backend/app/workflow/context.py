"""
WorkflowContext is the central shared data object passed through workflow stages,
tracking execution metadata, state, processed documents, and errors.

Created on: 2026-08-05
Author: Sudeep Varma K
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any
from uuid import uuid4

from app.models.clinical import (
    PriorAuthorizationRequest,
    PriorAuthorizationResult,
)
from app.models.document import Document
from app.workflow.state import WorkflowState
from app.healing.models import FailureReport


@dataclass
class WorkflowContext:
    trace_id: str = field(default_factory=lambda: str(uuid4()))

    state: WorkflowState = WorkflowState.RECEIVED

    document: Document | None = None

    extraction: PriorAuthorizationRequest | None = None

    decision: PriorAuthorizationResult | None = None

    metadata: dict[str, Any] = field(default_factory=dict)

    errors: list[str] = field(default_factory=list)

    events: list[str] = field(default_factory=list)

    requires_human_review: bool = False

    retry_count: int = 0

    review_reason: str | None = None

    def add_event(self, event: str) -> None:
        self.events.append(event)

    def add_error(self, error: str) -> None:
        self.errors.append(error)

        self.failure = FailureReport(
            component=self.state.value,
            error=error,
            trace_id=self.trace_id,
        )

        self.state = WorkflowState.FAILED