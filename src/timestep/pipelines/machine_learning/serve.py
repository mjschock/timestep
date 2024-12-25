import asyncio
import logging
import os
import time
from pprint import pprint
from threading import Thread
from typing import Any, Dict, List

from fastapi import FastAPI, Request
from openai.types.chat.chat_completion import ChatCompletion
from openai.types.chat.chat_completion import Choice as ChatCompletionChoice
from openai.types.chat.chat_completion_chunk import ChatCompletionChunk
from openai.types.chat.chat_completion_chunk import Choice as ChatCompletionChunkChoice
from openai.types.chat.chat_completion_chunk import ChoiceDelta
from openai.types.chat.chat_completion_message import ChatCompletionMessage
from openai.types.chat.completion_create_params import CompletionCreateParams
from pydantic import TypeAdapter
from ray import serve
from sse_starlette import EventSourceResponse
from starlette.responses import JSONResponse
from transformers.generation.streamers import AsyncTextIteratorStreamer
from transformers.image_utils import load_image
from unsloth import FastVisionModel

dtype = (
    None  # None for auto detection. Float16 for Tesla T4, V100, Bfloat16 for Ampere+
)
load_in_4bit = True  # Use 4bit quantization to reduce memory usage. Can be False.
max_seq_length = 2048  # Supports RoPE Scaling interally, so choose any!
# max_seq_length = 4096 # Choose any! We auto support RoPE Scaling internally!


logger = logging.getLogger("ray.serve")

os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "expandable_segments:True"

app = FastAPI()

# middlewares = [
#     middleware
#     for middleware in ConnexionMiddleware.default_middlewares
#     if middleware is not SecurityMiddleware
# ]

# connexion_app = AsyncApp(import_name=__name__, middlewares=middlewares)

# connexion_app.add_api(
#     # "api/openai/v1/openapi/openapi.yaml",
#     "api/v1/openapi/openapi.yaml",
#     # base_path="/openai/v1",
#     base_path="/v1",
#     pythonic_params=True,
#     resolver_error=501,
# )

# # fastapi_app.mount("/api", ConnexionMiddleware(app=connexion_app, import_name=__name__))
# # app.mount("/api", ConnexionMiddleware(app=connexion_app, import_name=__name__))
# app.mount(
#     "/",
#     ConnexionMiddleware(
#         app=connexion_app,
#         import_name=__name__,
#         # middlewares=middlewares,
#     ),
# )


@serve.deployment(
    autoscaling_config={
        # https://docs.ray.io/en/latest/serve/advanced-guides/advanced-autoscaling.html#required-define-upper-and-lower-autoscaling-limits
        "max_replicas": 1,
        "min_replicas": 1,  # TOOD: set to 0
        "target_ongoing_requests": 2,  # https://docs.ray.io/en/latest/serve/advanced-guides/advanced-autoscaling.html#target-ongoing-requests-default-2
    },
    max_ongoing_requests=5,  # https://docs.ray.io/en/latest/serve/advanced-guides/advanced-autoscaling.html#max-ongoing-requests-default-5
    ray_actor_options={"num_gpus": 1},
)
@serve.ingress(app)
class ModelDeployment:
    def __init__(
        self,
        model_name: str,
    ):
        self.model_name = model_name

        model, processor = FastVisionModel.from_pretrained(
            load_in_4bit=load_in_4bit,
            max_seq_length=max_seq_length,
            model_name=self.model_name,
        )

        with open("chat_template.txt", "r") as f:
            processor.chat_template = f.read()
            processor.tokenizer.chat_template = processor.chat_template

        FastVisionModel.for_inference(model)  # Enable native 2x faster inference

        self.model = model
        self.processor = processor

    def reconfigure(self, config: Dict[str, Any]):
        print("=== reconfigure ===")
        print("config:")
        print(config)
        # https://docs.ray.io/en/latest/serve/production-guide/config.html#dynamically-change-parameters-without-restarting-replicas-user-config

    @app.post("/v1/chat/completions")
    async def create_chat_completion(self, body: dict, raw_request: Request):
        """Creates a model response for the given chat conversation. Learn more in the [text generation](/docs/guides/text-generation), [vision](/docs/guides/vision), and [audio](/docs/guides/audio) guides.  Parameter support can differ depending on the model used to generate the response, particularly for newer reasoning models. Parameters that are only supported for reasoning models are noted below. For the current state of  unsupported parameters in reasoning models,  [refer to the reasoning guide](/docs/guides/reasoning).

        # noqa: E501

        :param create_chat_completion_request:
        :type create_chat_completion_request: dict | bytes

        :rtype: Union[CreateChatCompletionResponse, Tuple[CreateChatCompletionResponse, int], Tuple[CreateChatCompletionResponse, int, Dict[str, str]]
        """
        print("=== create_chat_completion ===")

        print("body:")
        pprint(body)

        ta = TypeAdapter(CompletionCreateParams)

        print("ta.validate_python...")
        pprint(ta.validate_python(body))

        max_new_tokens = body.get("max_completion_tokens", body.get("max_tokens"))
        messages = body.get("messages")
        model_name = body.get("model")
        stream = body.get("stream", False)
        temperature = body.get("temperature")
        tools = body.get("tools")

        images = []

        for message in messages:
            for content in message["content"]:
                if "type" in content and content["type"] == "image_url":
                    image_url = content["image_url"]["url"]
                    image = load_image(image_url)
                    images.append(image)

                    content["type"] = "image"
                    del content["image_url"]

        images = images if images else None

        if model_name != self.model_name:
            return JSONResponse(content={"error": "Model not found"}, status_code=404)

        prompt = self.processor.apply_chat_template(
            add_generation_prompt=True,
            conversation=messages,
            # documents=documents,
            tools=tools,
        )

        inputs = self.processor(text=prompt, images=images, return_tensors="pt")
        inputs = inputs.to(self.model.device)
        input_ids = inputs.input_ids

        class GeneratorThread(Thread):
            """Thread to generate completions in the background."""

            def __init__(self, model, **generation_kwargs):
                super().__init__()

                self.chat_completion = None
                self.generation_kwargs = generation_kwargs
                self.model = model

            def run(self):
                import torch
                import torch._dynamo.config

                try:
                    try:
                        self.generated_ids = self.model.generate(
                            **self.generation_kwargs
                        )

                    except torch._dynamo.exc.BackendCompilerFailed as e:
                        print(e)
                        print("Disabling dynamo...")

                        torch._dynamo.config.disable = True

                        self.generated_ids = self.model.generate(
                            **self.generation_kwargs
                        )

                except Exception as e:
                    print(e)
                    print("Warning: Exception in GeneratorThread")
                    self.generated_ids = []

            def join(self, timeout=None):
                super().join()

                return self.generated_ids

        decode_kwargs = dict(skip_special_tokens=True)

        streamer = (
            AsyncTextIteratorStreamer(
                self.processor,
                skip_prompt=True,
                **decode_kwargs,
            )
            if stream
            else None
        )

        generation_kwargs = dict(
            **inputs,
            max_new_tokens=max_new_tokens,
            streamer=streamer,
            temperature=temperature,
            use_cache=True,
        )

        thread = GeneratorThread(self.model, **generation_kwargs)
        thread.start()

        if stream:

            async def event_publisher():
                i = 0

                try:
                    async for new_text in streamer:
                        choices: List[ChatCompletionChunkChoice] = [
                            ChatCompletionChunkChoice(
                                _request_id=None,
                                delta=ChoiceDelta(
                                    _request_id=None,
                                    content=new_text,
                                    function_call=None,
                                    refusal=None,
                                    role="assistant",
                                    tool_calls=None,
                                ),
                                finish_reason=None,
                                index=0,
                                logprobs=None,
                            )
                        ]

                        chat_completion_chunk = ChatCompletionChunk(
                            _request_id=None,
                            choices=choices,
                            created=int(time.time()),
                            id=str(i),
                            model=model_name,
                            object="chat.completion.chunk",
                            service_tier=None,
                            system_fingerprint=None,
                            usage=None,
                        )

                        yield chat_completion_chunk.model_dump_json()

                        i += 1

                except asyncio.CancelledError as e:
                    print("Disconnected from client (via refresh/close)")
                    raise e

                except Exception as e:
                    print(f"Exception: {e}")
                    raise e

            return EventSourceResponse(event_publisher())

        generated_ids = thread.join()
        input_length = input_ids.shape[1]

        batch_decoded_outputs = self.processor.batch_decode(
            generated_ids[:, input_length:],
            skip_special_tokens=True,
        )

        choices: List[ChatCompletionChoice] = []

        for i, response in enumerate(batch_decoded_outputs):
            # try:
            # response = json.loads(response)

            #         finish_reason: str = response.get("finish_reason")
            #         tool_calls_json = response.get("tool_calls")
            #         tool_calls: List[ToolCall] = []

            #         for tool_call_json in tool_calls_json:
            #             tool_call = ToolCall(
            #                 function=FunctionToolCallArguments(
            #                     arguments=tool_call_json.get("arguments"),
            #                     name=tool_call_json.get("name"),
            #                 ),
            #                 id=tool_call_json.get("id"),
            #                 type="function",
            #             )

            #             tool_calls.append(tool_call)

            #         message: ChatMessage = ChatMessage(
            #             role="assistant",
            #             tool_calls=tool_calls,
            #         )

            #     except json.JSONDecodeError:
            #         finish_reason: str = "stop"
            #         message: ChatMessage = ChatMessage(
            #             role="assistant",
            #             content=response,
            #         )

            message = ChatCompletionMessage(
                audio=None,
                content=response,
                refusal=None,
                role="assistant",
                tool_calls=None,
            )

            choices.append(
                ChatCompletionChoice(
                    index=i,
                    finish_reason="stop",
                    logprobs=None,
                    message=message,
                )
            )

        chat_completion = ChatCompletion(
            choices=choices,
            created=int(time.time()),
            id="1",
            model=model_name,
            object="chat.completion",
            service_tier=None,
            system_fingerprint=None,
            usage=None,
        )

        return chat_completion.model_dump(mode="json")


def build_app(cli_args: Dict[str, str]) -> serve.Application:
    """Builds the Serve app based on CLI arguments."""
    return ModelDeployment.options().bind(
        cli_args.get("model_name"),
    )
