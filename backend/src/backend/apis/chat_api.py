from fastapi import APIRouter, Depends, Request, Response

from backend.logging_config import logger
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

        # Set proper headers for OpenAI client compatibility
        response.headers["Content-Type"] = "application/json"
        result = await service.create_chat_completion(body)

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
