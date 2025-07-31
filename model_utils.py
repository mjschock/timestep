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


def normalize_content(content: str | list[dict[str, Any]]) -> list[dict[str, Any]]:
    """
    Normalize content to list format for consistent handling.

    Args:
        content: Either string or list of content items

    Returns:
        List of content dictionaries
    """
    if isinstance(content, str):
        return [{"type": "text", "text": content}]
    elif isinstance(content, list):
        return content
    else:
        raise ValueError(f"Content must be string or list, got {type(content)}")


def convert_tool_calls_to_content(message: dict[str, Any]) -> dict[str, Any]:
    """
    Convert tool_calls to content format for compatibility with Jinja templates.

    If a message has tool_calls, convert them to content wrapped in <tool_call> tags
    using json.dumps. This ensures compatibility even if the Jinja template doesn't
    support tool_calls.

    Args:
        message: Message dictionary that may contain tool_calls

    Returns:
        Message with tool_calls converted to content if present
    """
    if "tool_calls" in message and message["tool_calls"]:
        # Convert each tool call to individual <tool_call> tags
        tool_call_parts = []
        for tool_call in message["tool_calls"]:
            tool_call_json = json.dumps(
                tool_call, separators=(",", ":"), sort_keys=True
            )
            tool_call_parts.append(f"<tool_call>\n{tool_call_json}\n</tool_call>")

        # Concatenate all tool calls
        tool_call_content = "".join(tool_call_parts)

        # Create new message with content instead of tool_calls
        converted_message = message.copy()
        converted_message["content"] = tool_call_content
        # Remove tool_calls since we've converted them to content
        converted_message.pop("tool_calls", None)

        return converted_message

    return message


def _tensor_to_list(tensor_or_list):
    """
    Convert tensor to list if needed, otherwise return as-is.

    Args:
        tensor_or_list: A tensor with .tolist() method or any other object

    Returns:
        List representation if input has .tolist() method, otherwise original input
    """
    if hasattr(tensor_or_list, "tolist"):
        return tensor_or_list.tolist()
    return tensor_or_list


def _flatten_if_nested(lst):
    """
    Flatten list if it's a list of lists.

    Args:
        lst: Input list that may contain nested sublists

    Returns:
        Flattened list if input contains sublists, otherwise original list

    Note:
        Only flattens one level deep. Assumes all elements are lists if first element is a list.
    """
    if lst and isinstance(lst[0], list):
        return [item for sublist in lst for item in sublist]
    return lst


def _process_tensor_data(data):
    """
    Convert tensor to list and flatten if nested - common pattern.

    Args:
        data: Tensor or nested list structure to process

    Returns:
        Flattened list representation of the input data
    """
    return _flatten_if_nested(_tensor_to_list(data))


def _create_system_message(system_parts: list[str]) -> dict[str, Any]:
    """
    Create a system message with proper content structure.

    Args:
        system_parts: List of string components to join into system message

    Returns:
        Dictionary with 'role': 'system' and 'content' as list of text content
    """
    return {
        "role": "system",
        "content": [{"type": "text", "text": "\n\n".join(system_parts)}],
    }


def _prepare_messages_for_tokenizer(
    messages: list[dict[str, list[dict[str, Any]] | float]],
) -> list[dict[str, list[dict[str, Any]]]]:
    """
    Convert messages with weights to tokenizer-compatible format by stripping weights.

    Args:
        messages: List of messages that may contain weights

    Returns:
        List of messages without weights
    """
    return [{"role": msg["role"], "content": msg["content"]} for msg in messages]


def _build_system_message_parts(
    system_message: str | None = DEFAULT_SYSTEM_MESSAGE,
    developer_message: str | None = None,
    tools: list[dict[str, Any]] | None = None,
    n_shot: int = DEFAULT_N_SHOT,
) -> list[str]:
    """
    Build system message parts from components.

    Args:
        system_message: Base system prompt
        developer_message: Developer instructions
        tools: Tool definitions
        n_shot: Number of n-shot examples to include

    Returns:
        List of system message parts
    """
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


def _create_n_shot_example(n: int = 0) -> str:
    """
    Create a generic n-shot example for tool calling.

    Args:
        n: Number of examples to include (0 returns empty string)

    Returns:
        String containing n example conversations, or all available if n exceeds count.
        Empty string if n is 0.
    """
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
    """
    Format tools into a readable string for the system message.

    Args:
        tools: List of tool definition dictionaries with 'type', 'name', 'description',
               and 'parameters' keys

    Returns:
        Formatted string describing available tools and usage instructions.
        Empty string if no tools provided.

    Note:
        Tools are automatically sorted by name for consistent output.
    """
    if not tools:
        return ""

    # Sort tools by name
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


def prepare_model_inputs(
    messages: list[dict[str, Any]],
    processor,
    system_message: str | None = DEFAULT_SYSTEM_MESSAGE,
    developer_message: str | None = None,
    tools: list[dict[str, Any]] | None = None,
) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    """
    Prepare messages for inference with multimodal support.

    Args:
        messages: List of messages with content and optional weight values.
                 Each message should have 'role', 'content', and optionally 'weight' keys.
        processor: Processor with chat_template
        system_message: System prompt
        developer_message: Developer instructions
        tools: Available tools

    Returns:
        Tuple of (inputs, messages, prompt) where:
        - inputs: Dictionary with inference data as PyTorch tensors:
          * "input_ids": Token ID tensor for the conversation
          * "attention_mask": Attention mask tensor
          * "pixel_values": Image tensor (only present for vision models with images)
        - messages: List of processed messages with normalized content structure
        - prompt: Formatted text prompt string from apply_chat_template with generation prompt
    """
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

    # raise ValueError('stop here')

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


def _create_weighted_labels_multimodal(
    messages: list[dict[str, list[dict[str, Any]] | float]], processor
) -> dict[str, Any]:
    """
    Create input_ids and labels with message-level weighting for multimodal models.

    Args:
        messages: List of messages with content and optional weight values.
                 Each message should have 'role', 'content', and optionally 'weight' keys.
        processor: Processor or tokenizer with apply_chat_template method

    Returns:
        Dictionary containing:
        - 'input_ids': List of token IDs for the full conversation
        - 'labels': List of label IDs (-100 for ignored tokens, token IDs for training)
        - 'attention_mask': List of attention mask values (1 for valid tokens)
        - Additional modality fields (e.g., 'pixel_values' for vision models)

    Note:
        Processes messages incrementally to determine token boundaries for each message.
        Tokens from messages with weight > 0 are included in training (labels = token IDs).
        Tokens from messages with weight = 0 are ignored in training (labels = -100).
    """
    # Initialize result
    result = {"input_ids": [], "labels": [], "attention_mask": []}

    # Process messages incrementally to identify token boundaries
    for i, message in enumerate(messages):
        weight = message.get("weight", 0.0)

        # Get conversation up to this point (inclusive)
        # Create processor-compatible format (strip weights)
        tokenizer_messages = _prepare_messages_for_tokenizer(messages[: i + 1])

        # Tokenize current conversation
        current_inputs = processor.apply_chat_template(
            tokenizer_messages,
            add_generation_prompt=False,
            tokenize=True,
            return_dict=True,
        )
        current_tokens = _tensor_to_list(current_inputs["input_ids"])
        # Flatten if batch dimension exists
        if current_tokens and isinstance(current_tokens[0], list):
            current_tokens = current_tokens[0]

        # Get conversation up to previous message (exclusive)
        if i == 0:
            prev_tokens = []
        else:
            prev_tokenizer_messages = _prepare_messages_for_tokenizer(messages[:i])
            prev_inputs = processor.apply_chat_template(
                prev_tokenizer_messages,
                add_generation_prompt=False,
                tokenize=True,
                return_dict=True,
            )
            prev_tokens = _tensor_to_list(prev_inputs["input_ids"])
            # Flatten if batch dimension exists
            if prev_tokens and isinstance(prev_tokens[0], list):
                prev_tokens = prev_tokens[0]

        # Find tokens added by this message
        new_tokens = current_tokens[len(prev_tokens) :]

        # Add to input_ids
        result["input_ids"].extend(new_tokens)

        # Add to labels based on message weight
        if weight > 0:
            # Include these tokens in loss calculation
            result["labels"].extend(new_tokens)
        else:
            # Ignore these tokens in loss calculation
            result["labels"].extend([-100] * len(new_tokens))

        # Handle attention mask
        result["attention_mask"].extend([1] * len(new_tokens))

    # Add other modalities from final tokenization (like pixel_values for vision)
    final_inputs = processor.apply_chat_template(
        _prepare_messages_for_tokenizer(messages),
        add_generation_prompt=False,
        tokenize=True,
        return_dict=True,
    )

    # Copy over non-text inputs (like pixel_values)
    for key, value in final_inputs.items():
        if key not in result and key not in ["input_ids", "attention_mask"]:
            result[key] = value

    return result


def blah(
    conversation: list[dict[str, str | list[dict[str, Any]] | float]],
    processor,
    system_message: str | None = None,
    developer_message: str | None = None,
    tools: list[dict[str, Any]] | None = None,
    train: bool = False,
) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    if train:
        raise NotImplementedError("TODO: Implement training for prepare_model_inputs")

    # Validate input
    if not conversation:
        raise ValueError("Conversation cannot be empty")

    # Build system message parts
    system_parts = _build_system_message_parts(system_message, developer_message, tools)

    # Prepare full conversation with system message
    messages = []
    if system_parts:
        system_msg = _create_system_message(system_parts)
        system_msg["weight"] = 0.0  # Never train on system message
        messages.append(system_msg)

    # Add conversation messages with default weights and normalized content
    for msg in conversation:
        # Convert tool_calls to content if present
        msg = convert_tool_calls_to_content(msg)

        message = {"role": msg["role"], "content": normalize_content(msg["content"])}
        # Default weights: assistant=1.0, others=0.0
        if "weight" not in msg:
            message["weight"] = 1.0 if message["role"] == "assistant" else 0.0
        else:
            message["weight"] = msg["weight"]
        messages.append(message)

    # Create labels with message-level weights
    result = _create_weighted_labels_multimodal(messages, processor)

    # Generate formatted prompt text
    prompt = processor.apply_chat_template(
        _prepare_messages_for_tokenizer(messages),
        add_generation_prompt=False,
        tokenize=False,
    )

    return result, messages, prompt


def _validate_basic_structure(
    example: dict[str, Any],
) -> tuple[list[str], list, list, list]:
    """
    Validate basic structure of training example.

    Args:
        example: Dictionary containing 'input_ids', 'labels', and optionally 'attention_mask'

    Returns:
        Tuple of (issues, input_ids, labels, attention_mask) where:
        - issues: List of validation error messages
        - input_ids: Processed input_ids as flat list
        - labels: Processed labels as flat list
        - attention_mask: Processed attention_mask as flat list
    """
    issues = []
    input_ids = example["input_ids"]
    labels = example["labels"]
    attention_mask = example.get("attention_mask", [])

    # Convert tensors to lists and flatten if needed
    input_ids = _process_tensor_data(input_ids)
    labels = _process_tensor_data(labels)
    attention_mask = _process_tensor_data(attention_mask)

    # Basic length checks
    if len(input_ids) != len(labels):
        issues.append(
            f"Length mismatch: input_ids={len(input_ids)}, labels={len(labels)}"
        )

    if attention_mask and len(input_ids) != len(attention_mask):
        issues.append(
            f"Attention mask mismatch: input_ids={len(input_ids)}, attention_mask={len(attention_mask)}"
        )

    return issues, input_ids, labels, attention_mask


def _validate_token_alignment(input_ids: list, labels: list) -> list[str]:
    """
    Validate token alignment between input_ids and labels.

    Args:
        input_ids: List of input token IDs
        labels: List of label token IDs (may contain -100 for ignored tokens)

    Returns:
        List of validation issues. Empty list if no alignment problems found.

    Note:
        Checks that non-ignored labels (not -100) match corresponding input_ids.
    """
    issues = []
    # Check for mismatched tokens (where label != input_id when label != -100)
    mismatched = []
    # Use min length to avoid zip strict error
    min_length = min(len(input_ids), len(labels))
    for i in range(min_length):
        inp = input_ids[i]
        lab = labels[i]
        if lab != -100 and lab != inp:
            mismatched.append(i)

    if mismatched:
        issues.append(
            f"Token mismatches at positions: {mismatched[:5]}..."
        )  # Show first 5

    return issues


def _validate_vocabulary(input_ids: list, processor) -> list[str]:
    """
    Validate token IDs against vocabulary.

    Args:
        input_ids: List of token IDs to validate
        processor: Processor or tokenizer with vocabulary size information

    Returns:
        List of validation issues. Empty list if all token IDs are valid.

    Note:
        Checks that all token IDs are within valid vocabulary range [0, vocab_size).
        Skips nested structures and non-numeric tokens gracefully.
    """
    issues = []
    # Check for valid token IDs
    if hasattr(processor, "tokenizer"):
        vocab_size = len(processor.tokenizer)
    else:
        vocab_size = len(processor)

    # Ensure vocab_size is an integer
    if hasattr(vocab_size, "__len__") and not isinstance(vocab_size, int):
        vocab_size = len(vocab_size)

    # Ensure all token_ids are integers before comparison
    invalid_tokens = []
    for i, token_id in enumerate(input_ids):
        if isinstance(token_id, list | tuple):
            # Skip nested structures
            continue
        try:
            if token_id >= vocab_size or token_id < 0:
                invalid_tokens.append(i)
        except (TypeError, ValueError):
            # Skip non-numeric tokens
            continue

    if invalid_tokens:
        issues.append(f"Invalid token IDs at positions: {invalid_tokens[:5]}...")

    return issues


def validate_training_example(
    example: dict[str, Any], processor, messages: list[dict[str, Any]] | None = None
) -> dict[str, Any]:
    """
    Validate and analyze a training example with comprehensive checks.

    Args:
        example: Training example to validate
        processor: Processor used to create the example
        messages: Optional list of messages used to create the example (for debugging)

    Returns:
        Analysis dictionary with validation results and message information
    """
    # Validate basic structure
    issues, input_ids, labels, attention_mask = _validate_basic_structure(example)

    # Count token types
    total_tokens = len(input_ids)
    training_tokens = sum(1 for x in labels if x != -100)
    ignored_tokens = sum(1 for x in labels if x == -100)

    # Validate token alignment
    issues.extend(_validate_token_alignment(input_ids, labels))

    # Validate vocabulary
    issues.extend(_validate_vocabulary(input_ids, processor))

    analysis = {
        "total_tokens": total_tokens,
        "training_tokens": training_tokens,
        "ignored_tokens": ignored_tokens,
        "training_ratio": training_tokens / total_tokens if total_tokens > 0 else 0,
        "issues": issues,
        "valid": len(issues) == 0,
        "has_multimodal": "pixel_values" in example,
        "messages": messages,
    }

    return analysis


def assert_training_correctness(example: dict[str, Any], processor):
    """
    Assert that a training example is correctly formatted.
    Raises AssertionError if any issues are found.
    """
    analysis = validate_training_example(example, processor)

    if not analysis["valid"]:
        raise AssertionError(
            f"Training example validation failed: {analysis['issues']}"
        )
    if analysis["training_ratio"] <= 0:
        raise AssertionError("No tokens marked for training")
    if analysis["total_tokens"] <= 0:
        raise AssertionError("Empty training example")

    # Ensure labels alignment
    input_ids = example["input_ids"]
    labels = example["labels"]

    # Convert tensors to lists and flatten if needed
    input_ids = _process_tensor_data(input_ids)
    labels = _process_tensor_data(labels)

    for i, (inp, lab) in enumerate(zip(input_ids, labels, strict=True)):
        if lab != -100:
            if lab != inp:
                raise AssertionError(
                    f"Label mismatch at position {i}: input_id={inp}, label={lab}"
                )


def get_processor():
    """
    Get or create the processor instance.

    Returns:
        AutoProcessor instance for MODEL_PATH, cached globally after first call

    Note:
        Uses global PROCESSOR variable for caching to avoid repeated loading.
        No parameters required - uses global MODEL_PATH constant.
    """
    global PROCESSOR
    if PROCESSOR is None:
        PROCESSOR = AutoProcessor.from_pretrained(MODEL_PATH)
    return PROCESSOR


def get_model(with_peft: bool = False):
    """
    Get or create the model instance.

    Args:
        with_peft: If True, return model with QLoRA (4-bit quantized LoRA) for training.
                  If False, return the base model for inference.

    Returns:
        AutoModelForImageTextToText instance.
        If with_peft=False: loaded with float16 precision on CUDA.
        If with_peft=True: loaded with 4-bit quantization and LoRA adapters.

    Note:
        Uses global MODEL variable for caching base model. PEFT model is created fresh each time.
        Model is automatically moved to CUDA device.
        No parameters required - uses global MODEL_PATH constant.

    Raises:
        Exception: If CUDA is not available or model loading fails
    """
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


class ToolCallStoppingCriteria(StoppingCriteria):
    """
    Custom stopping criteria for model generation that stops on tool call end tags.

    This stopping criteria monitors generated text for the presence of '</tool_call>'
    and stops generation when this end tag is encountered.

    Args:
        tokenizer: Tokenizer used for decoding generated tokens
        start_length: Initial input length to skip when checking for stop condition
        stop_str: String pattern to stop on (default: "</tool_call>")
    """

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
