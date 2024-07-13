import asyncio
import json
import connexion
from typing import Dict, Iterator
from typing import Tuple
from typing import Union

from fastapi.responses import StreamingResponse
import flask
from llama_cpp.llama_types import CreateChatCompletionResponse, CreateChatCompletionStreamResponse
from llama_cpp.server.types import CreateChatCompletionRequest
from openai import OpenAI, Stream
from openai.types.chat.chat_completion_chunk import ChatCompletionChunk
from openai.types.chat.chat_completion import ChatCompletion
from sse_starlette.sse import EventSourceResponse

# from timestep.apis.openai.models.create_chat_completion_request import CreateChatCompletionRequest  # noqa: E501
# from timestep.apis.openai.models.create_chat_completion_response import CreateChatCompletionResponse  # noqa: E501
from timestep.apis.openai import util
from timestep.services.model import llm

async def create_chat_completion(body): # req: Request
    """Creates a model response for the given chat conversation.

     # noqa: E501

    :param create_chat_completion_request: 
    :type create_chat_completion_request: dict | bytes

    :rtype: Union[CreateChatCompletionResponse, Tuple[CreateChatCompletionResponse, int], Tuple[CreateChatCompletionResponse, int, Dict[str, str]]
    """
    # if connexion.request.is_json:
    #     create_chat_completion_request = CreateChatCompletionRequest.from_dict(connexion.request.get_json())  # noqa: E501

    create_chat_completion_request = CreateChatCompletionRequest(**body)
    create_chat_completion_kwargs = create_chat_completion_request.model_dump(
        exclude=[
            'logit_bias_type',
            'min_tokens',
            'n',
            'user',
        ]
    )

    if create_chat_completion_request.stream:
        async def event_publisher():
            response: Iterator[CreateChatCompletionStreamResponse] = llm.create_chat_completion(**create_chat_completion_kwargs)

            try:
                for chunk in response:
                    yield json.dumps(chunk)

            except asyncio.CancelledError as e:
                # print(f"Disconnected from client (via refresh/close) {req.client}")
                print(f"Disconnected from client (via refresh/close)")
                # Do any other cleanup, if any
                raise e

        return EventSourceResponse(event_publisher())

    else:
        response: CreateChatCompletionResponse = llm.create_chat_completion(**create_chat_completion_kwargs)

        return response
