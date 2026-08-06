"""
LoaderFactory creates and returns a loader instance based on the file extension.

Created on: 2026-08-05
Author: Sudeep Varma K
"""

from __future__ import annotations
from pathlib import Path
from app.document.loaders.docx_loader import DocxLoader
from app.document.loaders.image_loader import ImageLoader
from app.document.loaders.pdf_loader import PDFLoader
from app.document.loaders.text_loader import TextLoader


class LoaderFactory:
    """
    Returns the appropriate loader based on file extension.
    """

    LOADERS = {
        ".pdf": PDFLoader,
        ".txt": TextLoader,
        ".md": TextLoader,
        ".docx": DocxLoader,
        ".png": ImageLoader,
        ".jpg": ImageLoader,
        ".jpeg": ImageLoader,
        ".tif": ImageLoader,
        ".tiff": ImageLoader,
        ".bmp": ImageLoader,
    }

    @classmethod
    def create(cls, path: Path):

        suffix = path.suffix.lower()

        if suffix not in cls.LOADERS:
            raise ValueError(f"Unsupported document type: {suffix}")

        return cls.LOADERS[suffix]()