import logging
from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from web.services.agents import AgentsService, init_agents_service

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

agents_router = APIRouter(tags=["agents"])
security = HTTPBearer()


@agents_router.on_event("startup")
async def startup():
    logger.info("Starting up agents router")

    # agents_router.state.agents_service: AgentsService = await init_agents_service()


@agents_router.post("")
async def create_agent(
    credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)],
):
    # logger.debug("Creating agent")
    # logger.debug(f"credentials: {credentials}")
    # logger.info(f"credentials: {credentials}")

    # print('credentials', credentials)

    # print('message', "Creating agent")

    # agent = await agents_router.state.agents_service.create_agent()
    # agent = {"message": "Agent created"}

    agents_service: AgentsService = await init_agents_service()
    agent = await agents_service.create_agent()

    return agent
