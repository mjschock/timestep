from typing import Annotated

from fastapi import APIRouter, Depends, Response
from pydantic import BaseModel
from starlette.background import BackgroundTask

from ..services.agents import AgentsService, get_agent_service

router = APIRouter(
    prefix="/api/agents",
    tags=["agents"],
    # dependencies=[Depends(get_current_user)],
    responses={404: {"description": "Not found"}},
)


class AgentConfig(BaseModel):
    agent_type: str = "dqn"
    agent_name: str = "dqn_agent"


async def create_agent_flow(agent_config: AgentConfig, agent_service: AgentsService):
    print("create_agent_flow")
    print("agent_config: ", agent_config)
    agent_id = await agent_service.create_agent()

    return agent_id


@router.post(
    "",
    responses={
        202: {"description": "Agent created"},
        403: {"description": "Operation forbidden"},
    },
)
async def create_agent(
    agent_config: AgentConfig,
    agent_service: Annotated[AgentsService, Depends(get_agent_service)],
):
    background_task: BackgroundTask = BackgroundTask(
        func=create_agent_flow,
        agent_config=agent_config,
        agent_service=agent_service,
    )

    return Response(
        background=background_task,
        status_code=202,
    )


@router.delete(
    "",
    responses={
        204: {"description": "Agent deleted"},
        403: {"description": "Operation forbidden"},
    },
)
async def delete_agent(
    agent_service: Annotated[AgentsService, Depends(get_agent_service)],
    agent_id: str = "default",
):
    print("delete_agent")
    await agent_service.delete_agent(agent_id=agent_id)

    return Response(status_code=204)


@router.get(
    "",
    responses={
        200: {"description": "Agent query successful"},
        403: {"description": "Operation forbidden"},
    },
)
async def query_agent(
    agent_service: Annotated[AgentsService, Depends(get_agent_service)], query: str
):
    print("query_agent")
    resp = await agent_service.query_agent(query=query)

    print("resp", resp)

    return resp
