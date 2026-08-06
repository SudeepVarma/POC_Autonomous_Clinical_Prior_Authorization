"""
Backend API routes.

Created on: 2026-08-05
Author: Sudeep Varma K
"""

from __future__ import annotations
import shutil
from pathlib import Path

from fastapi import APIRouter, File, HTTPException, UploadFile

from app.config import settings
from app.models.document import (
    Document,
    DocumentMetadata,
)
from app.workflow.context import WorkflowContext
from app.workflow.workflow import Workflow

from app.agents.document_agent import DocumentAgent
from app.agents.extraction_agent import ExtractionAgent
from app.agents.governance_agent import GovernanceAgent


router = APIRouter()


workflow = Workflow()

workflow.register(DocumentAgent())
workflow.register(ExtractionAgent())
workflow.register(GovernanceAgent())


UPLOAD_DIR = Path(settings.UPLOAD_DIRECTORY)

UPLOAD_DIR.mkdir(
    parents=True,
    exist_ok=True,
)


@router.post("/extract")
async def extract(
    file: UploadFile = File(...),
):

    destination = UPLOAD_DIR / file.filename

    with destination.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    document = Document(
        path=destination,
        text="",
        metadata=DocumentMetadata(
            filename=file.filename,
            content_type=file.content_type,
        ),
    )

    context = WorkflowContext(
        document=document,
    )

    result = workflow.run(context)

    if result.errors:
        raise HTTPException(
            status_code=500,
            detail=result.errors,
        )

    return {
        "trace_id": result.trace_id,
        "state": result.state.value,
        "events": result.events,
        "human_review": result.requires_human_review,
        "review_reason": result.review_reason,
        "extraction": (
            result.extraction.model_dump()
            if result.extraction
            else None
        ),
        "decision": (
            result.decision.model_dump()
            if result.decision
            else None
        ),
    }


@router.get("/health")
async def health():

    return {
        "status": "ok",
        "model": settings.OLLAMA_MODEL,
    }