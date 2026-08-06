"""
Manages the end-to-end document ingestion pipeline, including loading, text extraction, cleaning, chunking, and OCR processing as needed.

Created on: 2026-08-05
Author: Sudeep Varma K
"""

from __future__ import annotations
from pathlib import Path
from app.document.chunker import Chunker
from app.document.cleaner import Cleaner
from app.document.detector import OCRDetector
from app.document.loaders.factory import LoaderFactory
from app.document.ocr.factory import OCRFactory


class DocumentService:
    """
    Complete document ingestion pipeline.
    """

    def __init__(self) -> None:

        self.cleaner = Cleaner()

        self.chunker = Chunker()

        self.detector = OCRDetector()

    def process(self, path: Path):

        loader = LoaderFactory.create(path)

        document = loader.load(path)

        if self.detector.requires_ocr(document.text):

            ocr = OCRFactory.create()

            document.text = ocr.execute(path)

        document.text = self.cleaner.clean(document.text)

        document.chunks = self.chunker.split(document.text)

        return document