import pytest
from conftest import MODEL_NAME


@pytest.mark.asyncio
async def test_responses_api(async_client):
    # The OpenAI SDK may not accept 'messages' for responses, so use a simple input
    response = await async_client.responses.create(
        model=MODEL_NAME, input="What is the capital of France?"
    )
    assert hasattr(response, "object")
    assert response.object == "response"
    assert hasattr(response, "status")
    assert response.status == "completed"
    assert hasattr(response, "output")
    assert isinstance(response.output, list)
    assert response.output[0].type == "message"
    assert hasattr(response.output[0], "content")
    assert isinstance(response.output[0].content, list)
    assert response.output[0].content[0].type == "output_text"
    assert hasattr(response.output[0].content[0], "text")
    assert hasattr(response, "usage")
    assert hasattr(response.usage, "input_tokens")
    assert hasattr(response.usage, "output_tokens")
    assert hasattr(response.usage, "total_tokens")
    assert hasattr(response.usage, "input_tokens_details")
    assert hasattr(response.usage, "output_tokens_details")
