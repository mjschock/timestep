import asyncio
import json
import time
import uuid
from typing import List, Optional

from openai.pagination import AsyncCursorPage
from openai.types.beta.assistant import Assistant
from openai.types.beta.assistant_deleted import AssistantDeleted
from openai.types.beta.assistant_update_params import AssistantUpdateParams
from openai.types.beta.thread import Thread
from openai.types.beta.threads.message import Attachment, Message, MessageContent
from openai.types.beta.threads.run import Run
from openai.types.beta.threads.text import Text
from openai.types.beta.threads.text_content_block import TextContentBlock
from prefect.client.orchestration import get_client
from prefect.deployments import run_deployment
from prefect.deployments.flow_runs import FlowRun
from prefect.flow_runs import wait_for_flow_run
from sse_starlette import EventSourceResponse

from timestep.services import agent_service, run_service, thread_service

# class StateType(AutoEnum):
#     """Enumeration of state types."""

#     SCHEDULED = AutoEnum.auto()
#     PENDING = AutoEnum.auto()
#     RUNNING = AutoEnum.auto()
#     COMPLETED = AutoEnum.auto()
#     FAILED = AutoEnum.auto()
#     CANCELLED = AutoEnum.auto()
#     CRASHED = AutoEnum.auto()
#     PAUSED = AutoEnum.auto()
#     CANCELLING = AutoEnum.auto()

# RunStatus = Literal[
#     "queued",
#     "in_progress",
#     "requires_action",
#     "cancelling",
#     "cancelled",
#     "failed",
#     "completed",
#     "incomplete",
#     "expired",
# ]

state_type_to_run_status = {
    "SCHEDULED": "queued",
    "PENDING": "queued",
    "RUNNING": "in_progress",
    "COMPLETED": "completed",
    "FAILED": "failed",
    "CANCELLED": "cancelled",
    "CRASHED": "failed",
    "PAUSED": "incomplete",
    "CANCELLING": "cancelling",
}

# from timestep.worker import step

# TODO: I see this OpenAI-Beta header in the openai spec, e.g.:
# curl https://api.openai.com/v1/assistants/asst_abc123 \
# -H "Content-Type: application/json" \
# -H "Authorization: Bearer $OPENAI_API_KEY" \
# -H "OpenAI-Beta: assistants=v2" \
# -d '{
#     "instructions": "You are an HR bot, and you have access to files to answer employee questions about company policies. Always response with info from either of the files.",
#     "tools": [{"type": "file_search"}],
#     "model": "gpt-4-turbo"
#     }'
# do I need to handle this in the API?


async def cancel_run(*args, **kwargs):
    """Cancels a run that is &#x60;in_progress&#x60;.

    :param thread_id: The ID of the thread to which this run belongs.
    :type thread_id: str
    :param run_id: The ID of the run to cancel.
    :type run_id: str

    :rtype: Union[RunObject, Tuple[RunObject, int], Tuple[RunObject, int, Dict[str, str]]
    """
    print("=== cancel_run ===")
    print("args: ", args)
    print("kwargs: ", kwargs)

    return await run_service.cancel_run(*args, **kwargs)


# def create_assistant(create_assistant_request):  # noqa: E501
async def create_assistant(body, token_info: dict, user: str):
    """Create an assistant with a model and instructions.

     # noqa: E501

    :param create_assistant_request:
    :type create_assistant_request: dict | bytes

    :rtype: Union[AssistantObject, Tuple[AssistantObject, int], Tuple[AssistantObject, int, Dict[str, str]]
    """
    agent = await agent_service.insert_agent(
        body=body,
    )

    assistant = Assistant(
        id=str(agent.id),
        created_at=agent.created_at.timestamp(),
        description=body.get("description"),
        instructions=body.get("instructions"),
        model=body.get("model"),
        name=body.get("name"),
        object="assistant",
        tools=body.get("tools", []),
    )

    print("assistant: ", assistant)

    return assistant.model_dump(mode="json")


# def create_message(thread_id, create_message_request):  # noqa: E501
async def create_message(body, token_info, thread_id, user):
    """Create a message.

     # noqa: E501

    :param thread_id: The ID of the [thread](/docs/api-reference/threads) to create a message for.
    :type thread_id: str
    :param create_message_request:
    :type create_message_request: dict | bytes

    :rtype: Union[MessageObject, Tuple[MessageObject, int], Tuple[MessageObject, int, Dict[str, str]]
    """
    message = await thread_service.insert_message(
        body=body,
        token_info=token_info,
        thread_id=thread_id,
        user=user,
    )

    message = Message(
        id=str(message.id),
        attachments=[Attachment(**attachment) for attachment in message.attachments],
        content=[
            TextContentBlock(**content) for content in message.content
        ],  # TODO: handle other content types
        created_at=message.created_at.timestamp(),
        object="thread.message",
        role=message.role,
        status=message.status,
        thread_id=str(message.thread_id),
    )

    return message.model_dump(mode="json")


async def create_run(body, token_info, thread_id, user):
    """Create a run.

     # noqa: E501

    :param thread_id: The ID of the thread to run.
    :type thread_id: str
    :param create_run_request:
    :type create_run_request: dict | bytes

    :rtype: Union[RunObject, Tuple[RunObject, int], Tuple[RunObject, int, Dict[str, str]]
    """
    stream = body.get("stream", False)
    assistant_id = body.get("assistant_id")

    flow_run: FlowRun = await run_deployment(
        # idempotency_key=run.id,
        name="agent-flow/agent-flow-deployment",
        parameters={
            "inputs": {
                "agent_id": assistant_id,
                "thread_id": thread_id,
            }
        },
        # job_variables={"env": {"MY_ENV_VAR": "staging"}},
        timeout=0,  # don't wait for the run to finish
    )

    print("flow_run: ", flow_run)

    if stream:
        raise NotImplementedError

        # async def run_event_publisher():
        #     wait_for_flow_run(flow_run.id)

        #     try:
        #         # for chunk in response:
        #         # # async for chunk in response:
        #         #     chunk = ChatCompletionChunk(**chunk)
        #         #     # yield json.dumps(chunk)
        #         #     yield json.dumps(chunk.model_dump(mode="json"))
        #         #     # yield ChatCompletionChunk(**chunk).model_dump(mode="json")
        #         #     # yield chunk.model_dump(mode="json")

        #     except asyncio.CancelledError as e:
        #         # print(f"Disconnected from client (via refresh/close) {req.client}")
        #         print(f"Disconnected from client (via refresh/close)")
        #         # Do any other cleanup, if any
        #         raise e

        # # print(f'=== RETURN: {__name__}.create_chat_completion(body: CompletionCreateParams, token_info: dict, user: str)) ===')
        # return EventSourceResponse(run_event_publisher())

    else:
        agent = await agent_service.get_agent(id=assistant_id)

        run = Run(
            id=str(flow_run.id),
            assistant_id=str(agent.id),
            created_at=int(flow_run.created.timestamp()),
            instructions=agent.instructions,
            model=agent.model,
            object="thread.run",
            parallel_tool_calls=False,
            status="queued",
            thread_id=thread_id,
            tools=agent.tools,
        )

        return run.model_dump(mode="json")


async def create_thread(body, token_info, user):
    """Create a thread.

     # noqa: E501

    :param create_thread_request:
    :type create_thread_request: dict | bytes

    :rtype: Union[ThreadObject, Tuple[ThreadObject, int], Tuple[ThreadObject, int, Dict[str, str]]
    """
    thread = await thread_service.insert_thread(body, token_info, user)

    thread = Thread(
        id=str(thread.id),
        created_at=int(time.time()),
        object="thread",
        # tool_resources
    )

    return thread.model_dump(mode="json")


# def create_thread_and_run(create_thread_and_run_request):  # noqa: E501
async def create_thread_and_run(*args, **kwargs):
    """Create a thread and run it in one request.

     # noqa: E501

    :param create_thread_and_run_request:
    :type create_thread_and_run_request: dict | bytes

    :rtype: Union[RunObject, Tuple[RunObject, int], Tuple[RunObject, int, Dict[str, str]]
    """
    # if connexion.request.is_json:
    #     create_thread_and_run_request = CreateThreadAndRunRequest.from_dict(connexion.request.get_json())  # noqa: E501

    print("=== create_thread_and_run ===")
    print("args: ", args)
    print("kwargs: ", kwargs)

    # thread = client.beta.threads.create()
    # run = submit_message(MATH_ASSISTANT_ID, thread, user_input)
    # return thread, run

    raise NotImplementedError


# def delete_assistant(assistant_id):  # noqa: E501
async def delete_assistant(assistant_id: str, token_info: dict, user: str):
    """Delete an assistant.

     # noqa: E501

    :param assistant_id: The ID of the assistant to delete.
    :type assistant_id: str

    :rtype: Union[DeleteAssistantResponse, Tuple[DeleteAssistantResponse, int], Tuple[DeleteAssistantResponse, int, Dict[str, str]]
    """
    agent = await agent_service.delete_agent(id=assistant_id)

    return AssistantDeleted(
        id=str(agent.id),
        deleted=True,
        object="assistant.deleted",
    ).model_dump(mode="json")


# def delete_message(thread_id, message_id):  # noqa: E501
async def delete_message(*args, **kwargs):
    """Deletes a message.

     # noqa: E501

    :param thread_id: The ID of the thread to which this message belongs.
    :type thread_id: str
    :param message_id: The ID of the message to delete.
    :type message_id: str

    :rtype: Union[DeleteMessageResponse, Tuple[DeleteMessageResponse, int], Tuple[DeleteMessageResponse, int, Dict[str, str]]
    """
    print("=== delete_message ===")
    print("args: ", args)
    print("kwargs: ", kwargs)

    raise NotImplementedError


# def delete_thread(thread_id):  # noqa: E501
async def delete_thread(*args, **kwargs):
    """Delete a thread.

     # noqa: E501

    :param thread_id: The ID of the thread to delete.
    :type thread_id: str

    :rtype: Union[DeleteThreadResponse, Tuple[DeleteThreadResponse, int], Tuple[DeleteThreadResponse, int, Dict[str, str]]
    """
    print("=== delete_thread ===")
    print("args: ", args)
    print("kwargs: ", kwargs)

    raise NotImplementedError


# def get_assistant(assistant_id):  # noqa: E501
async def get_assistant(assistant_id, token_info, user):
    """Retrieves an assistant.

     # noqa: E501

    :param assistant_id: The ID of the assistant to retrieve.
    :type assistant_id: str

    :rtype: Union[AssistantObject, Tuple[AssistantObject, int], Tuple[AssistantObject, int, Dict[str, str]]
    """
    agent = await agent_service.get_agent(id=assistant_id)

    assistant = Assistant(
        id=str(agent.id),
        created_at=agent.created_at.timestamp(),
        instructions=agent.instructions,
        model=agent.model,
        name=agent.name,
        object="assistant",
        tools=agent.tools,
    )

    print("assistant: ", assistant)

    return assistant.model_dump(mode="json")


# def get_message(thread_id, message_id):  # noqa: E501
async def get_message(*args, **kwargs):
    """Retrieve a message.

     # noqa: E501

    :param thread_id: The ID of the [thread](/docs/api-reference/threads) to which this message belongs.
    :type thread_id: str
    :param message_id: The ID of the message to retrieve.
    :type message_id: str

    :rtype: Union[MessageObject, Tuple[MessageObject, int], Tuple[MessageObject, int, Dict[str, str]]
    """
    print("=== get_message ===")
    print("args: ", args)
    print("kwargs: ", kwargs)

    raise NotImplementedError


# def get_run(thread_id, run_id):  # noqa: E501
async def get_run(run_id, thread_id, token_info, user):
    """Retrieves a run.

     # noqa: E501

    :param thread_id: The ID of the [thread](/docs/api-reference/threads) that was run.
    :type thread_id: str
    :param run_id: The ID of the run to retrieve.
    :type run_id: str

    :rtype: Union[RunObject, Tuple[RunObject, int], Tuple[RunObject, int, Dict[str, str]]
    """
    client = get_client()
    flow_run: FlowRun = await client.read_flow_run(flow_run_id=uuid.UUID(run_id))
    assistant_id = flow_run.parameters["inputs"]["agent_id"]

    agent = await agent_service.get_agent(id=assistant_id)

    run = Run(
        id=str(flow_run.id),
        assistant_id=str(agent.id),
        created_at=int(flow_run.created.timestamp()),
        instructions=agent.instructions,
        model=agent.model,
        object="thread.run",
        parallel_tool_calls=False,
        status=state_type_to_run_status[flow_run.state.type],
        thread_id=thread_id,
        tools=agent.tools,
    )

    return run.model_dump(mode="json")


# def get_run_step(thread_id, run_id, step_id):  # noqa: E501
async def get_run_step(*args, **kwargs):
    """Retrieves a run step.

     # noqa: E501

    :param thread_id: The ID of the thread to which the run and run step belongs.
    :type thread_id: str
    :param run_id: The ID of the run to which the run step belongs.
    :type run_id: str
    :param step_id: The ID of the run step to retrieve.
    :type step_id: str

    :rtype: Union[RunStepObject, Tuple[RunStepObject, int], Tuple[RunStepObject, int, Dict[str, str]]
    """
    print("=== get_run_step ===")
    print("args: ", args)
    print("kwargs: ", kwargs)

    raise NotImplementedError


# def get_thread(thread_id):  # noqa: E501
async def get_thread(token_info, thread_id, user):
    """Retrieves a thread.

     # noqa: E501

    :param thread_id: The ID of the thread to retrieve.
    :type thread_id: str

    :rtype: Union[ThreadObject, Tuple[ThreadObject, int], Tuple[ThreadObject, int, Dict[str, str]]
    """
    print("=== get_thread ===")
    raise NotImplementedError


# def list_assistants(limit=None, order=None, after=None, before=None):  # noqa: E501
async def list_assistants(*args, **kwargs):
    """Returns a list of assistants.

     # noqa: E501

    :param limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.
    :type limit: int
    :param order: Sort order by the &#x60;created_at&#x60; timestamp of the objects. &#x60;asc&#x60; for ascending order and &#x60;desc&#x60; for descending order.
    :type order: str
    :param after: A cursor for use in pagination. &#x60;after&#x60; is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after&#x3D;obj_foo in order to fetch the next page of the list.
    :type after: str
    :param before: A cursor for use in pagination. &#x60;before&#x60; is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include before&#x3D;obj_foo in order to fetch the previous page of the list.
    :type before: str

    :rtype: Union[ListAssistantsResponse, Tuple[ListAssistantsResponse, int], Tuple[ListAssistantsResponse, int, Dict[str, str]]
    """
    print("=== list_assistants ===")
    print("args: ", args)
    print("kwargs: ", kwargs)

    raise NotImplementedError


# def list_messages(thread_id, limit=None, order=None, after=None, before=None, run_id=None):  # noqa: E501
async def list_messages(
    token_info: dict,
    thread_id: str,
    user: str,
    after: Optional[str] = None,
    before: Optional[str] = None,
    limit: int = 20,
    order: str = "desc",
):
    """Returns a list of messages for a given thread.

     # noqa: E501

    :param thread_id: The ID of the [thread](/docs/api-reference/threads) the messages belong to.
    :type thread_id: str
    :param limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.
    :type limit: int
    :param order: Sort order by the &#x60;created_at&#x60; timestamp of the objects. &#x60;asc&#x60; for ascending order and &#x60;desc&#x60; for descending order.
    :type order: str
    :param after: A cursor for use in pagination. &#x60;after&#x60; is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after&#x3D;obj_foo in order to fetch the next page of the list.
    :type after: str
    :param before: A cursor for use in pagination. &#x60;before&#x60; is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include before&#x3D;obj_foo in order to fetch the previous page of the list.
    :type before: str
    :param run_id: Filter messages by the run ID that generated them.
    :type run_id: str

    :rtype: Union[ListMessagesResponse, Tuple[ListMessagesResponse, int], Tuple[ListMessagesResponse, int, Dict[str, str]]
    """
    messages = await thread_service.get_thread_messages(
        token_info=token_info,
        thread_id=thread_id,
        user=user,
        after=after,
        before=before,
        limit=limit,
        order=order,
    )

    # TODO: handle AsyncCursoPage as well
    return AsyncCursorPage(
        # return SyncCursorPage(
        data=messages,
    ).model_dump(mode="json")


# def list_run_steps(thread_id, run_id, limit=None, order=None, after=None, before=None):  # noqa: E501
async def list_run_steps(*args, **kwargs):
    """Returns a list of run steps belonging to a run.

     # noqa: E501

    :param thread_id: The ID of the thread the run and run steps belong to.
    :type thread_id: str
    :param run_id: The ID of the run the run steps belong to.
    :type run_id: str
    :param limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.
    :type limit: int
    :param order: Sort order by the &#x60;created_at&#x60; timestamp of the objects. &#x60;asc&#x60; for ascending order and &#x60;desc&#x60; for descending order.
    :type order: str
    :param after: A cursor for use in pagination. &#x60;after&#x60; is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after&#x3D;obj_foo in order to fetch the next page of the list.
    :type after: str
    :param before: A cursor for use in pagination. &#x60;before&#x60; is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include before&#x3D;obj_foo in order to fetch the previous page of the list.
    :type before: str

    :rtype: Union[ListRunStepsResponse, Tuple[ListRunStepsResponse, int], Tuple[ListRunStepsResponse, int, Dict[str, str]]
    """
    print("=== list_run_steps ===")
    print("args: ", args)
    print("kwargs: ", kwargs)

    raise NotImplementedError


# def list_runs(thread_id, limit=None, order=None, after=None, before=None):  # noqa: E501
async def list_runs(*args, **kwargs):
    """Returns a list of runs belonging to a thread.

     # noqa: E501

    :param thread_id: The ID of the thread the run belongs to.
    :type thread_id: str
    :param limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.
    :type limit: int
    :param order: Sort order by the &#x60;created_at&#x60; timestamp of the objects. &#x60;asc&#x60; for ascending order and &#x60;desc&#x60; for descending order.
    :type order: str
    :param after: A cursor for use in pagination. &#x60;after&#x60; is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after&#x3D;obj_foo in order to fetch the next page of the list.
    :type after: str
    :param before: A cursor for use in pagination. &#x60;before&#x60; is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include before&#x3D;obj_foo in order to fetch the previous page of the list.
    :type before: str

    :rtype: Union[ListRunsResponse, Tuple[ListRunsResponse, int], Tuple[ListRunsResponse, int, Dict[str, str]]
    """
    print("=== list_runs ===")
    print("args: ", args)
    print("kwargs: ", kwargs)

    raise NotImplementedError


# def modify_assistant(assistant_id, modify_assistant_request):  # noqa: E501
async def modify_assistant(
    assistant_id: str, body: AssistantUpdateParams, token_info, user
):
    """Modifies an assistant.

     # noqa: E501

    :param assistant_id: The ID of the assistant to modify.
    :type assistant_id: str
    :param modify_assistant_request:
    :type modify_assistant_request: dict | bytes

    :rtype: Union[AssistantObject, Tuple[AssistantObject, int], Tuple[AssistantObject, int, Dict[str, str]]
    """
    agent = await agent_service.update_agent(
        id=assistant_id,
        body=body,
    )

    assistant = Assistant(
        id=str(agent.id),
        created_at=agent.created_at.timestamp(),
        # description=agent.description,
        instructions=agent.instructions,
        model=agent.model,
        name=agent.name,
        object="assistant",
        tools=agent.tools,
    )

    return assistant.model_dump(mode="json")


# def modify_message(thread_id, message_id, modify_message_request):  # noqa: E501
async def modify_message(*args, **kwargs):
    """Modifies a message.

     # noqa: E501

    :param thread_id: The ID of the thread to which this message belongs.
    :type thread_id: str
    :param message_id: The ID of the message to modify.
    :type message_id: str
    :param modify_message_request:
    :type modify_message_request: dict | bytes

    :rtype: Union[MessageObject, Tuple[MessageObject, int], Tuple[MessageObject, int, Dict[str, str]]
    """
    # if connexion.request.is_json:
    #     modify_message_request = ModifyMessageRequest.from_dict(connexion.request.get_json())  # noqa: E501

    print("=== modify_message ===")
    print("args: ", args)
    print("kwargs: ", kwargs)

    raise NotImplementedError


# def modify_run(thread_id, run_id, modify_run_request):  # noqa: E501
async def modify_run(modify_run_request, run_id, token_info, thread_id, user, **kwargs):
    """Modifies a run.

     # noqa: E501

    :param thread_id: The ID of the [thread](/docs/api-reference/threads) that was run.
    :type thread_id: str
    :param run_id: The ID of the run to modify.
    :type run_id: str
    :param modify_run_request:
    :type modify_run_request: dict | bytes

    :rtype: Union[RunObject, Tuple[RunObject, int], Tuple[RunObject, int, Dict[str, str]]
    """
    print("=== modify_run ===")
    raise NotImplementedError


async def modify_thread(*args, **kwargs):
    """Modifies a thread.

     # noqa: E501

    :param thread_id: The ID of the thread to modify. Only the &#x60;metadata&#x60; can be modified.
    :type thread_id: str
    :param modify_thread_request:
    :type modify_thread_request: dict | bytes

    :rtype: Union[ThreadObject, Tuple[ThreadObject, int], Tuple[ThreadObject, int, Dict[str, str]]
    """
    # if connexion.request.is_json:
    #     modify_thread_request = ModifyThreadRequest.from_dict(connexion.request.get_json())  # noqa: E501

    print("=== modify_thread ===")
    print("args: ", args)
    print("kwargs: ", kwargs)

    raise NotImplementedError


async def submit_tool_ouputs_to_run(
    *args, **kwargs
):  # NOTE: the typo in outputs is b/c the auto-generated openai-openapi spec has that typo
    """When a run has the &#x60;status: \&quot;requires_action\&quot;&#x60; and &#x60;required_action.type&#x60; is &#x60;submit_tool_outputs&#x60;, this endpoint can be used to submit the outputs from the tool calls once they&#39;re all completed. All outputs must be submitted in a single request.

    :param thread_id: The ID of the [thread](/docs/api-reference/threads) to which this run belongs.
    :type thread_id: str
    :param run_id: The ID of the run that requires the tool output submission.
    :type run_id: str
    :param submit_tool_outputs_run_request:
    :type submit_tool_outputs_run_request: dict | bytes

    :rtype: Union[RunObject, Tuple[RunObject, int], Tuple[RunObject, int, Dict[str, str]]
    """
    # if connexion.request.is_json:
    #     submit_tool_outputs_run_request = SubmitToolOutputsRunRequest.from_dict(connexion.request.get_json())  # noqa: E501

    print("=== submit_tool_outputs_to_run ===")
    print("args: ", args)
    print("kwargs: ", kwargs)

    raise NotImplementedError
