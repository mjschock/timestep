import pytest
import torch

from model_utils import (
    get_processor,
    assert_training_correctness,
    build_messages,
    normalize_content,
    prepare_inference_messages,
    prepare_training_example,
    validate_training_example,
)


class TestMultimodalMessageProcessor:
    @pytest.fixture(scope="class")
    def processor(self):
        """Load the SmolVLM2 processor for testing."""
        return get_processor()

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
                "name": "get_weather",
                "description": "Get current weather",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {"type": "string", "description": "City name"}
                    },
                    "required": ["location"],
                    "additionalProperties": False,
                },
                "strict": False,
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
        example, _, _ = prepare_training_example(
            conversation=simple_conversation,
            processor=processor,
            system_message="You are a helpful assistant",
        )

        # Basic structure checks
        assert "input_ids" in example, "Missing input_ids"
        assert "labels" in example, "Missing labels"
        assert "attention_mask" in example, "Missing attention_mask"

        # Length consistency
        assert len(example["input_ids"]) == len(example["labels"]), (
            "Length mismatch between input_ids and labels"
        )
        assert len(example["input_ids"]) == len(example["attention_mask"]), (
            "Length mismatch between input_ids and attention_mask"
        )

        # Should have some training tokens (assistant messages)
        training_tokens = sum(1 for x in example["labels"] if x != -100)
        assert training_tokens > 0, "No training tokens found"

        # Validate correctness
        assert_training_correctness(example, processor)

    def test_prepare_training_example_multimodal(
        self, processor, multimodal_conversation
    ):
        """Test training example preparation with multimodal conversation."""
        example, _, _ = prepare_training_example(
            conversation=multimodal_conversation,
            processor=processor,
            system_message="You are a helpful assistant",
        )

        # Should have all standard fields
        assert "input_ids" in example, "Missing input_ids"
        assert "labels" in example, "Missing labels"
        assert "attention_mask" in example, "Missing attention_mask"

        # May have multimodal fields (like pixel_values)
        # This depends on the processor implementation

        # Length consistency
        assert len(example["input_ids"]) == len(example["labels"]), (
            "Length mismatch between input_ids and labels"
        )

        # Should have some training tokens
        training_tokens = sum(1 for x in example["labels"] if x != -100)
        assert training_tokens > 0, "No training tokens found"

        # Validate correctness
        assert_training_correctness(example, processor)

    def test_custom_message_weights(self, processor, simple_conversation):
        """Test custom message-level weights."""
        # Add custom weights to conversation
        weighted_conversation = []
        for i, msg in enumerate(simple_conversation):
            weighted_msg = msg.copy()
            if msg["role"] == "assistant" and i == 1:  # First assistant message
                weighted_msg["weight"] = 1.0  # Train on this
            elif msg["role"] == "assistant" and i == 3:  # Second assistant message
                weighted_msg["weight"] = 0.0  # Skip this
            weighted_conversation.append(weighted_msg)

        example, _, _ = prepare_training_example(
            conversation=weighted_conversation, processor=processor
        )

        # Should still have some training tokens, but fewer than default
        training_tokens = sum(1 for x in example["labels"] if x != -100)
        assert training_tokens > 0, "No training tokens found"

        # Compare with default weights
        default_example, _, _ = prepare_training_example(
            conversation=simple_conversation, processor=processor
        )
        default_training_tokens = sum(1 for x in default_example["labels"] if x != -100)

        # Custom weights should result in fewer training tokens
        assert training_tokens <= default_training_tokens, (
            "Custom weights should result in fewer or equal training tokens"
        )

    def test_inference_preparation(self, processor):
        """Test inference message preparation."""
        inputs, messages, _ = prepare_inference_messages(
            user_input="Hello there!",
            processor=processor,
            system_message="You are helpful",
        )

        # Should have the fields needed for generation
        assert "input_ids" in inputs, "Missing input_ids"

        # Should be ready for model.generate()
        assert isinstance(inputs["input_ids"], list | torch.Tensor), (
            "input_ids should be list or tensor"
        )

        # Should return the messages used for inference
        assert isinstance(messages, list), "Messages should be a list"
        assert all(
            isinstance(msg, dict) and "role" in msg and "content" in msg
            for msg in messages
        ), "Messages should be a list of dicts with 'role' and 'content'"

    def test_validation_functions(self, processor, simple_conversation):
        """Test validation and analysis functions."""
        example, _, _ = prepare_training_example(
            conversation=simple_conversation, processor=processor
        )

        # Test validation function
        analysis = validate_training_example(example, processor)
        assert analysis["valid"], (
            f"Validation should pass, issues: {analysis.get('issues', [])}"
        )
        assert analysis["total_tokens"] > 0, "Should have total tokens"
        assert analysis["training_tokens"] > 0, "Should have training tokens"
        assert analysis["training_ratio"] > 0, "Should have training ratio"

        # Test assertion function (should not raise)
        assert_training_correctness(example, processor)

    def test_label_alignment_edge_cases(self, processor):
        """Test edge cases for label alignment."""
        # Empty conversation
        with pytest.raises((ValueError, AssertionError)):
            prepare_training_example([], processor)

        # Conversation with only user messages (no training tokens)
        user_only = [{"role": "user", "content": "Hello"}]
        example, _, _ = prepare_training_example(user_only, processor)
        training_tokens = sum(1 for x in example["labels"] if x != -100)
        assert training_tokens == 0, (
            "Should have no training tokens for user-only conversation"
        )
