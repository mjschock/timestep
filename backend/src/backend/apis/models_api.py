from fastapi import APIRouter, Request

from backend.logging_config import logger
from backend.services.models_service import get_models_service

models_router = APIRouter()


@models_router.get("/models")
def list_models(request: Request):
    """
    Lists the currently available models, and provides basic information about each one such as the owner and availability.
    """
    service = get_models_service()
    logger.info("Listing models")
    return service.list_models()


@models_router.get("/models/{model:path}")
def retrieve_model(model: str, request: Request):
    """
    Retrieves a model instance, providing basic information about the model such as the owner and permissioning.
    """
    service = get_models_service()
    logger.info(f"Retrieving model: {model}")
    return service.retrieve_model(model)


@models_router.delete("/models/{model}")
def delete_model(model: str, request: Request):
    """
    Delete a fine-tuned model. You must have the Owner role in your organization to delete a model.
    """
    service = get_models_service()
    logger.info(f"Deleting model: {model}")
    return service.delete_model(model)
