"""
Determines whether OCR (Optical Character Recognition) is required for a PDF based on the presence and length of searchable text.

Created on: 2026-08-05
Author: Sudeep Varma K
"""

class OCRDetector:
    """
    Determines whether OCR is required.

    If very little searchable text exists,
    assume the PDF is scanned.
    """

    MIN_TEXT_LENGTH = 100

    def requires_ocr(self, text: str) -> bool:

        if text is None:
            return True

        return len(text.strip()) < self.MIN_TEXT_LENGTH