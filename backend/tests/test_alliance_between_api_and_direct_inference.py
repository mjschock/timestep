import pytest
import torch
from transformers import (
    AutoModelForImageTextToText,
    AutoProcessor,
    StoppingCriteriaList,
)

from backend.utils.model_utils import (
    BUILTIN_TOOLS,
    ToolCallStoppingCriteria,
    create_base_messages,
)

# Common test configuration
MODEL_NAME = "HuggingFaceTB/SmolVLM2-256M-Video-Instruct"
DEFAULT_MAX_TOKENS = 64
MULTI_IMAGE_MAX_TOKENS = 32
TOOL_CALLING_MAX_TOKENS = 1024

# Custom tools for testing
CUSTOM_TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_stock_price",
            "description": "Get the current stock price of a company",
            "parameters": {
                "type": "object",
                "properties": {
                    "company": {
                        "type": "string",
                        "description": "The name of the company",
                    }
                },
                "required": ["company"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_movie_details",
            "description": "Get details about a movie",
            "parameters": {
                "type": "object",
                "properties": {
                    "title": {"type": "string", "description": "The title of the movie"}
                },
                "required": ["title"],
            },
        },
    },
]

# Tool combinations for different test scenarios
TOOLS = BUILTIN_TOOLS + CUSTOM_TOOLS

# Shared test data for simple inference
SIMPLE_INFERENCE_MESSAGES = [
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
]

SIMPLE_INFERENCE_EXPECTED_RESPONSE = "The image depicts a close-up view of a pink flower with a bee on it. The flower is in the center of the image, with the bee positioned near the center of the flower. The flower has a light pink color, and the bee is black and yellow, with a fuzzy body. The flower has a"

# Video inference test data
VIDEO_INFERENCE_MESSAGES = [
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
]

VIDEO_INFERENCE_EXPECTED_RESPONSE = "The video showcases a scene from a dog show, specifically focusing on a dog in a metal cage. The cage is enclosed by a brown tarp, which is partially covered by a white cloth, and is situated on a concrete surface. The dog, a black and white dog, is standing on the ground, facing the"

# Multi-image interleaved test data
MULTI_IMAGE_MESSAGES = [
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
]

MULTI_IMAGE_EXPECTED_RESPONSE = "Unknown"

# Video caption test data
VIDEO_CAPTION_MESSAGES = [
    {
        "role": "user",
        "content": [
            {"type": "text", "text": "Caption the video."},
            {
                "type": "video",
                "path": "https://huggingface.co/datasets/hexuan21/VideoFeedback-videos-mp4/resolve/main/p/p000304.mp4",
            },
        ],
    },
]

VIDEO_CAPTION_EXPECTED_RESPONSE = (
    "A woman in a white shirt is speaking into a microphone at a podium."
)

# Tool calling test data
TOOL_CALLING_MESSAGES = create_base_messages(TOOLS) + [
    {
        "content": "What's the stock price for Nvidia?",
        "role": "user",
    },
]

TOOL_CALLING_EXPECTED_RESPONSE = """<observation>The user is asking me to find the stock price for Nvidia. I should search the stock price data on the Nvidia website.</observation><thought>I have the stock price data from the Nvidia website. I should communicate this to the user.</thought><tool_call>
{'name': 'web_search', 'arguments': {'query': 'What is the stock price for Nvidia?'}}
</tool_call>"""

# Format messages for tool calling tests
TOOL_CALLING_FORMATTED_MESSAGES = [
    {"role": message["role"], "content": [{"type": "text", "text": message["content"]}]}
    for message in TOOL_CALLING_MESSAGES
]


# Helper functions for DRY testing
def run_direct_inference(
    messages,
    expected_response,
    max_tokens=DEFAULT_MAX_TOKENS,
    tools=None,
    tool_choice=None,
):
    """Load model, run inference, then clean up to maintain test isolation."""
    processor = AutoProcessor.from_pretrained(MODEL_NAME)
    model = AutoModelForImageTextToText.from_pretrained(
        MODEL_NAME, torch_dtype=torch.bfloat16
    ).to("cuda")

    try:
        inputs = processor.apply_chat_template(
            messages,
            tools=tools,
            add_generation_prompt=True,
            tokenize=True,
            return_dict=True,
            return_tensors="pt",
        ).to(model.device, dtype=torch.bfloat16)

        # Add stopping criteria for tool calls if tools are provided
        stopping_criteria = None
        if tools:
            stopping_criteria = StoppingCriteriaList(
                [ToolCallStoppingCriteria(processor.tokenizer, "</tool_call>")]
            )

        generated_ids = model.generate(
            **inputs,
            do_sample=False,
            max_new_tokens=max_tokens,
            stopping_criteria=stopping_criteria,
            pad_token_id=processor.tokenizer.eos_token_id,
        )
        generated_texts = processor.batch_decode(
            generated_ids, skip_special_tokens=True
        )

        print(f"Generated text: {generated_texts[0]}")

        # Extract just the assistant's response (after "Assistant: ")
        full_text = generated_texts[0]
        assistant_response = full_text.split("Assistant: ")[-1].strip()

        # If the stopping criteria cut off the response, add the closing tag back
        if (
            tools
            and not assistant_response.endswith("</tool_call>")
            and "<tool_call>" in assistant_response
        ):
            assistant_response += "</tool_call>"

        print(f"Assistant response: {assistant_response}")

        # Test that we get the expected output
        assert assistant_response == expected_response

        return expected_response, messages
    finally:
        # Clean up to prevent memory issues
        del model, processor, inputs, generated_ids, generated_texts
        torch.cuda.empty_cache()


async def run_api_test(
    async_client,
    messages,
    expected_response,
    max_tokens=DEFAULT_MAX_TOKENS,
    tools=None,
    tool_choice=None,
):
    """Run API test without loading any models locally."""
    api_kwargs = {
        "model": f"openai/{MODEL_NAME}",
        "messages": messages,
        "max_tokens": max_tokens,
        "temperature": 0,
    }

    if tools is not None:
        api_kwargs["tools"] = tools
    if tool_choice is not None:
        api_kwargs["tool_choice"] = tool_choice

    response = await async_client.chat.completions.create(**api_kwargs)
    api_response = response.choices[0].message.content.strip()
    print(f"API response: {api_response}")
    print(f"Expected response: {expected_response}")
    assert api_response == expected_response

    # Additional assertions for tool calls
    if tools:
        # Assert that tool calls are properly formatted in the response
        message = response.choices[0].message
        assert hasattr(message, "tool_calls"), (
            "Response message should have tool_calls attribute"
        )
        assert message.tool_calls is not None, "Tool calls should not be None"
        assert len(message.tool_calls) == 1, "Should have exactly one tool call"

        tool_call = message.tool_calls[0]
        assert tool_call.type == "function", "Tool call type should be 'function'"
        assert tool_call.function.name == "web_search", (
            "Tool call should use web_search function"
        )

        # Parse and verify the exact arguments
        import json

        arguments = json.loads(tool_call.function.arguments)
        expected_arguments = {"query": "What is the stock price for Nvidia?"}
        assert arguments == expected_arguments, (
            f"Tool call arguments should be {expected_arguments}, got {arguments}"
        )

        print(
            f"Tool call verified: {tool_call.function.name}({tool_call.function.arguments})"
        )


# Simple inference tests
def test_simple_inference_direct():
    """Test SmolVLM2 model inference directly with transformers (no server)."""
    run_direct_inference(SIMPLE_INFERENCE_MESSAGES, SIMPLE_INFERENCE_EXPECTED_RESPONSE)


def test_simple_inference_api(async_client):
    """Test SmolVLM2 model inference via chat completions API."""
    import asyncio

    asyncio.run(
        run_api_test(
            async_client, SIMPLE_INFERENCE_MESSAGES, SIMPLE_INFERENCE_EXPECTED_RESPONSE
        )
    )


# Video inference tests
def test_video_inference_direct():
    """Test SmolVLM2 model video inference directly with transformers (no server)."""
    run_direct_inference(VIDEO_INFERENCE_MESSAGES, VIDEO_INFERENCE_EXPECTED_RESPONSE)


def test_video_inference_api(async_client):
    """Test SmolVLM2 model video inference via chat completions API."""
    import asyncio

    asyncio.run(
        run_api_test(
            async_client, VIDEO_INFERENCE_MESSAGES, VIDEO_INFERENCE_EXPECTED_RESPONSE
        )
    )


# Multi-image tests (skipped due to CUDA memory)
@pytest.mark.skip(reason="CUDA out of memory when processing two images simultaneously")
def test_multi_image_interleaved_inference_direct():
    """Test SmolVLM2 model multi-image interleaved inference directly with transformers (no server)."""
    run_direct_inference(
        MULTI_IMAGE_MESSAGES, MULTI_IMAGE_EXPECTED_RESPONSE, MULTI_IMAGE_MAX_TOKENS
    )


@pytest.mark.skip(reason="CUDA out of memory when processing two images simultaneously")
def test_multi_image_interleaved_inference_api(async_client):
    """Test SmolVLM2 model multi-image interleaved inference via chat completions API."""
    import asyncio

    asyncio.run(
        run_api_test(
            async_client,
            MULTI_IMAGE_MESSAGES,
            MULTI_IMAGE_EXPECTED_RESPONSE,
            MULTI_IMAGE_MAX_TOKENS,
        )
    )


# Video caption tests
def test_video_caption_direct():
    """Test SmolVLM2 model video captioning directly with transformers (no server)."""
    run_direct_inference(VIDEO_CAPTION_MESSAGES, VIDEO_CAPTION_EXPECTED_RESPONSE)


def test_video_caption_api(async_client):
    """Test SmolVLM2 model video captioning via chat completions API."""
    import asyncio

    asyncio.run(
        run_api_test(
            async_client, VIDEO_CAPTION_MESSAGES, VIDEO_CAPTION_EXPECTED_RESPONSE
        )
    )


# Tool calling tests
def test_stock_price_tool_direct():
    """Test SmolVLM2 model inference directly with transformers (no server) with tools."""
    run_direct_inference(
        TOOL_CALLING_FORMATTED_MESSAGES,
        TOOL_CALLING_EXPECTED_RESPONSE,
        TOOL_CALLING_MAX_TOKENS,
        tools=TOOLS,
    )


def test_stock_price_tool_api(async_client):
    """Test SmolVLM2 model inference via chat completions API with tools."""
    import asyncio

    asyncio.run(
        run_api_test(
            async_client,
            TOOL_CALLING_FORMATTED_MESSAGES,
            TOOL_CALLING_EXPECTED_RESPONSE,
            TOOL_CALLING_MAX_TOKENS,
            tools=TOOLS,
            tool_choice="required",
        )
    )
