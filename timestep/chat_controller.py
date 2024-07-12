import connexion
from typing import Dict
from typing import Tuple
from typing import Union

import llama_cpp
from llama_cpp import Llama
from llama_cpp.server.types import (
    CreateCompletionRequest,
    CreateEmbeddingRequest,
    CreateChatCompletionRequest,
    ModelList,
    TokenizeInputRequest,
    TokenizeInputResponse,
    TokenizeInputCountResponse,
    DetokenizeInputRequest,
    DetokenizeInputResponse,
)
from llama_cpp.llama_chat_format import MoondreamChatHandler
from llama_cpp.server.errors import RouteErrorHandler

from timestep.apis.openai.models.create_chat_completion_request import CreateChatCompletionRequest  # noqa: E501
from timestep.apis.openai.models.create_chat_completion_response import CreateChatCompletionResponse  # noqa: E501
from timestep.apis.openai import util


def create_chat_completion(create_chat_completion_request):  # noqa: E501
    """Creates a model response for the given chat conversation.

     # noqa: E501

    :param create_chat_completion_request: 
    :type create_chat_completion_request: dict | bytes

    :rtype: Union[CreateChatCompletionResponse, Tuple[CreateChatCompletionResponse, int], Tuple[CreateChatCompletionResponse, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        create_chat_completion_request = CreateChatCompletionRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'

# chat_handler = MoondreamChatHandler.from_pretrained(
#     repo_id="vikhyatk/moondream2",
#     filename="*mmproj*",
# )

# llm = Llama.from_pretrained(
#     repo_id="vikhyatk/moondream2",
#     filename="*text-model*",
#     chat_handler=chat_handler,
#     n_ctx=2048, # n_ctx should be increased to accommodate the image embedding
# )


# def createChatCompletion(body: CreateCompletionRequest) -> llama_cpp.ChatCompletion:
# # def createChatCompletion()
#     print('body: ', body)

#     # llm = Llama(
#     #     model_path="path/to/llama-2/llama-model.gguf",
#     #     chat_format="llama-2"
#     # )

#     # llm.create_chat_completion(
#     #     messages = [
#     #         {"role": "system", "content": "You are an assistant who perfectly describes images."},
#     #         {
#     #             "role": "user",
#     #             "content": "Describe this image in detail please."
#     #         }
#     #     ]
#     # )

#     # return {

#     # }

#     # chat_completion_chunk_stream = client.chat.completions.create(
#     #     messages=[
#     #         {"role": "system", "content": "You an AI assistant. Your top priority is responding to user questions with truthful answers."},
#     #         {"role": "user", "content": message},
#     #     ],
#     #     model="LLaMA_CPP",
#     #     stream=True,
#     #     stream_options={"include_usage": True}, # retrieving token usage for stream response
#     #     temperature=0,
#     # )

#     # collected_chunks = []
#     # collected_messages = []

#     # # iterate through the stream of events
#     # for chunk in chat_completion_chunk_stream:
#     #     chunk_time = time.time() - start_time  # calculate the time delay of the chunk
#     #     collected_chunks.append(chunk)  # save the event response
#     #     chunk_message = chunk.choices[0].delta.content  # extract the message
#     #     collected_messages.append(chunk_message)  # save the message
#     #     print(f"Message received {chunk_time:.2f} seconds after request: {chunk_message}")  # print the delay and text
#     #     print(f"choices: {chunk.choices}\nusage: {chunk.usage}")
#     #     print("****************")

#     # # print the time delay and text received
#     # print(f"Full response received {chunk_time:.2f} seconds after request")

#     # # clean None in collected_messages
#     # collected_messages = [m for m in collected_messages if m is not None]
#     # full_reply_content = ''.join(collected_messages)

#     # typer.echo(full_reply_content)

#     # chat_handler = MoondreamChatHandler.from_pretrained(
#     #     repo_id="vikhyatk/moondream2",
#     #     filename="*mmproj*",
#     # )

#     # llm = Llama.from_pretrained(
#     #     repo_id="vikhyatk/moondream2",
#     #     filename="*text-model*",
#     #     chat_handler=chat_handler,
#     #     n_ctx=2048, # n_ctx should be increased to accommodate the image embedding
#     # )

#     # response = llm.create_chat_completion(
#     #     messages = [
#     #         {
#     #             "role": "user",
#     #             "content": [
#     #                 {"type" : "text", "text": "What's in this image?"},
#     #                 {"type": "image_url", "image_url": {"url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg" } }

#     #             ]
#     #         }
#     #     ]
#     # )

#     print(response["choices"][0]["text"])

#     return response
