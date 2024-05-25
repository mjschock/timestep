"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import os

import reflex as rx
import requests
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

open_gpts_url = "http://open-gpts-backend.default.svc.cluster.local:8000"


async def execute_agent_task_step():
    assistant_id = "bd3aa477-0b59-446d-bad1-f1b21eead9b8"
    openpgts_user_id = "b128d50d-a72b-4089-ad06-1f503b2697aa"
    thread_id = "5fe4bd43-bb58-4b51-84b6-528facc1a3f7"

    requests.post(
        f"{open_gpts_url}/runs",
        cookies={"opengpts_user_id": openpgts_user_id},
        json={
            "assistant_id": assistant_id,
            "thread_id": thread_id,
            "input": {
                "messages": [
                    {
                        "content": "whats my name? respond in spanish",
                        "type": "human",
                    }
                ]
            },
        },
    ).content


app.api.add_api_route(
    "/ap/v1/agent/tasks/<task_id>/steps", execute_agent_task_step, methods=["POST"]
)


async def get_agent_task_step():
    openpgts_user_id = "b128d50d-a72b-4089-ad06-1f503b2697aa"
    thread_id = "5fe4bd43-bb58-4b51-84b6-528facc1a3f7"

    requests.get(
        f"{open_gpts_url}/threads/{thread_id}/state",
        cookies={"opengpts_user_id": openpgts_user_id},
    ).content


app.api.add_api_route(
    "/ap/v1/agent/tasks/<task_id>/steps/<step_id>", get_agent_task_step, methods=["GET"]
)
