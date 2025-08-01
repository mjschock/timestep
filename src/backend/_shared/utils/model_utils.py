# ruff: noqa: S101

import json
import os
import uuid
from copy import deepcopy
from typing import Any

import torch
from datasets import Dataset
from peft import (
    LoraConfig,
    PeftModel,
    TaskType,
    get_peft_model,
    prepare_model_for_kbit_training,
)
from torch.utils.data import Dataset as TorchDataset, IterableDataset
from transformers import (
    AutoModelForImageTextToText,
    AutoProcessor,
    BitsAndBytesConfig,
    StoppingCriteria,
    Trainer,
    TrainingArguments,
)

from backend._shared.config.constants import (
    DEFAULT_N_SHOT,
    DEFAULT_SYSTEM_MESSAGE,
    DEFAULT_TOOLS,
    N_SHOT_EXAMPLES,
)

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
        tool_names = {tool["name"] for tool in tools}
        merged_tools = tools.copy()
        for default_tool in DEFAULT_TOOLS:
            if default_tool["name"] not in tool_names:
                merged_tools.append(default_tool)
        # Sort tools by name
        merged_tools = sorted(merged_tools, key=lambda t: t["name"])
        tool_content = format_tool_definitions(merged_tools)
        if tool_content:
            parts.append(tool_content)
            # Add n-shot example after tool definitions
            if DEFAULT_N_SHOT > 0:
                n_shot_example = _create_n_shot_example(DEFAULT_N_SHOT)
                if n_shot_example:
                    parts.append(n_shot_example)

    # Check if system message already exists and raise error if system parts also exist
    if parts and any(msg["role"] == "system" for msg in messages):
        raise NotImplementedError("TODO: Merge system message into system_parts")

    # Add combined system message if any parts exist
    if parts:
        system_message_dict = {
            "role": "system",
            "content": [{"type": "text", "text": "\n\n".join(parts)}],
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


def prepare_model_inputs(
    messages: list[dict[str, Any]],
    processor,
    model=None,
    system_message: str | None = DEFAULT_SYSTEM_MESSAGE,
    developer_message: str | None = None,
    tools: list[dict[str, Any]] | None = None,
    train: bool = False,
) -> tuple[dict[str, Any], Any]:
    # Create deep copies to avoid mutating the original conversation data
    messages = deepcopy(messages)
    tools = deepcopy(tools) if tools is not None else None

    # Add system message to messages
    _add_system_message_to_messages(messages, system_message, developer_message, tools)

    # Convert messages to processor format
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

    processed_messages = [convert_message(msg) for msg in messages]

    # Create dataset format (consistent for both training and inference)
    processed_dataset = [{"messages": processed_messages}]
    
    # Create collate function based on training mode
    if train:
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
                instance = processor.apply_chat_template(
                    messages,
                    add_generation_prompt=False,
                    tokenize=True,
                    return_dict=True,
                    return_tensors="pt",
                )

                for key in instance.keys():
                    if hasattr(instance[key], "to"):
                        instance[key] = instance[key].to(device=model.device)

            finally:
                processor.image_processor.do_image_splitting = (
                    original_do_image_splitting
                )
                processor.image_processor.video_sampling["video_size"][
                    "longest_edge"
                ] = original_video_size

            out = {
                "input_ids": instance["input_ids"],
                "attention_mask": instance["attention_mask"],
                "labels": instance["input_ids"].clone(),
            }

            out["labels"][out["labels"] == image_token_id] = -100

            if "pixel_values" in instance and instance["pixel_values"] is not None:
                out["pixel_values"] = instance["pixel_values"]

            return out

        # Return for training mode
        return {
            "data_collator": data_collator,
            "train_dataset": processed_dataset,
            "eval_dataset": None,
            "test_dataset": None,
        }
    
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
                processed_inputs["pixel_values"] = processed_inputs["pixel_values"].to(dtype=model_dtype)

            return processed_inputs

        # Return for inference mode
        return {
            "data_collator": data_collator,
            "train_dataset": None,
            "eval_dataset": None,
            "test_dataset": processed_dataset,
        }


def process_model_inputs(
    model,
    processor,
    data_collator: Any | None = None,
    train_dataset: TorchDataset | IterableDataset | Dataset | None = None,
    eval_dataset: TorchDataset | dict[str, TorchDataset] | Dataset | None = None,
    test_dataset: TorchDataset | dict[str, TorchDataset] | Dataset | None = None,
):
    if data_collator is None:
        raise ValueError("data_collator is required")
    
    if train_dataset is not None:
        # For training, run the training process
            
        # Print model info
        model.print_trainable_parameters()
        print(f"  Model dtype: {model.dtype}")

        # Generate unique output directory using GUID
        model_guid = str(uuid.uuid4())
        output_dir = f"data/models/{os.getenv('HF_USERNAME', os.getenv('USER'))}/{PRETRAINED_MODEL_NAME_OR_PATH.split('/')[-1]}-{model_guid}"
        
        training_args = TrainingArguments(
            num_train_epochs=1,
            per_device_train_batch_size=1,
            gradient_accumulation_steps=1,
            warmup_steps=50,
            learning_rate=1e-4,
            weight_decay=0.01,
            logging_steps=25,
            save_strategy="epoch",
            optim="paged_adamw_8bit",
            bf16=True,
            output_dir=output_dir,
            remove_unused_columns=False,
            report_to=[],
            label_names=["labels"],
            dataloader_pin_memory=False,
            gradient_checkpointing=True,
            gradient_checkpointing_kwargs={"use_reentrant": False},
            dataloader_num_workers=0,
        )

        # Create trainer with train and eval datasets
        trainer = Trainer(
            model=model,
            args=training_args,
            data_collator=data_collator,
            train_dataset=train_dataset,
            eval_dataset=eval_dataset,
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

        # Verify that training actually improved the model
        assert train_result.training_loss < initial_loss, (
            "Training should improve the model"
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

            model_outputs = model.generate(
                **inference_inputs,
                max_new_tokens=100,
                do_sample=False,
                temperature=0.0,
                pad_token_id=processor.tokenizer.eos_token_id,
            )

    # Always return consistent format
    return {
        "train_result": train_result,
        "model_path": model_path, 
        "model_outputs": model_outputs,
        "input_length": input_length
    }


def process_model_outputs(result, processor):
    """Process results from process_model_inputs.
    
    Args:
        result: Dictionary with 'model_outputs' and/or 'train_result' keys
        processor: The processor for decoding
        
    Returns:
        For training: {"train_result": ..., "model_path": ..., "response": ...}
        For inference: {"response": ...}
    """
    # Auto-detect training mode based on presence of train_result
    is_training = result.get("train_result") is not None
    
    if is_training:
        # For training, we may have both training results and model outputs
        train_result = result.get("train_result")
        model_path = result.get("model_path")
        model_outputs = result.get("model_outputs")
        
        output = {
            "train_result": train_result,
            "model_path": model_path
        }
        
        # If we have model outputs from post-training inference, decode them
        if model_outputs is not None:
            input_length = result.get("input_length")
            if input_length is not None:
                # Decode only the newly generated tokens
                response = processor.tokenizer.decode(
                    model_outputs[0][input_length:],
                    skip_special_tokens=True,
                )
            else:
                # Fallback to full decode (shouldn't happen)
                response = processor.tokenizer.decode(
                    model_outputs[0],
                    skip_special_tokens=True,
                )
            output["response"] = response
            
        return output

    else:
        # For inference, decode the response
        model_outputs = result.get("model_outputs")
        input_length = result.get("input_length")
        if model_outputs is None:
            raise ValueError("No model outputs found in result")
        
        if input_length is not None:
            # Decode only the newly generated tokens
            response = processor.tokenizer.decode(
                model_outputs[0][input_length:],
                skip_special_tokens=True,
            )
        else:
            # Fallback to full decode (shouldn't happen)
            response = processor.tokenizer.decode(
                model_outputs[0],
                skip_special_tokens=True,
            )

        return {"response": response}


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
