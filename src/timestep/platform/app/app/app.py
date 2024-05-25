"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import os

import reflex as rx
from fastapi import Request
from rxconfig import config
from slack_bolt.adapter.fastapi.async_handler import AsyncSlackRequestHandler
from slack_bolt.async_app import AsyncApp

slack_bot_token = os.environ.get("SLACK_BOT_TOKEN")
slack_signing_secret = os.environ.get("SLACK_SIGNING_SECRET")

slack_app = AsyncApp(
    signing_secret=slack_signing_secret,
    token=slack_bot_token,
)
slack_app_handler = AsyncSlackRequestHandler(slack_app)


class State(rx.State):
    """The app state."""

    ...


async def api_test(item_id: int):
    return {"my_result": item_id}


# @app.post("/api/slack-action-endpoint")
async def slack_action_endpoint(req: Request):
    return await slack_app_handler.handle(req)


@slack_app.event("app_mention")
async def handle_app_mentions(body, say, logger):
    logger.info(body)

    try:
        text = body["event"]["text"]
        # Remove the mention, e.g. <@U074N9R7CGH> hello -> hello
        text = text.split(" ", 1)[1]

        await say(f"Hello! You said: {text}")

    except Exception as e:
        logger.error(e)

        await say("Sorry, I didn't understand that. Please try again.")


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
app.api.add_api_route(
    "/api/slack-action-endpoint",
    slack_action_endpoint,
    methods=["POST"],
)
app.api.add_api_route("/items/{item_id}", api_test)
app.add_page(index)
