#!/usr/bin/env python3
"""
Unified testing script for fine-tuning utilities.
This script prepares datasets, populates file metadata, and runs fine-tuning.
Run this from the project root directory.
"""

import sys
import os
import time
import json
import shutil
from typing import Any

# Add the src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from backend.services.files_service import DATA_DIR, FILES_METADATA
from backend.utils.fine_tuning_utils import main
from datasets import load_dataset

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

def copy_drone_training_file():
    """Copy the drone training JSONL file directly to data/files directory."""
    source_file = "tests/fixtures/jsonl/drone_training.jsonl"
    target_file = os.path.join(DATA_DIR, "file-drone-training-default.jsonl")

    # Ensure files directory exists
    os.makedirs(DATA_DIR, exist_ok=True)

    # Check if target file already exists
    if os.path.exists(target_file):
        file_size = os.path.getsize(target_file)
        print(f"    ⏭️  Skipping drone training file (already exists): {target_file} ({file_size} bytes)")
        return target_file

    if os.path.exists(source_file):
        try:
            shutil.copy2(source_file, target_file)
            file_size = os.path.getsize(target_file)
            print(f"    ✅ Copied drone training file to {target_file} ({file_size} bytes)")
            return target_file
        except Exception as e:
            print(f"    ❌ Error copying drone training file: {e}")
            return None
    else:
        print(f"    ❌ Source file not found: {source_file}")
        return None

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
        print(f"Could not detect vision for dataset {dataset_name}: {e}")
        return False

def prepare_datasets():
    """Prepare all datasets in SFT format."""
    print("🔧 Preparing all datasets in SFT format...")

    # Copy drone training file first
    print("📊 Processing drone training file...")
    copy_drone_training_file()

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
            jsonl_file_path = os.path.join(DATA_DIR, f"{file_id}-default.jsonl")
            
            # Check if file already exists
            if os.path.exists(jsonl_file_path):
                file_size = os.path.getsize(jsonl_file_path)
                print(f"    ⏭️  Skipping {dataset_name} (already exists): {jsonl_file_path} ({file_size} bytes)")
            else:
                train_ds.to_json(jsonl_file_path)
                file_size = os.path.getsize(jsonl_file_path)
                print(
                    f"    ✅ Saved {len(train_ds)} examples to {jsonl_file_path} ({file_size} bytes)"
                )

        except Exception as e:
            print(f"    ❌ Error processing {dataset_name}: {e}")

    print("🎉 Dataset preparation completed!")

def populate_files_metadata():
    """Populate FILES_METADATA with existing files."""
    
    print("🔧 Populating FILES_METADATA with existing files...")
    
    # Scan the data/files directory
    if not os.path.exists(DATA_DIR):
        print(f"    ❌ Data directory not found: {DATA_DIR}")
        return
    
    files = os.listdir(DATA_DIR)
    print(f"    📁 Found {len(files)} files in {DATA_DIR}")
    
    # Define the expected file mappings
    file_mappings = {
        "file-drone-training-default.jsonl": {
            "file_id": "file-drone-training-default",
            "filename": "drone_training.jsonl",
            "purpose": "fine-tune"
        },
        "file-tiger-lab-video-feedback-default.jsonl": {
            "file_id": "file-tiger-lab-video-feedback-default", 
            "filename": "tiger_lab_video_feedback.jsonl",
            "purpose": "fine-tune"
        },
        "file-jofthomas-hermes-function-calling-thinking-v1-default.jsonl": {
            "file_id": "file-jofthomas-hermes-function-calling-thinking-v1",
            "filename": "hermes_function_calling_thinking.jsonl",
            "purpose": "fine-tune"
        },
        "file-nous-research-hermes-function-calling-v1-default.jsonl": {
            "file_id": "file-nous-research-hermes-function-calling-v1",
            "filename": "hermes_function_calling.jsonl", 
            "purpose": "fine-tune"
        }
    }
    
    for filename in files:
        if filename.endswith('.jsonl'):
            if filename in file_mappings:
                mapping = file_mappings[filename]
                file_id = mapping["file_id"]
                actual_filename = mapping["filename"]
                purpose = mapping["purpose"]
                
                file_path = os.path.join(DATA_DIR, filename)
                file_size = os.path.getsize(file_path)
                
                # Create file object
                file_obj = {
                    "id": file_id,
                    "object": "file",
                    "bytes": file_size,
                    "created_at": int(time.time()),
                    "filename": actual_filename,
                    "purpose": purpose,
                    "status": "uploaded",
                    "status_details": None,
                    "file_path": file_path
                }
                
                FILES_METADATA[file_id] = file_obj
                print(f"    ✅ Registered {file_id}: {actual_filename} ({file_size} bytes)")
            else:
                print(f"    ⚠️  Skipping unknown file: {filename}")
    
    print(f"📊 Total files in FILES_METADATA: {len(FILES_METADATA)}")
    for file_id, metadata in FILES_METADATA.items():
        print(f"    - {file_id}: {metadata['filename']} ({metadata['bytes']} bytes)")

if __name__ == "__main__":
    # Step 1: Prepare datasets (download and format)
    print("="*80)
    print("STEP 1: Preparing datasets...")
    print("="*80)
    prepare_datasets()
    
    # Step 2: Populate the files metadata
    print("\n" + "="*80)
    print("STEP 2: Populating file metadata...")
    print("="*80)
    populate_files_metadata()
    
    # Step 3: Run the fine-tuning
    print("\n" + "="*80)
    print("STEP 3: Running fine-tuning...")
    print("="*80)
    main() 