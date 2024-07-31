import asyncio
import json
from typing import Iterator

from llama_cpp import Llama
from llama_cpp.llama_types import CreateCompletionStreamResponse
from llama_cpp.server.types import CreateCompletionRequest
from openai.types.completion import Completion
from sse_starlette import EventSourceResponse

from timestep.services import agent_service

model_instance_store = agent_service.ModelInstanceStoreSingleton()


# @flow(log_prints=True)
async def create_completion(body, token_info: dict, user: str):  # noqa: E501
    """Creates a completion for the provided prompt and parameters.

     # noqa: E501

    :param create_completion_request:
    :type create_completion_request: dict | bytes

    :rtype: Union[CreateCompletionResponse, Tuple[CreateCompletionResponse, int], Tuple[CreateCompletionResponse, int, Dict[str, str]]
    """
    # if connexion.request.is_json:
    #     create_completion_request = CreateCompletionRequest.from_dict(connexion.request.get_json())  # noqa: E501
    # raise NotImplementedError

    # print(f'=== ENTER: {__name__}.create_completion(body, token_info: dict, user: str) ===')
    # pprint.pp({
    #     "body": body,
    #     "token_info": token_info,
    #     "user": user,
    # })

    create_completion_request = CreateCompletionRequest(**body)
    create_completion_kwargs = create_completion_request.model_dump(
        exclude=[
            "best_of",
            "logit_bias",  # ValueError: invalid literal for int() with base 10: 'key' for { "key": 1 }
            "logit_bias_type",
            "logprobs",  # ValueError: logprobs is not supported for models created with logits_all=False
            "min_tokens",
            "n",
            "user",
        ]
    )
    # instance_store = InstanceStoreSingleton()
    # model: Llama = instance_store._shared_instance_state["models"][create_completion_request.model]
    # model: Llama = agent_service.get_default_agent().get_model(create_completion_request.model)
    model: Llama = model_instance_store._shared_model_instances[
        create_completion_request.model
    ]

    if create_completion_request.stream:

        async def event_publisher():
            response: Iterator[CreateCompletionStreamResponse] = (
                model.create_completion(**create_completion_kwargs)
            )

            try:
                for chunk in response:
                    # chunk = Completion(**chunk)
                    # chunk = Stream
                    yield json.dumps(chunk)
                    # yield json.dumps(chunk.model_dump(mode="json"))
                    # await asyncio.sleep(0.2)

            except asyncio.CancelledError as e:
                # print(f"Disconnected from client (via refresh/close) {req.client}")
                print(f"Disconnected from client (via refresh/close)")
                # Do any other cleanup, if any
                raise e

        # print(f'=== RETURN: {__name__}.create_completion(body, token_info: dict, user: str) ===')
        return EventSourceResponse(event_publisher())

    else:
        response: CreateCompletionStreamResponse = model.create_completion(
            **create_completion_kwargs
        )
        completion = Completion(**response)

        # print(f'=== RETURN: {__name__}.create_completion(body, token_info: dict, user: str) ===')
        return completion.model_dump(mode="json")
