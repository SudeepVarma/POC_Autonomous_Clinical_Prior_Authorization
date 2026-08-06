"""
Implements OCR functionality using PyMuPDF and Tesseract to extract text from PDFs and images.

Created on: 2026-08-05
Author: Sudeep Varma K
"""

from __future__ import annotations
from pathlib import Path

import fitz
try:
    import pytesseract
except ImportError:
    pytesseract = None
from PIL import Image
from app.document.ocr.base import BaseOCR


class TesseractOCR(BaseOCR):
    """
    OCR implementation using PyMuPDF + Tesseract.
    """

    def execute(self, path: Path) -> str:

        if pytesseract is None:
            raise RuntimeError(
                "pytesseract is not installed."
            )

        suffix = path.suffix.lower()

        if suffix == ".pdf":

            pdf = fitz.open(path)

            pages = []

            try:

                for page in pdf:

                    pix = page.get_pixmap(dpi=300)

                    image = Image.frombytes(
                        "RGB",
                        (pix.width, pix.height),
                        pix.samples,
                    )

                    pages.append(
                        pytesseract.image_to_string(image)
                    )

            finally:
                pdf.close()

            return "\n".join(pages)

        image = Image.open(path)

        return pytesseract.image_to_string(image)