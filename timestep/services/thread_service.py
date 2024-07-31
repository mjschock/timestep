import time
import uuid
from typing import List, Optional

from openai.types.beta.thread import Thread
from openai.types.beta.threads.message import Message, MessageContent
from openai.types.beta.threads.text import Text
from openai.types.beta.threads.text_content_block import TextContentBlock


# def create_message(thread_id, create_message_request):  # noqa: E501
async def create_thread_message(body, token_info, thread_id, user):
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

    # return message.model_dump(mode="json")
    return message


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

    # return thread.model_dump(mode="json")
    return thread


async def get_thread_messages(
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

    # return AsyncCursorPage(
    # # return SyncCursorPage(
    #     data=messages,
    # ).model_dump(mode="json")

    return messages


async def mutate_thread(*args, **kwargs):
    raise NotImplementedError


async def query_thread(*args, **kwargs):
    raise NotImplementedError
