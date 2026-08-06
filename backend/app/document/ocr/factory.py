"""
Returns an instance of the Tesseract-based OCR implementation for text extraction.

Created on: 2026-08-05
Author: Sudeep Varma K
"""

from __future__ import annotations
from app.document.ocr.tesseract import TesseractOCR


class OCRFactory:
    """
    Returns the configured OCR implementation.
    """

    @staticmethod
    def create():
        return TesseractOCR()