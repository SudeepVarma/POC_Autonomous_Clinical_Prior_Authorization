"""
Evaluates governance policies for clinical prior authorization requests using OPA (Open Policy Agent) and provides local fallback if OPA is unavailable.

Created on: 2026-08-05
Author: Sudeep Varma K
"""

from __future__ import annotations
from app.models.clinical import (
    PriorAuthorizationRequest,
    PriorAuthorizationResult,
)
from app.tools.opa import OPATool


class PolicyEngine:
    """
    Applies governance rules using OPA.

    Falls back to a simple local decision if OPA
    is unavailable.
    """

    def __init__(self) -> None:

        self.opa = OPATool()

    def evaluate(
            self,
            request: PriorAuthorizationRequest,
    ) -> PriorAuthorizationResult:

        if request.estimated_cost is None:
            return PriorAuthorizationResult(
                approved=False,
                decision="HUMAN_REVIEW",
                confidence=1.0,
                reasons=[
                    "Estimated cost is missing."
                ],
                extracted_request=request,
            )


        try:

            result = self.opa.evaluate(request)

            decision = result.get("decision", "ESCALATE")
            reasons = result.get("reasons", [])

        except Exception:

            if request.estimated_cost <= 5000:

                decision = "APPROVE"
                reasons = [
                    "OPA unavailable - local fallback"
                ]

            else:

                decision = "ESCALATE"
                reasons = [
                    "OPA unavailable - manual review"
                ]

        return PriorAuthorizationResult(
            approved=decision == "APPROVE",
            decision=decision,
            confidence=1.0,
            reasons=reasons,
            extracted_request=request,
        )