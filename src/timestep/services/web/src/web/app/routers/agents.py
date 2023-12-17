from typing import Annotated

from fastapi import APIRouter, Depends

from ..dependencies import get_current_user
from ..services.agents import AgentsService, get_agent_service

router = APIRouter(
    prefix="/api/agents",
    tags=["agents"],
    # dependencies=[Depends(get_token_header)],
    dependencies=[Depends(get_current_user)],
    responses={404: {"description": "Not found"}},
)


@router.post(
    "",
    responses={403: {"description": "Operation forbidden"}},
)
async def create_agent(
    agent_service: Annotated[AgentsService, Depends(get_agent_service)],
):
    agent_id = await agent_service.create_agent()

    return {
        "agent_id": agent_id,
    }
