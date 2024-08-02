import asyncio

from openai import AsyncOpenAI, AsyncStream
from openai.types.chat.chat_completion import ChatCompletion
from openai.types.chat.chat_completion_chunk import ChatCompletionChunk
from openai.types.chat.completion_create_params import CompletionCreateParams
from sse_starlette import EventSourceResponse


async def create_chat_completion(
    body: CompletionCreateParams, token_info: dict, user: str, **kwargs
):
    """Creates a model response for the given chat conversation.

     # noqa: E501

    :param create_chat_completion_request:
    :type create_chat_completion_request: dict | bytes

    :rtype: Union[CreateChatCompletionResponse, Tuple[CreateChatCompletionResponse, int], Tuple[CreateChatCompletionResponse, int, Dict[str, str]]
    """
    client = AsyncOpenAI(
        api_key="sk-no-key-required",
        base_url="http://localhost:8080/v1",
    )

    chat_completion: ChatCompletion | AsyncStream[ChatCompletionChunk] = (
        await client.chat.completions.create(
            **body,
            user=user,
        )
    )

    if type(chat_completion) == AsyncStream:

        async def event_publisher():
            try:
                async for chunk in chat_completion:
                    yield chunk.model_dump_json()

            except asyncio.CancelledError as e:
                print(f"Disconnected from client (via refresh/close)")
                # Do any other cleanup, if any
                raise e

        return EventSourceResponse(event_publisher())

    else:
        return chat_completion.model_dump(mode="json")
