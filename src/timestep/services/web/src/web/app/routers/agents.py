import logging
import os
from typing import Annotated, Any, Callable, Coroutine, Optional

import requests
from agent_protocol import Agent
from agent_protocol.db import Step, Task
from agent_protocol.models import (
    TaskRequestBody,
)
from fastapi import APIRouter, Depends, logger

# from web.app.local_dev import app as local_dev
# from ..services.agent import app as agent_deployment
# from ..workflows.agent import deploy_flow
# from ..services import agent_deployment
# from ..services.agent import deploy_create_agent_flow
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from ..services import agents as agent_service

agent_id = "58648f86-a691-11ee-b5cf-2bc42583c635"

StepHandler = Callable[[Step], Coroutine[Any, Any, Step]]
TaskHandler = Callable[[Task], Coroutine[Any, Any, None]]


_task_handler: Optional[TaskHandler]
_step_handler: Optional[StepHandler]

security = HTTPBearer()

router = APIRouter(
    prefix="/api/agents",
    tags=["agents"],
    # dependencies=[Depends(get_current_user)],
    # responses={404: {"description": "Not found"}},
)


@router.on_event("startup")
async def startup():
    # logger.info("Starting up agents router")
    print("=== (print) Starting up agents router ===")
    logger.logger.info("=== (fastapi logger) Starting up agents router ===")
    logging.getLogger("uvicorn").info(
        "=== (uvicorn logger) Starting up agents router ==="
    )  # noqa: E501

    await agent_service.init_agent_service()


@router.post("/{agent_id}/ap/v1/agent/tasks", response_model=Task, tags=["agent"])
async def create_agent_task(
    credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)],
    agent_id: str,
    body: TaskRequestBody | None = None,
) -> Task:
    """
    Creates a task for the agent.
    """
    if not _task_handler:  # noqa: F821
        raise Exception("Task handler not defined")

    task = await Agent.db.create_task(
        input=body.input if body else None,
        additional_input=body.additional_input if body else None,
    )
    await _task_handler(task)  # noqa: F821

    return task


@router.get("")
async def get_agents(
    credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)],
):
    response = requests.get(
        "http://ollama.default.svc.cluster.local:80/api/tags",
        # params={"name": name},  # noqa: E501
    ).json()

    print("response: ", response)

    models = response["models"]

    print("models: ", models)

    model_ids = [model["name"] for model in models]
    agents = [
        {
            "id": agent_id,
            # "name": "Timestep AI Agent",
            "name": "agent@timestep.ai",
            "model_ids": model_ids,
            "version": os.getenv("VERSION"),
        }
    ]

    return {
        "agents": agents,
    }


# @router.post("")
# async def create_agent():
#     # https://github.com/langchain-ai/langchain/blob/master/cookbook/petting_zoo.ipynb
#     # Just use the phi2 model with the langchain Ollama integration in place of ChatGPT  # noqa: E501
#     # Wrap PettingZooAgent in Agent from Agent protocol

#     # POST /API/agents would create an agent row and model rows that have foreign
#     # key to agent table and action client which retrains models on  schedule and
#     # can be queried for inference (See Fine-Tuning and RAG in reference section
#     # below)


# @router.post("/{agent_id}/models")
# async def create_agent_model(agent_id: str, model_id: str):
#     response = requests.delete(
#         "http://ollama.default.svc.cluster.local:80/api/delete",
#         json={"name": model_id},  # noqa: E501
#     ).json()

#     print("response: ", response)

#     return {
#         "message": response,
#     }


# @router.delete("/{agent_id}/models/{model_id}")
# async def delete_agent_model(agent_id: str, model_id: str):
#     response = requests.delete(
#         "http://ollama.default.svc.cluster.local:80/api/delete",
#         json={"name": model_id},  # noqa: E501
#     ).json()

#     print("response: ", response)

#     return {
#         "message": response,
#     }


# @router.get("/hello2")
# async def hello2(name: str = "Ray"):
#     response = requests.get(
#         "http://ray-cluster-kuberay-head-svc.default.svc.cluster.local:8000/",
#         params={"name": name},  # noqa: E501
#     ).json()

#     return {
#         "message": response,
#     }
