# mypy: ignore-errors

from fastapi import APIRouter, Depends, Request

from backend.logging_config import logger
from backend.services.embeddings_service import EmbeddingsService

embeddings_router = APIRouter()


@embeddings_router.post("/embeddings")
async def create_embedding(request: Request, service: EmbeddingsService = Depends()):  # noqa: B008
    """Creates an embedding vector representing the input text."""
    logger.info("Creating embedding via API")
    return await service.create_embedding(request)
