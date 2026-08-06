"""
BaseLoader abstract class serves as a base interface for loading documents in a specific format.

Created on: 2026-08-05
Author: Sudeep Varma K
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path

from app.models.document import Document


class BaseLoader(ABC):
    """
    Base interface for all document loaders.
    """

    @abstractmethod
    def load(self, path: Path) -> Document:
        raise NotImplementedError