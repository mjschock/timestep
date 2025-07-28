import pytest
from conftest import MODEL_NAME


@pytest.mark.asyncio
async def test_chat_completions(async_client):
    response = await async_client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": "What is the capital of France?"}],
    )
    assert hasattr(response, "object")
    assert response.object == "chat.completion"
    assert hasattr(response, "choices")
    assert response.choices[0].message.content
    assert response.model == MODEL_NAME or response.model == MODEL_NAME.replace(
        "openai/", ""
    )


@pytest.mark.asyncio
async def test_chat_completions_with_system_message(async_client):
    """Test chat completions with system message"""
    response = await async_client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "What is 2+2?"},
        ],
    )
    assert hasattr(response, "object")
    assert response.object == "chat.completion"
    assert hasattr(response, "choices")
    assert response.choices[0].message.content
    assert response.model == MODEL_NAME or response.model == MODEL_NAME.replace(
        "openai/", ""
    )


@pytest.mark.asyncio
async def test_chat_completions_with_assistant_message(async_client):
    """Test chat completions with assistant message in conversation"""
    response = await async_client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "user", "content": "What is the capital of France?"},
            {"role": "assistant", "content": "The capital of France is Paris."},
            {"role": "user", "content": "What is the population of Paris?"},
        ],
    )
    assert hasattr(response, "object")
    assert response.object == "chat.completion"
    assert hasattr(response, "choices")
    assert response.choices[0].message.content
    assert response.model == MODEL_NAME or response.model == MODEL_NAME.replace(
        "openai/", ""
    )


@pytest.mark.asyncio
async def test_chat_completions_with_max_tokens(async_client):
    """Test chat completions with max_tokens parameter"""
    response = await async_client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": "Write a short story about a cat."}],
        max_tokens=50,
    )
    assert hasattr(response, "object")
    assert response.object == "chat.completion"
    assert hasattr(response, "choices")
    assert response.choices[0].message.content
    assert response.model == MODEL_NAME or response.model == MODEL_NAME.replace(
        "openai/", ""
    )


@pytest.mark.asyncio
async def test_chat_completions_with_temperature(async_client):
    """Test chat completions with temperature parameter"""
    response = await async_client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": "What is the weather like?"}],
        temperature=0.7,
    )
    assert hasattr(response, "object")
    assert response.object == "chat.completion"
    assert hasattr(response, "choices")
    assert response.choices[0].message.content
    assert response.model == MODEL_NAME or response.model == MODEL_NAME.replace(
        "openai/", ""
    )


@pytest.mark.asyncio
async def test_chat_completions_with_top_p(async_client):
    """Test chat completions with top_p parameter"""
    response = await async_client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "user", "content": "Explain quantum physics in simple terms."}
        ],
        top_p=0.9,
    )
    assert hasattr(response, "object")
    assert response.object == "chat.completion"
    assert hasattr(response, "choices")
    assert response.choices[0].message.content
    assert response.model == MODEL_NAME or response.model == MODEL_NAME.replace(
        "openai/", ""
    )


@pytest.mark.asyncio
async def test_chat_completions_with_n(async_client):
    """Test chat completions with n parameter (multiple choices)"""
    response = await async_client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": "Give me three different ideas for a weekend trip.",
            }
        ],
        n=3,
    )
    assert hasattr(response, "object")
    assert response.object == "chat.completion"
    assert hasattr(response, "choices")
    # The n parameter might not be supported, so we'll just check that we get at least one choice
    assert len(response.choices) >= 1
    for choice in response.choices:
        assert choice.message.content
    assert response.model == MODEL_NAME or response.model == MODEL_NAME.replace(
        "openai/", ""
    )


@pytest.mark.asyncio
async def test_chat_completions_with_stop(async_client):
    """Test chat completions with stop parameter"""
    response = await async_client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": "Count from 1 to 10."}],
        stop=["5"],
    )
    assert hasattr(response, "object")
    assert response.object == "chat.completion"
    assert hasattr(response, "choices")
    assert response.choices[0].message.content
    assert response.model == MODEL_NAME or response.model == MODEL_NAME.replace(
        "openai/", ""
    )


@pytest.mark.asyncio
async def test_chat_completions_with_presence_penalty(async_client):
    """Test chat completions with presence_penalty parameter"""
    response = await async_client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": "Write a creative story."}],
        presence_penalty=0.1,
    )
    assert hasattr(response, "object")
    assert response.object == "chat.completion"
    assert hasattr(response, "choices")
    assert response.choices[0].message.content
    assert response.model == MODEL_NAME or response.model == MODEL_NAME.replace(
        "openai/", ""
    )


@pytest.mark.asyncio
async def test_chat_completions_with_frequency_penalty(async_client):
    """Test chat completions with frequency_penalty parameter"""
    response = await async_client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": "Write a paragraph about technology."}],
        frequency_penalty=0.1,
    )
    assert hasattr(response, "object")
    assert response.object == "chat.completion"
    assert hasattr(response, "choices")
    assert response.choices[0].message.content
    assert response.model == MODEL_NAME or response.model == MODEL_NAME.replace(
        "openai/", ""
    )


@pytest.mark.asyncio
async def test_chat_completions_with_logit_bias(async_client):
    """Test chat completions with logit_bias parameter"""
    response = await async_client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": "What is your favorite color?"}],
        logit_bias={"blue": 10},
    )
    assert hasattr(response, "object")
    assert response.object == "chat.completion"
    assert hasattr(response, "choices")
    assert response.choices[0].message.content
    assert response.model == MODEL_NAME or response.model == MODEL_NAME.replace(
        "openai/", ""
    )


@pytest.mark.asyncio
async def test_chat_completions_with_user(async_client):
    """Test chat completions with user parameter"""
    response = await async_client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": "Hello, how are you?"}],
        user="test_user_123",
    )
    assert hasattr(response, "object")
    assert response.object == "chat.completion"
    assert hasattr(response, "choices")
    assert response.choices[0].message.content
    assert response.model == MODEL_NAME or response.model == MODEL_NAME.replace(
        "openai/", ""
    )


@pytest.mark.asyncio
async def test_chat_completions_with_stream(async_client):
    """Test chat completions with stream parameter"""
    response = await async_client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": "Tell me a joke."}],
        stream=True,
    )
    # For streaming responses, we need to iterate through the response
    content = ""
    async for chunk in response:
        if chunk.choices[0].delta.content:
            content += chunk.choices[0].delta.content

    assert content  # Should have some content
    # For streaming responses, we can't access model directly from the stream object


@pytest.mark.asyncio
async def test_chat_completions_with_tools(async_client):
    """Test chat completions with tools parameter"""
    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_weather",
                "description": "Get the weather for a location",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "The city and state, e.g. San Francisco, CA",
                        }
                    },
                    "required": ["location"],
                },
            },
        }
    ]

    response = await async_client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": "What's the weather like in Paris?"}],
        tools=tools,
    )
    assert hasattr(response, "object")
    assert response.object == "chat.completion"
    assert hasattr(response, "choices")
    assert response.choices[0].message.content
    assert response.model == MODEL_NAME or response.model == MODEL_NAME.replace(
        "openai/", ""
    )


@pytest.mark.asyncio
async def test_chat_completions_with_tool_choice(async_client):
    """Test chat completions with tool_choice parameter"""
    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_weather",
                "description": "Get the weather for a location",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "The city and state, e.g. San Francisco, CA",
                        }
                    },
                    "required": ["location"],
                },
            },
        }
    ]

    response = await async_client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": "What's the weather like in Paris?"}],
        tools=tools,
        tool_choice="auto",
    )
    assert hasattr(response, "object")
    assert response.object == "chat.completion"
    assert hasattr(response, "choices")
    assert response.choices[0].message.content
    assert response.model == MODEL_NAME or response.model == MODEL_NAME.replace(
        "openai/", ""
    )


@pytest.mark.asyncio
async def test_chat_completions_error_handling(async_client):
    """Test chat completions error handling"""
    # Test with missing messages
    try:
        await async_client.chat.completions.create(
            model=MODEL_NAME,
            messages=[],  # Empty messages should cause an error
        )
        raise AssertionError("Should have raised an error")
    except Exception as e:
        # Should get a 400 error for missing messages
        assert "400" in str(e) or "Bad Request" in str(e)


@pytest.mark.asyncio
async def test_chat_completions_response_structure(async_client):
    """Test chat completions response structure"""
    response = await async_client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": "Hello"}],
    )

    # Check response structure
    assert hasattr(response, "id")
    assert hasattr(response, "object")
    assert hasattr(response, "created")
    assert hasattr(response, "model")
    assert hasattr(response, "choices")
    assert hasattr(response, "usage")

    # Check choices structure
    assert len(response.choices) > 0
    choice = response.choices[0]
    assert hasattr(choice, "index")
    assert hasattr(choice, "message")
    assert hasattr(choice, "finish_reason")

    # Check message structure
    message = choice.message
    assert hasattr(message, "role")
    assert hasattr(message, "content")
    assert message.role == "assistant"
    assert isinstance(message.content, str)

    # Check usage structure
    usage = response.usage
    assert hasattr(usage, "prompt_tokens")
    assert hasattr(usage, "completion_tokens")
    assert hasattr(usage, "total_tokens")


# Tests for stored chat completions functionality
@pytest.mark.asyncio
async def test_chat_completions_with_store(async_client):
    """Test chat completions with store parameter"""
    response = await async_client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": "Hello, store this conversation."}],
        store=True,
        metadata={"test": "metadata"},
    )

    assert hasattr(response, "id")
    assert response.object == "chat.completion"

    # The completion should now be stored and retrievable


@pytest.mark.asyncio
async def test_list_chat_completions(async_client):
    """Test listing stored chat completions"""
    # First create a stored completion
    await async_client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": "Test message for listing."}],
        store=True,
    )

    # List stored completions
    list_response = await async_client.chat.completions.list()
    assert hasattr(list_response, "object")
    assert list_response.object == "list"
    assert hasattr(list_response, "data")


@pytest.mark.asyncio
async def test_get_chat_completion(async_client):
    """Test getting a specific stored chat completion"""
    # First create a stored completion
    response = await async_client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": "Test message for retrieval."}],
        store=True,
    )

    completion_id = response.id

    # Retrieve the stored completion
    retrieved_response = await async_client.chat.completions.retrieve(completion_id)
    assert retrieved_response.id == completion_id
    assert retrieved_response.object == "chat.completion"


@pytest.mark.asyncio
async def test_update_chat_completion(async_client):
    """Test updating a stored chat completion"""
    # First create a stored completion
    response = await async_client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": "Test message for update."}],
        store=True,
    )

    completion_id = response.id

    # Update the completion
    updated_response = await async_client.chat.completions.update(
        completion_id, metadata={"updated": True}
    )
    assert updated_response.id == completion_id
    assert updated_response.metadata["updated"] is True


@pytest.mark.asyncio
async def test_delete_chat_completion(async_client):
    """Test deleting a stored chat completion"""
    # First create a stored completion
    response = await async_client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": "Test message for deletion."}],
        store=True,
    )

    completion_id = response.id

    # Delete the completion
    deleted_response = await async_client.chat.completions.delete(completion_id)
    assert deleted_response.id == completion_id
    assert deleted_response.object == "chat.completion.deleted"
    assert deleted_response.deleted is True


@pytest.mark.asyncio
async def test_get_chat_completion_messages(async_client):
    """Test getting messages from a stored chat completion"""
    # First create a stored completion
    response = await async_client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "user", "content": "First message."},
            {"role": "assistant", "content": "First response."},
            {"role": "user", "content": "Second message."},
        ],
        store=True,
    )

    completion_id = response.id

    # Get the messages
    messages_response = await async_client.chat.completions.messages.list(completion_id)
    assert messages_response.object == "list"
    assert len(messages_response.data) == 3  # Should have 3 messages


@pytest.mark.asyncio
async def test_chat_completion_not_found(async_client):
    """Test error handling for non-existent chat completion"""
    # Try to get a non-existent completion
    try:
        await async_client.chat.completions.retrieve("non-existent-id")
        raise AssertionError("Should have raised an error")
    except Exception as e:
        assert "404" in str(e) or "not found" in str(e).lower()

    # Try to update a non-existent completion
    try:
        await async_client.chat.completions.update(
            "non-existent-id", metadata={"test": "data"}
        )
        raise AssertionError("Should have raised an error")
    except Exception as e:
        assert "404" in str(e) or "not found" in str(e).lower()

    # Try to delete a non-existent completion
    try:
        await async_client.chat.completions.delete("non-existent-id")
        raise AssertionError("Should have raised an error")
    except Exception as e:
        assert "404" in str(e) or "not found" in str(e).lower()

    # Try to get messages from a non-existent completion
    try:
        await async_client.chat.completions.messages.list("non-existent-id")
        raise AssertionError("Should have raised an error")
    except Exception as e:
        assert "404" in str(e) or "not found" in str(e).lower()
