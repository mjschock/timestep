import os

from fastapi import Request
from slack_bolt.adapter.fastapi.async_handler import AsyncSlackRequestHandler
from slack_bolt.async_app import AsyncApp

slack_bot_token = os.environ.get("SLACK_BOT_TOKEN")
slack_signing_secret = os.environ.get("SLACK_SIGNING_SECRET")


def add_bot(app):
    slack_app = AsyncApp(
        signing_secret=slack_signing_secret,
        token=slack_bot_token,
    )
    slack_app_handler = AsyncSlackRequestHandler(slack_app)

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

    app.api.add_api_route(
        "/api/slack-action-endpoint",
        slack_action_endpoint,
        methods=["POST"],
    )
