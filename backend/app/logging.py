"""
A logging utility to print informational messages.

Created on: 2026-08-05
Author: Sudeep Varma K
"""

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
)

logger = logging.getLogger("clinical-platform")