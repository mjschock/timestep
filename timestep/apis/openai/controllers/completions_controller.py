import asyncio
import json
import connexion
from typing import Dict, Iterator
from typing import Tuple
from typing import Union

from fastapi.responses import StreamingResponse
import flask
from llama_cpp.llama_types import CreateCompletionStreamResponse, CreateCompletionStreamResponse
from llama_cpp.server.types import CreateCompletionRequest
from openai import OpenAI, Stream
from openai.types.chat.chat_completion_chunk import ChatCompletionChunk
from openai.types.chat.chat_completion import ChatCompletion
from sse_starlette.sse import EventSourceResponse

from timestep.apis.openai import util
from timestep.services.model import llm

async def create_completion(body):  # noqa: E501
    """Creates a completion for the provided prompt and parameters.

     # noqa: E501

    :param create_completion_request: 
    :type create_completion_request: dict | bytes

    :rtype: Union[CreateCompletionResponse, Tuple[CreateCompletionResponse, int], Tuple[CreateCompletionResponse, int, Dict[str, str]]
    """
    # if connexion.request.is_json:
    #     create_completion_request = CreateCompletionRequest.from_dict(connexion.request.get_json())  # noqa: E501
    # return 'do some magic!'

    create_completion_request = CreateCompletionRequest(**body)
    create_completion_kwargs = create_completion_request.model_dump(
        exclude=[
            'best_of',
            'logit_bias', # ValueError: invalid literal for int() with base 10: 'key' for { "key": 1 }
            'logit_bias_type',
            'logprobs', # ValueError: logprobs is not supported for models created with logits_all=False
            'min_tokens',
            'n',
            'user',
        ]
    )

    if create_completion_request.stream:
        async def event_publisher():
            response: Iterator[CreateCompletionStreamResponse] = llm.create_completion(**create_completion_kwargs)

            try:
                for chunk in response:
                    yield json.dumps(chunk)
                    # await asyncio.sleep(0.2)

            except asyncio.CancelledError as e:
                # print(f"Disconnected from client (via refresh/close) {req.client}")
                print(f"Disconnected from client (via refresh/close)")
                # Do any other cleanup, if any
                raise e

        return EventSourceResponse(event_publisher())

    else:
        response: CreateCompletionStreamResponse = llm.create_completion(**create_completion_kwargs)

        return response
