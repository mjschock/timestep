from typing import List

from fastapi import APIRouter, HTTPException, Request, status
from fastapi.responses import StreamingResponse
from llama_index.llms.base import ChatMessage
from llama_index.llms.types import MessageRole
from pydantic import BaseModel

from ..services.agents import query_agent

router = APIRouter(
    prefix="/api/chat",
)


class _Message(BaseModel):
    role: MessageRole
    content: str


class _ChatData(BaseModel):
    messages: List[_Message]


@router.post("")
async def chat(
    request: Request,
    # Note: To support clients sending a JSON object using content-type "text/plain",
    # we need to use Depends(json_to_model(_ChatData)) here
    # data: _ChatData = Depends(json_to_model(_ChatData)),
    data: _ChatData,
    # index: VectorStoreIndex = Depends(get_index), # TODO: agent instead of index
):
    response = await query_agent(data.messages)

    return {
        "data": data,
        "response": response,
    }

    # check preconditions and get last message
    if len(data.messages) == 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No messages provided",
        )

    lastMessage = data.messages.pop()  # noqa: N806

    if lastMessage.role != MessageRole.USER:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Last message must be from user",
        )

    # convert messages coming from the request to type ChatMessage
    messages = [
        ChatMessage(
            role=m.role,
            content=m.content,
        )
        for m in data.messages
    ]

    # query chat engine
    chat_engine = index.as_chat_engine()  # noqa: F821
    response = chat_engine.stream_chat(lastMessage.content, messages)

    # stream response
    async def event_generator():
        for token in response.response_gen:
            # If client closes connection, stop sending events
            if await request.is_disconnected():
                break

            yield token

    return StreamingResponse(event_generator(), media_type="text/plain")
