#!/usr/bin/env python3
import json
import logging
import os
from typing import Any, get_args

from datasets import load_dataset

# Extract method type values from OpenAI API type definition
from openai.types.fine_tuning.fine_tuning_job import Method

METHOD_TYPES = get_args(Method.model_fields["type"].annotation)
METHOD_TYPE_SUPERVISED, METHOD_TYPE_DPO, METHOD_TYPE_REINFORCEMENT = METHOD_TYPES

# File ID to dataset mapping
FILE_ID_TO_DATASET = {
    "file-tiger-lab-video-feedback": "TIGER-Lab/VideoFeedback",
    "file-nous-research-hermes-function-calling-v1": "NousResearch/hermes-function-calling-v1",
    "file-jofthomas-hermes-function-calling-thinking-v1": "Jofthomas/hermes-function-calling-thinking-V1",
}

# Dataset configurations
DATASET_CONFIGS = {
    "TIGER-Lab/VideoFeedback": {
        "config": "real",
        "has_vision": True,
    },
    "NousResearch/hermes-function-calling-v1": {
        "config": None,
        "has_vision": False,
    },
    "Jofthomas/hermes-function-calling-thinking-V1": {
        "config": None,
        "has_vision": False,
    },
}

# Constants
FILES_DIR = "data/files"


def detect_vision_dataset(dataset_name: str, ds: Any) -> bool:
    """Detect if a dataset contains vision data by checking its configuration."""
    if dataset_name in DATASET_CONFIGS:
        return DATASET_CONFIGS[dataset_name]["has_vision"]

    # Fallback: try to detect from dataset structure
    try:
        example = ds[0]

        # Check for common vision indicators
        vision_indicators = [
            "video link" in example,
            "image" in example,
            "video" in example,
            "pixel_values" in example,
            "image_path" in example,
            "video_path" in example,
        ]

        return any(vision_indicators)
    except Exception as e:
        logging.warning(f"Could not detect vision for dataset {dataset_name}: {e}")
        return False


def load_and_prepare_dataset(dataset_name: str, method: str) -> Any:
    """Load and prepare dataset based on dataset name and training method."""
    logging.info("🔧 STEP 2: Loading and preparing dataset...")

    # Load dataset using configuration
    dataset_config = DATASET_CONFIGS.get(
        dataset_name, {"config": None, "has_vision": False}
    )
    logging.info(f"    📥 Loading {dataset_name} dataset...")

    ds = (
        load_dataset(dataset_name, dataset_config["config"])
        if dataset_config["config"]
        else load_dataset(dataset_name)
    )
    logging.info(f"    ✅ Dataset loaded: {ds}")

    # Split dataset
    logging.info("    ✂️  Splitting dataset (test_size=0.5)...")
    train_ds = ds["train"].train_test_split(test_size=0.5)["train"]
    logging.info(f"    ✅ Training split created with {len(train_ds)} examples")

    # Detect if this is a vision dataset
    has_vision = detect_vision_dataset(dataset_name, train_ds)
    logging.info(f"    🔍 Detected vision dataset: {has_vision}")

    # Clean up memory
    del ds
    logging.info("    🧹 Cleaned up unused dataset objects")

    # Format dataset based on method
    logging.info(f"    🔄 Preparing dataset for {method.upper()} training...")

    if method == METHOD_TYPE_SUPERVISED:
        # SFT: Convert to OpenAI API conversation format
        if has_vision:

            def sft_vision_example(example):
                # For SFT, we'll use a simpler format with just text content
                # The video URL will be handled by the processor during training
                messages = [
                    {
                        "role": "user",
                        "content": f"Caption the video: {example['video link']}",
                    },
                    {"role": "assistant", "content": example["text prompt"]},
                ]
                return {"messages": messages}

            train_ds = train_ds.map(
                sft_vision_example, remove_columns=train_ds.column_names
            )
        else:

            def sft_function_example(example):
                if "conversations" in example:
                    messages = []
                    for conv in example["conversations"]:
                        if "from" in conv and "value" in conv:
                            role = "user" if conv["from"] == "human" else "assistant"
                            content = (
                                conv["value"]
                                if isinstance(conv["value"], str)
                                else str(conv["value"])
                            )
                        elif "role" in conv and "content" in conv:
                            role = "user" if conv["role"] == "human" else "assistant"
                            content = (
                                conv["content"]
                                if isinstance(conv["content"], str)
                                else str(conv["content"])
                            )
                        else:
                            role, content = "assistant", str(conv)
                        messages.append({"role": role, "content": content})
                elif "messages" in example:
                    # Ensure all content is string format
                    messages = []
                    for msg in example["messages"]:
                        if isinstance(msg.get("content"), list):
                            # Convert list content to string for SFT
                            content_parts = []
                            for item in msg["content"]:
                                if (
                                    isinstance(item, dict)
                                    and item.get("type") == "text"
                                ):
                                    content_parts.append(item.get("text", ""))
                                elif isinstance(item, str):
                                    content_parts.append(item)
                            content = (
                                " ".join(content_parts)
                                if content_parts
                                else str(msg["content"])
                            )
                        else:
                            content = msg.get("content", "")
                        messages.append(
                            {"role": msg.get("role", "user"), "content": content}
                        )
                    return {"messages": messages}
                else:
                    messages = [
                        {
                            "role": "user",
                            "content": example.get(
                                "input",
                                example.get("prompt", "Generate a function call."),
                            ),
                        },
                        {
                            "role": "assistant",
                            "content": example.get(
                                "output", example.get("response", "")
                            ),
                        },
                    ]
                return {"messages": messages}

            train_ds = train_ds.map(
                sft_function_example, remove_columns=train_ds.column_names
            )
    else:
        # DPO: Convert to OpenAI API preference pair format
        if has_vision:

            def dpo_vision_example(example):
                return {
                    "input": {
                        "messages": [
                            {"role": "user", "content": "Caption the video."},
                            {
                                "role": "user",
                                "content": [
                                    {
                                        "type": "image_url",
                                        "image_url": {"url": example["video link"]},
                                    }
                                ],
                            },
                        ],
                        "tools": [],
                        "parallel_tool_calls": False,
                    },
                    "preferred_output": [
                        {"role": "assistant", "content": example["text prompt"]}
                    ],
                    "non_preferred_output": [
                        {"role": "assistant", "content": "No caption available."}
                    ],
                }

            train_ds = train_ds.map(
                dpo_vision_example, remove_columns=train_ds.column_names
            )
        else:

            def dpo_function_example(example):
                if "conversations" in example and len(example["conversations"]) >= 2:
                    conv = example["conversations"]
                    if "value" in conv[0]:
                        user_msg, assistant_msg = (
                            conv[0]["value"],
                            conv[1]["value"] if len(conv) > 1 else "",
                        )
                    else:
                        user_msg = next(
                            (
                                msg.get("content", "")
                                for msg in conv
                                if msg.get("role") in ["human", "user"]
                            ),
                            "",
                        )
                        assistant_msg = next(
                            (
                                msg.get("content", "")
                                for msg in conv
                                if msg.get("role") in ["assistant", "model"]
                            ),
                            "",
                        )
                elif "messages" in example and len(example["messages"]) >= 2:
                    user_msg, assistant_msg = (
                        example["messages"][0]["content"],
                        example["messages"][1]["content"],
                    )
                else:
                    user_msg = example.get(
                        "input", example.get("prompt", "Generate a function call.")
                    )
                    assistant_msg = example.get("output", example.get("response", ""))

                return {
                    "input": {
                        "messages": [{"role": "user", "content": user_msg}],
                        "tools": [],
                        "parallel_tool_calls": False,
                    },
                    "preferred_output": [
                        {"role": "assistant", "content": assistant_msg}
                    ],
                    "non_preferred_output": [
                        {
                            "role": "assistant",
                            "content": "I cannot help with that function call.",
                        }
                    ],
                }

            train_ds = train_ds.map(
                dpo_function_example, remove_columns=train_ds.column_names
            )

    logging.info(f"    ✅ {method.upper()} dataset prepared")
    return train_ds


def prepare_and_save_dataset(training_file_id: str, method_type: str) -> str:
    """Prepare dataset and save as JSONL file."""
    # Resolve training file ID to dataset
    if training_file_id not in FILE_ID_TO_DATASET:
        raise ValueError(
            f"Unknown training_file ID: {training_file_id}. Available IDs: {list(FILE_ID_TO_DATASET.keys())}"
        )

    dataset_name = FILE_ID_TO_DATASET[training_file_id]

    # Load and prepare dataset
    train_dataset = load_and_prepare_dataset(
        dataset_name=dataset_name, method=method_type
    )

    # Ensure files directory exists
    os.makedirs(FILES_DIR, exist_ok=True)

    # Create filename based on method type
    if method_type == METHOD_TYPE_DPO:
        jsonl_file_path = os.path.join(FILES_DIR, f"{training_file_id}-dpo.jsonl")
    else:
        jsonl_file_path = os.path.join(FILES_DIR, f"{training_file_id}-default.jsonl")

    logging.info(f"💾 Saving dataset to {jsonl_file_path}")
    with open(jsonl_file_path, "w") as f:
        for example in train_dataset:
            f.write(json.dumps(example) + "\n")

    logging.info(f"✅ Dataset saved with {len(train_dataset)} examples")
    return jsonl_file_path


def validate_dataset_file(
    training_file_id: str, method_type: str = METHOD_TYPE_SUPERVISED
) -> bool:
    """Validate that the dataset file exists and is in the correct format."""
    # Create filename based on method type
    if method_type == METHOD_TYPE_DPO:
        jsonl_file_path = os.path.join(FILES_DIR, f"{training_file_id}-dpo.jsonl")
    else:
        jsonl_file_path = os.path.join(FILES_DIR, f"{training_file_id}-default.jsonl")

    if not os.path.exists(jsonl_file_path):
        raise ValueError(f"Dataset file not found: {jsonl_file_path}")

    # Check file format by reading first few lines
    try:
        with open(jsonl_file_path) as f:
            for i, line in enumerate(f):
                if i >= 5:  # Check first 5 lines
                    break
                example = json.loads(line.strip())
                # Basic validation - ensure it's a dict
                if not isinstance(example, dict):
                    raise ValueError(
                        f"Invalid JSONL format: line {i + 1} is not a JSON object"
                    )

                # Method-specific validation
                if method_type == METHOD_TYPE_SUPERVISED:
                    if "messages" not in example:
                        raise ValueError(
                            f"Invalid SFT format: line {i + 1} missing 'messages' field"
                        )
                elif method_type == METHOD_TYPE_DPO:
                    required_fields = [
                        "input",
                        "preferred_output",
                        "non_preferred_output",
                    ]
                    for field in required_fields:
                        if field not in example:
                            raise ValueError(
                                f"Invalid DPO format: line {i + 1} missing '{field}' field"
                            )
        logging.info(f"✅ Dataset file validated: {jsonl_file_path}")
        return True
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSONL format in {jsonl_file_path}: {e}") from e
    except Exception as e:
        raise ValueError(f"Error validating dataset file {jsonl_file_path}: {e}") from e


def main():
    """Main function to prepare all datasets in SFT format."""
    print("🔧 Preparing all datasets in SFT format...")

    for file_id, dataset_name in FILE_ID_TO_DATASET.items():
        print(f"📊 Processing dataset: {dataset_name} (file_id: {file_id})")

        try:
            # Load the dataset
            if dataset_name == "TIGER-Lab/VideoFeedback":
                dataset = load_dataset(dataset_name, "annotated")
            else:
                dataset = load_dataset(dataset_name)
            train_ds = dataset["train"]

            # Detect if this is a vision dataset
            has_vision = detect_vision_dataset(dataset_name, train_ds)
            print(f"    Vision dataset: {has_vision}")

            # Format for SFT (same format for both vision and text)
            def sft_format_example(example, vision_flag=has_vision):
                if vision_flag:
                    # For vision data, use simple text format to avoid mixing issues
                    # The processor will handle video URLs as text
                    messages = [
                        {
                            "role": "user",
                            "content": f"Caption the video: {example['video link']}",
                        },
                        {"role": "assistant", "content": example["text prompt"]},
                    ]
                else:
                    # For text data, use simple conversation format
                    if "conversations" in example:
                        messages = []
                        for conv in example["conversations"]:
                            if "from" in conv and "value" in conv:
                                role = (
                                    "user" if conv["from"] == "human" else "assistant"
                                )
                                content = (
                                    conv["value"]
                                    if isinstance(conv["value"], str)
                                    else str(conv["value"])
                                )
                            elif "role" in conv and "content" in conv:
                                role = (
                                    "user" if conv["role"] == "human" else "assistant"
                                )
                                content = (
                                    conv["content"]
                                    if isinstance(conv["content"], str)
                                    else str(conv["content"])
                                )
                            else:
                                role, content = "assistant", str(conv)
                            messages.append({"role": role, "content": content})
                    elif "messages" in example:
                        # Ensure all content is string format
                        messages = []
                        for msg in example["messages"]:
                            if isinstance(msg.get("content"), list):
                                # Convert list content to string for SFT
                                content_parts = []
                                for item in msg["content"]:
                                    if (
                                        isinstance(item, dict)
                                        and item.get("type") == "text"
                                    ):
                                        content_parts.append(item.get("text", ""))
                                    elif isinstance(item, str):
                                        content_parts.append(item)
                                content = (
                                    " ".join(content_parts)
                                    if content_parts
                                    else str(msg["content"])
                                )
                            else:
                                content = msg.get("content", "")
                            messages.append(
                                {"role": msg.get("role", "user"), "content": content}
                            )
                    else:
                        messages = [
                            {
                                "role": "user",
                                "content": example.get(
                                    "input",
                                    example.get("prompt", "Generate a response."),
                                ),
                            },
                            {
                                "role": "assistant",
                                "content": example.get(
                                    "output", example.get("response", "")
                                ),
                            },
                        ]

                return {"messages": messages}

            # Apply formatting and remove all other columns
            train_ds = train_ds.map(
                sft_format_example, remove_columns=train_ds.column_names
            )

            # Save to JSONL file
            jsonl_file_path = os.path.join(FILES_DIR, f"{file_id}-default.jsonl")
            train_ds.to_json(jsonl_file_path)

            file_size = os.path.getsize(jsonl_file_path)
            print(
                f"    ✅ Saved {len(train_ds)} examples to {jsonl_file_path} ({file_size} bytes)"
            )

        except Exception as e:
            print(f"    ❌ Error processing {dataset_name}: {e}")

    print("🎉 Dataset preparation completed!")


if __name__ == "__main__":
    main()
