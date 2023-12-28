import logging
import os

import requests
from fastapi import APIRouter, logger

# from web.app.local_dev import app as local_dev
# from ..services.agent import app as agent_deployment
# from ..workflows.agent import deploy_flow
# from ..services import agent_deployment
# from ..services.agent import deploy_create_agent_flow
from ..services import agents as agent_service

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


@router.get("")
async def get_agents():
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
            "id": "47",
            # "name": "Timestep AI Agent",
            "name": "agent@timestep.ai",
            "model_ids": model_ids,
            "version": os.getenv("VERSION"),
        }
    ]

    return {
        "agents": agents,
    }


@router.post("/{agent_id}/models")
async def create_agent_model(agent_id: str, model_id: str):
    response = requests.delete(
        "http://ollama.default.svc.cluster.local:80/api/delete",
        json={"name": model_id},  # noqa: E501
    ).json()

    print("response: ", response)

    return {
        "message": response,
    }


@router.delete("/{agent_id}/models/{model_id}")
async def delete_agent_model(agent_id: str, model_id: str):
    response = requests.delete(
        "http://ollama.default.svc.cluster.local:80/api/delete",
        json={"name": model_id},  # noqa: E501
    ).json()

    print("response: ", response)

    return {
        "message": response,
    }


# @router.get("/hello2")
# async def hello2(name: str = "Ray"):
#     response = requests.get(
#         "http://ray-cluster-kuberay-head-svc.default.svc.cluster.local:8000/",
#         params={"name": name},  # noqa: E501
#     ).json()

#     return {
#         "message": response,
#     }
