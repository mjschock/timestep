import asyncio
import os

from openai import AsyncOpenAI, AsyncStream
from openai.types.create_embedding_response import CreateEmbeddingResponse
from sse_starlette import EventSourceResponse

from timestep.config import settings


async def create_embedding(body, token_info: dict, user: str, **kwargs):
    """Creates an embedding vector representing the input text.

    :param create_embedding_request:
    :type create_embedding_request: dict | bytes

    :rtype: Union[CreateEmbeddingResponse, Tuple[CreateEmbeddingResponse, int], Tuple[CreateEmbeddingResponse, int, Dict[str, str]]
    """
    print("=== create_embedding ===")
    # print('args:', args)
    print("body:", body)
    print("kwargs:", kwargs)

    client = AsyncOpenAI(
        api_key=settings.openai_api_key.get_secret_value(),
        base_url="http://localhost:8080/v1",
    )

    # completion: Completion | AsyncStream[Completion] = await client.completions.create(
    create_embedding_response: (
        CreateEmbeddingResponse | AsyncStream[CreateEmbeddingResponse]
    ) = await client.embeddings.create(
        **body,
        # user=user,
    )

    if type(create_embedding_response) == AsyncStream:

        async def event_publisher():
            try:
                async for chunk in create_embedding_response:
                    yield chunk.model_dump_json()

            except asyncio.CancelledError as e:
                print(f"Disconnected from client (via refresh/close)")
                # Do any other cleanup, if any
                raise e

        return EventSourceResponse(event_publisher())

    else:
        return create_embedding_response.model_dump(mode="json")
