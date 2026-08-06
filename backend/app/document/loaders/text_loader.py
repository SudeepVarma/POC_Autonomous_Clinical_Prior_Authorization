"""
TextLoader class is a concrete implementation of the document loading interface, designed to load plain text documents.

Created on: 2026-08-05
Author: Sudeep Varma K
"""

from pathlib import Path
from app.document.metadata import MetadataExtractor
from app.models.document import Document
from app.document.loaders.base import BaseLoader


class TextLoader(BaseLoader):

    def load(
        self,
        path: Path,
    ) -> Document:

        text = path.read_text(
            encoding="utf-8",
            errors="ignore",
        )

        metadata = MetadataExtractor().from_file(
            path,
            "text/plain",
        )

        return Document(
            path=path,
            text=text,
            metadata=metadata,
        )