# ruff: noqa: S101

import copy

# Constants
DEFAULT_N_SHOT = 3
DEFAULT_SYSTEM_MESSAGE = "You are a helpful assistant."

# N-shot examples for tool usage demonstrations
# Each example is a list of OpenAI message format conversations
N_SHOT_EXAMPLES = [
    [
        {"role": "user", "content": "How many r's are in the word 'strawberry'?"},
        {
            "role": "assistant",
            "tool_calls": [
                {
                    "name": "code_interpreter",
                    "arguments": {"code": "'strawberry'.count('r')"},
                }
            ],
        },
        {
            "role": "tool",
            "tool_call_id": "call_1",
            "name": "code_interpreter",
            "content": "3",
        },
        {"role": "assistant", "content": "There are 3 r's in the word 'strawberry'."},
    ],
    [
        {"role": "user", "content": "What are the Three Laws of Robotics?"},
        {
            "role": "assistant",
            "tool_calls": [
                {"name": "web_search", "arguments": {"query": "Three Laws of Robotics"}}
            ],
        },
        {
            "role": "tool",
            "tool_call_id": "call_2",
            "name": "web_search",
            "content": "The Three Laws of Robotics are:\n1. A robot may not injure a human being or, through inaction, allow a human being to come to harm.\n2. A robot must obey the orders given it by human beings except where such orders would conflict with the First Law.\n3. A robot must protect its own existence as long as such protection does not conflict with the First or Second Laws.",
        },
        {
            "role": "assistant",
            "content": "The Three Laws of Robotics are:\n1. A robot may not injure a human being or, through inaction, allow a human being to come to harm.\n2. A robot must obey the orders given it by human beings except where such orders would conflict with the First Law.\n3. A robot must protect its own existence as long as such protection does not conflict with the First or Second Laws.",
        },
    ],
    [
        {
            "role": "user",
            "content": "What is the answer to the Ultimate Question of Life, the Universe, and Everything?",
        },
        {
            "role": "assistant",
            "tool_calls": [
                {
                    "name": "web_search",
                    "arguments": {
                        "query": "What is the answer to the Ultimate Question of Life, the Universe, and Everything?"
                    },
                }
            ],
        },
        {
            "role": "tool",
            "tool_call_id": "call_3",
            "name": "web_search",
            "content": "The answer to the Ultimate Question of Life, the Universe, and Everything is 42.",
        },
        {"role": "assistant", "content": "42"},
    ],
]

DEFAULT_TOOLS = [
    {
        "type": "function",
        "name": "code_interpreter",
        "description": "Execute Python code and return the result.",
        "parameters": {
            "type": "object",
            "properties": {
                "code": {
                    "type": "string",
                    "description": "Python code to execute",
                }
            },
            "required": ["code"],
            "additionalProperties": False,
        },
        "strict": False,
    },
    {
        "type": "function",
        "name": "web_search",
        "description": "Search the web for information.",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "Search query",
                }
            },
            "required": ["query"],
            "additionalProperties": False,
        },
        "strict": False,
    },
]

BASE_WEATHER_CONVERSATION = {
    "expected": {
        "messages": [
            {
                "role": "system",
                "content": [
                    {
                        "type": "text",
                        "text": """You are a helpful assistant.

The following tools are available:

Tool name: code_interpreter
Description: Execute Python code and return the result.
Parameters:
- code (string): Python code to execute

Tool name: get_weather
Description: Get current temperature for a given location.
Parameters:
- location (string): City and country e.g. Bogotá, Colombia

Tool name: web_search
Description: Search the web for information.
Parameters:
- query (string): Search query

To use a tool, respond with:
<tool_call>
{ ... }
</tool_call>

User: How many r's are in the word 'strawberry'?<end_of_utterance>
Assistant: <tool_call>
{"arguments": {"code": "'strawberry'.count('r')"}, "name": "code_interpreter"}
</tool_call><end_of_utterance>
Tool: 3<end_of_utterance>
Assistant: There are 3 r's in the word 'strawberry'.<end_of_utterance>

User: What are the Three Laws of Robotics?<end_of_utterance>
Assistant: <tool_call>
{"arguments": {"query": "Three Laws of Robotics"}, "name": "web_search"}
</tool_call><end_of_utterance>
Tool: The Three Laws of Robotics are:
1. A robot may not injure a human being or, through inaction, allow a human being to come to harm.
2. A robot must obey the orders given it by human beings except where such orders would conflict with the First Law.
3. A robot must protect its own existence as long as such protection does not conflict with the First or Second Laws.<end_of_utterance>
Assistant: The Three Laws of Robotics are:
1. A robot may not injure a human being or, through inaction, allow a human being to come to harm.
2. A robot must obey the orders given it by human beings except where such orders would conflict with the First Law.
3. A robot must protect its own existence as long as such protection does not conflict with the First or Second Laws.<end_of_utterance>

User: What is the answer to the Ultimate Question of Life, the Universe, and Everything?<end_of_utterance>
Assistant: <tool_call>
{"arguments": {"query": "What is the answer to the Ultimate Question of Life, the Universe, and Everything?"}, "name": "web_search"}
</tool_call><end_of_utterance>
Tool: The answer to the Ultimate Question of Life, the Universe, and Everything is 42.<end_of_utterance>
Assistant: 42""",
                    }
                ],
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "What is the weather like in Oakland today?",
                    }
                ],
            },
        ],
        "prompt": """<|im_start|>System: You are a helpful assistant.

The following tools are available:

Tool name: code_interpreter
Description: Execute Python code and return the result.
Parameters:
- code (string): Python code to execute

Tool name: get_weather
Description: Get current temperature for a given location.
Parameters:
- location (string): City and country e.g. Bogotá, Colombia

Tool name: web_search
Description: Search the web for information.
Parameters:
- query (string): Search query

To use a tool, respond with:
<tool_call>
{ ... }
</tool_call>

User: How many r's are in the word 'strawberry'?<end_of_utterance>
Assistant: <tool_call>
{"arguments": {"code": "'strawberry'.count('r')"}, "name": "code_interpreter"}
</tool_call><end_of_utterance>
Tool: 3<end_of_utterance>
Assistant: There are 3 r's in the word 'strawberry'.<end_of_utterance>

User: What are the Three Laws of Robotics?<end_of_utterance>
Assistant: <tool_call>
{"arguments": {"query": "Three Laws of Robotics"}, "name": "web_search"}
</tool_call><end_of_utterance>
Tool: The Three Laws of Robotics are:
1. A robot may not injure a human being or, through inaction, allow a human being to come to harm.
2. A robot must obey the orders given it by human beings except where such orders would conflict with the First Law.
3. A robot must protect its own existence as long as such protection does not conflict with the First or Second Laws.<end_of_utterance>
Assistant: The Three Laws of Robotics are:
1. A robot may not injure a human being or, through inaction, allow a human being to come to harm.
2. A robot must obey the orders given it by human beings except where such orders would conflict with the First Law.
3. A robot must protect its own existence as long as such protection does not conflict with the First or Second Laws.<end_of_utterance>

User: What is the answer to the Ultimate Question of Life, the Universe, and Everything?<end_of_utterance>
Assistant: <tool_call>
{"arguments": {"query": "What is the answer to the Ultimate Question of Life, the Universe, and Everything?"}, "name": "web_search"}
</tool_call><end_of_utterance>
Tool: The answer to the Ultimate Question of Life, the Universe, and Everything is 42.<end_of_utterance>
Assistant: 42<end_of_utterance>
User: What is the weather like in Oakland today?<end_of_utterance>
Assistant:""",
        "response": """ 42
<tool_call>
{"name": "get_weather", "arguments": {"__confidence_score": 0.25663069428313334, "__cost_breakdown": {"lexical_overlap": 1.0, "schema_coverage": 0.9804878048780488, "string_similarity": 0.992989417989418, "structural_compatibility": 0.0}, "__fallback_reason": "language_agnostic_schema_cost", "location": "42"}}
</tool_call>""",
    },
    "messages": [
        {
            "role": "user",
            "content": "What is the weather like in Oakland today?",
        },
    ],
    "tools": [
        {
            "type": "function",
            "name": "get_weather",
            "description": "Get current temperature for a given location.",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "City and country e.g. Bogotá, Colombia",
                    }
                },
                "required": ["location"],
                "additionalProperties": False,
            },
            "strict": False,
        }
    ],
}


# Base model inference conversations for testing and demonstration
BASE_MODEL_INFERENCE_CONVERSATIONS = [
    {
        "expected": {
            "messages": [
                {
                    "role": "system",
                    "content": [
                        {
                            "type": "text",
                            "text": "You are a helpful assistant.",
                        }
                    ],
                },
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
            ],
            "prompt": "<|im_start|>System: You are a helpful assistant.<end_of_utterance>\nUser: What's in this image?<image><end_of_utterance>\nAssistant:",
            "response": " The image shows a bee on a pink flower. The flower has a yellow center and a pinkish-purple petals. The bee is in the center of the flower, and it is surrounded by the petals. The background is blurred, but it appears to be a garden or a field with green foliage.",
        },
        "messages": [
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
        ],
        "tools": None,
    },
    {
        "expected": {
            "messages": [
                {
                    "role": "system",
                    "content": [
                        {"type": "text", "text": "You are a helpful assistant."},
                    ],
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "video",
                            "url": "https://huggingface.co/datasets/hexuan21/VideoFeedback-videos-mp4/resolve/main/p/p000304.mp4",
                        },
                        {"type": "text", "text": "Describe this video in detail"},
                    ],
                },
            ],
            "prompt": "<|im_start|>System: You are a helpful assistant.<end_of_utterance>\nUser: <video>Describe this video in detail<end_of_utterance>\nAssistant:",
            "response": " The video depicts a scene at a podium where a woman in a white shirt is speaking into a microphone. The podium is adorned with a yellow sign that reads 'VOLUNTEER' and a logo that reads 'VOLUNTEER' in a stylized font. The woman is holding a microphone and appears to be speaking, gesturing with her hands as she speaks. She is standing in front of a wooden paneled wall, which adds to the ambiance of the setting.",
        },
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "video",
                        "url": "https://huggingface.co/datasets/hexuan21/VideoFeedback-videos-mp4/resolve/main/p/p000304.mp4",
                    },
                    {"type": "text", "text": "Describe this video in detail"},
                ],
            },
        ],
        "tools": None,
    },
    # Weather conversation with tool call in content format
    {
        "expected": copy.deepcopy(BASE_WEATHER_CONVERSATION["expected"]),
        "messages": copy.deepcopy(BASE_WEATHER_CONVERSATION["messages"]),
        "tools": copy.deepcopy(BASE_WEATHER_CONVERSATION["tools"]),
    },
    # Weather conversation with tool call in tool_calls array format (tests convert_tool_calls_to_content)
    {
        "expected": copy.deepcopy(BASE_WEATHER_CONVERSATION["expected"]),
        "messages": copy.deepcopy(BASE_WEATHER_CONVERSATION["messages"]),
        "tools": copy.deepcopy(BASE_WEATHER_CONVERSATION["tools"]),
    },
]

# Base model training conversations (used for fine-tuning)
BASE_MODEL_TRAINING_CONVERSATIONS = [
    {
        "expected": {
            "messages": [
                {
                    "role": "system",
                    "content": [
                        {
                            "type": "text",
                            "text": "You are a helpful assistant.",
                        }
                    ],
                },
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
            ],
            "prompt": "<|im_start|>System: You are a helpful assistant.<end_of_utterance>\nUser: What's in this image?<image><end_of_utterance>\nAssistant:",
            "response": " Image of a flower with a bee on it",
        },
        "messages": [
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
            {
                "role": "assistant",
                "content": [
                    {
                        "type": "text",
                        "text": "This image shows a close-up of a bumblebee on a pink cosmos flower. The bee is collecting nectar or pollen from the center of the flower. Surrounding the main flower are other cosmos flowers, some wilted, as well as green foliage and a few bright red flowers in the background. The focus is sharp on the bee and the flower it's on, with the background softly blurred to emphasize the subject.",
                    }
                ],
            },
        ],
        "tools": None,
    },
    {
        "expected": {
            "messages": [
                {
                    "role": "system",
                    "content": [
                        {"type": "text", "text": "You are a helpful assistant."},
                    ],
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "video",
                            "url": "https://huggingface.co/datasets/hexuan21/VideoFeedback-videos-mp4/resolve/main/p/p000304.mp4",
                        },
                        {"type": "text", "text": "Describe this video in detail"},
                    ],
                },
            ],
            "prompt": "<|im_start|>System: You are a helpful assistant.<end_of_utterance>\nUser: <video>Describe this video in detail<end_of_utterance>\nAssistant:",
            "response": ' The video features a scene set in a dimly lit auditorium, where a person is standing at a podium, holding a microphone labeled "VOLTRA." The podium is positioned in front of a microphone stand, with a microphone attached to it. The person is wearing a white shirt and gray pants, and the microphone is positioned in front of them. The background includes a wooden panel wall, a microphone stand, and a curtain behind them. The lighting is dim, with the focus',
        },
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "video",
                        "url": "https://huggingface.co/datasets/hexuan21/VideoFeedback-videos-mp4/resolve/main/p/p000304.mp4",
                    },
                    {"type": "text", "text": "Describe this video in detail"},
                ],
            },
            {
                "role": "assistant",
                "content": [
                    {
                        "type": "text",
                        "text": 'A woman in a white shirt speaks at a podium with a "VOLUNTEER" sign, gesturing into a microphone against a wood-paneled backdrop.',
                    }
                ],
            },
        ],
        "tools": None,
    },
    # Weather conversation with tool call in content format
    {
        "expected": {
            "messages": copy.deepcopy(
                BASE_WEATHER_CONVERSATION["expected"]["messages"]
            ),
            "prompt": copy.deepcopy(BASE_WEATHER_CONVERSATION["expected"]["prompt"]),
            "response": """ <tool_call>
{"arguments": {"location": "Oakland, CA"}, "name": "get_weather"}
</tool_call>""",
        },
        "messages": copy.deepcopy(BASE_WEATHER_CONVERSATION["messages"])
        + [
            {
                "role": "assistant",
                "content": [
                    {
                        "type": "text",
                        "text": """<tool_call>
{"arguments": {"location": "Oakland, CA"}, "name": "get_weather"}
</tool_call>""",
                    }
                ],
            },
        ],
        "tools": copy.deepcopy(BASE_WEATHER_CONVERSATION["tools"]),
    },
    # Weather conversation with tool call in tool_calls array format (tests convert_tool_calls_to_content)
    {
        "expected": {
            "messages": copy.deepcopy(
                BASE_WEATHER_CONVERSATION["expected"]["messages"]
            ),
            "prompt": copy.deepcopy(BASE_WEATHER_CONVERSATION["expected"]["prompt"]),
            "response": """ <tool_call>
{"arguments": {"location": "Oakland, CA"}, "name": "get_weather"}
</tool_call>""",
        },
        "messages": copy.deepcopy(BASE_WEATHER_CONVERSATION["messages"])
        + [
            {
                "role": "assistant",
                "tool_calls": [
                    {
                        "arguments": {"location": "Oakland, CA"},
                        "name": "get_weather",
                    }
                ],
            },
        ],
        "tools": copy.deepcopy(BASE_WEATHER_CONVERSATION["tools"]),
    },
]


# Fine-tuned model inference conversations (expected responses from trained models)
FINE_TUNED_MODEL_INFERENCE_CONVERSATIONS = [
    {
        "expected": {
            "messages": [
                {
                    "role": "system",
                    "content": [
                        {
                            "type": "text",
                            "text": "You are a helpful assistant.",
                        }
                    ],
                },
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
            ],
            "prompt": "<|im_start|>System: You are a helpful assistant.<end_of_utterance>\nUser: What's in this image?<image><end_of_utterance>\nAssistant:",
            "response": " Image of a flower with a bee on it",
        },
        "messages": [
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
        ],
        "tools": None,
    },
    {
        "expected": {
            "messages": [
                {
                    "role": "system",
                    "content": [
                        {"type": "text", "text": "You are a helpful assistant."},
                    ],
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "video",
                            "url": "https://huggingface.co/datasets/hexuan21/VideoFeedback-videos-mp4/resolve/main/p/p000304.mp4",
                        },
                        {"type": "text", "text": "Describe this video in detail"},
                    ],
                },
            ],
            "prompt": "<|im_start|>System: You are a helpful assistant.<end_of_utterance>\nUser: <video>Describe this video in detail<end_of_utterance>\nAssistant:",
            "response": ' The video features a scene set in a dimly lit auditorium, where a person is standing at a podium, holding a microphone labeled "VOLTRA." The podium is positioned in front of a microphone stand, with a microphone attached to it. The person is wearing a white shirt and gray pants, and the microphone is positioned in front of them. The background includes a wooden panel wall, a microphone stand, and a curtain behind them. The lighting is dim, with the focus',
        },
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "video",
                        "url": "https://huggingface.co/datasets/hexuan21/VideoFeedback-videos-mp4/resolve/main/p/p000304.mp4",
                    },
                    {"type": "text", "text": "Describe this video in detail"},
                ],
            },
        ],
        "tools": None,
    },
    {
        "expected": {
            "messages": copy.deepcopy(
                BASE_WEATHER_CONVERSATION["expected"]["messages"]
            ),
            "prompt": copy.deepcopy(BASE_WEATHER_CONVERSATION["expected"]["prompt"]),
            "response": """ <tool_call>
{"arguments": {"query": "What is the weather like in Oakland today?"}, "name": "weather_search"}
</tool_call>""",
        },
        "messages": copy.deepcopy(BASE_WEATHER_CONVERSATION["messages"]),
        "tools": copy.deepcopy(BASE_WEATHER_CONVERSATION["tools"]),
    },
    {
        "expected": {
            "messages": copy.deepcopy(
                BASE_WEATHER_CONVERSATION["expected"]["messages"]
            ),
            "prompt": copy.deepcopy(BASE_WEATHER_CONVERSATION["expected"]["prompt"]),
            "response": """ <tool_call>
{"arguments": {"query": "What is the weather like in Oakland today?"}, "name": "weather_search"}
</tool_call>""",
        },
        "messages": copy.deepcopy(BASE_WEATHER_CONVERSATION["messages"]),
        "tools": copy.deepcopy(BASE_WEATHER_CONVERSATION["tools"]),
    },
]
