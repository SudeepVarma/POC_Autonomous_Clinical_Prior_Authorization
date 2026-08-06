"""
A singleton class that instantiates and provides a single, globally accessible instance of the LLMTool service.

Created on: 2026-08-05
Author: Sudeep Varma K
"""

from __future__ import annotations
from app.tools.llm import LLMTool

class ToolRegistry:
    """
    Lightweight singleton registry.

    Keeps one instance of each expensive service.
    """

    def __init__(self) -> None:

        self._llm = LLMTool()

    @property
    def llm(self) -> LLMTool:
        return self._llm


tool_registry = ToolRegistry()