"""
Implements a simple sliding-window text chunker, splitting input text into fixed-size chunks with user-defined overlap.

Created on: 2026-08-05
Author: Sudeep Varma K
"""

from app.models.document import DocumentChunk

class Chunker:
    """
    Simple sliding-window text chunker.
    """

    def __init__(
        self,
        chunk_size: int = 1000,
        overlap: int = 200,
    ) -> None:

        self.chunk_size = chunk_size
        self.overlap = overlap

    def split(self, text: str) -> list[DocumentChunk]:

        if not text:
            return []

        chunks = []

        start = 0
        index = 0

        while start < len(text):

            end = start + self.chunk_size

            chunks.append(
                DocumentChunk(
                    index=index,
                    text=text[start:end],
                )
            )

            index += 1

            start += self.chunk_size - self.overlap

        return chunks