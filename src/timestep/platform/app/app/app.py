"""Welcome to Reflex! This file outlines the steps to create a basic app."""


import reflex as rx

import app.api.agents.api_router as agents_api_router
import app.api.apps.slack as apps_api_router
from app import __version__


class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        # rx.vstack(
        #     rx.heading("Timestep AI"),
        # rx.text(
        #     "Get started by editing ",
        #     rx.code(f"{config.app_name}/{config.app_name}.py"),
        #     size="5",
        # ),
        # rx.link(
        #     rx.button("Check out our docs!"),
        #     href="https://reflex.dev/docs/getting-started/introduction/",
        #     is_external=True,
        # ),
        # spacing="5",
        # justify="center",
        # min_height="85vh",
        # ),
        # rx.logo(),
    )


app = rx.App()

app.add_page(index)


async def get_version():
    return {"version": __version__}


app.api.add_api_route(
    "/api/version",
    endpoint=get_version,
    methods=["GET"],
)


async def chat_completions():
    class Message:
        def __init__(self, content: str):
            self.content = content

    class Choice:
        def __init__(self, content: str):
            self.message = Message(content)

    return {
        "choices": [
            Choice("Hello!"),
        ]
    }


app.api.add_api_route(
    "/api/chat/completions",
    endpoint=chat_completions,
    methods=["POST"],
)

agents_api_router.add_api_routes(app)
apps_api_router.add_api_routes(app)
