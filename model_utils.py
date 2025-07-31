# ruff: noqa: S101

import json
from typing import Any

import torch
from peft import LoraConfig, TaskType, get_peft_model, prepare_model_for_kbit_training
from transformers import (
    AutoModelForImageTextToText,
    AutoProcessor,
    BitsAndBytesConfig,
    StoppingCriteria,
)

from constants import DEFAULT_N_SHOT, DEFAULT_SYSTEM_MESSAGE, DEFAULT_TOOLS

# Global model and processor instances
MODEL_PATH = "HuggingFaceTB/SmolVLM2-256M-Video-Instruct"
PROCESSOR = None
MODEL = None


def _create_system_message(system_parts: list[str]) -> dict[str, Any]:
    return {
        "role": "system",
        "content": [{"type": "text", "text": "\n\n".join(system_parts)}],
    }


def _create_n_shot_example(n: int = 0) -> str:
    if n == 0:
        return ""

    examples = [
        "User: How many r's are in the word 'strawberry'?<end_of_utterance>\nAssistant: <tool_call>\n{\"arguments\": {\"code\": \"'strawberry'.count('r')\"}, \"name\": \"code_interpreter\"}\n</tool_call><end_of_utterance>\nTool: 3<end_of_utterance>\nAssistant: There are 3 r's in the word 'strawberry'.",
        "User: What are the Three Laws of Robotics?<end_of_utterance>\nAssistant: <tool_call>\n{'arguments': {'query': 'Three Laws of Robotics'}, 'name': 'web_search'}\n</tool_call><end_of_utterance>\nTool: The Three Laws of Robotics are:\n1. A robot may not injure a human being or, through inaction, allow a human being to come to harm.\n2. A robot must obey the orders given it by human beings except where such orders would conflict with the First Law.\n3. A robot must protect its own existence as long as such protection does not conflict with the First or Second Laws.<end_of_utterance>\nAssistant: The Three Laws of Robotics are:\n1. A robot may not injure a human being or, through inaction, allow a human being to come to harm.\n2. A robot must obey the orders given it by human beings except where such orders would conflict with the First Law.\n3. A robot must protect its own existence as long as such protection does not conflict with the First or Second Laws.",
        "User: What is the answer to the Ultimate Question of Life, the Universe, and Everything?<end_of_utterance>\nAssistant: <tool_call>\n{'arguments': {'query': 'What is the answer to the Ultimate Question of Life, the Universe, and Everything?'}, 'name': 'web_search'}\n</tool_call><end_of_utterance>\nTool: The answer to the Ultimate Question of Life, the Universe, and Everything is 42.<end_of_utterance>\nAssistant: 42",
    ]

    # Return the first n examples, or all if n > number of examples
    selected_examples = examples[:n] if n <= len(examples) else examples
    return "<end_of_utterance>\n\n".join(selected_examples)


def format_tool_definitions(tools: list[dict[str, Any]]) -> str:
    if not tools:
        return ""

    tools = sorted(tools, key=lambda t: t["name"])

    tool_content = "The following tools are available:\n\n"

    for tool in tools:
        if tool["type"] == "function":
            tool_content += f"Tool name: {tool['name']}\n"
            tool_content += f"Description: {tool['description']}\n"
            tool_content += "Parameters:\n"
            for name, spec in tool["parameters"]["properties"].items():
                line = f"- {name} ({spec['type']}): {spec.get('description', '')}"
                if "enum" in spec:
                    line += f" (One of: {', '.join(spec['enum'])})"
                tool_content += line + "\n"
            tool_content += "\n"

    tool_content += "To use a tool, respond with:\n<tool_call>\n{ ... }\n</tool_call>"
    return tool_content.strip()


def _build_system_message_parts(
    system_message: str | None = DEFAULT_SYSTEM_MESSAGE,
    developer_message: str | None = None,
    tools: list[dict[str, Any]] | None = None,
    n_shot: int = DEFAULT_N_SHOT,
) -> list[str]:
    system_parts = []

    if system_message:
        system_parts.append(system_message)

    if developer_message:
        system_parts.append(f"[Developer Instructions]: {developer_message}")

    # Only include n-shot examples if there are tools
    if tools:
        # Merge default tools if not present
        tool_names = {tool["name"] for tool in tools}
        merged_tools = tools.copy()
        for default_tool in DEFAULT_TOOLS:
            if default_tool["name"] not in tool_names:
                merged_tools.append(default_tool)
        # Sort tools by name
        merged_tools = sorted(merged_tools, key=lambda t: t["name"])
        tool_content = format_tool_definitions(merged_tools)
        if tool_content:
            system_parts.append(tool_content)
            # Add n-shot example after tool definitions
            if n_shot > 0:
                n_shot_example = _create_n_shot_example(n_shot)
                if n_shot_example:
                    system_parts.append(n_shot_example)

    return system_parts


def get_model(with_peft: bool = False):
    global MODEL

    if with_peft:
        # For training with QLoRA, load fresh quantized model each time
        # Configuration matching the working script
        lora_config = LoraConfig(
            r=8,
            lora_alpha=8,
            lora_dropout=0.1,
            target_modules=r".*text_model\.layers\.\d+\.(self_attn\.(q_proj|k_proj|v_proj|o_proj)|mlp\.(gate_proj|up_proj|down_proj))",
            use_dora=False,  # False for QLoRA
            init_lora_weights="gaussian",
            task_type=TaskType.CAUSAL_LM,
        )
        lora_config.inference_mode = False

        bnb_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_use_double_quant=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=torch.bfloat16,
        )

        # Load model with quantization - following the working script pattern
        model = AutoModelForImageTextToText.from_pretrained(
            MODEL_PATH, quantization_config=bnb_config, device_map="auto"
        )

        # Apply LoRA following the working script sequence
        model.add_adapter(lora_config)
        model.enable_adapters()
        model = prepare_model_for_kbit_training(model)
        peft_model = get_peft_model(model, lora_config)

        return peft_model

    # For inference, use cached full precision model
    if MODEL is None:
        MODEL = AutoModelForImageTextToText.from_pretrained(
            MODEL_PATH, torch_dtype=torch.float16
        ).to("cuda")

    return MODEL


def get_processor():
    global PROCESSOR
    if PROCESSOR is None:
        PROCESSOR = AutoProcessor.from_pretrained(MODEL_PATH)
    return PROCESSOR


def prepare_model_inputs(
    messages: list[dict[str, Any]],
    processor,
    system_message: str | None = DEFAULT_SYSTEM_MESSAGE,
    developer_message: str | None = None,
    tools: list[dict[str, Any]] | None = None,
) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    # Build system message parts
    system_parts = _build_system_message_parts(system_message, developer_message, tools)

    print("system_parts:")
    print(system_parts)

    # if system_parts and messages has system message raise a NotImplementedError
    if system_parts and any(msg["role"] == "system" for msg in messages):
        raise NotImplementedError("TODO: Merge system message into system_parts")

    # Add combined system message if any parts exist
    if system_parts:
        messages.insert(0, _create_system_message(system_parts))

    print("messages [before]:")
    print(messages)

    # Convert message to processor format with content array and tool_calls converted to content
    def convert_message(msg):
        content = msg.get("content")
        role = msg["role"]
        tool_calls = msg.get("tool_calls", [])

        if tool_calls:
            assert content is None, (
                "Content cannot be provided when tool calls are present"
            )
            assert role == "assistant", (
                "Tool calls are only allowed for assistant messages"
            )

            content = [
                {
                    "text": f"<tool_call>\n{json.dumps(tool_call)}\n</tool_call>",
                    "type": "text",
                }
                for tool_call in tool_calls
            ]

        assert content is not None, "Content is required"

        if isinstance(content, str):
            content = [{"text": content, "type": "text"}]

        assert isinstance(content, list), "Content must be a list"

        for item in content:
            assert "type" in item, "Each item in content must have a type"
            # assert "text" in item or "image" in item or "video" in item, "Each item in content must have a text, image, or video"
            assert (
                "image" in item
                or "path" in item
                or "text" in item
                or "url" in item
                or "video" in item
            ), "Each item in content must have an image, path, text, url, or video"

        return {
            "role": role,
            "content": content,
        }

    messages = [convert_message(msg) for msg in messages]

    print("messages [after]:")
    print(messages)

    # Apply chat template
    inputs = processor.apply_chat_template(
        messages,
        tokenize=True,
        add_generation_prompt=True,
        return_tensors="pt",
        return_dict=True,
    )

    # Generate formatted prompt text
    prompt = processor.apply_chat_template(
        messages,
        add_generation_prompt=True,
        tokenize=False,
    )

    return inputs, messages, prompt


def process_model_inputs(inputs, model, processor, train=False):
    if train:
        raise NotImplementedError("TODO: Implement training for process_model_inputs")

    # Move inputs to the same device as the model
    device = next(model.parameters()).device

    inputs = {
        k: v.to(device=device) if hasattr(v, "to") else v for k, v in inputs.items()
    }

    # Convert pixel_values to float16 if present (but keep input_ids as long)
    if "pixel_values" in inputs:
        inputs["pixel_values"] = inputs["pixel_values"].to(dtype=torch.float16)

    with torch.no_grad():
        model_outputs = model.generate(
            **inputs,
            max_new_tokens=100,
            do_sample=False,
            temperature=0.0,
            pad_token_id=processor.tokenizer.eos_token_id,
        )

    return model_outputs


def process_model_outputs(model_inputs, model_outputs, processor, train=False):
    if train:
        raise NotImplementedError("TODO: Implement training for process_model_outputs")

    response = processor.tokenizer.decode(
        model_outputs[0][model_inputs["input_ids"].shape[-1] :],
        skip_special_tokens=True,
    )

    return response

class ToolCallStoppingCriteria(StoppingCriteria):
    def __init__(self, tokenizer, start_length, stop_str="</tool_call>"):
        super().__init__()
        self.tokenizer = tokenizer
        self.start_length = start_length
        self.stop_str = stop_str

    def __call__(self, input_ids, scores, **kwargs):
        # Only check the newly generated tokens
        decoded = self.tokenizer.decode(
            input_ids[0][self.start_length :], skip_special_tokens=True
        )
        return self.stop_str in decoded
