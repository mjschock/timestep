import asyncio
import os

from openai import AsyncOpenAI, AsyncStream
from openai.types.completion import Completion
from sse_starlette import EventSourceResponse

from timestep.config import settings


async def create_completion(body, token_info: dict, user: str):
    """Creates a completion for the provided prompt and parameters.

    :param create_completion_request:
    :type create_completion_request: dict | bytes

    :rtype: Union[CreateCompletionResponse, Tuple[CreateCompletionResponse, int], Tuple[CreateCompletionResponse, int, Dict[str, str]]
    """
    client = AsyncOpenAI(
        api_key=settings.openai_api_key.get_secret_value(),
        base_url="http://localhost:8080/v1",
    )

    completion: Completion | AsyncStream[Completion] = await client.completions.create(
        **body,
        # user=user,
    )

    if type(completion) == AsyncStream:

        async def event_publisher():
            try:
                async for chunk in completion:
                    yield chunk.model_dump_json()

            except asyncio.CancelledError as e:
                print(f"Disconnected from client (via refresh/close)")
                # Do any other cleanup, if any
                raise e

        return EventSourceResponse(event_publisher())

    else:
        return completion.model_dump(mode="json")
