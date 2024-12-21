import os
from typing import Dict, Optional, List
import logging

from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import StreamingResponse, JSONResponse

from ray import serve
from transformers.image_utils import load_image

from vllm.engine.arg_utils import AsyncEngineArgs
from vllm.engine.async_llm_engine import AsyncLLMEngine
from vllm.entrypoints.openai.cli_args import make_arg_parser
from vllm.entrypoints.openai.protocol import (
    # ChatCompletionRequest,
    # ChatCompletionResponse,
    ErrorResponse,
)
from vllm.entrypoints.openai.serving_chat import OpenAIServingChat
from vllm.entrypoints.openai.serving_engine import LoRAModulePath, PromptAdapterPath
from vllm.utils import FlexibleArgumentParser
from vllm.entrypoints.logger import RequestLogger
import torch
from fastapi import FastAPI
from ray import serve
from unsloth import FastVisionModel
from transformers import TextStreamer
# from mlflow.types.llm import (
#     ChatChoice,
#     ChatCompletionRequest,
#     ChatCompletionResponse,
#     ChatMessage,
#     ChatParams,
#     FunctionToolCallArguments,
#     FunctionToolDefinition,
#     ParamProperty,
#     ToolCall,
#     ToolParamsSchema,
# )
from openai.types.chat.completion_create_params import CompletionCreateParams
from pydantic import ConfigDict, TypeAdapter, ValidationError

# torch._dynamo.config.disable = True

dtype = (
    None  # None for auto detection. Float16 for Tesla T4, V100, Bfloat16 for Ampere+
)
load_in_4bit = True  # Use 4bit quantization to reduce memory usage. Can be False.
max_seq_length = 2048  # Supports RoPE Scaling interally, so choose any!
# max_seq_length = 4096 # Choose any! We auto support RoPE Scaling internally!


logger = logging.getLogger("ray.serve")

os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "expandable_segments:True"

app = FastAPI()


@serve.deployment(
    autoscaling_config={
        "min_replicas": 1,
        # "max_replicas": 10,
        "max_replicas": 1,
        "target_ongoing_requests": 5,
    },
    ray_actor_options={"num_gpus": 1},
    max_ongoing_requests=10,
)
@serve.ingress(app)
class VLLMDeployment:
    def __init__(
        self,
        model_name: str,
        # engine_args: AsyncEngineArgs,
        # response_role: str,
        # lora_modules: Optional[List[LoRAModulePath]] = None,
        # prompt_adapters: Optional[List[PromptAdapterPath]] = None,
        request_logger: Optional[RequestLogger] = None,
        # chat_template: Optional[str] = None,
    ):
        # logger.info(f"Starting with engine args: {engine_args}")
        # self.openai_serving_chat = None
        # self.engine_args = engine_args
        # self.response_role = response_role
        # self.lora_modules = lora_modules
        # self.prompt_adapters = prompt_adapters
        # self.request_logger = request_logger
        # self.chat_template = chat_template
        # self.engine = AsyncLLMEngine.from_engine_args(engine_args)

        self.model_name = model_name
        # self.model = None
        # self.processor = None

        model, processor = FastVisionModel.from_pretrained(
            load_in_4bit=load_in_4bit,
            max_seq_length=max_seq_length,
            # model_name=model_path,
            model_name=self.model_name,
        )

        FastVisionModel.for_inference(model)  # Enable native 2x faster inference

        self.model = model
        self.processor = processor

    @app.post("/v1/chat/completions")
    async def create_chat_completion(
        # self, request: ChatCompletionRequest, raw_request: Request
        # self, request: CompletionCreateParams, raw_request: Request
        self, request: dict, raw_request: Request
    ):
        """OpenAI-compatible HTTP endpoint.

        API reference:
            - https://docs.vllm.ai/en/latest/serving/openai_compatible_server.html
        """
        # if not self.openai_serving_chat:
        #     model_config = await self.engine.get_model_config()
        #     # Determine the name of the served model for the OpenAI client.
        #     if self.engine_args.served_model_name is not None:
        #         served_model_names = self.engine_args.served_model_name
        #     else:
        #         served_model_names = [self.engine_args.model]
        #     self.openai_serving_chat = OpenAIServingChat(
        #         self.engine,
        #         model_config,
        #         served_model_names,
        #         self.response_role,
        #         lora_modules=self.lora_modules,
        #         prompt_adapters=self.prompt_adapters,
        #         request_logger=self.request_logger,
        #         chat_template=self.chat_template,
        #     )
        # logger.info(f"Request: {request}")
        # generator = await self.openai_serving_chat.create_chat_completion(
        #     request, raw_request
        # )

        print('request:')
        print(request)

        print('raw_request:')
        print(raw_request)

        ta = TypeAdapter(CompletionCreateParams)

        print('ta.validate_python...')
        print(ta.validate_python(request))

        # add_generation_prompt = request.add_generation_prompt
        # documents = request.documents
        # messages = request.messages
        messages = request.get('messages')
        # max_completion_tokens = request.max_completion_tokens
        # max_tokens = request.max_tokens
        max_tokens = request.get('max_tokens')
        # model = request.model
        model = request.get('model')
        # temperature = request.temperature
        temperature = request.get('temperature')
        # tools = request.tools
        tools = request.get('tools')

        # print('add_generation_prompt:')
        # print(add_generation_prompt)

        print('messages:')
        print(messages)

        # print('max_completion_tokens:')
        # print(max_completion_tokens)

        print('max_tokens:')
        print(max_tokens)

        print('model:')
        print(model)

        print('temperature:')
        print(temperature)

        print('tools:')
        print(tools)

        # if not self.model:
        #     print('=== Loading model ===')
        #     # model_path = "/root/sky_workdir/lora_model"

        #     model, processor = FastVisionModel.from_pretrained(
        #         load_in_4bit=load_in_4bit,
        #         max_seq_length=max_seq_length,
        #         # model_name=model_path,
        #         model_name=self.model_name,
        #     )

        #     FastVisionModel.for_inference(model)  # Enable native 2x faster inference

        #     self.model = model
        #     self.processor = processor

        if model != self.model_name:
            return JSONResponse(
                content={"error": "Model not found"}, status_code=404
            )

        images = []

        for message in messages:
            for content in message['content']:
                if content['type'] == 'image_url':
                    image_url = content['image_url']['url']
                    image = load_image(image_url)
                    images.append(image)

                    content['type'] = 'image'
                    del content['image_url']

        print('images:')
        print(images)

        print('messages:')
        print(messages)

        prompt = self.processor.apply_chat_template(
            add_generation_prompt=True,
            # add_generation_prompt=add_generation_prompt,
            conversation=messages,
            # documents=documents,
            # return_tensors="pt",
            # tokenize=True,
            # tokenize=False,
            # tools=tools,
            # ).to(device)
        # ).to(self.model.device)
        )

        print('prompt:')
        print(prompt)

        print('=== Processing inputs ===')

        # inputs = self.processor.apply_chat_template(
        #     add_generation_prompt=True,
        #     # add_generation_prompt=add_generation_prompt,
        #     conversation=messages,
        #     # documents=documents,
        #     return_tensors="pt",
        #     tokenize=True,
        #     tools=tools,
        #     # ).to(device)
        # ).to(self.model.device)

        inputs = self.processor(text=prompt, images=images, return_tensors="pt")
        inputs = inputs.to(self.model.device)

        print('inputs:')
        print(inputs)

        # torch._dynamo.config.disable = True

        # text_streamer = TextStreamer(tokenizer, skip_prompt = True)
        # text_streamer = TextStreamer(self.processor, skip_prompt = True)

        print('=== Generating outputs ===')

        import torch

        try:
            generated_ids = self.model.generate(
                **inputs,
                # do_sample=False,
                # input_ids=inputs,
                # max_new_tokens=256,
                max_new_tokens=max_tokens,
                # use_cache=True,
                # temperature=temperature,
            )

        except torch._dynamo.exc.BackendCompilerFailed as e:
            print('=== BackendCompilerFailed ===')
            print(e)

            print('=== Disabling dynamo ===')

            import torch._dynamo.config
            torch._dynamo.config.disable = True

            generated_ids = self.model.generate(
                **inputs,
                # do_sample=False,
                # input_ids=inputs,
                # max_new_tokens=256,
                max_new_tokens=max_tokens,
                # use_cache=True,
                # temperature=temperature,
            )

        print('generated_ids:')
        print(generated_ids)

        batch_decoded_outputs = self.processor.batch_decode(
            generated_ids,
            skip_special_tokens=True,
        )

        print('batch_decoded_outputs:')
        print(batch_decoded_outputs)

        # if isinstance(generator, ErrorResponse):
        #     return JSONResponse(
        #         content=generator.model_dump(), status_code=generator.code
        #     )

        # if request.stream:
        #     return StreamingResponse(content=generator, media_type="text/event-stream")

        # else:
        #     assert isinstance(generator, ChatCompletionResponse)
        #     return JSONResponse(content=generator.model_dump())


def parse_vllm_args(cli_args: Dict[str, str]):
    """Parses vLLM args based on CLI inputs.

    Currently uses argparse because vLLM doesn't expose Python models for all of the
    config options we want to support.
    """
    arg_parser = FlexibleArgumentParser(
        description="vLLM OpenAI-Compatible RESTful API server."
    )

    parser = make_arg_parser(arg_parser)
    arg_strings = []
    for key, value in cli_args.items():
        arg_strings.extend([f"--{key}", str(value)])
    logger.info(arg_strings)
    parsed_args = parser.parse_args(args=arg_strings)
    return parsed_args


def build_app(cli_args: Dict[str, str]) -> serve.Application:
    """Builds the Serve app based on CLI arguments.

    See https://docs.vllm.ai/en/latest/serving/openai_compatible_server.html#command-line-arguments-for-the-server
    for the complete set of arguments.

    Supported engine arguments: https://docs.vllm.ai/en/latest/models/engine_args.html.
    """  # noqa: E501
    # if "accelerator" in cli_args.keys():
    #     accelerator = cli_args.pop("accelerator")
    # else:
    #     accelerator = "GPU"
    # parsed_args = parse_vllm_args(cli_args)
    # engine_args = AsyncEngineArgs.from_cli_args(parsed_args)
    # engine_args.worker_use_ray = True

    # tp = engine_args.tensor_parallel_size
    # logger.info(f"Tensor parallelism = {tp}")
    # pg_resources = []
    # pg_resources.append({"CPU": 1})  # for the deployment replica
    # for i in range(tp):
    #     pg_resources.append({"CPU": 1, accelerator: 1})  # for the vLLM actors

    # print('pg_resources:')
    # print(pg_resources)
    # print('parsed_args:')
    # print(parsed_args)

    print('cli_args:')
    print(cli_args)

    # We use the "STRICT_PACK" strategy below to ensure all vLLM actors are placed on
    # the same Ray node.
    return VLLMDeployment.options(
        # placement_group_bundles=pg_resources, placement_group_strategy="STRICT_PACK"
    ).bind(
        # engine_args,
        cli_args.get("model_name"),
        # parsed_args.response_role,
        # parsed_args.lora_modules,
        # parsed_args.prompt_adapters,
        cli_args.get("request_logger"),
        # parsed_args.chat_template,
    )
