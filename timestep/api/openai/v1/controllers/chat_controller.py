import asyncio
import os

import instructor
from openai import AsyncOpenAI, AsyncStream
from openai.types.chat.chat_completion import ChatCompletion
from openai.types.chat.chat_completion_chunk import ChatCompletionChunk
from openai.types.chat.completion_create_params import CompletionCreateParams
from sse_starlette import EventSourceResponse

from timestep.config import settings

# import pprint
# from pprint import pprint


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
        api_key=settings.openai_api_key.get_secret_value(),
        base_url="http://localhost:8080/v1",
    )

    # client = instructor.from_openai(client)

    # pprint(body)

    chat_completion: ChatCompletion | AsyncStream[ChatCompletionChunk] = (
        await client.chat.completions.create(
            **body,
            # response_model=(
            #     ChatCompletion if not kwargs.get("stream") else ChatCompletionChunk
            # ),
            # user=user,
        )
    )

    if body.get("tool_choice", "auto") == "required":
        # if not chat_completion.choices[0].finish_reason == "tool_calls":
        #     raise ValueError("Tool calls are required but none were made")
        try:
            assert all(
                choice.finish_reason == "tool_calls"
                for choice in chat_completion.choices
            ), "Tool calls are required but none were made"

        except AssertionError as e:
            print(e)

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
