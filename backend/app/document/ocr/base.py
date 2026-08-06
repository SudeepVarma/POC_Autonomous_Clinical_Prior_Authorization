"""
Defines a base interface for Optical Character Recognition (OCR) engines.

Created on: 2026-08-05
Author: Sudeep Varma K
"""

from abc import ABC, abstractmethod
from pathlib import Path


class BaseOCR(ABC):
    """
    Base interface for OCR engines.
    """

    @abstractmethod
    def execute(self, path: Path) -> str:
        raise NotImplementedError