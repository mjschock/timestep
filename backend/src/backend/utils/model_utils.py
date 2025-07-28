import pprint
from typing import Any

import torch
from transformers import StoppingCriteria


class ToolCallStoppingCriteria(StoppingCriteria):
    def __init__(self, tokenizer: Any, stop_string: str = "</tool_call>") -> None:
        self.tokenizer = tokenizer
        self.stop_string = stop_string
        # Encode the stop string
        self.stop_token_ids = tokenizer.encode(stop_string, add_special_tokens=False)

    def __call__(
        self, input_ids: torch.LongTensor, scores: torch.FloatTensor, **kwargs: Any
    ) -> bool:
        # Check if the last generated tokens match our stop sequence
        for batch_idx in range(input_ids.shape[0]):
            # Get the last few tokens to check
            last_tokens = input_ids[batch_idx, -len(self.stop_token_ids) :].tolist()
            if last_tokens == self.stop_token_ids:
                return True
        return False


# All built-in tools (alphabetical order by name)
BUILTIN_TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "code_interpreter",
            "description": "Execute Python code to perform calculations or data processing.",
            "parameters": {
                "type": "object",
                "properties": {
                    "code": {
                        "type": "string",
                        "description": "The Python code to execute",
                    }
                },
                "required": ["code"],
                "additionalProperties": False,
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "talk_to_user",
            "description": "Communicate with the user by providing a text response",
            "parameters": {
                "type": "object",
                "properties": {
                    "response": {
                        "type": "string",
                        "description": "The message to communicate to the user",
                    }
                },
                "required": ["response"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "web_search",
            "description": "Search the web for information.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The search query to look up",
                    }
                },
                "required": ["query"],
                "additionalProperties": False,
            },
        },
    },
]

# Mapping of built-in tools to their 1-shot examples (excluding talk_to_user)
BUILTIN_TOOL_EXAMPLES = {
    "code_interpreter": {
        "user_message": "How many r's are in the word 'strawberry'?",
        "assistant_response": "<observation>The user is asking me to count the letter 'r' in the word 'strawberry'.</observation><thought>I need to count the occurrences of the letter 'r' in 'strawberry'. I can use Python code to do this accurately with the count() method.</thought><tool_call>\n{'name': 'code_interpreter', 'arguments': {'code': \"'strawberry'.count('r')\"}}\n</tool_call>",
        "tool_response": "3",
        "final_response": "<observation>The code execution returned 3, indicating there are 3 r's in 'strawberry'.</observation><thought>I have the answer to the user's question. I should communicate this result clearly to the user.</thought><tool_call>\n{'name': 'talk_to_user', 'arguments': {'response': \"There are 3 r's in the word 'strawberry'.\"}}\n</tool_call>",
    },
    "web_search": {
        "user_message": "What is the answer to the Ultimate Question of Life, the Universe, and Everything?",
        "assistant_response": "<observation>The user is asking about the Ultimate Question of Life, the Universe, and Everything.</observation><thought>This is a reference to Douglas Adams' 'The Hitchhiker's Guide to the Galaxy'. I should search the web to get accurate information about this famous question and its answer.</thought><tool_call>\n{'name': 'web_search', 'arguments': {'query': 'What is the answer to the Ultimate Question of Life, the Universe, and Everything?'}}\n</tool_call>",
        "tool_response": "The answer to the Ultimate Question of Life, the Universe, and Everything is 42.",
        "final_response": "<observation>The web search returned that the answer to the Ultimate Question of Life, the Universe, and Everything is 42.</observation><thought>I have the answer from the web search. This is the famous answer from Douglas Adams' work. I should communicate this to the user.</thought><tool_call>\n{'name': 'talk_to_user', 'arguments': {'response': '42'}}\n</tool_call>",
    },
}


def create_base_messages(tools: list[dict[str, Any]]) -> list[dict[str, str]]:
    """Create the base conversation messages for tool calling demonstrations."""
    messages = [
        {
            "content": f"""You are an AI agent acting as an assistant on behalf of a human user.

You are aware of the following tools available to the human user in this environment:
{pprint.pformat(tools)}

You MUST always respond in exactly this format:
1. <observation></observation> - Your observation of the user message or tool response
2. <thought></thought> - Your reasoning about what to do next
3. <tool_call></tool_call> - A tool call (use talk_to_user to communicate responses)

For tool calls, use this exact JSON format:
{{'name': 'function_name', 'arguments': {{'parameter': 'value'}}}}

To communicate with the user, use:
{{'name': 'talk_to_user', 'arguments': {{'response': 'your message here'}}}}

You will follow this agent-environment cycle of sensing, thinking, and acting consistently.""",
            "role": "system",
        }
    ]

    # Find which built-in tools are present in the tools list (excluding talk_to_user)
    tool_names = {
        tool["function"]["name"] for tool in tools if tool.get("type") == "function"
    }

    # Add 1-shot examples for built-in tools that are present (in a consistent order)
    for tool_name in ["code_interpreter", "web_search"]:  # Maintain consistent order
        if tool_name in tool_names and tool_name in BUILTIN_TOOL_EXAMPLES:
            example = BUILTIN_TOOL_EXAMPLES[tool_name]

            # Add the example conversation
            messages.extend(
                [
                    {
                        "content": example["user_message"],
                        "role": "user",
                    },
                    {
                        "content": example["assistant_response"],
                        "role": "assistant",
                    },
                    {
                        "content": example["tool_response"],
                        "role": "tool",
                    },
                    {
                        "content": example["final_response"],
                        "role": "assistant",
                    },
                ]
            )

    return messages


def validate_chat_template(processor: Any, original_chat_template: str = "") -> None:
    """Validate that the chat template works correctly with expected message formats.

    WARNING: Do not pass chat_template explicitly to apply_chat_template() as it bypasses
    video preprocessing and will break video content handling (<video> tags).
    """
    from backend.logging_config import logger

    # Test messages with different scenarios our training data will have
    test_cases = [
        {
            "name": "simple_text_message",
            "messages": [
                {
                    "role": "system",
                    "content": [
                        {"type": "text", "text": "You are a helpful assistant."}
                    ],
                },
                {
                    "role": "user",
                    "content": [{"type": "text", "text": "Hello, how are you?"}],
                },
                {
                    "role": "assistant",
                    "content": [{"type": "text", "text": "I'm doing well, thank you!"}],
                },
            ],
            "expected": "<|im_start|>System: You are a helpful assistant.<end_of_utterance>\nUser: Hello, how are you?<end_of_utterance>\nAssistant: I'm doing well, thank you!<end_of_utterance>\n",
            "add_generation_prompt": False,
            "tools": None,
        },
        {
            "name": "simple_text_message_with_generation",
            "messages": [
                {
                    "role": "system",
                    "content": [
                        {"type": "text", "text": "You are a helpful assistant."}
                    ],
                },
                {
                    "role": "user",
                    "content": [{"type": "text", "text": "Hello, how are you?"}],
                },
            ],
            "expected": "<|im_start|>System: You are a helpful assistant.<end_of_utterance>\nUser: Hello, how are you?<end_of_utterance>\nAssistant:",
            "add_generation_prompt": True,
            "tools": None,
        },
        {
            "name": "assistant_with_tool_calls_only",
            "messages": [
                {
                    "role": "system",
                    "content": [
                        {"type": "text", "text": "You are a drone controller."}
                    ],
                },
                {
                    "role": "user",
                    "content": [{"type": "text", "text": "Take off to 100 meters"}],
                },
                {
                    "role": "assistant",
                    "content": [],
                    "tool_calls": [
                        {
                            "id": "call_1",
                            "type": "function",
                            "function": {
                                "name": "takeoff_drone",
                                "arguments": '{"altitude": 100}',
                            },
                        }
                    ],
                },
            ],
            "expected": '<|im_start|>System: You are a drone controller.<end_of_utterance>\nUser: Take off to 100 meters<end_of_utterance>\nAssistant: <tool_call>\n{"arguments": {"altitude": 100}, "name": "takeoff_drone"}\n</tool_call><end_of_utterance>\n',
            "add_generation_prompt": False,
            "tools": [
                {
                    "type": "function",
                    "function": {
                        "name": "takeoff_drone",
                        "description": "Control the drone to take off to a specified altitude",
                        "parameters": {
                            "type": "object",
                            "properties": {
                                "altitude": {
                                    "type": "integer",
                                    "description": "The altitude in meters to take off to",
                                }
                            },
                            "required": ["altitude"],
                        },
                    },
                }
            ],
        },
        {
            "name": "user_with_image_content",
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "image",
                            "url": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/bee.jpg",
                        },
                        {"type": "text", "text": "Can you describe this image?"},
                    ],
                },
            ],
            "expected": "<|im_start|>User:<image>Can you describe this image?<end_of_utterance>\nAssistant:",
            "add_generation_prompt": True,
            "tools": None,
        },
        {
            "name": "user_with_video_content",
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "video",
                            "path": "https://huggingface.co/datasets/hexuan21/VideoFeedback-videos-mp4/resolve/main/p/p110924.mp4",
                        },
                        {"type": "text", "text": "Describe this video in detail"},
                    ],
                },
            ],
            # TODO: Video content should be handled by processor, not template - will revisit later
            "expected": "<|im_start|>User: <video>Describe this video in detail<end_of_utterance>\nAssistant:",
            "add_generation_prompt": True,
            "tools": None,
        },
        {
            "name": "user_with_multiple_images",
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "What is the similarity between these two images?",
                        },
                        {
                            "type": "image",
                            "url": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/bee.jpg",
                        },
                        {
                            "type": "image",
                            "url": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/0052a70beed5bf71b92610a43a52df6d286cd5f3/diffusers/rabbit.jpg",
                        },
                    ],
                },
            ],
            "expected": "<|im_start|>User: What is the similarity between these two images?<image><image><end_of_utterance>\nAssistant:",
            "add_generation_prompt": True,
            "tools": None,
        },
    ]

    logger.info("🧪 Starting chat template validation...")

    # First validate with the original chat template if provided
    if original_chat_template:
        logger.info("🧪 Validating original chat template...")

        # Save current template and set original template on processor
        current_template = processor.chat_template
        processor.chat_template = original_chat_template

        try:
            for test_case in test_cases:
                # Skip test cases with tools for original template validation
                if test_case["tools"] is not None:
                    logger.info(
                        f"Skipping original template validation for {test_case['name']} (has tools)"
                    )
                    continue

                try:
                    logger.info(f"Testing original template: {test_case['name']}")

                    # Apply chat template without explicit template parameter to enable video preprocessing
                    result = processor.apply_chat_template(
                        test_case["messages"],
                        add_generation_prompt=test_case["add_generation_prompt"],
                        tools=test_case["tools"],
                        tokenize=False,
                        return_dict=False,
                    )

                    logger.info(f"Original template output for {test_case['name']}:")
                    logger.info(f"'{result}'")

                    # Exact assertion for original template
                    assert test_case["expected"] == result, (  # noqa: S101
                        f"Original template failed: {test_case['expected']}\n!=\n{result}"
                    )

                    logger.info(
                        f"✅ Original template {test_case['name']} validation passed"
                    )

                except Exception as e:
                    logger.error(
                        f"❌ Original chat template validation failed for {test_case['name']}: {e}"
                    )
                    logger.error(f"Messages: {test_case['messages']}")
                    raise RuntimeError(
                        f"Original chat template validation failed: {e}"
                    ) from e
        finally:
            # Restore current template
            processor.chat_template = current_template

    # Then validate with the current chat template
    logger.info("🧪 Validating custom chat template...")

    # Assert that the required generation tags are present in the chat template
    chat_template = processor.chat_template
    assert (  # noqa: S101
        "{% if message['role'] == 'assistant' and message.get('weight', 1) == 1 %}{% generation %}"
        in chat_template
    ), "Chat template must contain the exact generation start pattern"
    assert "{% endgeneration %}" in chat_template, (  # noqa: S101
        "Chat template must contain '{% endgeneration %}' tag"
    )

    for test_case in test_cases:
        try:
            logger.info(f"Testing: {test_case['name']}")

            # Apply chat template without tokenization to see the text output
            result = processor.apply_chat_template(
                test_case["messages"],
                add_generation_prompt=test_case["add_generation_prompt"],
                tools=test_case["tools"],
                tokenize=False,
                return_dict=False,
            )

            logger.info(f"Chat template output for {test_case['name']}:")
            logger.info(f"'{result}'")

            # Exact assertion
            assert test_case["expected"] == result, (  # noqa: S101
                f"{test_case['expected']}\n!=\n{result}"
            )

            logger.info(f"✅ {test_case['name']} validation passed")

        except Exception as e:
            logger.error(
                f"❌ Chat template validation failed for {test_case['name']}: {e}"
            )
            logger.error(f"Messages: {test_case['messages']}")
            raise RuntimeError(f"Chat template validation failed: {e}") from e

    logger.info("🎉 All chat template validations passed!")
