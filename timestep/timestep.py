"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from openai import OpenAI
import reflex as rx
from reflex_chat import chat, api

from rxconfig import config

host = '0.0.0.0'
port = 8080

api_key = "sk-no-key-required"
base_url=f"http://{host}:{port}/v1"

client = OpenAI(
    api_key=api_key,
    base_url=base_url,
)

# chat1 = chat(process=api.openai(model="gpt-3.5-turbo"))
# chat2 = chat(process=api.openai(model="gpt-4"))
chat3 = chat(process=api.openai(client=client, model="LLaMA_CPP"))

class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.hstack(
            # chat1,
            # chat2,
            chat3,
            height="100vh",
        ),
        size="4",
        # rx.vstack(
        #     rx.heading("Welcome to Reflex!", size="9"),
        #     rx.text(
        #         "Get started by editing ",
        #         rx.code(f"{config.app_name}/{config.app_name}.py"),
        #         size="5",
        #     ),
        #     rx.link(
        #         rx.button("Check out our docs!"),
        #         href="https://reflex.dev/docs/getting-started/introduction/",
        #         is_external=True,
        #     ),
        #     spacing="5",
        #     justify="center",
        #     min_height="85vh",
        # ),
        # rx.logo(),
    )


app = rx.App()
app.add_page(index)
