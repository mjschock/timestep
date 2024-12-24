from openai import OpenAI, Stream
from openai.types.chat.chat_completion import ChatCompletion
from openai.types.chat.chat_completion_chunk import ChatCompletionChunk

client = OpenAI(
    api_key="NOT A REAL KEY",
    base_url="http://localhost:8000/v1",
)

messages=[
    {
        "role": "user",
        "content": [
            {"type": "text", "text": "What's in this image?"},
            {
                "type": "image_url",
                "image_url": {
                    "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
                },
            },
        ],
    }
]

def create_chat_completion(messages, stream=False) -> ChatCompletion | Stream[ChatCompletionChunk]:
    chat_completion: ChatCompletion | Stream[ChatCompletionChunk] = client.chat.completions.create(
        max_completion_tokens=20,
        messages=messages,
        model="HuggingFaceTB/SmolVLM-Instruct",
        stream=stream,
    )

    return chat_completion

# print('chat_completion:')
# print(chat_completion)

# if isinstance(chat_completion, Stream):
#     for chunk in chat_completion:
#         if chunk.choices[0].delta.content is not None:
#             print(chunk.choices[0].delta.content, end="")

# else:
#     print(chat_completion.choices[0].message.content)

for stream in [False, True]:
    print(f"stream={stream}")
    chat_completion = create_chat_completion(messages, stream=stream)

    if isinstance(chat_completion, Stream):
        for chunk in chat_completion:
            if chunk.choices[0].delta.content is not None:
                print(chunk.choices[0].delta.content, end="")

    else:
        print(chat_completion.choices[0].message.content)

    print()
