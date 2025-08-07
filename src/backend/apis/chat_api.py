from fastapi import APIRouter, Depends, HTTPException, Request, Response
from openai.types.chat import ChatCompletion
from openai.types.chat.completion_create_params import (
    CompletionCreateParamsNonStreaming,
    CompletionCreateParamsStreaming,
)

from backend._shared.logging_config import logger
from backend._shared.utils.common_utils import validate_and_convert_openai_request
from backend.services.chat_service import ChatService

chat_router = APIRouter()


@chat_router.get("/chat/completions")
def list_chat_completions(
    model: str = None,
    metadata: str = None,
    after: str = None,
    limit: str = None,
    order: str = None,
    request: Request = None,
    service: ChatService = Depends(),  # noqa: B008
):
    """
    List stored Chat Completions. Only Chat Completions that have been stored
    with the `store` parameter set to `true` will be returned.
    """
    return service.list_chat_completions(model, metadata, after, limit, order)


@chat_router.post("/chat/completions")
async def create_chat_completion(
    request: Request,
    response: Response,
    service: ChatService = Depends(),  # noqa: B008
):
    """
    **Starting a new project?** We recommend trying [Responses](/docs/api-reference/responses)
    to take advantage of the latest OpenAI platform features. Compare
    [Chat Completions with Responses](/docs/guides/responses-vs-chat-completions?api-mode=responses).

    ---

    Creates a model response for the given chat conversation. Learn more in the
    [text generation](/docs/guides/text-generation), [vision](/docs/guides/vision),
    and [audio](/docs/guides/audio) guides.

    Parameter support can differ depending on the model used to generate the
    response, particularly for newer reasoning models. Parameters that are only
    supported for reasoning models are noted below. For the current state of
    unsupported parameters in reasoning models,
    [refer to the reasoning guide](/docs/guides/reasoning).
    """
    try:
        body = await request.json()
        logger.info(
            f"API received request for chat completion: {request.method} {request.url}"
        )

        # Validate the entire request using OpenAI types
        try:
            # Check if streaming is requested to use the correct validation model
            is_streaming = body.get("stream", False)

            if is_streaming:
                completion_create_params_streaming: CompletionCreateParamsStreaming = (
                    validate_and_convert_openai_request(
                        body,
                        CompletionCreateParamsStreaming,
                        "completion_create_params_streaming",
                    )
                )
                validated_request = completion_create_params_streaming
            else:
                completion_create_params_non_streaming: CompletionCreateParamsNonStreaming = validate_and_convert_openai_request(
                    body,
                    CompletionCreateParamsNonStreaming,
                    "completion_create_params_non_streaming",
                )
                validated_request = completion_create_params_non_streaming
        except Exception as e:
            # Add detailed error logging for debugging
            import json

            print(f"DEBUG: Validation failed for request: {json.dumps(body, indent=2)}")
            print(f"DEBUG: Full error details: {repr(e)}")
            if hasattr(e, "errors"):
                print(f"DEBUG: Validation errors: {e.errors()}")
            raise HTTPException(
                status_code=400, detail=f"Invalid request format: {e}"
            ) from e

        # Validate messages are not empty
        messages = validated_request.get("messages", [])
        if not messages:
            raise HTTPException(status_code=400, detail="messages cannot be empty")

        # Set proper headers for OpenAI client compatibility
        response.headers["Content-Type"] = "application/json"
        result = await service.create_chat_completion(validated_request)

        # Validate the response using OpenAI types
        if isinstance(result, dict):
            try:
                validated_response = ChatCompletion.model_validate(result)
                result = validated_response.model_dump(exclude_unset=True)
            except Exception as e:
                logger.error(f"Invalid response format from service: {e}")
                raise HTTPException(
                    status_code=500,
                    detail="Internal server error: invalid response format",
                ) from e

        # Log meaningful response information
        if isinstance(result, dict):
            model_name = result.get("model", "unknown")
            usage = result.get("usage", {})
            prompt_tokens = usage.get("prompt_tokens", 0)
            completion_tokens = usage.get("completion_tokens", 0)
            total_tokens = usage.get("total_tokens", 0)

            # Get a brief summary of the response content
            choices = result.get("choices", [])
            if choices and len(choices) > 0:
                first_choice = choices[0]
                message = first_choice.get("message", {})
                content = message.get("content", "")
                if content is None:
                    content_preview = "null (tool calls present)"
                else:
                    content_preview = (
                        content[:100] + "..." if len(content) > 100 else content
                    )
                finish_reason = first_choice.get("finish_reason", "unknown")
            else:
                content_preview = "no content"
                finish_reason = "unknown"

            logger.info(
                f"Chat completion response: model={model_name}, "
                f"tokens={prompt_tokens}+{completion_tokens}={total_tokens}, "
                f"finish_reason={finish_reason}, "
                f"content_preview='{content_preview}'"
            )
        else:
            logger.info(f"Chat completion response: {type(result).__name__}")

        return result
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Exception in API endpoint: {e}", exc_info=True)
        raise


@chat_router.get("/chat/completions/{completion_id}")
def get_chat_completion(
    completion_id: str,
    request: Request = None,
    service: ChatService = Depends(),  # noqa: B008
):
    """
    Get a stored chat completion. Only Chat Completions that have been created
    with the `store` parameter set to `true` will be returned.
    """
    return service.get_chat_completion(completion_id)


@chat_router.post("/chat/completions/{completion_id}")
async def update_chat_completion(
    completion_id: str,
    request: Request,
    service: ChatService = Depends(),  # noqa: B008
):
    """
    Modify a stored chat completion. Only Chat Completions that have been
    created with the `store` parameter set to `true` can be modified. Currently,
    the only supported modification is to update the `metadata` field.
    """
    body = await request.json()
    return service.update_chat_completion(completion_id, body)


@chat_router.delete("/chat/completions/{completion_id}")
def delete_chat_completion(
    completion_id: str,
    request: Request = None,
    service: ChatService = Depends(),  # noqa: B008
):
    """
    Delete a stored chat completion. Only Chat Completions that have been
    created with the `store` parameter set to `true` can be deleted.
    """
    return service.delete_chat_completion(completion_id)


@chat_router.get("/chat/completions/{completion_id}/messages")
def get_chat_completion_messages(
    completion_id: str,
    after: str = None,
    limit: str = None,
    order: str = None,
    request: Request = None,
    service: ChatService = Depends(),  # noqa: B008
):
    """
    Get the messages in a stored chat completion. Only Chat Completions that
    have been created with the `store` parameter set to `true` will be
    returned.
    """
    return service.get_chat_completion_messages(completion_id, after, limit, order)
