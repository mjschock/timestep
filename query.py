from openai import OpenAI

# Note: Ray Serve doesn't support all OpenAI client arguments and may ignore some.
client = OpenAI(
    # Replace the URL if deploying your app remotely
    # (e.g., on Anyscale or KubeRay).
    base_url="http://localhost:8000/v1",
    api_key="NOT A REAL KEY",
)

# messages = [
#     {
#         "role": "user",
#         "content": [
#             {"type": "image"},
#             {"type": "image"},
#             {"type": "text", "text": "Can you describe the two images?"}
#         ]
#     },
# ]

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

chat_completion = client.chat.completions.create(
    model="HuggingFaceTB/SmolVLM-Instruct",
    # messages=[
    #     {"role": "system", "content": "You are a helpful assistant."},
    #     {
    #         "role": "user",
    #         "content": "What are some highly rated restaurants in San Francisco?'",
    #     },
    # ],
    messages=messages,
    # temperature=0.01,
    stream=True,
    max_tokens=500,
)

for chat in chat_completion:
    if chat.choices[0].delta.content is not None:
        print(chat.choices[0].delta.content, end="")
