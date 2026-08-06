"""
OPA Rest api wrapper.

Created on: 2026-08-05
Author: Sudeep Varma K
"""

from __future__ import annotations
import requests
from app.config import settings
from app.models.clinical import PriorAuthorizationRequest


class OPATool:
    """
    Thin wrapper around the OPA REST API.
    """

    def evaluate(
        self,
        request: PriorAuthorizationRequest,
    ) -> dict:

        payload = {
            "input": request.model_dump()
        }

        response = requests.post(
            settings.OPA_URL,
            json=payload,
            timeout=10,
        )

        response.raise_for_status()

        body = response.json()

        return body.get("result", {})