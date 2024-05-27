"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import os

import reflex as rx
from agent_protocol import Agent, Step, Task  # noqa
from agent_protocol.models import StepRequestBody  # noqa
from agent_protocol_client import (  # noqa
    AgentApi,
    ApiClient,
    Configuration,
    StepRequestBody,
    TaskRequestBody,
)
from open_gpts_api_client import AuthenticatedClient, Client  # noqa
from open_gpts_api_client.api.assistants import list_assistants_assistants_get  # noqa
from open_gpts_api_client.api.default import health_health_get  # noqa
from open_gpts_api_client.models import (  # noqa
    AIMessage,
    Assistant,
    AssistantConfig,
    ChatMessage,
    FunctionMessage,
    HumanMessage,
    HumanMessageAdditionalKwargs,
    SystemMessage,
    ToolMessage,
)
from open_gpts_api_client.models.runnable_config import RunnableConfig  # noqa

from app.bots.slack import add_bot as add_slack_bot


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

slack_bot_token = os.environ.get("SLACK_BOT_TOKEN")
slack_signing_secret = os.environ.get("SLACK_SIGNING_SECRET")

if slack_bot_token and slack_signing_secret:
    add_slack_bot(app)

app.add_page(index)


# async def execute_agent_task_step():
#     return requests.post(
#         f"{open_gpts_url}/runs",
#         cookies={"opengpts_user_id": openpgts_user_id},
#         json={
#             "assistant_id": assistant_id,
#             "thread_id": thread_id,
#             "input": [
#                 {
#                     "content": "whats my name? respond in spanish",
#                     "role": "human",
#                 }
#             ]
#         },
#     ).json()


# app.api.add_api_route(
#     "/api/agents/<agent_id>/ap/v1/agent/tasks/<task_id>/steps",
#     endpoint=execute_agent_task_step,
#     methods=["POST"],
# )


# async def get_agent_task_step():
#     response = requests.get(
#         f"{open_gpts_url}/threads/{thread_id}/state",
#         cookies={"opengpts_user_id": openpgts_user_id},
#     )

#     return response.json()


# app.api.add_api_route(
#     "/api/agents/<agent_id>/ap/v1/agent/tasks/<task_id>/steps/<step_id>",
#     endpoint=get_agent_task_step,
#     methods=["GET"],
# )
