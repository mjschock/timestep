import logging

from fastapi import APIRouter

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

agents_router = APIRouter(tags=["agents"])


@agents_router.on_event("startup")
async def startup():
    logger.info("Starting up agents router")

    # agents_router.state.agents_service: AgentsService = await init_agents_service()


@agents_router.post("")
async def create_agent():
    logger.debug("Creating agent")

    # agent = await agents_router.state.agents_service.create_agent()
    agent = {"message": "Agent created"}

    return agent
