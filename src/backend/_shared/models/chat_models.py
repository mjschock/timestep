"""
Chat completion request/response models for internal use.
"""

from typing import Any

from pydantic import BaseModel


class ChatCompletionRequest(BaseModel):
    """
    Pydantic model for chat completion requests.

    This wraps the validated OpenAI TypedDict data to provide
    better type safety and easier access to fields.
    """

    messages: list[dict]
    model: str
    stream: bool = False
    temperature: float | None = None
    max_tokens: int | None = None
    tools: list[dict] | None = None
    tool_choice: Any | None = None
    parallel_tool_calls: bool | None = None
    top_p: float | None = None
    n: int | None = None
    stop: Any | None = None
    presence_penalty: float | None = None
    frequency_penalty: float | None = None
    logprobs: bool | None = None
    top_logprobs: int | None = None
    user: str | None = None
    response_format: dict | None = None
    seed: int | None = None
    logit_bias: dict | None = None

    class Config:
        extra = "allow"  # Allow additional OpenAI fields we might not have covered

    @classmethod
    def from_validated_request(cls, validated_request: dict) -> "ChatCompletionRequest":
        """
        Create a ChatCompletionRequest from TypeAdapter validated data.

        Args:
            validated_request: Dict from TypeAdapter.validate_python() containing ValidatorIterators

        Returns:
            ChatCompletionRequest instance with plain Python types
        """
        # Convert ValidatorIterators to lists
        messages = (
            list(validated_request["messages"])
            if "messages" in validated_request
            else []
        )
        tools = (
            list(validated_request["tools"]) if "tools" in validated_request else None
        )

        return cls(
            messages=messages,
            model=validated_request["model"],
            stream=validated_request.get("stream", False),
            temperature=validated_request.get("temperature"),
            max_tokens=validated_request.get("max_tokens"),
            tools=tools,
            tool_choice=validated_request.get("tool_choice"),
            parallel_tool_calls=validated_request.get("parallel_tool_calls"),
            top_p=validated_request.get("top_p"),
            n=validated_request.get("n"),
            stop=validated_request.get("stop"),
            presence_penalty=validated_request.get("presence_penalty"),
            frequency_penalty=validated_request.get("frequency_penalty"),
            logprobs=validated_request.get("logprobs"),
            top_logprobs=validated_request.get("top_logprobs"),
            user=validated_request.get("user"),
            response_format=validated_request.get("response_format"),
            seed=validated_request.get("seed"),
            logit_bias=validated_request.get("logit_bias"),
        )
