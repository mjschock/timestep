from typing import Any

from fastapi import HTTPException
from openai import OpenAI


class ModerationsService:
    def __init__(self) -> None:
        # Initialize OpenAI client - in a real implementation, this would use proper API key management
        self.client = OpenAI(api_key="dummy_key", base_url="http://localhost:8000/v1")

    def create_moderation(self, body: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Classifies if text inputs are potentially harmful.

        Args:
            body: Request body containing 'input' field with text to moderate

        Returns:
            Dictionary with moderation results
        """
        try:
            if not body:
                body = {}

            # Extract input from request body
            input_data = body.get("input")

            # Validate input
            if not input_data:
                raise HTTPException(status_code=400, detail="'input' is required")

            # Handle both string and list inputs
            if isinstance(input_data, str):
                inputs = [input_data]
            elif isinstance(input_data, list):
                inputs = input_data
                # Validate that all items are strings
                for i, item in enumerate(inputs):
                    if not isinstance(item, str):
                        raise HTTPException(
                            status_code=400, detail=f"Input item {i} must be a string"
                        )
            else:
                raise HTTPException(
                    status_code=400,
                    detail="'input' must be a string or array of strings",
                )

            # Create moderation results
            results = []
            for text_input in inputs:
                # In a real implementation, this would call the actual OpenAI moderation API
                # For now, we'll create a mock response that follows the OpenAI format
                result = self._create_moderation_result(text_input)
                results.append(result)

            return {
                "id": "modr-123456789",
                "model": "text-moderation-007",
                "results": results,
            }

        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Failed to create moderation: {str(e)}"
            ) from e

    def _create_moderation_result(self, text: str) -> dict[str, Any]:
        """
        Create a moderation result for a given text input.
        This is a mock implementation that follows the OpenAI moderation API format.
        """
        # Simple keyword-based moderation for demonstration
        # In a real implementation, this would call the actual OpenAI moderation API
        text_lower = text.lower()

        # Define categories and their keywords - using actual OpenAI category names
        categories = {
            "harassment": ["harass", "bully", "abuse", "intimidate"],
            "harassment_threatening": [
                "kill you",
                "death to",
                "exterminate",
                "threaten",
            ],
            "hate": ["hate", "racist", "sexist", "discriminate", "bigot"],
            "hate_threatening": ["kill you", "death to", "exterminate", "eliminate"],
            "self_harm": ["suicide", "kill myself", "self harm", "end my life"],
            "self_harm_instructions": [
                "how to kill yourself",
                "suicide method",
                "ways to die",
            ],
            "self_harm_intent": [
                "I want to die",
                "I want to kill myself",
                "I want to end it",
            ],
            "sexual": ["sex", "porn", "nude", "explicit", "sexual"],
            "sexual_minors": ["child", "minor", "underage", "pedo"],
            "violence": [
                "violence",
                "fight",
                "attack",
                "weapon",
                "kill",
                "murder",
                "assault",
            ],
            "violence_graphic": ["blood", "gore", "torture", "mutilate", "dismember"],
            "illicit": ["drugs", "illegal", "criminal", "contraband"],
            "illicit_violent": ["bomb", "terrorist", "assassinate", "explosive"],
        }

        # Check each category
        category_scores = {}
        flagged = False

        for category, keywords in categories.items():
            score = 0.0
            for keyword in keywords:
                if keyword in text_lower:
                    score = max(score, 0.8)  # High score if keyword found
                    flagged = True

            category_scores[category] = score

        # Add all categories that the OpenAI API expects, even if they have None values
        all_categories = [
            "harassment",
            "harassment_threatening",
            "hate",
            "hate_threatening",
            "self_harm",
            "self_harm_instructions",
            "self_harm_intent",
            "sexual",
            "sexual_minors",
            "violence",
            "violence_graphic",
            "illicit",
            "illicit_violent",
        ]

        # Ensure all categories are present
        for category in all_categories:
            if category not in category_scores:
                category_scores[category] = 0.0

        return {
            "flagged": flagged,
            "categories": category_scores,
            "category_scores": category_scores,
        }
