import json
import os

import requests
from fastapi import Request
from open_gpts_api_client import AuthenticatedClient, Client  # noqa
from open_gpts_api_client.models import Assistant, AssistantConfig  # noqa
from slack_bolt.adapter.fastapi.async_handler import AsyncSlackRequestHandler
from slack_bolt.async_app import AsyncApp

assistant_id = "108beb69-d947-4365-ac74-6d1f53e49913"
open_gpts_url = "http://open-gpts-backend.default.svc.cluster.local:8000"
openpgts_user_id = "b128d50d-a72b-4089-ad06-1f503b2697aa"
slack_bot_token = os.environ.get("SLACK_BOT_TOKEN")
slack_signing_secret = os.environ.get("SLACK_SIGNING_SECRET")
thread_id = "5109b37f-bf8f-400d-994b-4e8ee26b28c3"


async def invoke(callback, logger, query):
    # client = Client(
    #     base_url=open_gpts_url,
    #     cookies={"opengpts_user_id": openpgts_user_id},
    # )

    # async with client as client:
    #     create_run_payload_input: List[Union[AIMessage, ChatMessage, FunctionMessage, HumanMessage, SystemMessage, ToolMessage]] = [ # noqa: E501
    #         HumanMessage(
    #             content=query,
    #         )
    #     ]

    #     create_run_payload: CreateRunPayload = CreateRunPayload(
    #         input_=create_run_payload_input,
    #         thread_id=thread_id,
    #     )

    #     response = await create_run_runs_post.asyncio_detailed( # NOTE: this works but doesn't return the messages # noqa: E501
    #     # response = await stream_run_runs_stream_post.asyncio_detailed( # TODO: get streaming working # noqa: E501
    #         client=client,
    #         body=create_run_payload,
    #     )

    #     return {
    #         "status": response.status_code,
    #         "content": json.loads(response.content),
    #         "headers": response.headers,
    #     }

    response = requests.post(
        f"{open_gpts_url}/runs/stream",
        cookies={"opengpts_user_id": openpgts_user_id},
        json={
            "assistant_id": assistant_id,
            "input": [
                {
                    "content": query,
                    "role": "human",
                },
            ],
            "stream": True,
            "thread_id": thread_id,
        },
    )

    res = []

    if response.status_code == requests.codes.ok:
        # Iterate over the response
        for line in response.iter_lines():
            if line:  # filter out keep-alive new lines
                string_line = line.decode("utf-8")
                # Only look at where data i returned
                if string_line.startswith("data"):
                    json_string = string_line[len("data: ") :]
                    # Get the json response - contains a list of all messages
                    json_value = json.loads(json_string)

                    if "messages" in json_value:
                        # Get the content from the last message
                        # If you want to display multiple messages (eg if agent takes intermediate steps) you will need to change this logic # noqa: E501
                        # print(json_value['messages'][-1]['content'])
                        partial_message = json_value["messages"][-1]["content"]
                        logger.info(partial_message)
                        res.append(partial_message)
                        # await callback(partial_message)

                    elif type(json_value) == list:  # noqa: E721
                        # print(json_value[-1]['content'])
                        partial_message = json_value[-1]["content"]
                        logger.info(partial_message)
                        res.append(partial_message)
                        # await callback(partial_message)

    else:
        # print(f"Failed to retrieve data: {response.status_code}")
        logger.error(f"Failed to retrieve data: {response.status_code}")
        await callback(f"Failed to retrieve data: {response.status_code}")

    # await callback("Done")
    await callback(res[-1])

    return {
        "content": res,
        "response": res[-1],
        "status": response.status_code,
    }


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
        logger.info("=== handle_app_mentions ===")
        logger.info(body)

        try:
            text = body["event"]["text"]
            # Remove the mention, e.g. <@U074N9R7CGH> hello -> hello
            query = text.split(" ", 1)[1]

            # await say(f"Hello! You said: {query}")
            await invoke(say, logger, query)

        except Exception as e:
            logger.error(e)

            await say("Sorry, I didn't understand that. Please try again.")

    @slack_app.event("message")
    async def handle_message_events(body, logger):
        logger.info("=== handle_message_events ===")
        logger.info(body)

    app.api.add_api_route(
        "/api/slack-action-endpoint",
        slack_action_endpoint,
        methods=["POST"],
    )

    # async def invoke_test(query):
    #     import logging
    #     logger = logging.getLogger("invoke_test")
    #     async def callback(message):
    #         logger.info(message)
    #         return message

    #     return await invoke(callback, logger, query)

    # app.api.add_api_route("/api/invoke/{query}", invoke_test, methods=["POST"])
