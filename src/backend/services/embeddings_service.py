# mypy: ignore-errors
from typing import Any

from fastapi import HTTPException, Request

from backend._shared.logging_config import logger


class EmbeddingsService:
    async def create_embedding(self, request: Request) -> dict[str, Any]:
        """Creates an embedding vector representing the input text."""
        logger.info("Creating embedding")
        body = await self._get_request_body(request)
        input_data = self._extract_input_data(body)
        model = body.get("model", "sentence-transformers/paraphrase-MiniLM-L3-v2")
        logger.debug(f"Using model: {model}")

        try:
            # Handle both single string and list of strings
            if isinstance(input_data, str):
                # Single string input
                logger.debug("Processing single string input")
                embeddings = [self._generate_embedding(input_data, model)]
                total_tokens = len(input_data.split())
            else:
                # List of strings input
                logger.debug(f"Processing list of {len(input_data)} strings")
                embeddings = [
                    self._generate_embedding(text, model) for text in input_data
                ]
                total_tokens = sum(len(text.split()) for text in input_data)

            logger.info(
                f"Generated {len(embeddings)} embeddings with {total_tokens} total tokens"
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
            logger.error(f"Embedding creation failed: {e}", exc_info=True)
            raise HTTPException(
                status_code=500, detail=f"Embedding creation failed: {str(e)}"
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

    def _generate_embedding(self, input_text: str, model: str) -> list[float]:
        # Dummy implementation for demonstration
        logger.debug(f"Generating embedding for text of length {len(input_text)}")
        return [0.0] * 768
