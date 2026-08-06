"""
A minimal FastAPI REST layer connects the Streamlit frontend to the workflow engine, handling validation, initialization, and errors without containing business logic.

Created on: 2026-08-05
Author: Sudeep Varma K
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.api.routes import router


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.APP_NAME,
        version=settings.APP_VERSION,
        debug=settings.DEBUG,
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(router)

    @app.get("/", tags=["System"])
    async def root():
        return {
            "application": settings.APP_NAME,
            "version": settings.APP_VERSION,
            "status": "running",
        }

    @app.get("/health", tags=["System"])
    async def health():
        return {
            "status": "healthy",
            "ollama": settings.OLLAMA_BASE_URL,
            "opa": settings.OPA_URL,
        }

    return app


app = create_app()