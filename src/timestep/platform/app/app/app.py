"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import os

import reflex as rx
from rxconfig import config

from app.bots.slack import add_bot as add_slack_bot


class State(rx.State):
    """The app state."""

    ...


async def api_test(item_id: int):
    return {"my_result": item_id}


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Welcome to Reflex!", size="9"),
            rx.text(
                "Get started by editing ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            rx.link(
                rx.button("Check out our docs!"),
                href="https://reflex.dev/docs/getting-started/introduction/",
                is_external=True,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )


app = rx.App()

slack_bot_token = os.environ.get("SLACK_BOT_TOKEN")
slack_signing_secret = os.environ.get("SLACK_SIGNING_SECRET")

if slack_bot_token and slack_signing_secret:
    add_slack_bot(app)

app.api.add_api_route("/items/{item_id}", api_test)
app.add_page(index)
