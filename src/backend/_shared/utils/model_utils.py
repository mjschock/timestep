# ruff: noqa: S101

import json
import os
import uuid
from copy import deepcopy
from typing import Any, Iterable

from pydantic import TypeAdapter
from openai.types.chat import (
    ChatCompletionMessageParam,
    ChatCompletionToolParam,
)

import torch
from datasets import Dataset, DatasetDict
from peft import (
    LoraConfig,
    PeftModel,
    TaskType,
    get_peft_model,
    prepare_model_for_kbit_training,
)
from torch.utils.data import Dataset as TorchDataset
from torch.utils.data import IterableDataset
from transformers import (
    AutoModelForImageTextToText,
    AutoProcessor,
    BitsAndBytesConfig,
    StoppingCriteria,
    TextIteratorStreamer,
    Trainer,
    TrainingArguments,
)

from backend._shared.config.constants import (
    DEFAULT_N_SHOT,
    DEFAULT_SYSTEM_MESSAGE,
    DEFAULT_TOOLS,
    N_SHOT_EXAMPLES,
)


def compute_lcs(seq1, seq2):
    """Compute the Longest Common Subsequence (LCS) between two sequences."""
    m, n = len(seq1), len(seq2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if seq1[i - 1] == seq2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Backtrack to find the LCS
    i, j = m, n
    lcs_indices_seq1 = []
    lcs_indices_seq2 = []

    while i > 0 and j > 0:
        if seq1[i - 1] == seq2[j - 1]:
            lcs_indices_seq1.append(i - 1)
            lcs_indices_seq2.append(j - 1)
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return lcs_indices_seq1[::-1], lcs_indices_seq2[::-1]


# Global model and processor instances
PRETRAINED_MODEL_NAME_OR_PATH = "HuggingFaceTB/SmolVLM2-256M-Video-Instruct"
PROCESSOR = None
MODEL = None


def _add_system_message_to_messages(
    messages: list[dict[str, Any]],
    system_message: str | None = DEFAULT_SYSTEM_MESSAGE,
    developer_message: str | None = None,
    tools: list[dict[str, Any]] | None = None,
) -> None:
    """
    Add a system message to the beginning of the messages list if system parts exist.

    Args:
        messages: The messages list to modify
        system_message: The system message to include
        developer_message: Developer instructions to include
        tools: Tools to include in system message
    """
    # Build system message parts
    parts = []

    if system_message:
        parts.append(system_message)

    if developer_message:
        parts.append(f"[Developer Instructions]: {developer_message}")

    # Only include n-shot examples if there are tools
    if tools:
        # Merge default tools if not present
        tool_names = set()
        for tool in tools:
            if tool is None:
                continue
            tool_name = tool.get("name") or tool.get("function", {}).get("name")
            if tool_name:  # Only add non-None names
                tool_names.add(tool_name)

        merged_tools = [tool for tool in tools if tool is not None]
        for default_tool in DEFAULT_TOOLS:
            default_tool_name = default_tool.get("name") or default_tool.get(
                "function", {}
            ).get("name")
            if default_tool_name and default_tool_name not in tool_names:
                merged_tools.append(default_tool)

        # Sort tools by name, filtering out None names
        def get_tool_name(t):
            if t is None:
                return ""
            return t.get("name") or t.get("function", {}).get("name") or ""

        merged_tools = sorted(merged_tools, key=get_tool_name)
        tool_content = format_tool_definitions(merged_tools)
        if tool_content:
            parts.append(tool_content)
            # Add n-shot examples after tool definitions
            if DEFAULT_N_SHOT > 0:
                # Simply extend with the raw message lists from N_SHOT_EXAMPLES
                for i in range(min(DEFAULT_N_SHOT, len(N_SHOT_EXAMPLES))):
                    messages.extend(N_SHOT_EXAMPLES[i])

    # Check if system message already exists and merge if needed
    existing_system_messages = [
        i for i, msg in enumerate(messages) if msg["role"] == "system"
    ]

    if parts:
        combined_content = "\n\n".join(parts)

        if existing_system_messages:
            # Merge with existing system messages
            for i in existing_system_messages:
                existing_content = messages[i]["content"]
                if isinstance(existing_content, list):
                    # If content is already a list, append our content
                    existing_content.append({"type": "text", "text": combined_content})
                else:
                    # If content is a string, convert to list and add our content
                    messages[i]["content"] = [
                        {"type": "text", "text": existing_content},
                        {"type": "text", "text": combined_content},
                    ]
        else:
            # Add new system message
            system_message_dict = {
                "role": "system",
                "content": [{"type": "text", "text": combined_content}],
            }
            messages.insert(0, system_message_dict)


def _create_n_shot_example(n: int = 0) -> str:
    if n == 0:
        return ""

    # Return the first n examples, or all if n > number of examples
    selected_examples = (
        N_SHOT_EXAMPLES[:n] if n <= len(N_SHOT_EXAMPLES) else N_SHOT_EXAMPLES
    )

    # Convert each example (list of messages) to the expected string format
    formatted_examples = []
    for example in selected_examples:
        formatted_parts = []
        for message in example:
            if message["role"] == "user":
                formatted_parts.append(f"User: {message['content']}<end_of_utterance>")
            elif message["role"] == "assistant":
                if "tool_calls" in message:
                    # Format tool calls with proper JSON formatting
                    for tool_call in message["tool_calls"]:
                        tool_call_json = json.dumps(
                            {
                                "arguments": tool_call["arguments"],
                                "name": tool_call["name"],
                            }
                        )
                        formatted_parts.append(
                            f"Assistant: <tool_call>\n{tool_call_json}\n</tool_call><end_of_utterance>"
                        )
                else:
                    # Regular assistant message
                    formatted_parts.append(f"Assistant: {message['content']}")
            elif message["role"] == "tool":
                formatted_parts.append(f"Tool: {message['content']}<end_of_utterance>")

        formatted_examples.append("\n".join(formatted_parts))

    return "<end_of_utterance>\n\n".join(formatted_examples)


def format_tool_definitions(tools: list[dict[str, Any]]) -> str:
    if not tools:
        return ""

    # Filter out None tools and sort by name
    valid_tools = [tool for tool in tools if tool is not None]
    if not valid_tools:
        return ""

    def get_tool_name(t):
        if t is None:
            return ""
        return t.get("name") or t.get("function", {}).get("name") or ""

    valid_tools = sorted(valid_tools, key=get_tool_name)

    tool_content = "The following tools are available:\n\n"

    for tool in valid_tools:
        if tool is None:
            continue

        if tool.get("type") == "function":
            # Handle both flattened and nested formats
            if "function" in tool:
                # Nested format
                function_data = tool["function"]
                if function_data is None:
                    continue
                tool_name = function_data.get("name", "")
                tool_description = function_data.get("description", "")
                tool_parameters = function_data.get("parameters", {})
            else:
                # Flattened format
                tool_name = tool.get("name", "")
                tool_description = tool.get("description", "")
                tool_parameters = tool.get("parameters", {})

            tool_content += f"Tool name: {tool_name}\n"
            tool_content += f"Description: {tool_description}\n"
            tool_content += "Parameters:\n"
            if tool_parameters and isinstance(tool_parameters, dict):
                for name, spec in tool_parameters.get("properties", {}).items():
                    if spec and isinstance(spec, dict):
                        line = f"- {name} ({spec.get('type', 'unknown')}): {spec.get('description', '')}"
                        if "enum" in spec:
                            line += f" (One of: {', '.join(spec['enum'])})"
                        tool_content += line + "\n"
            tool_content += "\n"

    tool_content += "To use a tool, respond with:\n<tool_call>\n{ ... }\n</tool_call>"
    return tool_content.strip()


def get_model(
    pretrained_model_name_or_path: str | None = PRETRAINED_MODEL_NAME_OR_PATH,
    train: bool = False,
):
    global MODEL

    if train:
        # For training, load fresh quantized model with PEFT adapters
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

        # Load model with quantization
        model = AutoModelForImageTextToText.from_pretrained(
            pretrained_model_name_or_path,
            quantization_config=bnb_config,
            device_map="auto",
        )

        # Apply LoRA for training
        model.add_adapter(lora_config)
        model.enable_adapters()
        model = prepare_model_for_kbit_training(model)
        peft_model = get_peft_model(model, lora_config)

        return peft_model

    # For inference
    if (
        pretrained_model_name_or_path != PRETRAINED_MODEL_NAME_OR_PATH
        and os.path.exists(pretrained_model_name_or_path)
    ):
        # Load fine-tuned model for inference
        print(f"Loading fine-tuned model from: {pretrained_model_name_or_path}")

        # Load the base model with quantization for inference
        bnb_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_use_double_quant=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=torch.bfloat16,
        )

        model = AutoModelForImageTextToText.from_pretrained(
            PRETRAINED_MODEL_NAME_OR_PATH,
            quantization_config=bnb_config,
            device_map="auto",
            torch_dtype=torch.bfloat16,
        )

        # Load the fine-tuned adapters
        model = PeftModel.from_pretrained(model, pretrained_model_name_or_path)
        return model

    # For inference with base model, use cached full precision model
    if MODEL is None:
        MODEL = AutoModelForImageTextToText.from_pretrained(
            pretrained_model_name_or_path, torch_dtype=torch.float16
        ).to("cuda")

    return MODEL


def get_processor():
    global PROCESSOR
    if PROCESSOR is None:
        PROCESSOR = AutoProcessor.from_pretrained(PRETRAINED_MODEL_NAME_OR_PATH)
    return PROCESSOR


def validate_example(example: dict[str, Any], dataset_type: str, example_index: int) -> None:
    """
    Validate that a dataset example conforms to OpenAI Chat Completions format.
    
    This function ensures strict type compliance for training examples and halts
    the application if validation fails to prevent silent corruption of training data.
    
    TODO: Handle DPO (Direct Preference Optimization) and RFT (Reinforcement Fine-Tuning) 
    formats in addition to standard SFT (Supervised Fine-Tuning) format.
    
    Args:
        example: The dataset example to validate
        dataset_type: The type of dataset split ('train', 'eval', 'test')
        example_index: The index of the example in the dataset for debugging
        
    Raises:
        ValueError: If the example format is invalid with detailed debugging information
    """
    try:
        # Validate messages field
        messages = example.get("messages", [])
        if not messages:
            raise ValueError("Example must contain non-empty 'messages' field")
            
        # Validate messages conform to ChatCompletionMessageParam format
        messages_adapter = TypeAdapter(Iterable[ChatCompletionMessageParam])
        messages_adapter.validate_python(messages)
        
        # Validate tools field if present
        tools = example.get("tools")
        if tools is not None:
            tools_adapter = TypeAdapter(Iterable[ChatCompletionToolParam])
            tools_adapter.validate_python(tools)
            
        # Validate parallel_tool_calls field if present
        parallel_tool_calls = example.get("parallel_tool_calls")
        if parallel_tool_calls is not None:
            if not isinstance(parallel_tool_calls, bool):
                raise ValueError(
                    f"parallel_tool_calls must be bool, got {type(parallel_tool_calls)}"
                )
                
    except Exception as e:
        # Provide detailed debugging information and halt execution
        error_details = {
            "dataset_type": dataset_type,
            "example_index": example_index,
            "example_keys": list(example.keys()),
            "messages_type": str(type(example.get("messages"))),
            "messages_length": len(example.get("messages", [])),
            "tools_type": str(type(example.get("tools"))) if "tools" in example else None,
            "parallel_tool_calls_type": str(type(example.get("parallel_tool_calls"))) if "parallel_tool_calls" in example else None,
        }
        
        # Include first few characters of example for debugging (truncated to avoid large output)
        example_preview = str(example)[:500]
        if len(str(example)) > 500:
            example_preview += "... [truncated]"
            
        error_msg = (
            f"CRITICAL: Invalid dataset example format detected!\n"
            f"Error: {e}\n"
            f"Debug info: {json.dumps(error_details, indent=2)}\n"
            f"Example preview: {example_preview}\n"
            f"This indicates a serious data format issue that must be fixed before training."
        )
        
        raise ValueError(error_msg) from e


def prepare_model_inputs(
    dataset: DatasetDict,
    model=None,
    processor=None,
    stream: bool = False,
) -> dict[str, Any]:
    # Validate required parameters
    if not dataset:
        raise ValueError("dataset is required")

    # Assert that dataset is a DatasetDict
    if not isinstance(dataset, DatasetDict):
        raise TypeError("dataset must be a DatasetDict instance")

    # Assert that each value in the DatasetDict is a Dataset
    for split_name, split_data in dataset.items():
        if not isinstance(split_data, Dataset):
            raise TypeError(
                f"dataset['{split_name}'] must be a Dataset instance, got {type(split_data)}"
            )

    if processor is None:
        processor = get_processor()

    # Initialize model inputs dictionary
    model_inputs = {
        "data_collator": None,
        "eval_dataset": None,
        "test_dataset": None,
        "train_dataset": None,
    }

    # Process each dataset split (eval, test, train)
    for dataset_type in ["eval", "test", "train"]:
        if dataset_type not in dataset:
            continue

        dataset_split = dataset[dataset_type]

        # Convert Dataset to list format for processing
        processed_dataset = []
        for example_index, example in enumerate(dataset_split):
            # Validate example format before processing
            validate_example(example, dataset_type, example_index)
            
            # Extract components from dataset example
            messages = example.get("messages", [])
            tools = example.get("tools")
            developer_message = example.get("developer_message")
            system_message = example.get("system_message", DEFAULT_SYSTEM_MESSAGE)

            if not messages:
                continue

            # Create deep copies to avoid mutating the original data
            messages = deepcopy(messages)

            # Add system message to messages
            _add_system_message_to_messages(
                messages, system_message, developer_message, tools
            )

            # Convert messages to processor format with weight support
            def convert_message(msg):
                content = msg.get("content")
                role = msg["role"]
                tool_calls = msg.get("tool_calls", [])
                # Support custom weight fields from user, fallback to OpenAI SFT standard
                weight = msg.get("weight", 1.0 if role == "assistant" else 0.0)

                if tool_calls:
                    assert content is None, (
                        "Content cannot be provided when tool calls are present"
                    )
                    assert role == "assistant", (
                        "Tool calls are only allowed for assistant messages"
                    )

                    content = []
                    for tool_call in tool_calls:
                        # Parse tool call to standard format
                        # tool_call_data = parse_tool_call(tool_call)
                        tool_call_data = tool_call

                        content.append(
                            {
                                "text": f"<tool_call>\n{json.dumps(tool_call_data)}\n</tool_call>",
                                "type": "text",
                            }
                        )

                assert content is not None, "Content is required"

                if isinstance(content, str):
                    content = [{"text": content, "type": "text"}]

                assert isinstance(content, list), "Content must be a list"

                for item in content:
                    assert "type" in item, "Each item in content must have a type"
                    assert (
                        "image" in item
                        or "path" in item
                        or "text" in item
                        or "url" in item
                        or "video" in item
                    ), (
                        "Each item in content must have an image, path, text, url, or video"
                    )

                return {
                    "role": role,
                    "content": content,
                    "weight": weight,
                }

            processed_messages = [convert_message(msg) for msg in messages]
            processed_dataset.append({"messages": processed_messages})

        # Store the dataset in the appropriate key
        model_inputs[f"{dataset_type}_dataset"] = processed_dataset

    # Create collate function for training mode (auto-detected from train dataset presence)
    if model_inputs.get("train_dataset"):
        # Create training collate function
        image_token_id = processor.tokenizer.additional_special_tokens_ids[
            processor.tokenizer.additional_special_tokens.index("<image>")
        ]

        def data_collator(examples):
            original_do_image_splitting = processor.image_processor.do_image_splitting
            original_video_size = processor.image_processor.video_sampling[
                "video_size"
            ]["longest_edge"]

            processor.image_processor.do_image_splitting = False
            processor.image_processor.video_sampling["video_size"]["longest_edge"] = 512

            try:
                example = examples[0]
                messages = example["messages"]

                # Extract weights from messages
                weights = [
                    msg.get("weight", 1.0 if msg["role"] == "assistant" else 0.0)
                    for msg in messages
                ]

                # Tokenize full conversation
                full_inputs = processor.apply_chat_template(
                    messages,
                    add_generation_prompt=False,
                    tokenize=True,
                    return_dict=True,
                    return_tensors="pt",
                )

                # Tokenize each message individually
                individual_inputs = []
                for msg in messages:
                    msg_inputs = processor.apply_chat_template(
                        [msg],  # Single message in a list
                        add_generation_prompt=False,
                        tokenize=True,
                        return_dict=True,
                        return_tensors="pt",
                    )
                    individual_inputs.append(msg_inputs)

                # Concatenate individual tokenizations
                individual_input_ids = torch.cat(
                    [inputs["input_ids"] for inputs in individual_inputs], dim=1
                )

                # Use LCS to align individual tokenization with full tokenization
                full_tokens = full_inputs["input_ids"][0].tolist()
                individual_tokens = individual_input_ids[0].tolist()

                if full_tokens != individual_tokens:
                    print(
                        f"Aligning tokenizations with LCS: full={len(full_tokens)}, individual={len(individual_tokens)}"
                    )

                    # Compute LCS between full and individual tokenizations
                    lcs_full_indices, lcs_individual_indices = compute_lcs(
                        full_tokens, individual_tokens
                    )

                    # Create mapping: individual position -> full position
                    individual_to_full = {}
                    for full_idx, individual_idx in zip(
                        lcs_full_indices, lcs_individual_indices, strict=False
                    ):
                        individual_to_full[individual_idx] = full_idx

                    print(
                        f"✅ LCS alignment: {len(lcs_full_indices)} matching tokens out of {len(full_tokens)} full tokens"
                    )

                    # Create labels based on LCS alignment
                    labels = torch.full_like(full_inputs["input_ids"], -100)

                    # Track individual message positions and apply weights
                    current_individual_pos = 0
                    for inputs, weight in zip(individual_inputs, weights, strict=False):
                        msg_tokens = inputs["input_ids"][0].tolist()
                        msg_len = len(msg_tokens)

                        if weight > 0:
                            # For weighted messages, find corresponding positions in full tokenization
                            for i in range(
                                current_individual_pos, current_individual_pos + msg_len
                            ):
                                if i in individual_to_full:
                                    full_pos = individual_to_full[i]
                                    labels[0, full_pos] = full_tokens[full_pos]

                        current_individual_pos += msg_len

                    # Still mask image tokens even for weighted messages
                    labels[labels == image_token_id] = -100

                else:
                    print("✅ Perfect tokenization match - no alignment needed")
                    # Perfect match - use simple position-based labeling
                    labels = torch.full_like(full_inputs["input_ids"], -100)

                    current_pos = 0
                    for inputs, weight in zip(individual_inputs, weights, strict=False):
                        msg_len = inputs["input_ids"].shape[1]
                        if weight > 0:
                            labels[0, current_pos : current_pos + msg_len] = (
                                full_inputs["input_ids"][
                                    0, current_pos : current_pos + msg_len
                                ]
                            )
                        current_pos += msg_len

                    # Still mask image tokens even for weighted messages
                    labels[labels == image_token_id] = -100

                # Use the full inputs for other fields
                inputs = full_inputs

                for key in inputs.keys():
                    if hasattr(inputs[key], "to") and model is not None:
                        inputs[key] = inputs[key].to(device=model.device)

            finally:
                processor.image_processor.do_image_splitting = (
                    original_do_image_splitting
                )
                processor.image_processor.video_sampling["video_size"][
                    "longest_edge"
                ] = original_video_size

            out = {
                "input_ids": inputs["input_ids"],
                "attention_mask": inputs["attention_mask"],
                "labels": labels.to(device=model.device)
                if model is not None
                else labels,
            }

            if "pixel_values" in inputs and inputs["pixel_values"] is not None:
                out["pixel_values"] = inputs["pixel_values"]

            return out

    else:
        # Create inference collate function
        def data_collator(examples):
            # For inference, process the dataset format to get inputs
            example = examples[0]
            messages = example["messages"]

            inputs = processor.apply_chat_template(
                messages,
                tokenize=True,
                add_generation_prompt=True,
                return_tensors="pt",
                return_dict=True,
            )

            # Move inputs to the same device as the model
            device = next(model.parameters()).device
            model_dtype = next(model.parameters()).dtype

            processed_inputs = {
                k: v.to(device=device) if hasattr(v, "to") else v
                for k, v in inputs.items()
            }

            # Convert pixel_values to the same dtype as the model if present
            if "pixel_values" in processed_inputs:
                processed_inputs["pixel_values"] = processed_inputs["pixel_values"].to(
                    dtype=model_dtype
                )

            return processed_inputs

    # Store the data collator
    model_inputs["data_collator"] = data_collator

    # Return model inputs dictionary
    return model_inputs


def process_model_inputs(
    data_collator: Any | None = None,
    eval_dataset: TorchDataset | dict[str, TorchDataset] | Dataset | None = None,
    model=None,
    processor=None,
    stream: bool = False,
    test_dataset: TorchDataset | dict[str, TorchDataset] | Dataset | None = None,
    train_dataset: TorchDataset | IterableDataset | Dataset | None = None,
):
    # Validate required parameters
    if data_collator is None:
        raise ValueError("data_collator is required")

    if model is None:
        model = get_model()

    if processor is None:
        processor = get_processor()

    if train_dataset is not None:
        # For training, run the training process

        # Print model info
        model.print_trainable_parameters()
        print(f"  Model dtype: {model.dtype}")

        # Generate unique output directory using GUID
        model_guid = str(uuid.uuid4())
        output_dir = f"data/models/{os.getenv('HF_USERNAME', os.getenv('USER'))}/{PRETRAINED_MODEL_NAME_OR_PATH.split('/')[-1]}-{model_guid}"

        # Advanced hyperparameters for maximum training improvement
        training_args = TrainingArguments(
            adam_beta1=0.9,
            adam_beta2=0.95,  # Lower beta2 for better convergence
            adam_epsilon=1e-6,  # Lower epsilon for precision
            bf16=True,
            dataloader_num_workers=0,
            dataloader_pin_memory=False,
            gradient_accumulation_steps=8,  # Even larger effective batch size
            gradient_checkpointing=True,
            gradient_checkpointing_kwargs={"use_reentrant": False},
            label_names=["labels"],
            learning_rate=2e-3,  # Higher peak learning rate
            logging_steps=3,
            lr_scheduler_type="cosine",  # Cosine annealing for better convergence
            max_grad_norm=0.5,  # Gradient clipping for stability
            num_train_epochs=8,  # More epochs for deeper learning
            optim="paged_adamw_8bit",
            output_dir=output_dir,
            per_device_train_batch_size=1,
            remove_unused_columns=False,
            report_to=[],
            save_strategy="epoch",
            warmup_steps=200,  # Extended warmup for stability
            weight_decay=0.00005,  # Even lower weight decay
        )

        # Create trainer with train and eval datasets
        trainer = Trainer(
            args=training_args,
            data_collator=data_collator,
            eval_dataset=eval_dataset,
            model=model,
            train_dataset=train_dataset,
        )

        # Record initial loss for comparison
        model.eval()
        with torch.no_grad():
            # Get a sample batch to compute initial loss
            sample_batch = data_collator([train_dataset[0]])
            device = next(model.parameters()).device
            sample_batch = {
                k: v.to(device) if hasattr(v, "to") else v
                for k, v in sample_batch.items()
            }

            initial_outputs = model(**sample_batch)
            initial_loss = initial_outputs.loss.item()

        print(f"  Initial loss: {initial_loss:.4f}")

        # Train for one epoch
        model.train()
        train_result = trainer.train()

        print("  Training completed!")
        print(f"  Final loss: {train_result.training_loss:.4f}")
        print(f"  Loss improvement: {initial_loss - train_result.training_loss:.4f}")

        # With improved hyperparameters, we should see consistent loss improvement
        print(
            f"  Loss change: {'improvement' if train_result.training_loss < initial_loss else 'regression'} of {abs(initial_loss - train_result.training_loss):.4f}"
        )

        # Require strict improvement with our optimized hyperparameters
        assert train_result.training_loss < initial_loss, (
            f"Training should improve the model. Initial: {initial_loss:.4f}, Final: {train_result.training_loss:.4f}"
        )

        # Return training results
        train_result = train_result
        model_path = training_args.output_dir

    else:
        # For inference mode
        if test_dataset is None:
            raise ValueError("test_dataset is required for inference")

        # Initialize training-specific results as None for inference
        train_result = None
        model_path = None

    # Process test_dataset if provided (works for both training and inference)
    model_outputs = None
    input_length = None
    if test_dataset is not None:
        if train_dataset is not None:
            print("  Running inference on test dataset after training...")

        model.eval()
        with torch.no_grad():
            # Process test dataset with data_collator
            test_batch = data_collator([test_dataset[0]])
            device = next(model.parameters()).device
            test_batch = {
                k: v.to(device) if hasattr(v, "to") else v
                for k, v in test_batch.items()
            }

            # Remove labels for inference if present
            inference_inputs = {k: v for k, v in test_batch.items() if k != "labels"}

            # Store input length for proper decoding
            input_length = inference_inputs["input_ids"].shape[-1]

            # Always use streaming internally for seamless operation
            # TODO: Support AsyncTextIteratorStreamer for async operations
            streamer = TextIteratorStreamer(
                processor.tokenizer, skip_prompt=True, skip_special_tokens=True
            )

            # Import threading for streaming
            import threading

            # Generate with streaming
            generation_kwargs = {
                **inference_inputs,
                "max_new_tokens": 100,
                "do_sample": False,
                "temperature": 0.0,
                "pad_token_id": processor.tokenizer.eos_token_id,
                "streamer": streamer,
            }

            # Start generation in a separate thread
            generation_thread = threading.Thread(
                target=model.generate, kwargs=generation_kwargs
            )
            generation_thread.start()

            if stream:
                # For streaming mode, return the streamer for external consumption
                # Store thread reference in streamer to prevent garbage collection
                streamer._generation_thread = generation_thread
                model_outputs = streamer
            else:
                # For non-streaming mode, collect all tokens and return full result
                generated_tokens = []
                for token in streamer:
                    generated_tokens.append(token)

                # Wait for generation to complete
                generation_thread.join()

                # Reconstruct full output by encoding the collected text
                full_generated_text = "".join(generated_tokens)
                generated_ids = processor.tokenizer.encode(
                    full_generated_text, return_tensors="pt", add_special_tokens=False
                )

                # Ensure generated_ids is on the same device as inference_inputs
                generated_ids = generated_ids.to(device=inference_inputs["input_ids"].device)

                # Combine input and generated tokens to match expected format
                model_outputs = torch.cat(
                    [inference_inputs["input_ids"], generated_ids], dim=1
                )

    # Always return consistent format
    return {
        "input_length": input_length,
        "model_outputs": model_outputs,
        "model_path": model_path,
        "train_result": train_result,
        "stream": stream,  # Include stream flag for downstream processing
    }


def process_model_outputs(model_outputs=None, processor=None, stream: bool = False):
    """Process results from process_model_inputs.

    Args:
        result: Dictionary with 'model_outputs' and/or 'train_result' keys
        processor: The processor for decoding

    Returns:
        For training: {"train_result": ..., "model_path": ..., "response": ...}
        For inference: {"response": ...}
    """
    # Validate required parameters
    if model_outputs is None:
        raise ValueError("model_outputs is required")

    if processor is None:
        processor = get_processor()

    # Auto-detect training mode based on presence of train_result
    is_training = model_outputs.get("train_result") is not None

    # Auto-detect streaming mode based on presence of stream flag
    is_streaming = model_outputs.get("stream", False)

    results = {}

    if is_training:
        # For training, we may have both training results and model outputs
        train_result = model_outputs.get("train_result")
        model_path = model_outputs.get("model_path")
        model_outputs_data = model_outputs.get("model_outputs")

        results["model_path"] = model_path
        results["train_result"] = train_result

        # If we have model outputs from post-training inference, decode them
        if model_outputs_data is not None:
            input_length = model_outputs.get("input_length")
            if input_length is not None:
                # Decode only the newly generated tokens
                response = processor.tokenizer.decode(
                    model_outputs_data[0][input_length:],
                    skip_special_tokens=True,
                )

            else:
                # Fallback to full decode (shouldn't happen)
                response = processor.tokenizer.decode(
                    model_outputs_data[0],
                    skip_special_tokens=True,
                )

            results["response"] = response

    else:
        # For inference, handle streaming vs non-streaming
        model_outputs_data = model_outputs.get("model_outputs")
        if model_outputs_data is None:
            raise ValueError("No model outputs found in model_outputs")

        if is_streaming:
            # For streaming mode, model_outputs_data is a TextIteratorStreamer
            # Return the streamer for external consumption
            results["response_stream"] = model_outputs_data
            results["stream"] = True
        else:
            # For non-streaming mode, decode the tensor response
            input_length = model_outputs.get("input_length")

            if input_length is not None:
                # Decode only the newly generated tokens
                response = processor.tokenizer.decode(
                    model_outputs_data[0][input_length:],
                    skip_special_tokens=True,
                )
            else:
                # Fallback to full decode (shouldn't happen)
                response = processor.tokenizer.decode(
                    model_outputs_data[0],
                    skip_special_tokens=True,
                )

            results["response"] = response

    return results


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
