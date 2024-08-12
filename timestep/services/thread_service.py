import uuid
from typing import List, Optional

from openai.types.beta.threads.message import Message
from sqlalchemy import func
from sqlmodel import Session, select

from timestep.database import MessageSQLModel, ThreadSQLModel, engine


async def insert_thread(*args, **kwargs):
    thread = ThreadSQLModel()

    with Session(engine) as session:

        session.add(thread)
        session.commit()
        session.refresh(thread)

    return thread


async def insert_message(*args, **kwargs):
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
    with Session(engine) as session:
        if after:
            after_message = session.exec(
                select(MessageSQLModel).where(MessageSQLModel.id == uuid.UUID(after))
            ).first()

            if after_message:
                after_created_at = after_message.created_at

            else:
                after_created_at = 0

        else:
            after_created_at = 0

        if before:
            before_message = session.exec(
                select(MessageSQLModel).where(MessageSQLModel.id == uuid.UUID(before))
            ).first()

            if before_message:
                before_created_at = before_message.created_at

            else:
                before_created_at = func.now()

        else:
            before_created_at = func.now()

        statement = (
            select(MessageSQLModel)
            .where(
                MessageSQLModel.thread_id == uuid.UUID(thread_id),
                MessageSQLModel.created_at.between(after_created_at, before_created_at),
            )
            .order_by(
                MessageSQLModel.created_at.desc()
                if order == "desc"
                else MessageSQLModel.created_at.asc()
            )
            .limit(limit)
        )

        results = session.exec(statement)

        messages: List[Message] = [
            Message(
                id=str(result.id),
                attachments=result.attachments,
                content=result.content,
                created_at=result.created_at.timestamp(),
                object="thread.message",
                role=result.role,
                status=result.status,
                thread_id=str(result.thread_id),
                updated_at=result.updated_at.timestamp(),
            )
            for result in results.all()
        ]

        return messages
