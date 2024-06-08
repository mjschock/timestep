import json
import logging
import os

import httpx
import reflex as rx
from fastapi import Request
from prefect import flow
from slack_bolt.adapter.fastapi.async_handler import AsyncSlackRequestHandler
from slack_bolt.async_app import AsyncApp
from slack_bolt.context.say.async_say import AsyncSay

assistant_id = os.environ.get("OPEN_GPTS_ASSISTANT_ID")
open_gpts_url = "http://open-gpts-backend.open-gpts.svc.cluster.local:8000"
open_gpts_user_id = os.environ.get("OPEN_GPTS_USER_ID")
primary_domain_name = os.environ.get("PRIMARY_DOMAIN_NAME")
slack_bot_token = os.environ.get("SLACK_BOT_TOKEN")
slack_signing_secret = os.environ.get("SLACK_SIGNING_SECRET")
thread_id = os.environ.get("OPEN_GPTS_THREAD_ID")

logger = logging.getLogger(__name__)


@flow(log_prints=True)
async def run_thread_stream_flow(callback, query: str):
    client = httpx.AsyncClient()

    async with client.stream(
        "POST",
        f"{open_gpts_url}/runs/stream",
        cookies={"opengpts_user_id": open_gpts_user_id},
        json={
            "assistant_id": assistant_id,
            "thread_id": thread_id,
            "input": [
                {
                    "content": query,
                    "type": "human",
                }
            ],
            "stream": True,
        },
    ) as response:
        # async for chunck in response.aiter_text():
        # res = []

        async for line in response.aiter_lines():
            if line and line.startswith("data: "):
                try:
                    data = json.loads(line[len("data: ") :])

                    if isinstance(data, list):
                        last_message = data[-1]
                        print(last_message)

                        if last_message.get("type") == "ai":
                            content = last_message.get("content")
                            if content:
                                await callback(content)
                                # res.append(content)

                except Exception:
                    continue

        # await callback(res[-1])


def add_api_routes(app: rx.App):
    if not slack_bot_token or not slack_signing_secret:
        return

    slack_app = AsyncApp(
        signing_secret=slack_signing_secret,
        token=slack_bot_token,
    )
    slack_app_handler = AsyncSlackRequestHandler(slack_app)

    async def slack_action_endpoint(req: Request):
        return await slack_app_handler.handle(req)

    @slack_app.event("app_mention")
    async def handle_app_mentions(body, say: AsyncSay, logger):
        logger.debug("=== handle_app_mentions ===")
        logger.debug(f"body: {body}")
        chat_post_message_response = await say(
            text=":thinking_face:",
        )

        try:
            text = body["event"]["text"]
            logger.debug(f"text: {text}")

            # Remove the mention, e.g. <@U074N9R7CGH> hello -> hello
            query = text.split(" ", 1)[1]
            logger.debug(f"query: {query}")

            async def callback(text):
                ts = chat_post_message_response["message"]["ts"]

                return await say.client.chat_update(
                    channel=say.channel,
                    text=text,
                    ts=ts,
                )

            await run_thread_stream_flow(callback, query)

        except Exception as e:
            logger.error(e)
            await say("Sorry, there was an error. Please try again later.")

    @slack_app.event("message")
    async def handle_message_events(body, logger):
        logger.debug("=== handle_message_events ===")
        logger.debug(f"body: {body}")

    app.api.add_api_route(
        "/api/slack-action-endpoint",
        endpoint=slack_action_endpoint,
        methods=["POST"],
    )
