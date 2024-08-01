import asyncio
import json
import pprint
from typing import Iterator

import openai

# from llama_cpp import CreateChatCompletionStreamResponse, Llama
# from llama_cpp.server.types import CreateChatCompletionRequest
from langchain_community.llms.llamafile import Llamafile
from openai import AsyncOpenAI, AsyncStream, Stream
from openai.types.chat.chat_completion import ChatCompletion
from openai.types.chat.chat_completion_chunk import ChatCompletionChunk
from openai.types.chat.completion_create_params import CompletionCreateParams
from sse_starlette import EventSourceResponse

from timestep.services.agent_service import ModelInstanceStoreSingleton

model_instance_store = ModelInstanceStoreSingleton()


async def create_chat_completion(
    body: CompletionCreateParams, token_info: dict, user: str, **kwargs
):
    """Creates a model response for the given chat conversation.

     # noqa: E501

    :param create_chat_completion_request:
    :type create_chat_completion_request: dict | bytes

    :rtype: Union[CreateChatCompletionResponse, Tuple[CreateChatCompletionResponse, int], Tuple[CreateChatCompletionResponse, int, Dict[str, str]]
    """
    # if connexion.request.is_json:
    # create_chat_completion_request = CreateChatCompletionRequest.from_dict(connexion.request.get_json())  # noqa: E501
    print(
        f"=== ENTER: {__name__}.create_chat_completion(body: CompletionCreateParams, token_info: dict, user: str)) ==="
    )
    pprint.pp(
        {
            "body": body,
            "kwargs": kwargs,
            "token_info": token_info,
            "user": user,
        },
        compact=True,
        width=160,
    )

    # completion_create_params = CompletionCreateParams(**body)
    # print('completion_create_params:', completion_create_params)

    # if body.get("stream", False):
    #     completion_create_params = CompletionCreateParamsStreaming(**body)

    # else:
    #     completion_create_params = CompletionCreateParamsNonStreaming(**body)

    # TODO: does LangChain's LLamaCpp support mmproj models? Also, what's the best practice for converting response to OpenAI's ChatCompletion?
    # chat_prompt_template = ChatPromptTemplate.from_messages([
    #     ("system", "You are a helpful assistant"), # TODO: message history from user
    #     MessagesPlaceholder("msgs")
    # ])

    # # Callbacks support token-wise streaming
    # callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])

    # llm_kwargs = {
    #     # "chat_format": "nanollava",
    #     # "clip_model_path": "nanollava-mmproj-f16.gguf",
    #     # "embedding": False,
    #     # "hf_model_repo_id": "abetlen/nanollava-gguf",
    #     # "model": "nanollava-text-model-f16.gguf",
    #     # "model_alias": "nanoLLaVA",
    #     # "model_path": "models/mofosyne/TinyLLama-v0-5M-F16-llamafile/Tinyllama-5M-v0.2-F16.gguf",
    #     "n_ctx": 2048,
    #     "verbose": True,
    # }

    # # Make sure the model path is correct for your system!
    # model = LlamaCpp(
    #     callback_manager=callback_manager,
    #     grammar_path="timestep/grammers/json.gbnf",
    #     # model_path="models/mofosyne/TinyLLama-v0-5M-F16-llamafile/Tinyllama-5M-v0.2-F16.gguf",
    #     model_path="models/abetlen/nanollava-gguf/nanollava-text-model-f16.gguf",
    #     streaming=True, # default is True...
    #     # temperature=0.0,
    #     # # max_tokens=2048,
    #     # # top_p=1,
    #     # callback_manager=callback_manager,
    #     # verbose=True,  # Verbose is required to pass to the callback manager
    #     **llm_kwargs,
    # )

    # chain: Chain = chat_prompt_template | model

    # if completion_create_params.get("stream", False):
    #     async for event in chain.astream_events({"msgs": completion_create_params.get("messages")}, version="v2"):
    #         kind = event["event"]

    #         if kind == "on_chat_model_stream":
    #             print(event, end="|", flush=True)

    #         raise NotImplementedError("Streaming is not supported yet")

    # else:
    #     result = await chain.ainvoke({"msgs": completion_create_params.get("messages")})
    #     print('result:', result)

    # return result

    # create_chat_completion_request = CreateChatCompletionRequest(**body)
    # create_chat_completion_kwargs = create_chat_completion_request.model_dump(
    #     exclude=[
    #         "logit_bias_type",
    #         "min_tokens",
    #         "n",
    #         "user",
    #     ]
    # )
    # messages = create_chat_completion_request.messages

    # instance_store = InstanceStoreSingleton()
    # model: Llama = model_instance_store._shared_model_instances[
    #     create_chat_completion_request.model
    # ]

    # if create_chat_completion_request.stream:

    #     async def event_publisher():
    #         response: Iterator[CreateChatCompletionStreamResponse] = (
    #             model.create_chat_completion(**create_chat_completion_kwargs)
    #         )
    #         # response: Generator[ChatCompletionChunk] = model.create_chat_completion_openai_v1(**create_chat_completion_kwargs)
    #         # response: Stream[ChatCompletionChunk] = model.astream(input=messages)

    #         try:
    #             for chunk in response:
    #                 # async for chunk in response:
    #                 chunk = ChatCompletionChunk(**chunk)
    #                 # yield json.dumps(chunk)
    #                 yield json.dumps(chunk.model_dump(mode="json"))
    #                 # yield ChatCompletionChunk(**chunk).model_dump(mode="json")
    #                 # yield chunk.model_dump(mode="json")

    #         except asyncio.CancelledError as e:
    #             # print(f"Disconnected from client (via refresh/close) {req.client}")
    #             print(f"Disconnected from client (via refresh/close)")
    #             # Do any other cleanup, if any
    #             raise e

    #     # print(f'=== RETURN: {__name__}.create_chat_completion(body: CompletionCreateParams, token_info: dict, user: str)) ===')
    #     return EventSourceResponse(event_publisher())

    # else:
    #     # response: CreateChatCompletionResponse = model.create_chat_completion(**create_chat_completion_kwargs)
    #     response: ChatCompletion = model.create_chat_completion_openai_v1(
    #         **create_chat_completion_kwargs
    #     )

    #     # print(f'=== RETURN: {__name__}.create_chat_completion(body: CompletionCreateParams, token_info: dict, user: str)) ===')
    #     return response.model_dump(mode="json")

    # model: Llamafile = model_instance_store._shared_model_instances[body.get("model")]

    # if body.get("stream", False):
    #     raise NotImplementedError("Streaming is not supported yet")

    # else:
    #     response = await model.ainvoke(
    #         # input=body.get("messages"),
    #         # kwargs={
    #         #     "max_tokens": body.get("max_tokens"),
    #         #     "temperature": body.get("temperature"),
    #         # }
    #         kwargs=body,
    #     )
    #     print("response:", response)
    #     return response

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
