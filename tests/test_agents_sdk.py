import pytest
from agents import (
    Agent,
    ModelSettings,
    OpenAIChatCompletionsModel,
    OpenAIResponsesModel,
    Runner,
    function_tool,
)
from conftest import MODEL_NAME

# Shared test constants
DEFAULT_INSTRUCTIONS = "You are a helpful assistant."
DEFAULT_PROMPT = "What's the weather in Oakland?"


@function_tool
def get_weather(city: str):
    return f"The weather in {city} is sunny."


# Helper functions for creating agents
def create_agent(
    openai_client=None,
    api_type="responses",
    instructions=DEFAULT_INSTRUCTIONS,
    tool_choice="required",
):
    """Create an agent with specified API type and configuration

    Args:
        openai_client: OpenAI client (required for both API types)
        api_type: "chat_completions" or "responses" (default: "responses")
        instructions: Agent instructions
        tool_choice: Tool choice setting
    """
    if openai_client is None:
        raise ValueError("openai_client is required for both API types")

    if api_type == "chat_completions":
        model = OpenAIChatCompletionsModel(
            model=MODEL_NAME, openai_client=openai_client
        )
    elif api_type == "responses":
        model = OpenAIResponsesModel(model=MODEL_NAME, openai_client=openai_client)
    else:
        raise ValueError(
            f"Unknown api_type: {api_type}. Must be 'chat_completions' or 'responses'"
        )

    return Agent(
        name="Assistant",
        instructions=instructions,
        model=model,
        model_settings=ModelSettings(
            tool_choice=tool_choice,
            temperature=0,
            seed=42,
        ),
        tools=[get_weather],
    )


# Helper functions for running tests
async def run_async_test(agent, prompt=DEFAULT_PROMPT):
    """Run async non-streaming test and return result"""
    result = await Runner.run(agent, prompt)
    assert hasattr(result, "final_output")
    assert isinstance(result.final_output, str)
    assert len(result.final_output) > 0
    return result


async def run_async_streaming_test(agent, prompt=DEFAULT_PROMPT):
    """Run async streaming test and return result"""
    streamed = Runner.run_streamed(agent, prompt)
    events = []
    async for event in streamed.stream_events():
        events.append(event)
        print(f"DEBUG: Streaming event: {type(event)} - {event}")
    assert hasattr(streamed, "final_output")
    assert isinstance(streamed.final_output, str)
    assert len(streamed.final_output) > 0
    return streamed


def run_sync_test(agent, prompt=DEFAULT_PROMPT):
    """Run sync non-streaming test and return result"""
    result = Runner.run_sync(agent, prompt)
    assert hasattr(result, "final_output")
    assert isinstance(result.final_output, str)
    assert len(result.final_output) > 0
    return result


def check_tool_call(result, expected_tool_name="get_weather"):
    """Check if a specific tool call is present in the result"""
    _print_debug_info(result)

    tool_call_found = _check_agents_sdk_format(result, expected_tool_name)
    if not tool_call_found:
        tool_call_found = _check_fallback_formats(result, expected_tool_name)

    assert tool_call_found, f"No {expected_tool_name} tool call found in result"


def _print_debug_info(result):
    """Print debug information about the result structure."""
    print(f"DEBUG: Result type: {type(result)}")
    print(f"DEBUG: Result attributes: {dir(result)}")
    if hasattr(result, "new_items"):
        print(f"DEBUG: new_items: {result.new_items}")
        if result.new_items:
            for i, item in enumerate(result.new_items):
                print(f"DEBUG: new_items[{i}] type: {type(item)}")
                print(f"DEBUG: new_items[{i}] attributes: {dir(item)}")
                if hasattr(item, "tool_calls"):
                    print(f"DEBUG: new_items[{i}].tool_calls: {item.tool_calls}")


def _check_agents_sdk_format(result, expected_tool_name):
    """Check for tool calls in the agents SDK result format."""
    if not (hasattr(result, "new_items") and result.new_items):
        return False

    for item in result.new_items:
        if _check_tool_call_item(item, expected_tool_name):
            return True
    return False


def _check_tool_call_item(item, expected_tool_name):
    """Check a single item for tool calls."""
    # Check if this is a ToolCallItem
    if hasattr(item, "raw_item") and hasattr(item.raw_item, "name"):
        if item.raw_item.name == expected_tool_name:
            return True

    # Check for tool_calls attribute on the item itself
    if hasattr(item, "tool_calls") and item.tool_calls:
        for tc in item.tool_calls:
            if getattr(tc.function, "name", None) == expected_tool_name:
                return True

    # Check for tool_calls in raw_item (for MessageOutputItem)
    if (
        hasattr(item, "raw_item")
        and hasattr(item.raw_item, "tool_calls")
        and item.raw_item.tool_calls
    ):
        for tc in item.raw_item.tool_calls:
            if (
                isinstance(tc, dict)
                and tc.get("function", {}).get("name") == expected_tool_name
            ):
                return True

    return False


def _check_fallback_formats(result, expected_tool_name):
    """Check fallback formats for tool calls."""
    # Check direct tool_calls attribute
    if hasattr(result, "tool_calls") and result.tool_calls:
        for tc in result.tool_calls:
            if getattr(tc.function, "name", None) == expected_tool_name:
                return True

    # Check choices format
    if hasattr(result, "choices"):
        for choice in getattr(result, "choices", []):
            message = choice.get("message", {})
            for tc in message.get("tool_calls", []) or []:
                if tc.get("function", {}).get("name") == expected_tool_name:
                    return True

    return False


@pytest.mark.asyncio
async def test_agent_sdk_async_chat_completions_non_streaming(async_client):
    """Test agent SDK with OpenAIChatCompletionsModel (uses chat completions API) - non-streaming"""
    agent = create_agent(openai_client=async_client, api_type="chat_completions")
    result = await run_async_test(agent)
    check_tool_call(result)


@pytest.mark.asyncio
async def test_agent_sdk_async_responses_non_streaming(async_client):
    """Test agent SDK with OpenAIResponsesModel (uses responses API) - non-streaming"""
    agent = create_agent(openai_client=async_client, api_type="responses")
    result = await run_async_test(agent)
    check_tool_call(result)


@pytest.mark.asyncio
async def test_agent_sdk_async_chat_completions_streaming(async_client):
    """Test agent SDK with OpenAIChatCompletionsModel (uses chat completions API) - streaming"""
    agent = create_agent(openai_client=async_client, api_type="chat_completions")
    result = await run_async_streaming_test(agent)
    check_tool_call(result)


@pytest.mark.asyncio
async def test_agent_sdk_async_responses_streaming(async_client):
    """Test agent SDK with OpenAIResponsesModel (uses responses API) - streaming"""
    agent = create_agent(openai_client=async_client, api_type="responses")
    result = await run_async_streaming_test(agent)
    check_tool_call(result)


def test_agent_sdk_sync_chat_completions_non_streaming(async_client):
    """Test agent SDK with OpenAIChatCompletionsModel (uses chat completions API) - sync non-streaming"""
    # Use async_client for sync test since agents SDK requires async client
    agent = create_agent(openai_client=async_client, api_type="chat_completions")
    result = run_sync_test(agent)
    check_tool_call(result)


def test_agent_sdk_sync_responses_non_streaming(async_client):
    """Test agent SDK with OpenAIResponsesModel (uses responses API) - sync non-streaming"""
    # Use async_client for sync test since agents SDK requires async client
    agent = create_agent(openai_client=async_client, api_type="responses")
    result = run_sync_test(agent)
    check_tool_call(result)
