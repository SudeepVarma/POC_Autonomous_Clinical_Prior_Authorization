"""
A minimal HealingService class that logs failure reports to track and monitor system errors, that can later be extended.

Created on: 2026-08-05
Author: Sudeep Varma K
"""

import logging
from app.healing.models import FailureReport

logger = logging.getLogger(__name__)

class HealingService:
    """
    Minimal healing implementation.

    Currently logs failures.

    Can later be extended to generate patches.
    """

    def report(self, report: FailureReport) -> None:

        logger.exception(
            "[%s] %s : %s",
            report.trace_id,
            report.component,
            report.error,
        )