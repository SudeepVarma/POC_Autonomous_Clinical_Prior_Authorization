"""
Basic document cleaner, normalizing line endings and removing excessive whitespace to tidy up input text.

Created on: 2026-08-05
Author: Sudeep Varma K
"""

import re

class Cleaner:
    """
    Basic document cleanup.
    """

    def clean(self, text: str) -> str:

        if not text:
            return ""

        # Normalize line endings
        text = text.replace("\r\n", "\n")
        text = text.replace("\r", "\n")

        # Remove repeated whitespace
        text = re.sub(r"[ \t]+", " ", text)

        # Collapse excessive blank lines
        text = re.sub(r"\n{3,}", "\n\n", text)

        return text.strip()