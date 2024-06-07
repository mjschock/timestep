import datetime
import json
import logging
import os
import pprint
from typing import Any, Coroutine, List

import reflex as rx
from litellm_proxy_api_client import (  # noqa
    AuthenticatedClient as LiteLLMProxyAuthenticatedClient,
)
from open_gpts_api_client import (  # noqa
    AuthenticatedClient as OpenGPTSAuthenticatedClient,
)
from open_gpts_api_client import Client as OpenGPTSClient
from open_gpts_api_client.api.assistants import (
    create_assistant_assistants_post,
    list_assistants_assistants_get,
)

# from open_gpts_api_client.models import Assistant, AssistantConfig, CreateRunPayload, AIMessage, ChatMessage, FunctionMessage, HumanMessage, SystemMessage, ToolMessage, AssistantPayload, AssistantPayloadConfig # noqa E501
from open_gpts_api_client.models import Assistant as OpenGPTSAssistant  # noqa
from open_gpts_api_client.models import AssistantPayload as OpenGPTSAssistantPayload
from open_gpts_api_client.models import (
    AssistantPayloadConfig as OpenGPTSAssistantPayloadConfig,
)
from open_gpts_api_client.models.http_validation_error import HTTPValidationError
from open_gpts_api_client.types import Response
from openai.types.beta.assistant import Assistant
from pydantic import BaseModel

logger = logging.getLogger(__name__)

assistant_id = os.environ.get("OPEN_GPTS_ASSISTANT_ID")
litellm_proxy_url = "http://litellm-proxy.litellm-proxy.svc.cluster.local:4000"
open_gpts_url = "http://open-gpts-backend.open-gpts.svc.cluster.local:8000"
open_gpts_user_id = os.environ.get("OPEN_GPTS_USER_ID")
thread_id = os.environ.get("OPEN_GPTS_THREAD_ID")


class CreateAssistantsRequestModel(BaseModel):
    model: str
    instructions: str = None
    name: str = None
    tools: List[dict] = None


# async def create_assistant(assistant_create_params: AssistantCreateParams):
async def create_assistant(
    assistant_create_params: CreateAssistantsRequestModel,
) -> Assistant:
    client: OpenGPTSAuthenticatedClient | OpenGPTSClient = OpenGPTSClient(
        base_url=open_gpts_url,
        cookies={"opengpts_user_id": open_gpts_user_id},
    )

    model = assistant_create_params.model
    instructions = assistant_create_params.instructions
    name = assistant_create_params.name
    tools = assistant_create_params.tools

    # logger.info("Creating assistant")
    # logger.warn("Creating assistant")
    # logger.warn("assistant_create_params: %s", assistant_create_params)

    logger.warn("model: %s", model)
    logger.warn("instructions: %s", instructions)
    logger.warn("name: %s", name)
    logger.warn("tools: %s", tools)

    #   'config': {'configurable': {'type': 'agent',
    #                           'type==agent/agent_type': 'GPT 4o',
    #                           'type==agent/interrupt_before_action': False,
    #                           'type==agent/retrieval_description': 'Can be '
    #                                                                'used to '
    #                                                                'look up '
    #                                                                'information '
    #                                                                'that was '
    #                                                                'uploaded '
    #                                                                'to this '
    #                                                                'assistant.\n'
    #                                                                'If the '
    #                                                                'user is '
    #                                                                'referencing '
    #                                                                'particular '
    #                                                                'files, '
    #                                                                'that is '
    #                                                                'often a '
    #                                                                'good hint '
    #                                                                'that '
    #                                                                'information '
    #                                                                'may be '
    #                                                                'here.\n'
    #                                                                'If the '
    #                                                                'user asks '
    #                                                                'a vague '
    #                                                                'question, '
    #                                                                'they are '
    #                                                                'likely '
    #                                                                'meaning to '
    #                                                                'look up '
    #                                                                'info from '
    #                                                                'this '
    #                                                                'retriever, '
    #                                                                'and you '
    #                                                                'should '
    #                                                                'call it!',
    #                           'type==agent/system_message': 'You are a helpful '
    #                                                         'assistant that is '
    #                                                         'an expert in '
    #                                                         'making sure '
    #                                                         'proposals satisfy '
    #                                                         'the requirements '
    #                                                         'of an RFP. You '
    #                                                         'have the RFP in '
    #                                                         'your knowledge '
    #                                                         'base and will be '
    #                                                         'provided with a '
    #                                                         'draft proposal.',
    #                           'type==agent/tools': [{'config': {},
    #                                                  'description': 'Look up '
    #                                                                 'information '
    #                                                                 'in '
    #                                                                 'uploaded '
    #                                                                 'files.',
    #                                                  'id': 'retrieval',
    #                                                  'name': 'Retrieval',
    #                                                  'type': 'retrieval'}],
    #                           'type==chat_retrieval/llm_type': 'GPT 3.5 Turbo',
    #                           'type==chat_retrieval/system_message': 'You are '
    #                                                                  'a '
    #                                                                  'helpful '
    #                                                                  'assistant.',
    #                           'type==chatbot/llm_type': 'GPT 3.5 Turbo',
    #                           'type==chatbot/system_message': 'You are a '
    #                                                           'helpful '
    #                                                           'assistant.'}},

    open_gpts_assistant_tools = convert_openai_tools_to_open_gpts_tools(tools)

    config = {
        "configurable": {
            "type": "agent",
            "type==agent/agent_type": model,
            "type==agent/interrupt_before_action": False,
            "type==agent/retrieval_description": "Can be used to look up information that was uploaded to this assistant.\nIf the user is referencing particular files, that is often a good hint that information may be here.\nIf the user asks a vague question, they are likely meaning to look up info from this retriever, and you should call it!",  # noqa E501
            "type==agent/system_message": instructions,
            # "type==agent/tools": tools,
            "type==agent/tools": open_gpts_assistant_tools,
            "type==chat_retrieval/llm_type": "GPT 3.5 Turbo",
            "type==chat_retrieval/system_message": "You are a helpful assistant.",
            "type==chatbot/llm_type": "GPT 3.5 Turbo",
            "type==chatbot/system_message": "You are a helpful assistant.",
        }
    }

    config = OpenGPTSAssistantPayloadConfig.from_dict(config)

    async with client as client:
        assistant_payload: OpenGPTSAssistantPayload = OpenGPTSAssistantPayload(
            config=OpenGPTSAssistantPayloadConfig(
                # name="Assistant",
                # description="Assistant",
                # is_public=False,
            ),
            # name="Assistant",
            name=name,
            public=False,
        )

        response: Coroutine[
            Any, Any, Response[OpenGPTSAssistant | HTTPValidationError]
        ] = await create_assistant_assistants_post.asyncio_detailed(  # noqa E501
            body=assistant_payload,
            client=client,
        )

        json_response = json.loads(response.content)

        logger.warning(pprint.pformat(json_response))

        open_gpts_assistant: OpenGPTSAssistant = OpenGPTSAssistant(**json_response)

        return Assistant(
            id=open_gpts_assistant.assistant_id,
            object="assistant",
            created_at=int(
                datetime.datetime.strptime(
                    open_gpts_assistant.updated_at, "%Y-%m-%dT%H:%M:%S.%f%z"
                ).timestamp()
            ),  # noqa E501
            name=open_gpts_assistant.name,
            # description=open_gpts_assistant.description,
            # model=open_gpts_assistant.config["configurable"]['type==agent/agent_type'], # noqa E501
            model=open_gpts_assistant.config.get("configurable", {}).get(
                "type==agent/agent_type", "Unknown"
            ),  # noqa E501
            # instructions=open_gpts_assistant.config["configurable"]['type==agent/system_message'], # noqa E501
            instructions=open_gpts_assistant.config.get("configurable", {}).get(
                "type==agent/system_message", None
            ),  # noqa E501
            tools=convert_open_gpts_tools_to_openai_tools(open_gpts_assistant),
        )
    #     # return {
    #     #     "data": json.loads(response.content),
    #     #     "status": response.status_code,
    #     #     # "content": json.loads(response.content),
    #     #     # "headers": response.headers,
    #     # }


class ListAssistantsResponseModel(BaseModel):
    object: str = "list"
    data: List[Assistant]
    first_id: str
    last_id: str
    has_more: bool = False


# async def list_assistants() -> AsyncPaginator[Assistant, AsyncCursorPage[Assistant]]:
async def list_assistants(
    limit: int = 20,
    order: str = "desc",
    after: str = None,
    before: str = None,
) -> ListAssistantsResponseModel:
    client: OpenGPTSAuthenticatedClient | OpenGPTSClient = OpenGPTSClient(
        base_url=open_gpts_url,
        cookies={"opengpts_user_id": open_gpts_user_id},
    )

    async with client as client:
        response: Coroutine[
            Any, Any, Response[List[OpenGPTSAssistant]]
        ] = await list_assistants_assistants_get.asyncio_detailed(  # noqa E501
            client=client,
        )

        # return {
        #     "data": json.loads(response.content),
        #     "status": response.status_code,
        #     # "content": json.loads(response.content),
        #     # "headers": response.headers,
        # }

        # Convert the response to an AsyncPaginator
        # return AsyncPaginator(
        # )

        # {
        #     "object": "list",
        #     "data": [
        #         {
        #             "id": "asst_abc123",
        #             "object": "assistant",
        #             "created_at": 1698982736,
        #             "name": "Coding Tutor",
        #             "description": null,
        #             "model": "gpt-4-turbo",
        #             "instructions": "You are a helpful assistant designed to make me better at coding!", # noqa E501
        #             "tools": [],
        #             "tool_resources": {},
        #             "metadata": {},
        #             "top_p": 1.0,
        #             "temperature": 1.0,
        #             "response_format": "auto"
        #         },
        #     ],
        #     "first_id": "asst_abc123",
        #     "last_id": "asst_abc789",
        #     "has_more": false,
        # }

        # return AsyncPaginator(
        # client=client,
        # options={},
        # page_cls=None,
        # model=None,
        # )

        # logger.warn("response: %s", response.content)

        json_response = json.loads(response.content)

        logger.warning(pprint.pformat(json_response))

        open_gpts_assistants: List[OpenGPTSAssistant] = [
            OpenGPTSAssistant(**open_gpts_assistant)
            for open_gpts_assistant in json_response  # noqa E501
        ]
        assistants: List[Assistant] = [
            Assistant(
                id=open_gpts_assistant.assistant_id,
                object="assistant",
                # created_at=open_gpts_assistant.updated_at,
                # created_at needs to be to an integer
                # created_at=open_gpts_assistant.updated_at.timestamp(),
                # created_at=0,
                # format looks like 2024-06-04T16:21:15.590609+00:00
                created_at=int(
                    datetime.datetime.strptime(
                        open_gpts_assistant.updated_at, "%Y-%m-%dT%H:%M:%S.%f%z"
                    ).timestamp()
                ),  # noqa E501
                name=open_gpts_assistant.name,
                # description=open_gpts_assistant.description,
                # model=open_gpts_assistant.config["configurable"]['type==agent/agent_type'], # noqa E501
                model=open_gpts_assistant.config.get("configurable", {}).get(
                    "type==agent/agent_type", "Unknown"
                ),  # noqa E501
                # instructions=open_gpts_assistant.config["configurable"]['type==agent/system_message'], # noqa E501
                instructions=open_gpts_assistant.config.get("configurable", {}).get(
                    "type==agent/system_message", None
                ),  # noqa E501
                tools=convert_open_gpts_tools_to_openai_tools(open_gpts_assistant),
                # tool_resources=open_gpts_assistant.tool_resources,
            )
            for open_gpts_assistant in open_gpts_assistants
        ]

        return ListAssistantsResponseModel(
            object="list",
            data=assistants,
            first_id=assistants[0].id,
            last_id=assistants[-1].id,
            has_more=False,
        )


def convert_open_gpts_tools_to_openai_tools(open_gpts_assistant):
    # open_gpts_assistant_tools = open_gpts_assistant.config["configurable"]["type==agent/tools"] # noqa E501
    open_gpts_assistant_tools = open_gpts_assistant.config.get("configurable", {}).get(
        "type==agent/tools", []
    )  # noqa E501

    return [
        {
            # "type": "function", # could be "function", "code_interpreter", or "file_search", # noqa E501
            # "function": {
            #     "description": open_gpts_tool["description"],
            #     "name": open_gpts_tool["name"],
            #     "parameters": open_gpts_tool["parameters"],
            # }
            "type": "file_search"
            if open_gpts_tool["type"] == "retrieval"
            else NotImplementedError(
                f"Unsupported tool type: {open_gpts_tool['type']}"
            ),  # noqa E501
            # "file_search": {
            #     "max_num_results":
            # }
        }
        for open_gpts_tool in open_gpts_assistant_tools
    ]


def convert_openai_tools_to_open_gpts_tools(tools):
    return [
        {
            "config": {},
            "description": "Look up information in uploaded files.",
            "id": "retrieval",
            "name": "Retrieval",
            "type": "retrieval",
        }
    ]


def add_api_routes(app: rx.App):
    logger.debug("debug message")
    logger.info("info message")
    logger.warning("warn message")
    logger.error("error message")
    logger.critical("critical message")

    app.api.add_api_route(
        "/api/v1/assistants",
        # dependencies=[Depends(user_api_key_auth)],
        endpoint=list_assistants,
        methods=["GET"],
        # response_model=AsyncPaginator[Assistant, AsyncCursorPage[Assistant]],
        response_model=ListAssistantsResponseModel,
        tags=["assistants"],
    )

    app.api.add_api_route(
        "/api/v1/assistants",
        endpoint=create_assistant,
        methods=["POST"],
        response_model=Assistant,
        tags=["assistants"],
    )

    return app
