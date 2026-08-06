"""
PriorAuthorizationRequest represents the structured clinical information extracted from the uploaded document. It is produced by the ExtractionAgent and consumed by the GovernanceAgent.
PriorAuthorizationResult represents the result of a prior authorization request evaluation, including approval status, decision type, and associated reasoning.

Created on: 2026-08-05
Author: Sudeep Varma K
"""

from typing import Optional
from pydantic import BaseModel, Field, field_validator
import re


class PriorAuthorizationRequest(BaseModel):
    patient_name: Optional[str]
    patient_id: Optional[str]

    diagnosis: Optional[str]
    icd10_code: Optional[str]

    procedure: Optional[str]
    cpt_code: Optional[str]

    provider_name: Optional[str]

    payer: Optional[str]

    estimated_cost: Optional[str]

    confidence: float = 0.0

    clinical_notes: Optional[str]

    supporting_documents: list[str] = Field(default_factory=list)

    @field_validator("estimated_cost")
    @classmethod
    def validate_cost(cls, value: Optional[float]) -> Optional[float]:

        match = re.search(r'\d+(?:\.\d+)?', value)
        if match:
            value = float(match.group())
        else:
            return None

        if value < 0:
            raise ValueError("Estimated cost cannot be negative.")

        return value


class PriorAuthorizationResult(BaseModel):
    approved: bool

    decision: str

    reasons: list[str] = Field(default_factory=list)

    extracted_request: Optional[PriorAuthorizationRequest] = None