# mypy: ignore-errors
from typing import Any, Optional, Union
import torch
import numpy as np
from PIL import Image
import base64
import io

from fastapi import HTTPException, Request

from backend.logging_config import logger


class EmbeddingsService:
    def __init__(self):
        """Initialize the embeddings service with VLM-based embedding generation."""
        self.models_service = None  # Will be set by dependency injection
        
    def set_models_service(self, models_service):
        """Set the models service dependency."""
        self.models_service = models_service

    async def create_embedding(self, request: Request) -> dict[str, Any]:
        """Creates an embedding vector representing the input text using VLM."""
        logger.info("Creating VLM-based embedding")
        body = await self._get_request_body(request)
        input_data = self._extract_input_data(body)
        model = body.get("model", "HuggingFaceTB/SmolVLM2-256M-Video-Instruct")
        embedding_type = body.get("embedding_type", "cls")  # cls, mean, last_layer, multi_layer
        logger.debug(f"Using VLM model: {model}, embedding type: {embedding_type}")

        try:
            # Handle both single string and list of strings
            if isinstance(input_data, str):
                # Single string input
                logger.debug("Processing single string input")
                embeddings = [self._generate_vlm_embedding(input_data, model, embedding_type)]
                total_tokens = len(input_data.split())
            else:
                # List of strings input
                logger.debug(f"Processing list of {len(input_data)} strings")
                embeddings = [
                    self._generate_vlm_embedding(text, model, embedding_type) for text in input_data
                ]
                total_tokens = sum(len(text.split()) for text in input_data)

            logger.info(
                f"Generated {len(embeddings)} VLM embeddings with {total_tokens} total tokens"
            )

            # Return OpenAI-compatible response format
            return {
                "object": "list",
                "data": [
                    {"object": "embedding", "embedding": embedding, "index": i}
                    for i, embedding in enumerate(embeddings)
                ],
                "model": model,
                "usage": {"prompt_tokens": total_tokens, "total_tokens": total_tokens},
            }
        except Exception as e:
            logger.error(f"VLM embedding creation failed: {e}", exc_info=True)
            raise HTTPException(
                status_code=500, detail=f"VLM embedding creation failed: {str(e)}"
            ) from e

    async def create_multimodal_embedding(self, request: Request) -> dict[str, Any]:
        """Creates embeddings for text and image inputs using VLM."""
        logger.info("Creating multimodal VLM-based embedding")
        body = await self._get_request_body(request)
        
        text_input = body.get("text", "")
        image_input = body.get("image", None)  # Base64 encoded image
        model = body.get("model", "HuggingFaceTB/SmolVLM2-256M-Video-Instruct")
        embedding_type = body.get("embedding_type", "cls")
        
        if not text_input and not image_input:
            raise HTTPException(status_code=400, detail="Either text or image input is required")
            
        try:
            embedding = self._generate_multimodal_vlm_embedding(
                text_input, image_input, model, embedding_type
            )
            
            return {
                "object": "list",
                "data": [
                    {"object": "embedding", "embedding": embedding, "index": 0}
                ],
                "model": model,
                "usage": {"prompt_tokens": len(text_input.split()) if text_input else 0, "total_tokens": len(text_input.split()) if text_input else 0},
            }
        except Exception as e:
            logger.error(f"Multimodal VLM embedding creation failed: {e}", exc_info=True)
            raise HTTPException(
                status_code=500, detail=f"Multimodal VLM embedding creation failed: {str(e)}"
            ) from e

    async def _get_request_body(self, request: Request) -> dict:
        try:
            return await request.json()
        except Exception as e:
            logger.error(f"Failed to parse request body: {e}")
            return {}

    def _extract_input_data(self, body: dict) -> str | list[str]:
        input_data = body.get("input")
        if not input_data:
            logger.error("Missing 'input' field in request")
            raise HTTPException(status_code=400, detail="'input' is required")
        return input_data

    def _decode_base64_image(self, image_data: str) -> Image.Image:
        """Decode base64 image data to PIL Image."""
        try:
            # Remove data URL prefix if present
            if image_data.startswith('data:image'):
                image_data = image_data.split(',')[1]
            
            image_bytes = base64.b64decode(image_data)
            image = Image.open(io.BytesIO(image_bytes))
            return image
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Invalid image data: {str(e)}")

    def _generate_vlm_embedding(
        self, 
        input_text: str, 
        model_name: str, 
        embedding_type: str = "cls"
    ) -> list[float]:
        """
        Generate embeddings using VLM by extracting latent representations.
        
        Args:
            input_text: Text to embed
            model_name: Name of the VLM model to use
            embedding_type: Type of embedding extraction ("cls", "mean", "last_layer", "multi_layer")
            
        Returns:
            List of float values representing the embedding
        """
        if not self.models_service:
            raise HTTPException(status_code=500, detail="Models service not initialized")
            
        logger.debug(f"Generating VLM embedding for text: {input_text[:100]}...")
        
        try:
            # Get the VLM model and processor
            model, processor = self.models_service.get_model_instance(model_name)
            
            # Prepare the input (text only, no image)
            inputs = processor(
                text=input_text,
                return_tensors="pt",
                padding=True,
                truncation=True,
                max_length=512  # Adjust based on model capabilities
            )
            
            # Move inputs to the same device as the model
            device = next(model.parameters()).device
            inputs = {k: v.to(device) for k, v in inputs.items()}
            
            # Forward pass to get the model outputs
            with torch.no_grad():
                outputs = model(**inputs, output_hidden_states=True)
            
            # Extract embeddings based on the specified type
            embedding = self._extract_embedding_from_outputs(outputs, inputs, embedding_type)
            
            logger.debug(f"Generated embedding of dimension: {len(embedding)}")
            return embedding
            
        except Exception as e:
            logger.error(f"Failed to generate VLM embedding: {e}")
            raise HTTPException(
                status_code=500, 
                detail=f"Failed to generate VLM embedding: {str(e)}"
            ) from e

    def _generate_multimodal_vlm_embedding(
        self, 
        text_input: str, 
        image_input: Optional[str], 
        model_name: str, 
        embedding_type: str = "cls"
    ) -> list[float]:
        """
        Generate embeddings for text and image inputs using VLM.
        
        Args:
            text_input: Text to embed
            image_input: Base64 encoded image
            model_name: Name of the VLM model to use
            embedding_type: Type of embedding extraction
            
        Returns:
            List of float values representing the embedding
        """
        if not self.models_service:
            raise HTTPException(status_code=500, detail="Models service not initialized")
            
        try:
            # Get the VLM model and processor
            model, processor = self.models_service.get_model_instance(model_name)
            
            # Prepare inputs
            inputs = {}
            
            if text_input:
                inputs["text"] = text_input
                
            if image_input:
                image = self._decode_base64_image(image_input)
                inputs["images"] = image
            
            # Process inputs
            processed_inputs = processor(
                **inputs,
                return_tensors="pt",
                padding=True,
                truncation=True,
                max_length=512
            )
            
            # Move inputs to the same device as the model
            device = next(model.parameters()).device
            processed_inputs = {k: v.to(device) for k, v in processed_inputs.items()}
            
            # Forward pass to get the model outputs
            with torch.no_grad():
                outputs = model(**processed_inputs, output_hidden_states=True)
            
            # Extract embeddings based on the specified type
            embedding = self._extract_embedding_from_outputs(outputs, processed_inputs, embedding_type)
            
            logger.debug(f"Generated multimodal embedding of dimension: {len(embedding)}")
            return embedding
            
        except Exception as e:
            logger.error(f"Failed to generate multimodal VLM embedding: {e}")
            raise HTTPException(
                status_code=500, 
                detail=f"Failed to generate multimodal VLM embedding: {str(e)}"
            ) from e

    def _extract_embedding_from_outputs(
        self, 
        outputs, 
        inputs: dict, 
        embedding_type: str
    ) -> list[float]:
        """
        Extract embeddings from model outputs using different strategies.
        
        Args:
            outputs: Model outputs with hidden states
            inputs: Input tensors
            embedding_type: Type of embedding extraction
            
        Returns:
            List of float values representing the embedding
        """
        hidden_states = outputs.hidden_states
        
        if embedding_type == "cls":
            # Use the last layer's [CLS] token (first token)
            last_hidden_state = hidden_states[-1]
            cls_embedding = last_hidden_state[:, 0, :]
            embedding = cls_embedding.cpu().numpy().flatten().tolist()
            
        elif embedding_type == "mean":
            # Use mean pooling across all tokens (excluding padding)
            last_hidden_state = hidden_states[-1]
            attention_mask = inputs.get('attention_mask', None)
            if attention_mask is not None:
                # Mean pooling excluding padding tokens
                mask_expanded = attention_mask.unsqueeze(-1).expand(last_hidden_state.size())
                masked_hidden = last_hidden_state * mask_expanded
                sum_hidden = torch.sum(masked_hidden, dim=1)
                count_mask = torch.sum(attention_mask, dim=1, keepdim=True)
                embedding = (sum_hidden / count_mask).cpu().numpy().flatten().tolist()
            else:
                # Fallback to mean pooling without mask
                embedding = torch.mean(last_hidden_state, dim=1).cpu().numpy().flatten().tolist()
                
        elif embedding_type == "last_layer":
            # Use the entire last hidden state (flattened)
            last_hidden_state = hidden_states[-1]
            embedding = last_hidden_state.cpu().numpy().flatten().tolist()
            
        elif embedding_type == "multi_layer":
            # Concatenate embeddings from multiple layers
            # Use last 3 layers for example
            layers_to_use = [-1, -2, -3]  # Last 3 layers
            layer_embeddings = []
            
            for layer_idx in layers_to_use:
                if abs(layer_idx) <= len(hidden_states):
                    layer_hidden = hidden_states[layer_idx]
                    # Use CLS token from each layer
                    layer_cls = layer_hidden[:, 0, :]
                    layer_embeddings.append(layer_cls)
            
            # Concatenate all layer embeddings
            if layer_embeddings:
                concatenated = torch.cat(layer_embeddings, dim=-1)
                embedding = concatenated.cpu().numpy().flatten().tolist()
            else:
                # Fallback to last layer CLS
                last_hidden_state = hidden_states[-1]
                embedding = last_hidden_state[:, 0, :].cpu().numpy().flatten().tolist()
                
        else:
            # Default to CLS token
            last_hidden_state = hidden_states[-1]
            embedding = last_hidden_state[:, 0, :].cpu().numpy().flatten().tolist()
            
        return embedding
