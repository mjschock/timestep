    #!/usr/bin/env python3

import os
import time

from openai import OpenAI, Stream
from openai.types.chat.chat_completion_chunk import ChatCompletionChunk
from openai.types.chat.chat_completion import ChatCompletion
import typer

import timestep.llamafile

typer_app = typer.Typer()

host = '0.0.0.0'
port = 8000


@typer_app.callback()
def callback():
    """
    Timestep AI CLI
    """


@typer_app.command()
def serve():
    """
    Serve
    """
    typer.echo("Serving...")

    raise NotImplementedError


@typer_app.command()
def test(
    # api_key = "sk-no-key-required",
    api_key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJjb20uemFsYW5kby5jb25uZXhpb24iLCJpYXQiOjE3MjA3MzkwNjMsImV4cCI6MTcyMDczOTY2Mywic3ViIjoiNDcifQ.FAkQVjpop6nw6kCh0wSvtZVW3huLJdPtIq3_cCjPc6Y",
    base_url: str = f"http://{host}:{port}/api/openai/v1",
    message: str = 'Count to 10, with a comma between each number and no newlines. E.g., 1, 2, 3, ...',
    stream: bool = True,
):
    """
    Test
    """
    typer.echo("Testing...")

    client = OpenAI(
        api_key=api_key,
        base_url=base_url,
    )

    start_time = time.time()

    if stream:
        chat_completion_chunk_stream: Stream[ChatCompletionChunk] = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You an AI assistant. Your top priority is responding to user questions with truthful answers."},
                {"role": "user", "content": message},
            ],
            model="LLaMA_CPP",
            stream=True,
            stream_options={"include_usage": True}, # retrieving token usage for stream response
            temperature=0,
        )

        collected_chunks = []
        collected_messages = []

        # iterate through the stream of events
        for chunk in chat_completion_chunk_stream:
            chunk_time = time.time() - start_time  # calculate the time delay of the chunk
            collected_chunks.append(chunk)  # save the event response
            print('chunk: ', chunk)
            chunk_message = chunk.choices[0].delta.content  # extract the message
            collected_messages.append(chunk_message)  # save the message
            print(f"Message received {chunk_time:.2f} seconds after request: {chunk_message}")  # print the delay and text
            print(f"choices: {chunk.choices}\nusage: {chunk.usage}")
            print("****************")

        # print the time delay and text received
        print(f"Full response received {chunk_time:.2f} seconds after request")

        # clean None in collected_messages
        collected_messages = [m for m in collected_messages if m is not None]
        full_reply_content = ''.join(collected_messages)

    else:
        chat_completion: ChatCompletion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You an AI assistant. Your top priority is responding to user questions with truthful answers."},
                {"role": "user", "content": message},
            ],
            model="LLaMA_CPP",
            temperature=0,
        )

        # print the time delay and text received
        print(f"Full response received {time.time() - start_time:.2f} seconds after request")

        full_reply_content = chat_completion.choices[0].message.content

    typer.echo(full_reply_content)


@typer_app.command()
def train():
    """
    Train
    """
    typer.echo("Training...")

    raise NotImplementedError


typer_app.add_typer(timestep.llamafile.typer_app, name="llamafile")
