# import requests
from typing import Annotated

import httpx
from fastapi import APIRouter, Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from pydantic import BaseModel

# client = httpx.AsyncClient()

security = HTTPBearer()

router = APIRouter(
    prefix="/api/threads",
    tags=["threads"],
    # dependencies=[Depends(get_current_user)],
    # responses={404: {"description": "Not found"}},
)


@router.on_event("startup")
async def startup():
    # logger.info("Starting up agents router")
    print("=== (print) Starting up threads router ===")

    # await threads_service.init_threads_service()


messages = [
    {
        "id": "4975920e-a4e3-11ee-a55c-17ba192d0095",
        "avatarUrl": "https://robohash.org/4975920e-a4e3-11ee-a55c-17ba192d0095",
        "content": "Hey there! I'm your assistant. How can I help you?",
        "images": [],
        "role": "assistant",
        # "timestamp": time.time(),
        # "timestamp": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
    },
]


@router.get(
    "",
)
async def get_threads(
    credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)],
):
    return {
        "threads": [
            {
                "id": "0d3f0dc0-a4e2-11ee-b859-e7ab6ec7d7f6",
                # "title": "Thread 1",
                "messages": [{"id": message["id"] for message in messages}],
            },
        ]
    }


@router.get(
    "/{thread_id}/messages",
)
async def get_messages(
    credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)],
    thread_id: str,
):
    return {
        "messages": messages,
    }


class Message(BaseModel):
    content: str
    images: list = []


@router.post(
    "/{thread_id}/messages"
    # responses={
    #     202: {"description": "Agent created"},
    #     403: {"description": "Operation forbidden"},
    # },
)
async def create_message(
    credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)],
    thread_id: str,
    # content: str,
    message: Message,
    # images: list = [],
    # agent_config: AgentConfig,
    # agent_service: Annotated[AgentsService, Depends(get_agent_service)],
):
    print("=== (print) create_message ===")
    print("message: ", message)

    _messages = messages.copy()
    _messages.append(
        {
            "role": "user",
            "content": message.content,
        }
    )

    # response = requests.post(
    #     "http://ollama.default.svc.cluster.local:80/api/chat",
    #     json={
    #         "model": "phi:latest",
    #         "messages": _messages,
    #         "stream": False,
    #     }
    # )

    async with httpx.AsyncClient(timeout=httpx.Timeout(timeout=None)) as client:
        try:
            response = await client.post(
                "http://ollama.default.svc.cluster.local:80/api/chat",
                json={
                    "model": "phi:latest",
                    "messages": _messages,
                    "stream": False,
                },
            )

        except httpx.HTTPError as exc:
            print("=== (print) httpx.HTTPError ===")
            print(exc)
            raise exc

    print("response: ", response)

    data = response.json()
    print("data: ", data)

    return {
        "data": data,
    }

    # background_task: BackgroundTask = BackgroundTask(
    #     # func=deploy_create_agent_flow,
    #     # func=agent_service.create_agent,
    #     func=agent_service_create_agent,
    #     content=content,
    #     images=images,
    #     # agent_config=agent_config,
    #     # agent_service=agent_service,
    # )

    # response = requests.post(
    #     "http://ollama.default.svc.cluster.local:80/api/chat",
    #     # params={"name": name},  # noqa: E501
    #     json={
    #         "model": "phi:latest",
    #         "messages": [
    #             {
    #                 "role": "user",
    #                 "content": content,
    #                 # "images": images,
    #             }
    #         ]
    #     },
    #     stream=True,
    # # ).json()
    # )

    # print("response: ", response)

    # return response

    # return StreamingResponse(response.iter_content(chunk_size=1024), media_type="text/plain")  # noqa: E501

    # return Response(
    #     background=background_task,
    #     status_code=202,
    # )

    # return StreamingResponse(
    #     agent_service_create_agent(content, images),
    #     media_type="text/plain",
    # )

    # client = httpx

    # async with client.stream(
    #     'POST',
    #     "http://ollama.default.svc.cluster.local:80/api/chat",
    #     # params={"name": name},  # noqa: E501
    #     json={
    #         "model": "phi:latest",
    #         "messages": [
    #             {
    #                 "role": "user",
    #                 "content": content,
    #                 # "images": images,
    #             }
    #         ]
    #     },
    #     # stream=True,
    # ) as response:
    #     async for chunk in response.aiter_bytes():
    #         yield chunk

    # print('message: ', message)

    # from llama_index.llms import ChatMessage, Ollama

    # llm = Ollama(
    #     base_url="http://ollama.default.svc.cluster.local:80",
    #     model="phi:latest"
    # )

    # messages = [
    #     ChatMessage(
    #         role="system", content="You are a pirate with a colorful personality"
    #     ),
    #     ChatMessage(role="user", content="What is your name"),
    # ]

    # async with httpx.AsyncClient() as client:
    #     response = await client.get('https://www.example.com/')
    #     print(response)

    # resp = llm.chat(messages)

    # resp = await llm.stream_chat(messages)

    # for r in resp:
    #     print(r.delta, end="")

    # print('resp: ', resp)

    # return resp

    # return StreamingResponse(

    # client = httpx.AsyncClient()

    # req = client.build_request(
    #     "POST",
    #     "http://ollama.default.svc.cluster.local:80/api/chat",
    #     json={
    #         "model": "phi:latest",
    #         "messages": [
    #             {
    #                 "role": "user",
    #                 "content": message.content,
    #                 # "images": images,
    #             }
    #         ]
    #     },
    # )
    # # r = await client.send(req, stream=True)
    # r = await client.send(req, stream=False)
    # return StreamingResponse(r.aiter_text(), background=BackgroundTask(r.aclose))

    # async with client.stream(
    #     "POST",
    #     "http://ollama.default.svc.cluster.local:80/api/chat",
    #     json={
    #         "model": "phi:latest",
    #         "messages": [
    #             {
    #                 "role": "user",
    #                 "content": message.content,
    #                 # "images": images,
    #             }
    #         ],
    #         "stream": True,
    #     },
    # ) as response:
    #     async for chunk in response.aiter_bytes():
    #         print('chunk: ', chunk)

    # async with client.stream(
    #     "POST",
    #     "http://ollama.default.svc.cluster.local:80/api/generate",
    #     json={
    #         "model": "phi:latest",
    #         "prompt": "Why is the sky blue?",
    #         # "messages": [
    #         #     {
    #         #         "role": "user",
    #         #         "content": message.content,
    #         #         # "images": images,
    #         #     }
    #         # ],
    #         "stream": True,
    #     },
    # ) as response:
    #     # async for chunk in response.aiter_bytes():
    #     #     print('chunk: ', chunk)
    #     print('response: ', response)

    # # return {

    # # }
