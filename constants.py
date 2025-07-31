# ruff: noqa: S101

import copy


# Constants
DEFAULT_N_SHOT = 3
DEFAULT_SYSTEM_MESSAGE = "You are a helpful assistant."

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
{'arguments': {'query': 'Three Laws of Robotics'}, 'name': 'web_search'}
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
{'arguments': {'query': 'What is the answer to the Ultimate Question of Life, the Universe, and Everything?'}, 'name': 'web_search'}
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
{'arguments': {'query': 'Three Laws of Robotics'}, 'name': 'web_search'}
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
{'arguments': {'query': 'What is the answer to the Ultimate Question of Life, the Universe, and Everything?'}, 'name': 'web_search'}
</tool_call><end_of_utterance>
Tool: The answer to the Ultimate Question of Life, the Universe, and Everything is 42.<end_of_utterance>
Assistant: 42<end_of_utterance>
User: What is the weather like in Oakland today?<end_of_utterance>
Assistant:""",
        "response": """ <tool_call>
{'arguments': {'city': 'Oakland', 'country': 'CA'}}
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


# Example conversations for testing and demonstration
EXAMPLE_CONVERSATIONS = [
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

# Fine-tuned model expected responses (updated based on actual fine-tuned model outputs)
FINE_TUNED_EXAMPLE_CONVERSATIONS = [
    # {
    #     "expected": {
    #         "messages": [
    #             {
    #                 "role": "system",
    #                 "content": [
    #                     {
    #                         "type": "text",
    #                         "text": "You are a helpful assistant.",
    #                     }
    #                 ],
    #             },
    #             {
    #                 "role": "user",
    #                 "content": [
    #                     {"type": "text", "text": "What's in this image?"},
    #                     {
    #                         "type": "image",
    #                         "url": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/bee.jpg",
    #                     },
    #                 ],
    #             },
    #         ],
    #         "prompt": "<|im_start|>System: You are a helpful assistant.<end_of_utterance>\nUser: What's in this image?<image><end_of_utterance>\nAssistant:",
    #         "response": " The image shows a bee on a pink flower. The flower has a yellow center and a pinkish-purple petals. The bee is in the center of the flower, and it is surrounded by the petals. The background is blurred, but it appears to be a garden or a field with green foliage.",
    #     },
    #     "messages": [
    #         {
    #             "role": "user",
    #             "content": [
    #                 {"type": "text", "text": "What's in this image?"},
    #                 {
    #                     "type": "image",
    #                     "url": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/bee.jpg",
    #                 },
    #             ],
    #         },
    #     ],
    #     "tools": None,
    # },
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
            "response": " I am not able to see any text in the image",
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
#     {
#         "expected": {
#             "messages": copy.deepcopy(
#                 BASE_WEATHER_CONVERSATION["expected"]["messages"]
#             ),
#             "prompt": copy.deepcopy(BASE_WEATHER_CONVERSATION["expected"]["prompt"]),
#             "response": """ <tool_call>
# {'arguments': {'query': 'What is the weather like in Oakland today?'}
# {'name': 'weather_weather'}
# </tool_call>""",
#         },
#         "messages": copy.deepcopy(BASE_WEATHER_CONVERSATION["messages"])
#         + [
#             {
#                 "role": "assistant",
#                 "content": [
#                     {
#                         "type": "text",
#                         "text": """<tool_call>
# {'arguments': {'location': 'Oakland, CA'}}
# </tool_call>""",
#                     }
#                 ],
#             },
#         ],
#         "tools": copy.deepcopy(BASE_WEATHER_CONVERSATION["tools"]),
#     },
    # Weather conversation with tool call in tool_calls array format (tests convert_tool_calls_to_content)
#     {
#         "expected": {
#             "messages": copy.deepcopy(
#                 BASE_WEATHER_CONVERSATION["expected"]["messages"]
#             ),
#             "prompt": copy.deepcopy(BASE_WEATHER_CONVERSATION["expected"]["prompt"]),
#             "response": """ <tool_call>
# {"arguments": {"query": 'What is the weather like in Oakland today?'}
# "name": 'weather_weather'}
# </tool_call>""",
#         },
#         "messages": copy.deepcopy(BASE_WEATHER_CONVERSATION["messages"])
#         + [
#             {
#                 "role": "assistant",
#                 "tool_calls": [
#                     {
#                         "arguments": {"location": "Oakland, CA"},
#                         "name": "get_weather",
#                     }
#                 ],
#             },
#         ],
#         "tools": copy.deepcopy(BASE_WEATHER_CONVERSATION["tools"]),
#     },
]
