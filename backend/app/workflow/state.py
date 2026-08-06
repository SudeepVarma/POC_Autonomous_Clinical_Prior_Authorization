"""
The data model for storing workflow state.

Created on: 2026-08-05
Author: Sudeep Varma K
"""

from enum import Enum

class WorkflowState(str, Enum):
    RECEIVED = "received"

    DOCUMENT_PROCESSED = "document_processed"

    EXTRACTING = "extracting"

    EXTRACTION_COMPLETE = "extraction_complete"

    VALIDATING = "validating"

    VALIDATION_COMPLETE = "validation_complete"

    GOVERNANCE = "governance"

    COMPLETED = "completed"

    HUMAN_REVIEW = "human_review"

    FAILED = "failed"