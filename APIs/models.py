from fastapi import APIRouter, HTTPException
from typing import List, Dict, Any

router = APIRouter()

# Available local models
LOCAL_MODELS = {
    "SmolVLM2-1.7B-Instruct": {
        "id": "SmolVLM2-1.7B-Instruct",
        "object": "model",
        "created": 1700000000,
        "owned_by": "timestep",
        "permission": [],
        "root": "SmolVLM2-1.7B-Instruct",
        "parent": None,
        "max_tokens": 4096,
        "supports_vision": True,
        "description": "SmolVLM2 1.7B Instruct model for chat completions and vision tasks"
    },
    "SmolVLM2-1.7B": {
        "id": "SmolVLM2-1.7B",
        "object": "model",
        "created": 1700000000,
        "owned_by": "timestep",
        "permission": [],
        "root": "SmolVLM2-1.7B",
        "parent": None,
        "max_tokens": 4096,
        "supports_vision": False,
        "description": "SmolVLM2 1.7B base model for text generation"
    },
    "SmolVLM2-1.7B-Instruct-finetuned": {
        "id": "SmolVLM2-1.7B-Instruct-finetuned",
        "object": "model",
        "created": 1700000000,
        "owned_by": "timestep",
        "permission": [],
        "root": "SmolVLM2-1.7B-Instruct-finetuned",
        "parent": "SmolVLM2-1.7B-Instruct",
        "max_tokens": 4096,
        "supports_vision": True,
        "description": "Fine-tuned SmolVLM2 1.7B Instruct model"
    }
}

@router.get("/models")
async def list_models():
    """List all available models"""
    return {
        "object": "list",
        "data": list(LOCAL_MODELS.values())
    }

@router.get("/models/{model_id}")
async def retrieve_model(model_id: str):
    """Retrieve a specific model"""
    if model_id not in LOCAL_MODELS:
        raise HTTPException(status_code=404, detail="Model not found")
    
    return LOCAL_MODELS[model_id]

@router.delete("/models/{model_id}")
async def delete_model(model_id: str):
    """Delete a model (not supported for local models)"""
    raise HTTPException(
        status_code=400,
        detail="Model deletion is not supported for local models"
    )