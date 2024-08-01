import asyncio
import json
import os
import time
import uuid
from typing import List, Optional

from openai.pagination import AsyncCursorPage
from openai.types.beta.assistant import Assistant
from openai.types.beta.assistant_deleted import AssistantDeleted
from openai.types.beta.assistant_update_params import AssistantUpdateParams
from openai.types.beta.thread import Thread
from openai.types.beta.threads.message import Message, MessageContent
from openai.types.beta.threads.run import Run
from openai.types.beta.threads.text import Text
from openai.types.beta.threads.text_content_block import TextContentBlock
from prefect.deployments import run_deployment
from prefect.deployments.flow_runs import FlowRun
from sse_starlette import EventSourceResponse

# from timestep.database import InstanceStoreSingleton
from timestep.worker import step


# def cancel_run(thread_id, run_id):  # noqa: E501
async def cancel_run(*args, **kwargs):
    """Cancels a run that is &#x60;in_progress&#x60;.

     # noqa: E501

    :param thread_id: The ID of the thread to which this run belongs.
    :type thread_id: str
    :param run_id: The ID of the run to cancel.
    :type run_id: str

    :rtype: Union[RunObject, Tuple[RunObject, int], Tuple[RunObject, int, Dict[str, str]]
    """
    print("=== cancel_run ===")
    print("args: ", args)
    print("kwargs: ", kwargs)

    raise NotImplementedError


# def create_assistant(create_assistant_request):  # noqa: E501
async def create_assistant(body, token_info: dict, user: str):
    """Create an assistant with a model and instructions.

     # noqa: E501

    :param create_assistant_request:
    :type create_assistant_request: dict | bytes

    :rtype: Union[AssistantObject, Tuple[AssistantObject, int], Tuple[AssistantObject, int, Dict[str, str]]
    """
    # if connexion.request.is_json:
    #     create_assistant_request = CreateAssistantRequest.from_dict(connexion.request.get_json())  # noqa: E501

    print("=== create_assistant ===")

    assistant = Assistant(
        id=str(uuid.uuid4()),
        created_at=int(time.time()),
        description=body.get("description"),
        instructions=body.get("instructions"),
        model=body.get("model"),
        name=body.get("name"),
        object="assistant",
        tools=body.get("tools", []),
    )

    print("assistant: ", assistant)

    instance_store = InstanceStoreSingleton()
    instance_store._shared_instance_state["assistants"][assistant.id] = assistant

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
    # if connexion.request.is_json:
    #     create_message_request = CreateMessageRequest.from_dict(connexion.request.get_json())  # noqa: E501

    print("=== create_message ===")

    # thread = instance_store._shared_instance_state["threads"][thread_id]
    thread: Thread = Thread(
        **await get_thread(token_info=token_info, thread_id=thread_id, user=user)
    )

    content: List[MessageContent] = []

    if body.get("content"):
        content.append(
            TextContentBlock(
                text=Text(
                    annotations=[],
                    value=(
                        body.get("content")
                        if type(body.get("content")) == str
                        else body.get("content")[0].get("text")
                    ),
                ),
                type="text",
            )
        )

    message = Message(
        id=str(uuid.uuid4()),
        attachments=[],
        content=content,
        created_at=int(time.time()),
        object="thread.message",
        role=body.get("role"),
        thread_id=thread.id,
        status="incomplete",
    )

    print("message: ", message)

    instance_store = InstanceStoreSingleton()
    instance_store._shared_instance_state["messages"][message.id] = message

    return message.model_dump(mode="json")


# TODO: move this somewhere more appropriate
# maybe get rid of BackgroundTask and just trigger a run deployment
# @flow(log_prints=True)
# @cf.flow
# async def run_run(run_id: str, token_info: dict, thread_id: str, user: str):
#     print('=== run_run ===')
#     run: Run = Run(**await get_run(run_id=run_id, token_info=token_info, thread_id=thread_id, user=user))
#     assistant: Assistant = Assistant(**await get_assistant(assistant_id=run.assistant_id, token_info=token_info, user=user))
#     thread: Thread = Thread(**await get_thread(token_info=token_info, thread_id=thread_id, user=user))

#     # # TODO: use ControlFlow to run_once...
#     # @cf.flow
#     # def run_run_flow():
#     #     agent = cf.Agent(
#     #         name=assistant.name,
#     #         description=assistant.description,
#     #         instructions=assistant.instructions,
#     #         # memory
#     #         # tools=,
#     #         # ...
#     #     )

#     #     task = cf.Task(
#     #         "Tell me something I don't know",
#     #         # objective=
#     #         # instructions=
#     #         agents=[agent]
#     #     )

#     #     return task

#     # result = run_run_flow()

#     # print('result: ', result)

#     # messages: List[Message] = list_messages(
#     # SyncCursorPage[Message] = await list_messages(
#     list_messages_response = await list_messages(
#         limit=-1,
#         order='asc',
#         token_info=token_info,
#         thread_id=thread_id,
#         user=user,
#     )

#     messages = list_messages_response.get("data")

#     system_message = {
#         "content": "You are a helpful assistant with access to tools. Please be honest and do not hallucinate.",
#         "role": "system",
#     }

#     messages = [system_message] + messages
#     print('messages: ', messages)

#     def get_message_content(message):
#         content = message.get("content")

#         if type(content) == list:
#             if message.get("role") == "user":
#                 return [{
#                     "text": _content.get("text").get("value"),
#                     "type": _content.get("type"),
#                 } for _content in content]

#             else:
#                 assert len(content) == 1
#                 return content[0].get("text").get("value")

#         else:
#             return content

#     body = { # CompletionCreateParamsNonStreaming
#         "messages": [ {
#             "content": get_message_content(message),
#             "role": message.get("role"),
#         } for message in messages ],
#         "model": assistant.model,
#         "tools": assistant.tools,
#     }
#     print('body: ', body)

#     chat_completion: ChatCompletion = ChatCompletion(**await create_chat_completion(body=body, token_info=token_info, user=user)) # TODO: handle streaming use case
#     print('chat_completion: ', chat_completion)

#     choice = chat_completion.choices[0]
#     print('choice: ', choice)

#     finish_reason = choice.finish_reason
#     print('finish_reason: ', finish_reason) # "stop", "length", "tool_calls", "content_filter", "function_call"

#     response_message = chat_completion.choices[0].message

#     tool_calls = response_message.tool_calls

#     if tool_calls:
#         raise NotImplementedError

#     await create_message(body={
#         "content": response_message.content,
#         "role": response_message.role,
#     }, token_info=token_info, thread_id=thread_id, user=user)

#     # time.sleep(1)  # wait for the process to finish

#     modify_run_request = {
#         "status": "completed",
#     }

#     await modify_run(modify_run_request=modify_run_request, run_id=run_id, token_info=token_info, thread_id=thread_id, user=user)

#     # run: Run = Run(**await get_run(run_id=run_id, token_info=token_info, thread_id=thread_id, user=user))

#     # return run


# def create_run(thread_id, create_run_request):  # noqa: E501
# def create_run(body, token_info, user, thread_id):
async def create_run(body, token_info, thread_id, user):
    """Create a run.

     # noqa: E501

    :param thread_id: The ID of the thread to run.
    :type thread_id: str
    :param create_run_request:
    :type create_run_request: dict | bytes

    :rtype: Union[RunObject, Tuple[RunObject, int], Tuple[RunObject, int, Dict[str, str]]
    """
    # if connexion.request.is_json:
    #     create_run_request = CreateRunRequest.from_dict(connexion.request.get_json())  # noqa: E501

    print("=== create_run ===")
    print("body: ", body)

    stream = body.get("stream", False)
    assistant_id = body.get("assistant_id")

    assistant: Assistant = Assistant(
        **await get_assistant(
            assistant_id=assistant_id, token_info=token_info, user=user
        )
    )
    thread: Thread = Thread(
        **await get_thread(token_info=token_info, thread_id=thread_id, user=user)
    )

    run = Run(
        id=str(uuid.uuid4()),
        assistant_id=assistant.id,
        created_at=int(time.time()),
        instructions=assistant.instructions,
        model=assistant.model,
        object="thread.run",
        parallel_tool_calls=False,
        status="queued",
        thread_id=thread.id,
        tools=assistant.tools,
    )

    print("run: ", run)
    run_id = run.id

    instance_store = InstanceStoreSingleton()
    instance_store._shared_instance_state["runs"][run.id] = run

    flow_run: FlowRun = await run_deployment(
        idempotency_key=run.id,
        name="agent-flow/agent-flow-deployment",
        parameters={
            "inputs": {
                "run_id": run_id,
            }
        },
        # job_variables={"env": {"MY_ENV_VAR": "staging"}},
        timeout=0,  # don't wait for the run to finish
    )

    print("flow_run: ", flow_run)

    if stream:

        async def run_event_publisher():
            run: Run = Run(
                **await get_run(
                    run_id=run_id, token_info=token_info, thread_id=thread_id, user=user
                )
            )

            # response: Iterator[CreateChatCompletionStreamResponse] = model.create_chat_completion(**create_chat_completion_kwargs)
            # response: Generator[ChatCompletionChunk] = model.create_chat_completion_openai_v1(**create_chat_completion_kwargs)
            # response: Stream[ChatCompletionChunk] = model.astream(input=messages)
            await step(
                run_id=run.id, token_info=token_info, thread_id=run.thread_id, user=user
            )

            run: Run = Run(
                **await get_run(
                    run_id=run.id, token_info=token_info, thread_id=thread_id, user=user
                )
            )

            try:
                yield json.dumps(run.model_dump(mode="json"))

                # for chunk in response:
                # # async for chunk in response:
                #     chunk = ChatCompletionChunk(**chunk)
                #     # yield json.dumps(chunk)
                #     yield json.dumps(chunk.model_dump(mode="json"))
                #     # yield ChatCompletionChunk(**chunk).model_dump(mode="json")
                #     # yield chunk.model_dump(mode="json")

            except asyncio.CancelledError as e:
                # print(f"Disconnected from client (via refresh/close) {req.client}")
                print(f"Disconnected from client (via refresh/close)")
                # Do any other cleanup, if any
                raise e

        # print(f'=== RETURN: {__name__}.create_chat_completion(body: CompletionCreateParams, token_info: dict, user: str)) ===')
        return EventSourceResponse(run_event_publisher())

    else:
        # task = BackgroundTask(step, run_id=run.id, token_info=token_info, thread_id=run.thread_id, user=user)

        # return JSONResponse(run.model_dump(mode="json"), background=task)
        return run.model_dump(mode="json")


# def create_thread(create_thread_request=None):  # noqa: E501
async def create_thread(*args, **kwargs):
    """Create a thread.

     # noqa: E501

    :param create_thread_request:
    :type create_thread_request: dict | bytes

    :rtype: Union[ThreadObject, Tuple[ThreadObject, int], Tuple[ThreadObject, int, Dict[str, str]]
    """
    # if connexion.request.is_json:
    #     create_thread_request = CreateThreadRequest.from_dict(connexion.request.get_json())  # noqa: E501

    print("=== create_thread ===")
    print("args: ", args)
    print("kwargs: ", kwargs)

    thread = Thread(
        id=str(uuid.uuid4()),
        created_at=int(time.time()),
        object="thread",
        # tool_resources
    )

    print("thread: ", thread)

    instance_store = InstanceStoreSingleton()
    instance_store._shared_instance_state["threads"][thread.id] = thread

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

    raise NotImplementedError


# def delete_assistant(assistant_id):  # noqa: E501
async def delete_assistant(assistant_id: str, token_info: dict, user: str):
    """Delete an assistant.

     # noqa: E501

    :param assistant_id: The ID of the assistant to delete.
    :type assistant_id: str

    :rtype: Union[DeleteAssistantResponse, Tuple[DeleteAssistantResponse, int], Tuple[DeleteAssistantResponse, int, Dict[str, str]]
    """
    print("=== delete_assistant ===")
    # print('args: ', args)
    # print('kwargs: ', kwargs)

    # raise NotImplementedError

    instance_store = InstanceStoreSingleton()
    del instance_store._shared_instance_state["assistants"][assistant_id]

    return AssistantDeleted(
        id=assistant_id,
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
    print("=== get_assistant ===")

    return (
        InstanceStoreSingleton()
        ._shared_instance_state["assistants"]
        .get(assistant_id)
        .model_dump(mode="json")
    )


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
    print("=== get_run ===")

    return (
        InstanceStoreSingleton()
        ._shared_instance_state["runs"]
        .get(run_id)
        .model_dump(mode="json")
    )


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
    instance_store = InstanceStoreSingleton()
    thread = instance_store._shared_instance_state["threads"][thread_id]

    return thread.model_dump(mode="json")


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
    print("=== list_messages ===")
    print("after: ", after)
    print("before: ", before)
    print("limit: ", limit)
    print("order: ", order)
    print("token_info: ", token_info)
    print("thread_id: ", thread_id)
    print("user: ", user)

    # thread: Thread = Thread(**await get_thread(token_info=token_info, thread_id=thread_id, user=user))

    after_created_at = (
        InstanceStoreSingleton()._shared_instance_state["messages"][after].created_at
        if after
        else 0
    )
    before_created_at = (
        InstanceStoreSingleton()._shared_instance_state["messages"][before].created_at
        if before
        else int(time.time())
    )
    limit = None if limit == -1 else limit

    # def message_filter(message: Message):
    #     return message.created_at > after_created_at and message.created_at < before_created_at and message.thread_id == thread_id

    # filtered_messages = list(filter(
    #     function=message_filter,
    #     iterable=InstanceStoreSingleton()._shared_instance_state["messages"].values(),
    # ))

    # filtered_messages =

    messages: List[Message] = sorted(
        [
            message
            for message in InstanceStoreSingleton()
            ._shared_instance_state["messages"]
            .values()
            if message.created_at > after_created_at
            and message.created_at < before_created_at
            and message.thread_id == thread_id
        ],
        key=lambda message: message.created_at,
        reverse=True if order == "desc" else False,
    )[0:limit]

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
    # if connexion.request.is_json:
    #     modify_assistant_request = ModifyAssistantRequest.from_dict(connexion.request.get_json())  # noqa: E501

    print("=== modify_assistant ===")
    print("assistant_id: ", assistant_id)
    print("body: ", body)

    assistant: Assistant = Assistant(
        **await get_assistant(
            assistant_id=assistant_id, token_info=token_info, user=user
        )
    )

    # assistant = Assistant(
    #     id=str(uuid.uuid4()),
    #     created_at=int(time.time()),
    #     description=body.get("description"),
    #     instructions=body.get("instructions"),
    #     model=body.get("model"),
    #     name=body.get("name"),
    #     object="assistant",
    #     tools=body.get("tools", [])
    # )

    print("assistant [before]: ", assistant)

    assistant.description = body.get("description", assistant.description)
    assistant.instructions = body.get("instructions", assistant.instructions)
    assistant.model = body.get("model", assistant.model)
    assistant.name = body.get("name", assistant.name)
    assistant.tools = body.get("tools", assistant.tools)

    print("assistant [after]: ", assistant)

    instance_store = InstanceStoreSingleton()
    instance_store._shared_instance_state["assistants"][assistant.id] = assistant

    return await get_assistant(
        assistant_id=assistant_id, token_info=token_info, user=user
    )


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
    # if connexion.request.is_json:
    #     modify_run_request = ModifyRunRequest.from_dict(connexion.request.get_json())  # noqa: E501

    print("=== modify_run ===")
    print("modify_run_request: ", modify_run_request)
    # print('args: ', args)
    print("kwargs: ", kwargs)

    run: Run = Run(
        **await get_run(
            run_id=run_id, token_info=token_info, thread_id=thread_id, user=user
        )
    )

    run.status = modify_run_request.get("status")

    InstanceStoreSingleton()._shared_instance_state["runs"][run_id] = run

    return run.model_dump(mode="json")


# def modify_thread(thread_id, modify_thread_request):  # noqa: E501
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


# def submit_tool_ouputs_to_run(thread_id, run_id, submit_tool_outputs_run_request):  # noqa: E501
async def submit_tool_outputs_to_run(*args, **kwargs):
    """When a run has the &#x60;status: \&quot;requires_action\&quot;&#x60; and &#x60;required_action.type&#x60; is &#x60;submit_tool_outputs&#x60;, this endpoint can be used to submit the outputs from the tool calls once they&#39;re all completed. All outputs must be submitted in a single request.

     # noqa: E501

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
