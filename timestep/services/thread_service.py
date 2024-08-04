import time
import uuid
from typing import List, Optional

from openai.types.beta.thread import Thread
from openai.types.beta.threads.message import Message, MessageContent
from openai.types.beta.threads.text import Text
from openai.types.beta.threads.text_content_block import TextContentBlock
from openai.types.model import Model
from sqlmodel import Field, Session, SQLModel, select

from timestep.config import Settings
from timestep.database import MessageSQLModel, ThreadSQLModel, engine


async def insert_thread(*args, **kwargs):
    thread = ThreadSQLModel()

    with Session(engine) as session:

        session.add(thread)
        session.commit()
        session.refresh(thread)

    return thread


async def insert_message(*args, **kwargs):
    print("=== insert_message ===")
    print("args: ", args)
    print("kwargs: ", kwargs)

    attachments = kwargs.get("attachments", [])

    body_content = kwargs.get("body", {}).get("content")
    # content: List[MessageContent] = []
    content: List[dict] = []

    if body_content:
        content.append(
            # TextContentBlock(
            dict(
                # text=Text(
                text=dict(
                    annotations=[],
                    value=(
                        body_content
                        if type(body_content) == str
                        else body_content[0].get("text")
                    ),
                ),
                type="text",
            )
        )

    message = MessageSQLModel(
        attachments=attachments,
        content=content,
        role=kwargs.get("body", {}).get("role"),
        status="incomplete",
        thread_id=uuid.UUID(kwargs.get("thread_id")),
    )

    with Session(engine) as session:

        session.add(message)
        session.commit()
        session.refresh(message)

    return message


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

    print("=== create_thread_message ===")
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
    messages: List[Message] = []

    with Session(engine) as session:
        if after:
            after_message = session.exec(
                select(MessageSQLModel).where(MessageSQLModel.id == uuid.UUID(after))
            ).first()

        after_created_at = after_message.created_at if after else 0

        before_created_at = (
            session.exec(
                select(MessageSQLModel).where(MessageSQLModel.id == uuid.UUID(before))
            )
            .first()
            .created_at
            if before
            else int(time.time())
        )

        statement = (
            select(MessageSQLModel)
            .where(
                MessageSQLModel.thread_id == uuid.UUID(thread_id),
                MessageSQLModel.created_at > after_created_at,
                MessageSQLModel.created_at < before_created_at,
            )
            .order_by(
                MessageSQLModel.created_at.desc()
                if order == "desc"
                else MessageSQLModel.created_at.asc()
            )
            .limit(limit)
        )

        results = session.exec(statement)
        messages = results.all()

    return messages


async def mutate_thread(*args, **kwargs):
    raise NotImplementedError


async def query_thread(*args, **kwargs):
    raise NotImplementedError
