"""
Local Ollama wrapper.

Created on: 2026-08-05
Author: Sudeep Varma K
"""

from __future__ import annotations

import instructor
from openai import OpenAI

from app.config import settings
from app.models.clinical import PriorAuthorizationRequest


SYSTEM_PROMPT = """
You are a healthcare prior authorization extraction assistant.

Extract the requested information from the clinical document.

Also estimate your confidence between 0 and 1.

Use low confidence when important information is missing.

Return ONLY valid JSON matching the schema.
"""


class LLMTool:
    """
    Wrapper around the local Ollama server using an OpenAI-compatible API.
    """

    def __init__(self) -> None:

        client = OpenAI(
            base_url=settings.OLLAMA_BASE_URL,
            api_key="ollama",
        )

        self.client = instructor.from_openai(client)

    def extract_prior_authorization(
        self,
        text: str,
    ) -> PriorAuthorizationRequest:

        return self.client.chat.completions.create(
            model=settings.OLLAMA_MODEL,
            response_model=PriorAuthorizationRequest,
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT,
                },
                {
                    "role": "user",
                    "content": text,
                },
            ],
            temperature=0,
        )