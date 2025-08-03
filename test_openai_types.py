#!/usr/bin/env python3
"""
Test script to understand how to work with validated OpenAI types
"""

import sys
sys.path.append('src')

from pydantic import TypeAdapter, BaseModel
from typing import List, Optional, Any
from openai.types.chat.completion_create_params import (
    CompletionCreateParamsNonStreaming,
    CompletionCreateParamsStreaming,
)
from datasets import Dataset, DatasetDict

# Create a simple Pydantic model for ChatCompletion requests
class ChatCompletionRequest(BaseModel):
    messages: List[dict]
    model: str
    temperature: Optional[float] = None
    stream: Optional[bool] = False
    tools: Optional[List[dict]] = None
    tool_choice: Optional[Any] = None
    max_tokens: Optional[int] = None
    
    class Config:
        extra = "allow"  # Allow additional fields

# Sample request data like what agents SDK sends
sample_request = {
    "messages": [
        {
            "content": "You are a helpful assistant.",
            "role": "system"
        },
        {
            "role": "user",
            "content": "What's the weather in Oakland?"
        }
    ],
    "model": "openai/HuggingFaceTB/SmolVLM2-256M-Video-Instruct",
    "stream": False,
    "temperature": 0.0,
    "tool_choice": "required",
    "tools": [
        {
            "type": "function",
            "function": {
                "name": "get_weather",
                "description": "",
                "parameters": {
                    "properties": {
                        "city": {
                            "title": "City",
                            "type": "string"
                        }
                    },
                    "required": ["city"],
                    "title": "get_weather_args",
                    "type": "object",
                    "additionalProperties": False
                }
            }
        }
    ]
}

print("🔍 Testing OpenAI type validation and dataset conversion...")

# 1. Validate with TypeAdapter (like our API does)
print("\n1. Validating request with TypeAdapter...")
adapter = TypeAdapter(CompletionCreateParamsNonStreaming)
validated_request = adapter.validate_python(sample_request)

print(f"Validated request type: {type(validated_request)}")
print(f"Validated request keys: {list(validated_request.keys())}")
print(f"Messages type: {type(validated_request['messages'])}")
print(f"Tools type: {type(validated_request['tools'])}")
# Convert ValidatorIterator to list first
messages_list = list(validated_request['messages'])
tools_list = list(validated_request['tools'])

print(f"Messages list length: {len(messages_list)}")
print(f"Tools list length: {len(tools_list)}")
if messages_list:
    print(f"First message type: {type(messages_list[0])}")

# 2. Try to create dataset directly
print("\n2. Testing Dataset creation...")
try:
    dataset = DatasetDict({"test": Dataset.from_list([{
        "messages": messages_list,
        "tools": tools_list,
        "parallel_tool_calls": None,
    }])})
    print("✅ Dataset creation successful!")
    print(f"Dataset keys: {list(dataset.keys())}")
    print(f"Test split sample: {dataset['test'][0]}")
except Exception as e:
    print(f"❌ Dataset creation failed: {e}")
    
    # 3. Try converting to dicts first
    print("\n3. Converting to plain dicts...")
    try:
        plain_messages = [dict(msg) for msg in messages_list]
        plain_tools = [dict(tool) for tool in tools_list]
        
        dataset = DatasetDict({"test": Dataset.from_list([{
            "messages": plain_messages,
            "tools": plain_tools,
            "parallel_tool_calls": None,
        }])})
        print("✅ Dataset creation with plain dicts successful!")
        print(f"Dataset keys: {list(dataset.keys())}")
        print(f"Test split sample: {dataset['test'][0]}")
    except Exception as e2:
        print(f"❌ Dataset creation with plain dicts also failed: {e2}")

# 4. Test instantiating TypedDict from validated data
print("\n4. Testing TypedDict instantiation...")
try:
    # Create TypedDict instance from validated data
    request_instance = CompletionCreateParamsNonStreaming({
        'messages': messages_list,
        'model': validated_request['model'],
        'stream': validated_request.get('stream', False),
        'temperature': validated_request.get('temperature'),
        'tools': tools_list,
        'tool_choice': validated_request.get('tool_choice'),
    })
    print(f"✅ TypedDict instance created successfully!")
    print(f"Instance type: {type(request_instance)}")
    print(f"Instance keys: {list(request_instance.keys())}")
    print(f"Messages type in instance: {type(request_instance['messages'])}")
    print(f"Tools type in instance: {type(request_instance['tools'])}")
    
    # Test dataset creation with TypedDict instance
    dataset = DatasetDict({"test": Dataset.from_list([{
        "messages": request_instance['messages'],
        "tools": request_instance['tools'] or [],
        "parallel_tool_calls": None,
    }])})
    print("✅ Dataset creation with TypedDict instance successful!")
    
except Exception as e:
    print(f"❌ TypedDict instantiation failed: {e}")

# 5. Deep examination of recursive validation
print("\n5. Examining recursive validation...")

print("Messages validation:")
for i, msg in enumerate(messages_list):
    print(f"  Message {i}: {type(msg)} - {msg}")
    # Check if this is a validated Pydantic object or plain dict
    if hasattr(msg, 'model_validate'):
        print(f"    -> Is Pydantic model: YES")
    else:
        print(f"    -> Is Pydantic model: NO (plain dict)")

print("\nTools validation:")
for i, tool in enumerate(tools_list):
    print(f"  Tool {i}: {type(tool)} - {tool}")
    if hasattr(tool, 'model_validate'):
        print(f"    -> Is Pydantic model: YES")
    else:
        print(f"    -> Is Pydantic model: NO (plain dict)")
    
    # Check nested function object
    if 'function' in tool:
        func = tool['function']
        print(f"    Function: {type(func)} - {func}")
        if hasattr(func, 'model_validate'):
            print(f"      -> Function is Pydantic model: YES")
        else:
            print(f"      -> Function is Pydantic model: NO (plain dict)")

# 6. Test with clearly invalid data
print("\n6. Testing validation with clearly invalid data...")

# Test 1: Missing required field
try:
    invalid_request1 = {"model": "test"}  # Missing messages
    adapter = TypeAdapter(CompletionCreateParamsNonStreaming)
    adapter.validate_python(invalid_request1)
    print("❌ Missing messages passed validation")
except Exception as e:
    print(f"✅ Missing messages caught: {str(e)[:100]}...")

# Test 2: Wrong type for messages
try:
    invalid_request2 = {"messages": "not a list", "model": "test"}
    adapter.validate_python(invalid_request2)
    print("❌ Wrong messages type passed validation")
except Exception as e:
    print(f"✅ Wrong messages type caught: {str(e)[:100]}...")

# Test 3: Invalid role (this might be more permissive)
try:
    invalid_request3 = {
        "messages": [{"content": "test", "role": "invalid_role"}],
        "model": "test"
    }
    result = adapter.validate_python(invalid_request3)
    print(f"⚠️  Invalid role allowed: {result['messages'][0]['role']}")
except Exception as e:
    print(f"✅ Invalid role caught: {str(e)[:100]}...")

print(f"\n7. Summary: TypeAdapter validation provides type safety but may be permissive with enum values.")