import json
from typing import List

import mlflow
import torch
from mlflow.entities.span import SpanType
from mlflow.models import set_model
from mlflow.types.llm import (
    ChatChoice,
    ChatCompletionResponse,
    ChatMessage,
    ChatParams,
    FunctionToolCallArguments,
    FunctionToolDefinition,
    ParamProperty,
    ToolCall,
    ToolParamsSchema,
)
from unsloth import FastVisionModel

torch._dynamo.config.disable = True

dtype = (
    None  # None for auto detection. Float16 for Tesla T4, V100, Bfloat16 for Ampere+
)
load_in_4bit = True  # Use 4bit quantization to reduce memory usage. Can be False.
max_seq_length = 2048  # Supports RoPE Scaling interally, so choose any!
# max_seq_length = 4096 # Choose any! We auto support RoPE Scaling internally!


class ModelClient:
    def __init__(self, model_path):
        model, processor = FastVisionModel.from_pretrained(
            load_in_4bit=load_in_4bit,
            max_seq_length=max_seq_length,
            model_name=model_path,
        )

        FastVisionModel.for_inference(model)  # Enable native 2x faster inference

        self.model = model
        self.processor = processor

    def chat_completion_request(
        self,
        documents: list,
        messages: list,
        tools: list,
    ):
        # FastLanguageModel.for_inference(model)  # Enable native 2x faster inference
        print("Calling model.generate()...")

        inputs = self.processor.apply_chat_template(
            add_generation_prompt=True,
            conversation=messages,
            documents=documents,
            return_tensors="pt",
            tokenize=True,
            tools=tools,
            # ).to(device)
        ).to(self.model.device)

        outputs = self.model.generate(
            do_sample=False,
            input_ids=inputs,
            max_new_tokens=256,
            use_cache=True,
            # temperature=0.0,
        )

        batch_decoded_outputs = self.processor.batch_decode(outputs)

        choices: List[ChatChoice] = []

        for i in range(len(batch_decoded_outputs)):
            response = batch_decoded_outputs[i][len(self.processor.decode(inputs[i])) :]
            # ].replace(
            # self.processor.eos_token, ""
            # )  # TODO: skip special tokens when decoding instead?

            try:
                response = json.loads(response)

                finish_reason: str = response.get("finish_reason")
                tool_calls_json = response.get("tool_calls")
                tool_calls: List[ToolCall] = []

                for tool_call_json in tool_calls_json:
                    tool_call = ToolCall(
                        function=FunctionToolCallArguments(
                            arguments=tool_call_json.get("arguments"),
                            name=tool_call_json.get("name"),
                        ),
                        id=tool_call_json.get("id"),
                        type="function",
                    )

                    tool_calls.append(tool_call)

                message: ChatMessage = ChatMessage(
                    role="assistant",
                    tool_calls=tool_calls,
                )

            except json.JSONDecodeError:
                finish_reason: str = "stop"
                message: ChatMessage = ChatMessage(
                    role="assistant",
                    content=response,
                )

            choices.append(
                ChatChoice(
                    index=i,
                    finish_reason=finish_reason,
                    logprobs=None,
                    message=message,
                )
            )

        return ChatCompletionResponse(
            choices=choices,
        )


class WeatherModel(mlflow.pyfunc.ChatModel):
    def __init__(self):
        self.model_name = "llama3.2:1b"
        self.client = None

        weather_tool = FunctionToolDefinition(
            name="get_weather",
            description="Get weather information",
            parameters=ToolParamsSchema(
                {
                    "city": ParamProperty(
                        type="string",
                        description="City name to get weather information for",
                    ),
                }
            ),
        ).to_tool_definition()

        self.tools = [weather_tool.to_dict()]

    @mlflow.trace(span_type=SpanType.TOOL)
    def get_weather(self, city: str) -> str:
        return "It's sunny in {}, with a temperature of 20C".format(city)

    def load_context(self, context):
        print("Loading context...")

        print("context.artifacts:")
        print(context.artifacts)

        print("context.model_config:")
        print(context.model_config)

        # self.client = OpenAI()
        # self.client = ollama.Client()
        self.client = ModelClient(
            # model_path=context["snapshot"],
            model_path=context.artifacts["snapshot"],
        )

    @mlflow.trace(span_type=SpanType.AGENT)
    def predict(self, context, messages: list[ChatMessage], params: ChatParams):
        # client = OpenAI()

        messages = [m.to_dict() for m in messages]

        # chat_completion_request = ChatCompletionRequest(
        #     # documents=[],
        #     messages=messages,
        #     tools=self.tools,
        # )

        # response = self.client.chat.completions.create(
        response = self.client.chat_completion_request(
            # model="gpt-4o-mini",
            documents=[],
            messages=messages,
            tools=self.tools,
        )

        tool_calls = response.choices[0].message.tool_calls
        if tool_calls:
            print("Received a tool call, calling the weather tool...")

            city = json.loads(tool_calls[0].function.arguments)["city"]
            tool_call_id = tool_calls[0].id

            tool_response = ChatMessage(
                role="tool",
                content=self.get_weather(city),
                tool_call_id=tool_call_id,
            ).to_dict()

            messages.append(response.choices[0].message)
            messages.append(tool_response)
            # response = self.client.chat.completions.create(
            response = self.client.chat_completion_request(
                model="gpt-4o-mini",
                messages=messages,
                tools=self.tools,
            )

        # return ChatResponse.from_dict(response.to_dict())
        return ChatCompletionResponse.from_dict(response.to_dict())


# https://mlflow.org/docs/latest/_modules/mlflow/models/model.html#set_model
set_model(WeatherModel())
