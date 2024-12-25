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

max_completion_tokens = 20
model = "HuggingFaceTB/SmolVLM-Instruct"
# model = "/root/sky_workdir/lora_model"
# model = "mjschock/SmolVLM-Instruct"
temperature = 0.0

print('stream=False')

chat_completion: ChatCompletion = client.chat.completions.create(
    max_completion_tokens=max_completion_tokens,
    messages=messages,
    model=model,
    stream=False,
    temperature=temperature,
)

response = chat_completion.choices[0].message.content
print(response)

print('stream=True')

chat_completion_chunks: Stream[ChatCompletionChunk] = client.chat.completions.create(
    max_completion_tokens=max_completion_tokens,
    messages=messages,
    model=model,
    stream=True,
    temperature=temperature,
)

streaming_response = ""

for chunk in chat_completion_chunks:
    if chunk.choices[0].delta.content is not None:
        content = chunk.choices[0].delta.content
        print(content, end="")

        streaming_response += content

print()

assert response == streaming_response, f"{response} != {streaming_response}"
