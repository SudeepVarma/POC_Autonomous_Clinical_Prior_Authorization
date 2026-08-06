"""
Backend configuration file for the platform.

Created on: 2026-08-05
Author: Sudeep Varma K
"""

from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    APP_NAME: str = "Autonomous Clinical Prior Authorization Platform"
    APP_VERSION: str = "0.1.0"
    DEBUG: bool = False

    HOST: str = "0.0.0.0"
    PORT: int = 8000

    OLLAMA_BASE_URL: str = Field(
        default="http://localhost:11434/v1"
    )

    OLLAMA_MODEL: str = Field(
        default="llama3.1:8b"
    )

    OPA_URL: str = Field(
        default="http://localhost:8181/v1/data/healthcare/prior_auth"
    )

    EMBEDDING_MODEL: str = Field(
        default="sentence-transformers/all-MiniLM-L6-v2"
    )

    CHROMA_PATH: str = Field(
        default="./data/chroma"
    )

    UPLOAD_DIRECTORY: str = Field(
        default="./uploads"
    )

    MAX_UPLOAD_SIZE: int = Field(
        default=20 * 1024 * 1024
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()