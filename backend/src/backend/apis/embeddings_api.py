# mypy: ignore-errors

from fastapi import APIRouter, Depends, Request

from backend.logging_config import logger
from backend.services.embeddings_service import EmbeddingsService
from backend.services.models_service import get_models_service

embeddings_router = APIRouter()


def get_embeddings_service() -> EmbeddingsService:
    """Dependency to get embeddings service with models service injected."""
    service = EmbeddingsService()
    service.set_models_service(get_models_service())
    return service


@embeddings_router.post("/embeddings")
async def create_embedding(
    request: Request, 
    service: EmbeddingsService = Depends(get_embeddings_service)  # noqa: B008
):
    """Creates an embedding vector representing the input text using VLM."""
    logger.info("Creating VLM embedding via API")
    return await service.create_embedding(request)


@embeddings_router.post("/embeddings/multimodal")
async def create_multimodal_embedding(
    request: Request, 
    service: EmbeddingsService = Depends(get_embeddings_service)  # noqa: B008
):
    """Creates embeddings for text and image inputs using VLM."""
    logger.info("Creating multimodal VLM embedding via API")
    return await service.create_multimodal_embedding(request)
