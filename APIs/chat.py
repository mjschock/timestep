from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse, StreamingResponse
from typing import Optional, List, Dict, Any
import json
import uuid
from datetime import datetime, timezone

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
        "supports_vision": True
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
        "supports_vision": False
    }
}

@router.post("/chat/completions")
async def create_chat_completion(request: Request):
    """Create a chat completion"""
    
    # Parse request body
    try:
        body = await request.json()
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Invalid JSON in request body")
    
    # Extract parameters
    model = body.get("model")
    messages = body.get("messages", [])
    stream = body.get("stream", False)
    max_tokens = body.get("max_tokens")
    temperature = body.get("temperature", 1.0)
    top_p = body.get("top_p", 1.0)
    n = body.get("n", 1)
    
    # Validate model
    if not model:
        raise HTTPException(status_code=400, detail="Model is required")
    
    if model not in LOCAL_MODELS:
        raise HTTPException(
            status_code=400,
            detail=f"Model '{model}' is not available. Available models: {list(LOCAL_MODELS.keys())}"
        )
    
    # Validate messages
    if not messages:
        raise HTTPException(status_code=400, detail="Messages are required")
    
    # Validate message format
    for i, message in enumerate(messages):
        if not isinstance(message, dict):
            raise HTTPException(status_code=400, detail=f"Message {i} must be an object")
        
        role = message.get("role")
        if role not in ["system", "user", "assistant"]:
            raise HTTPException(status_code=400, detail=f"Invalid role '{role}' in message {i}")
        
        content = message.get("content")
        if not content:
            raise HTTPException(status_code=400, detail=f"Content is required in message {i}")
    
    # Generate response (simulate local model inference)
    response_id = f"chatcmpl-{uuid.uuid4().hex[:8]}"
    created_at = datetime.now(timezone.utc)
    
    # Simple response generation (replace with actual model inference)
    last_message = messages[-1]
    if last_message["role"] == "user":
        response_content = f"I understand you said: '{last_message['content']}'. This is a simulated response from {model}."
    else:
        response_content = "I'm here to help! This is a simulated response from the local model."
    
    # Create response object
    response_obj = {
        "id": response_id,
        "object": "chat.completion",
        "created": int(created_at.timestamp()),
        "model": model,
        "choices": [
            {
                "index": 0,
                "message": {
                    "role": "assistant",
                    "content": response_content
                },
                "finish_reason": "stop"
            }
        ],
        "usage": {
            "prompt_tokens": len(str(messages)) // 4,  # Rough estimate
            "completion_tokens": len(response_content) // 4,
            "total_tokens": (len(str(messages)) + len(response_content)) // 4
        }
    }
    
    if stream:
        # Return streaming response
        async def generate_stream():
            # Send initial data
            yield f"data: {json.dumps(response_obj)}\n\n"
            # Send [DONE] marker
            yield "data: [DONE]\n\n"
        
        return StreamingResponse(
            generate_stream(),
            media_type="text/plain"
        )
    else:
        # Return regular response
        return response_obj

@router.get("/models")
async def list_models():
    """List available models"""
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