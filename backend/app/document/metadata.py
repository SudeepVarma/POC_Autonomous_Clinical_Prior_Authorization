"""
Extracts metadata from documents, including PDFs and other file types, providing information on filename, content type, page count, size, and SHA-256 hash.

Created on: 2026-08-05
Author: Sudeep Varma K
"""

from __future__ import annotations
import hashlib
from pathlib import Path

import fitz

from app.models.document import DocumentMetadata


class MetadataExtractor:
    """
    Extract metadata from a document.
    """

    @staticmethod
    def sha256(path: Path) -> str:
        digest = hashlib.sha256()

        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(8192), b""):
                digest.update(chunk)

        return digest.hexdigest()

    def from_pdf(
        self,
        pdf: fitz.Document,
        path: Path,
    ) -> DocumentMetadata:

        return DocumentMetadata(
            filename=path.name,
            content_type="application/pdf",
            pages=len(pdf),
            size=path.stat().st_size,
            sha256=self.sha256(path),
        )

    def from_file(
        self,
        path: Path,
        content_type: str,
    ) -> DocumentMetadata:

        return DocumentMetadata(
            filename=path.name,
            content_type=content_type,
            pages=1,
            size=path.stat().st_size,
            sha256=self.sha256(path),
        )