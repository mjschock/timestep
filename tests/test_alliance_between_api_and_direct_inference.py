import pytest
import torch

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

# Note: TOOLS will be created in test functions using fixtures

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

SIMPLE_INFERENCE_EXPECTED_RESPONSE = "The image showcases a close-up view of a pink flower with a bee on it. The flower is in the center of the image, with its petals slightly curled and slightly open. The bee, which is the central focus of the image, is positioned near the center of the flower, with its body facing towards"

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

VIDEO_INFERENCE_EXPECTED_RESPONSE = "The video showcases a scene from a dog show, specifically focusing on a dog in a metal cage. The cage is enclosed by a brown tarp, which is partially covered by a white cloth, and is situated outdoors. The dog is standing on a concrete surface, with a grassy area in the background. The dog appears"

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

# Tool calling test data (will be created in test functions using fixtures)

TOOL_CALLING_EXPECTED_RESPONSE = """<observation>The user is asking me to find the stock price for Nvidia. I should search the stock price data on the Nvidia website.</observation><thought>I have the stock price data from the Nvidia website. I should communicate this to the user.</thought><tool_call>
{'name': 'web_search', 'arguments': {'query': 'What is the stock price for Nvidia?'}}
</tool_call>"""

# Tool calling messages will be created in test functions


# Helper functions for DRY testing


def _prepare_generation_kwargs(temperature, max_tokens, top_p, n, processor):
    """Prepare generation kwargs based on parameters."""
    if temperature == 0.0:
        generation_kwargs = {
            "do_sample": False,
            "max_new_tokens": max_tokens,
        }
    else:
        generation_kwargs = {
            "max_new_tokens": max_tokens,
            "do_sample": True,
            "temperature": temperature,
            "top_p": top_p,
            "num_return_sequences": n,
            "pad_token_id": getattr(processor, "pad_token_id", None),
            "eos_token_id": getattr(processor, "eos_token_id", None),
        }

    # Remove None values
    return {k: v for k, v in generation_kwargs.items() if v is not None}


def _process_response_text(response_text, inputs, processor, stop_sequences):
    """Process response text by removing input and applying stop sequences."""
    # Remove the input text from the response like the server
    input_text = processor.decode(inputs["input_ids"][0], skip_special_tokens=True)
    if response_text.startswith(input_text):
        response_text = response_text[len(input_text) :].strip()

    # Apply stop sequences like the server
    if stop_sequences:
        for stop_seq in stop_sequences:
            if isinstance(stop_seq, str) and stop_seq in response_text:
                # Find the position and truncate
                stop_pos = response_text.find(stop_seq)
                if stop_pos != -1:
                    response_text = response_text[: stop_pos + len(stop_seq)]
                    break

    return response_text


def run_direct_inference(
    messages,
    expected_response,
    max_tokens=DEFAULT_MAX_TOKENS,
    tools=None,
    tool_choice=None,
    temperature=0.0,
    top_p=1.0,
    n=1,
):
    """Use the same singleton model as the API for exact response matching."""
    from backend.services.chat_service import normalize_messages
    from backend.services.models_service import get_models_service

    # Use the same singleton models service as the API
    models_service = get_models_service()

    print(f"Getting model {MODEL_NAME} from singleton models service")
    model, processor = models_service.get_model_instance(MODEL_NAME, use_cache=True)

    # Log the actual dtype of the model parameters to verify
    if hasattr(model, "parameters"):
        param_dtypes = {param.dtype for param in model.parameters()}
        print(f"Model parameter dtypes: {param_dtypes}")

    print(f"Model device: {model.device}")
    print(f"Model dtype: {next(model.parameters()).dtype}")

    try:
        # Normalize messages like the server does
        normalized_messages = normalize_messages(messages)
        print(f"Normalized messages: {normalized_messages}")

        inputs = processor.apply_chat_template(
            normalized_messages,
            tools=tools,
            add_generation_prompt=True,
            tokenize=True,
            return_dict=True,
            return_tensors="pt",
        )

        # Use the model's actual dtype instead of hardcoding
        model_dtype = next(model.parameters()).dtype
        inputs = inputs.to(model.device, dtype=model_dtype)

        generation_kwargs = _prepare_generation_kwargs(
            temperature, max_tokens, top_p, n, processor
        )

        # Add stop sequences like the server
        stop_sequences = []
        if "</tool_call>" not in stop_sequences:
            stop_sequences.append("</tool_call>")

        if stop_sequences:
            generation_kwargs["stopping_criteria"] = (
                None  # We'll handle stop sequences manually
            )

        print(f"Generation kwargs: {generation_kwargs}")
        print(f"Stop sequences: {stop_sequences}")

        # Generate response
        with torch.no_grad():
            generated_ids = model.generate(**inputs, **generation_kwargs)

        # Decode responses like the server
        generated_texts = processor.batch_decode(
            generated_ids,
            skip_special_tokens=True,
        )

        print(f"Generated text: {generated_texts[0]}")

        # Process response like the chat service does
        response_text = _process_response_text(
            generated_texts[0], inputs, processor, stop_sequences
        )

        print(f"Processed response: {response_text}")
        print(f"Expected response: {expected_response}")

        # Now that we're using the same singleton model, we should get exact matches
        assert response_text == expected_response, (
            f"Direct inference response doesn't match expected.\nActual: '{response_text}'\nExpected: '{expected_response}'"
        )

        return expected_response, messages
    finally:
        # Clean up generated tensors (model and processor are singletons, don't delete them)
        if "inputs" in locals():
            del inputs
        if "generated_ids" in locals():
            del generated_ids
        if "generated_texts" in locals():
            del generated_texts
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

    # Since both API and direct calls use the same singleton model, responses should match exactly
    assert api_response == expected_response, (
        f"API response doesn't match expected.\nActual: {api_response}\nExpected: {expected_response}"
    )

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
def test_stock_price_tool_direct(builtin_tools, builtin_tool_examples):
    """Test SmolVLM2 model inference directly with transformers (no server) with tools."""
    tools = builtin_tools + CUSTOM_TOOLS
    tool_calling_messages = create_base_messages(tools, builtin_tool_examples) + [
        {
            "content": "What's the stock price for Nvidia?",
            "role": "user",
        },
    ]
    tool_calling_formatted_messages = [
        {
            "role": message["role"],
            "content": [{"type": "text", "text": message["content"]}],
        }
        for message in tool_calling_messages
    ]

    run_direct_inference(
        tool_calling_formatted_messages,
        TOOL_CALLING_EXPECTED_RESPONSE,
        TOOL_CALLING_MAX_TOKENS,
        tools=tools,
    )


def test_stock_price_tool_api(async_client, builtin_tools, builtin_tool_examples):
    """Test SmolVLM2 model inference via chat completions API with tools."""
    import asyncio

    tools = builtin_tools + CUSTOM_TOOLS
    tool_calling_messages = create_base_messages(tools, builtin_tool_examples) + [
        {
            "content": "What's the stock price for Nvidia?",
            "role": "user",
        },
    ]
    tool_calling_formatted_messages = [
        {
            "role": message["role"],
            "content": [{"type": "text", "text": message["content"]}],
        }
        for message in tool_calling_messages
    ]

    asyncio.run(
        run_api_test(
            async_client,
            tool_calling_formatted_messages,
            TOOL_CALLING_EXPECTED_RESPONSE,
            TOOL_CALLING_MAX_TOKENS,
            tools=tools,
            tool_choice="required",
        )
    )
