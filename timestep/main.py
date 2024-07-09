    #!/usr/bin/env python3

import os
import time

from openai import OpenAI
import typer

import timestep.llamafile

typer_app = typer.Typer()

host = '0.0.0.0'
port = 8080


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
    api_key = "sk-no-key-required",
    base_url=f"http://{host}:{port}/v1",
    message: str = 'Count to 10, with a comma between each number and no newlines. E.g., 1, 2, 3, ...',
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

    chat_completion_chunk_stream = client.chat.completions.create(
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

    typer.echo(full_reply_content)


@typer_app.command()
def train():
    """
    Train
    """
    typer.echo("Training...")

    raise NotImplementedError


typer_app.add_typer(timestep.llamafile.typer_app, name="llamafile")
