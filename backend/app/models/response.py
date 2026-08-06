"""
Generic API response model with properties for success status, message, data, and any error details.

Created on: 2026-08-05
Author: Sudeep Varma K
"""

from typing import Any
from pydantic import BaseModel, Field

class APIResponse(BaseModel):
    success: bool = True

    message: str = ""

    data: Any = None

    errors: list[str] = Field(default_factory=list)