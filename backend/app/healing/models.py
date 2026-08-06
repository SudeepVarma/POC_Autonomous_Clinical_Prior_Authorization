"""
FailureReport model using Pydantic, representing failure reports with timestamp, component, error message, and unique identifier.

Created on: 2026-08-05
Author: Sudeep Varma K
"""

from datetime import datetime
from pydantic import BaseModel, Field

class FailureReport(BaseModel):
    timestamp: datetime = Field(default_factory=datetime.utcnow)

    component: str

    error: str

    trace_id: str