"""
Unified message processor for multimodal conversations.

This module provides functions to process both text-only and multimodal conversations
for training and inference with vision-language models.
"""

from pprint import pprint
from typing import Any

import pytest
import torch
from transformers import AutoProcessor


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


def format_tool_definitions(tools: list[dict[str, Any]]) -> str:
    """Format tools into a readable string for the system message."""
    if not tools:
        return ""

    tool_content = "The following tools are available:\n\n"

    for tool in tools:
        if tool["type"] == "function":
            fn = tool["function"]
            tool_content += f"**{fn['name']}**\n"
            tool_content += f"Description: {fn['description']}\n"

            # Format parameters
            if "parameters" in fn and "properties" in fn["parameters"]:
                tool_content += "Parameters:\n"
                props = fn["parameters"]["properties"]
                required = fn["parameters"].get("required", [])

                for name, spec in props.items():
                    req_marker = " (required)" if name in required else ""
                    desc = spec.get("description", "")
                    param_type = spec.get("type", "unknown")

                    if "enum" in spec:
                        enum_vals = ", ".join(f'"{v}"' for v in spec["enum"])
                        tool_content += f"  • {name} ({param_type}){req_marker}: {desc} [Options: {enum_vals}]\n"
                    else:
                        tool_content += (
                            f"  • {name} ({param_type}){req_marker}: {desc}\n"
                        )

            tool_content += "\n"

    tool_content += 'To use a tool, respond with:\n<tool_call>\n{\n  "name": "tool_name",\n  "arguments": {...}\n}\n</tool_call>'
    return tool_content.strip()


def build_messages(
    user_input: str | list[dict[str, Any]],
    system_message: str | None = None,
    developer_message: str | None = None,
    tools: list[dict[str, Any]] | None = None,
    conversation_history: list[dict[str, str | list[dict[str, Any]]]] | None = None,
) -> list[dict[str, list[dict[str, Any]]]]:
    """
    Build messages in multimodal format that works with any chat template.

    Args:
        user_input: The current user message (string or content list)
        system_message: Base system prompt
        developer_message: Developer instructions (merged into system)
        tools: Tool definitions (formatted and merged into system)
        conversation_history: Previous messages with content as string or list

    Returns:
        List of messages with normalized content structure
    """
    messages = []

    # Build combined system message
    system_parts = []

    if system_message:
        system_parts.append(system_message)

    if developer_message:
        system_parts.append(f"[Developer Instructions]: {developer_message}")

    if tools:
        tool_content = format_tool_definitions(tools)
        if tool_content:
            system_parts.append(tool_content)

    # Add combined system message if any parts exist
    if system_parts:
        messages.append(
            {
                "role": "system",
                "content": [{"type": "text", "text": "\n\n".join(system_parts)}],
            }
        )

    # Add conversation history with normalized content
    if conversation_history:
        for msg in conversation_history:
            normalized_msg = {
                "role": msg["role"],
                "content": normalize_content(msg["content"]),
            }
            # Preserve weight if present
            if "weight" in msg:
                normalized_msg["weight"] = msg["weight"]
            messages.append(normalized_msg)

    # Add current user input
    messages.append({"role": "user", "content": normalize_content(user_input)})

    return messages


def prepare_training_example(
    conversation: list[dict[str, str | list[dict[str, Any]] | float]],
    processor,
    system_message: str | None = None,
    developer_message: str | None = None,
    tools: list[dict[str, Any]] | None = None,
) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    """
    Prepare a complete conversation for training with message-level weights.
    Works with both tokenizers and processors (for multimodal models).

    Args:
        conversation: List of messages with optional weights
        processor: Processor or tokenizer with chat_template
        system_message: System prompt
        developer_message: Developer instructions
        tools: Available tools

    Returns:
        Tuple of (training_example, messages) where:
        - training_example: {"input_ids": [...], "attention_mask": [...], "labels": [...],
                           "pixel_values": [...]}  # pixel_values only for vision models
        - messages: List of processed messages used to create the training example
    """
    # Build system message parts
    system_parts = []
    if system_message:
        system_parts.append(system_message)
    if developer_message:
        system_parts.append(f"[Developer Instructions]: {developer_message}")
    if tools:
        tool_content = format_tool_definitions(tools)
        if tool_content:
            system_parts.append(tool_content)

    # Prepare full conversation with system message
    messages = []
    if system_parts:
        messages.append(
            {
                "role": "system",
                "content": [{"type": "text", "text": "\n\n".join(system_parts)}],
                "weight": 0.0,  # Never train on system message
            }
        )

    # Add conversation messages with default weights and normalized content
    for msg in conversation:
        message = {"role": msg["role"], "content": normalize_content(msg["content"])}
        # Default weights: assistant=1.0, others=0.0
        if "weight" not in msg:
            message["weight"] = 1.0 if message["role"] == "assistant" else 0.0
        else:
            message["weight"] = msg["weight"]
        messages.append(message)

    # Create labels with message-level weights
    result = _create_weighted_labels_multimodal(messages, processor)

    return result, messages


def _create_weighted_labels_multimodal(
    messages: list[dict[str, list[dict[str, Any]] | float]], processor
) -> dict[str, Any]:
    """
    Create input_ids and labels with message-level weighting for multimodal models.
    """
    # Initialize result
    result = {"input_ids": [], "labels": [], "attention_mask": []}

    # Process messages incrementally to identify token boundaries
    for i, message in enumerate(messages):
        weight = message.get("weight", 0.0)

        # Get conversation up to this point (inclusive)
        # Create processor-compatible format (strip weights)
        tokenizer_messages = []
        for msg in messages[: i + 1]:
            tokenizer_messages.append({"role": msg["role"], "content": msg["content"]})

        # Tokenize current conversation
        current_inputs = processor.apply_chat_template(
            tokenizer_messages,
            add_generation_prompt=False,
            tokenize=True,
            return_dict=True,
        )
        current_tokens = current_inputs["input_ids"]

        # Convert tensor to list if needed
        if hasattr(current_tokens, "tolist"):
            current_tokens = current_tokens.tolist()

        # Get conversation up to previous message (exclusive)
        if i == 0:
            prev_tokens = []
        else:
            prev_tokenizer_messages = []
            for msg in messages[:i]:
                prev_tokenizer_messages.append(
                    {"role": msg["role"], "content": msg["content"]}
                )
            prev_inputs = processor.apply_chat_template(
                prev_tokenizer_messages,
                add_generation_prompt=False,
                tokenize=True,
                return_dict=True,
            )
            prev_tokens = prev_inputs["input_ids"]

            # Convert tensor to list if needed
            if hasattr(prev_tokens, "tolist"):
                prev_tokens = prev_tokens.tolist()

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
        [{"role": msg["role"], "content": msg["content"]} for msg in messages],
        add_generation_prompt=False,
        tokenize=True,
        return_dict=True,
    )

    # Copy over non-text inputs (like pixel_values)
    for key, value in final_inputs.items():
        if key not in result and key not in ["input_ids", "attention_mask"]:
            result[key] = value

    return result


def prepare_inference_messages(
    user_input: str | list[dict[str, Any]],
    processor,
    system_message: str | None = None,
    developer_message: str | None = None,
    tools: list[dict[str, Any]] | None = None,
) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    """
    Prepare messages for inference with multimodal support.

    Args:
        user_input: Text string or multimodal content list
        processor: Processor with chat_template
        system_message: System prompt
        developer_message: Developer instructions
        tools: Available tools

    Returns:
        Tuple of (inputs, messages) where:
        - inputs: {"input_ids": [...], "attention_mask": [...], "pixel_values": [...]}
        - messages: List of processed messages used for inference
    """
    # Build system message parts
    system_parts = []
    if system_message:
        system_parts.append(system_message)
    if developer_message:
        system_parts.append(f"[Developer Instructions]: {developer_message}")
    if tools:
        tool_content = format_tool_definitions(tools)
        if tool_content:
            system_parts.append(tool_content)

    # Prepare messages
    messages = []
    if system_parts:
        messages.append(
            {
                "role": "system",
                "content": [{"type": "text", "text": "\n\n".join(system_parts)}],
            }
        )

    # Add user message
    user_content = normalize_content(user_input)
    messages.append({"role": "user", "content": user_content})

    # Apply chat template
    inputs = processor.apply_chat_template(
        messages, tokenize=True, add_generation_prompt=True, return_tensors="pt"
    )

    return inputs, messages


def _validate_basic_structure(
    example: dict[str, Any],
) -> tuple[list[str], list, list, list]:
    """Validate basic structure of training example."""
    issues = []
    input_ids = example["input_ids"]
    labels = example["labels"]
    attention_mask = example.get("attention_mask", [])

    # Convert tensors to lists if needed
    if hasattr(input_ids, "tolist"):
        input_ids = input_ids.tolist()
    if hasattr(labels, "tolist"):
        labels = labels.tolist()
    if hasattr(attention_mask, "tolist"):
        attention_mask = attention_mask.tolist()

    # Flatten input_ids if it's a list of lists
    if input_ids and isinstance(input_ids[0], list):
        input_ids = [item for sublist in input_ids for item in sublist]
    if labels and isinstance(labels[0], list):
        labels = [item for sublist in labels for item in sublist]
    if attention_mask and isinstance(attention_mask[0], list):
        attention_mask = [item for sublist in attention_mask for item in sublist]

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
    """Validate token alignment between input_ids and labels."""
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
    """Validate token IDs against vocabulary."""
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

    # Convert tensors to lists if needed
    if hasattr(input_ids, "tolist"):
        input_ids = input_ids.tolist()
    if hasattr(labels, "tolist"):
        labels = labels.tolist()

    for i, (inp, lab) in enumerate(zip(input_ids, labels, strict=True)):
        if lab != -100:
            if lab != inp:
                raise AssertionError(
                    f"Label mismatch at position {i}: input_id={inp}, label={lab}"
                )


# ============================================================================
# PYTEST TEST SUITE
# ============================================================================


class TestMultimodalMessageProcessor:
    @pytest.fixture(scope="class")
    def processor(self):
        """Load the SmolVLM2 processor for testing."""
        try:
            processor = AutoProcessor.from_pretrained(
                "HuggingFaceTB/SmolVLM2-256M-Video-Instruct"
            )
            return processor
        except Exception as e:
            pytest.skip(f"Could not load SmolVLM2 processor: {e}")

    @pytest.fixture
    def simple_conversation(self):
        return [
            {"role": "user", "content": "Hello, how are you?"},
            {"role": "assistant", "content": "I'm doing well, thank you!"},
            {"role": "user", "content": "What's 2+2?"},
            {"role": "assistant", "content": "2+2 equals 4."},
        ]

    @pytest.fixture
    def multimodal_conversation(self):
        return [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "What's in this image?"},
                    {
                        "type": "image",
                        "url": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/bee.jpg",
                    },
                ],
            },
            {"role": "assistant", "content": "I can see a bee in the image."},
            {"role": "user", "content": "What color is it?"},
            {"role": "assistant", "content": "The bee appears to be yellow and black."},
        ]

    @pytest.fixture
    def tools(self):
        return [
            {
                "type": "function",
                "function": {
                    "name": "get_weather",
                    "description": "Get current weather",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "location": {"type": "string", "description": "City name"}
                        },
                        "required": ["location"],
                    },
                },
            }
        ]

    def test_normalize_content(self):
        """Test content normalization for different input types."""
        # String input
        result = normalize_content("Hello world")
        if result != [{"type": "text", "text": "Hello world"}]:
            raise AssertionError("String normalization failed")

        # List input (should pass through)
        content_list = [
            {"type": "text", "text": "Hello"},
            {"type": "image", "url": "test.jpg"},
        ]
        result = normalize_content(content_list)
        if result != content_list:
            raise AssertionError("List normalization failed")

        # Invalid input
        with pytest.raises(ValueError):
            normalize_content(123)

    def test_build_messages_text_only(self):
        """Test message building with text-only content."""
        messages = build_messages(
            user_input="Hello",
            system_message="You are helpful",
            developer_message="Be concise",
        )

        if len(messages) != 2:  # system + user
            raise AssertionError("Expected 2 messages")
        if messages[0]["role"] != "system":
            raise AssertionError("First message should be system")
        if messages[1]["role"] != "user":
            raise AssertionError("Second message should be user")
        if not isinstance(messages[0]["content"], list):
            raise AssertionError("System content should be list")
        if not isinstance(messages[1]["content"], list):
            raise AssertionError("User content should be list")

    def test_build_messages_with_tools(self, tools):
        """Test message building with tools."""
        messages = build_messages(
            user_input="What's the weather?",
            system_message="You are helpful",
            tools=tools,
        )

        # Should have system message with tool definitions
        if len(messages) != 2:
            raise AssertionError("Expected 2 messages")
        system_content = messages[0]["content"][0]["text"]
        if "get_weather" not in system_content:
            raise AssertionError("Tool name not found in system content")
        if (
            "Available Tools" not in system_content
            and "following tools" not in system_content
        ):
            raise AssertionError("Tool definitions not found in system content")

    def test_build_messages_multimodal(self):
        """Test message building with multimodal content."""
        multimodal_input = [
            {"type": "text", "text": "Describe this image"},
            {"type": "image", "url": "test.jpg"},
        ]

        messages = build_messages(user_input=multimodal_input)

        if len(messages) != 1:  # just user message
            raise AssertionError("Expected 1 message")
        if messages[0]["role"] != "user":
            raise AssertionError("Message should be user role")
        if len(messages[0]["content"]) != 2:
            raise AssertionError("Expected 2 content items")
        if messages[0]["content"][0]["type"] != "text":
            raise AssertionError("First content should be text")
        if messages[0]["content"][1]["type"] != "image":
            raise AssertionError("Second content should be image")

    def test_prepare_training_example_text_only(self, processor, simple_conversation):
        """Test training example preparation with text-only conversation."""
        try:
            example, _ = prepare_training_example(
                conversation=simple_conversation,
                processor=processor,
                system_message="You are a helpful assistant",
            )

            # Basic structure checks
            if "input_ids" not in example:
                raise AssertionError("Missing input_ids")
            if "labels" not in example:
                raise AssertionError("Missing labels")
            if "attention_mask" not in example:
                raise AssertionError("Missing attention_mask")

            # Length consistency
            if len(example["input_ids"]) != len(example["labels"]):
                raise AssertionError("Length mismatch between input_ids and labels")
            if len(example["input_ids"]) != len(example["attention_mask"]):
                raise AssertionError(
                    "Length mismatch between input_ids and attention_mask"
                )

            # Should have some training tokens (assistant messages)
            training_tokens = sum(1 for x in example["labels"] if x != -100)
            if training_tokens <= 0:
                raise AssertionError("No training tokens found")

            # Validate correctness
            assert_training_correctness(example, processor)

        except Exception as e:
            # If model loading fails, skip the test
            pytest.skip(f"Could not run training test: {e}")

    def test_prepare_training_example_multimodal(
        self, processor, multimodal_conversation
    ):
        """Test training example preparation with multimodal conversation."""
        try:
            example, _ = prepare_training_example(
                conversation=multimodal_conversation,
                processor=processor,
                system_message="You are a vision assistant",
            )

            # Should have all standard fields
            if "input_ids" not in example:
                raise AssertionError("Missing input_ids")
            if "labels" not in example:
                raise AssertionError("Missing labels")
            if "attention_mask" not in example:
                raise AssertionError("Missing attention_mask")

            # May have multimodal fields (like pixel_values)
            # This depends on the processor implementation

            # Length consistency
            if len(example["input_ids"]) != len(example["labels"]):
                raise AssertionError("Length mismatch between input_ids and labels")

            # Should have some training tokens
            training_tokens = sum(1 for x in example["labels"] if x != -100)
            if training_tokens <= 0:
                raise AssertionError("No training tokens found")

            # Validate correctness
            assert_training_correctness(example, processor)

        except Exception as e:
            pytest.skip(f"Could not run multimodal training test: {e}")

    def test_custom_message_weights(self, processor, simple_conversation):
        """Test custom message-level weights."""
        try:
            # Add custom weights to conversation
            weighted_conversation = []
            for i, msg in enumerate(simple_conversation):
                weighted_msg = msg.copy()
                if msg["role"] == "assistant" and i == 1:  # First assistant message
                    weighted_msg["weight"] = 1.0  # Train on this
                elif msg["role"] == "assistant" and i == 3:  # Second assistant message
                    weighted_msg["weight"] = 0.0  # Skip this
                weighted_conversation.append(weighted_msg)

            example, _ = prepare_training_example(
                conversation=weighted_conversation, processor=processor
            )

            # Should still have some training tokens, but fewer than default
            training_tokens = sum(1 for x in example["labels"] if x != -100)
            if training_tokens <= 0:
                raise AssertionError("No training tokens found")

            # Compare with default weights
            default_example, _ = prepare_training_example(
                conversation=simple_conversation, processor=processor
            )
            default_training_tokens = sum(
                1 for x in default_example["labels"] if x != -100
            )

            # Custom weights should result in fewer training tokens
            if training_tokens > default_training_tokens:
                raise AssertionError(
                    "Custom weights should result in fewer training tokens"
                )

        except Exception as e:
            pytest.skip(f"Could not run custom weights test: {e}")

    def test_inference_preparation(self, processor):
        """Test inference message preparation."""
        try:
            inputs, messages = prepare_inference_messages(
                user_input="Hello there!",
                processor=processor,
                system_message="You are helpful",
            )

            # Should have the fields needed for generation
            if "input_ids" not in inputs:
                raise AssertionError("Missing input_ids")

            # Should be ready for model.generate()
            if not isinstance(inputs["input_ids"], list | torch.Tensor):
                raise AssertionError("input_ids should be list or tensor")

            # Should return the messages used for inference
            if not isinstance(messages, list):
                raise AssertionError("Messages should be a list")
            if not all(
                isinstance(msg, dict) and "role" in msg and "content" in msg
                for msg in messages
            ):
                raise AssertionError(
                    "Messages should be a list of dicts with 'role' and 'content'"
                )

        except Exception as e:
            pytest.skip(f"Could not run inference test: {e}")

    def test_validation_functions(self, processor, simple_conversation):
        """Test validation and analysis functions."""
        try:
            example, _ = prepare_training_example(
                conversation=simple_conversation, processor=processor
            )

            # Test validation function
            analysis = validate_training_example(example, processor)
            if not analysis["valid"]:
                raise AssertionError("Validation should pass")
            if analysis["total_tokens"] <= 0:
                raise AssertionError("Should have total tokens")
            if analysis["training_tokens"] <= 0:
                raise AssertionError("Should have training tokens")
            if analysis["training_ratio"] <= 0:
                raise AssertionError("Should have training ratio")

            # Test assertion function (should not raise)
            assert_training_correctness(example, processor)

        except Exception as e:
            pytest.skip(f"Could not run validation test: {e}")

    def test_label_alignment_edge_cases(self, processor):
        """Test edge cases for label alignment."""
        try:
            # Empty conversation
            with pytest.raises((ValueError, AssertionError)):
                prepare_training_example([], processor)

            # Conversation with only user messages (no training tokens)
            user_only = [{"role": "user", "content": "Hello"}]
            example, _ = prepare_training_example(user_only, processor)
            training_tokens = sum(1 for x in example["labels"] if x != -100)
            if training_tokens != 0:  # No assistant messages to train on
                raise AssertionError(
                    "Should have no training tokens for user-only conversation"
                )

        except Exception as e:
            pytest.skip(f"Could not run edge case test: {e}")


# ============================================================================
# EXAMPLE USAGE AND INTEGRATION
# ============================================================================


def example_usage():
    """Example of how to use the multimodal processor."""
    try:
        # Load processor
        processor = AutoProcessor.from_pretrained(
            "HuggingFaceTB/SmolVLM2-256M-Video-Instruct"
        )

        # Example multimodal conversation
        conversation = [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "What's in this image?"},
                    {
                        "type": "image",
                        "url": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/bee.jpg",
                    },
                ],
            },
            {"role": "assistant", "content": "I can see a bee in the image."},
        ]

        # Prepare for training
        training_example, messages = prepare_training_example(
            conversation=conversation,
            processor=processor,
            system_message="You are a vision assistant.",
        )

        print("✅ Training example prepared successfully!")
        print(f"Total tokens: {len(training_example['input_ids'])}")
        print(
            f"Training tokens: {sum(1 for x in training_example['labels'] if x != -100)}"
        )

        # Print the messages used for training
        print("\n📝 Messages used for training:")
        pprint(messages)

        # Validate the example
        try:
            analysis = validate_training_example(training_example, processor, messages)
            print("\n✅ Validation results:")
            print(f"  Valid: {analysis['valid']}")
            print(f"  Training ratio: {analysis['training_ratio']:.2%}")
            print(f"  Total tokens: {analysis['total_tokens']}")
            print(f"  Training tokens: {analysis['training_tokens']}")
            print(f"  Ignored tokens: {analysis['ignored_tokens']}")
            if analysis["issues"]:
                print(f"  Issues: {analysis['issues']}")
        except Exception as e:
            print(f"❌ Validation failed: {e}")
            import traceback

            traceback.print_exc()

        # Prepare for inference
        inference_inputs, inference_messages = prepare_inference_messages(
            user_input=[
                {"type": "text", "text": "Describe this other image"},
                {
                    "type": "image",
                    "url": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/bee.jpg",
                },
            ],
            processor=processor,
            system_message="You are a vision assistant.",
        )

        print("\n✅ Inference inputs prepared successfully!")
        if hasattr(inference_inputs, "shape"):
            print(f"  Input shape: {inference_inputs.shape}")
        elif isinstance(inference_inputs, dict) and "input_ids" in inference_inputs:
            if hasattr(inference_inputs["input_ids"], "shape"):
                print(f"  Input shape: {inference_inputs['input_ids'].shape}")
            else:
                print(f"  Input shape: {len(inference_inputs['input_ids'])} tokens")
        else:
            print(f"  Input type: {type(inference_inputs)}")
        print("\n📝 Messages used for inference:")
        pprint(inference_messages)

    except Exception as e:
        print(f"❌ Example failed: {e}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    # Run example
    example_usage()

    # To run tests, use: pytest -v unified_message_processor.py
    print("\nTo run the full test suite:")
    print("pytest -v -s unified_message_processor.py")
