"""
PDFLoader is a concrete implementation of the document loading interface for searching and extracting text from PDF files.

Created on: 2026-08-05
Author: Sudeep Varma K
"""

from __future__ import annotations
from pathlib import Path
import fitz
from app.document.metadata import MetadataExtractor
from app.models.document import Document
from app.document.loaders.base import BaseLoader



class PDFLoader(BaseLoader):
    """
    Loads searchable PDFs using PyMuPDF.

    OCR is handled later by OCRDetector if required.
    """

    def load(self, path: Path) -> Document:

        pdf = fitz.open(path)

        pages = []

        for page in pdf:
            pages.append(page.get_text())

        text = "\n".join(pages)

        metadata = MetadataExtractor().from_pdf(
            pdf,
            path,
        )

        pdf.close()

        return Document(
            path=path,
            text=text,
            metadata=metadata,
        )