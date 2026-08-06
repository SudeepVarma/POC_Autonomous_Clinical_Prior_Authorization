"""
Defines data models for document metadata and content, including utilities for parsing and serializing documents.

Created on: 2026-08-05
Author: Sudeep Varma K
"""

from pathlib import Path
from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class DocumentMetadata(BaseModel):
    filename: str
    content_type: str | None = None
    pages: int = 0
    size: int = 0
    sha256: str = ""


class DocumentChunk(BaseModel):
    index: int
    text: str


class Document(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    path: Path
    text: str = ""
    metadata: DocumentMetadata
    chunks: list[DocumentChunk] = Field(default_factory=list)

    def chunk_count(self) -> int:
        return len(self.chunks)

    def to_dict(self) -> dict[str, Any]:
        return self.model_dump()