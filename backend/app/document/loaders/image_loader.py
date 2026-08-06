"""
ImageLoader class loads images and returns an empty document with extracted metadata.

Created on: 2026-08-05
Author: Sudeep Varma K
"""

from __future__ import annotations
from pathlib import Path
from app.document.metadata import MetadataExtractor
from app.models.document import Document
from app.document.loaders.base import BaseLoader


class ImageLoader(BaseLoader):
    """
    Images are processed later by OCR.

    Therefore this loader simply returns an empty
    document with metadata.
    """

    def load(
        self,
        path: Path,
    ) -> Document:

        metadata = MetadataExtractor().from_file(
            path,
            "image",
        )

        return Document(
            path=path,
            text="",
            metadata=metadata,
        )