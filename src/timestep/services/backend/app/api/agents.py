from typing import Any, Dict, List, Optional

from agent_protocol import Step, StepRequestBody
from agent_protocol.models import (
    TaskListResponse,
    TaskStepsListResponse,
)
from fastapi import (
    APIRouter,
    BackgroundTasks,
    Response,
    status,
)
from pydantic import StrictStr

from app.services import agents as agents_service

account_id = "f215cf48-7458-4596-9aa5-2159fc6a3caf" # Temporary; same as S3_ROOT_FOLDER in NhostConstruct  # noqa: E501
available_agent_names = ("gpt-2", "gpt-4-vision-preview", "spaceflights-pandas")

agents_router = APIRouter()

@agents_router.post(
    "",
    status_code=status.HTTP_202_ACCEPTED,
    tags=["agents"],
)
async def create_agent(agent_name: str, background_tasks: BackgroundTasks):
    if agent_name not in available_agent_names:
        return Response(
            content=f"Please choose one of the following agents: {available_agent_names}",  # noqa: E501
            status_code=status.HTTP_400_BAD_REQUEST,
        )

    # async def create_agent_background_task(name: str):
        # await agents_service.create_agent(name)

    # background_tasks.add_task(create_agent_background_task, name)

    agents = await agents_service.get_agents(account_id)

    if agent_name in [agent["name"] for agent in agents]:
        return Response(
            content=f"Agent with name '{agent_name}' already exists.",
            status_code=status.HTTP_409_CONFLICT,
        )

    await agents_service.create_agent(account_id=account_id, agent_name=agent_name)

    return Response(
        status_code=status.HTTP_202_ACCEPTED,
    )

@agents_router.delete(
    "/{agent_id}",
    tags=["agents"],
)
async def delete_agent(agent_id: str):
    agent: Dict[str, Any] = await agents_service.delete_agent(account_id, agent_id)

    return {
        "agent": agent,
    }

@agents_router.get(
    "/{agent_id}",
    tags=["agents"],
)
async def get_agent(agent_id: str):
    agent: Dict[str, Any] = await agents_service.get_agent(account_id, agent_id)

    return {
        "agent": agent,
    }

@agents_router.get(
    "/{agent_id}/livez",
    tags=["agents"],
)
async def get_agent_livez(agent_id: str):
    return await agents_service.get_agent_livez(account_id, agent_id)

@agents_router.get(
    "/{agent_id}/readyz",
    tags=["agents"],
)
async def get_agent_readyz(agent_id: str):
    return await agents_service.get_agent_readyz(account_id, agent_id)

@agents_router.get(
    "",
    tags=["agents"],
)
async def list_agents():
    agents: List[Dict[str, Any]] = await agents_service.get_agents(account_id)

    return {
        "agents": agents,
    }

@agents_router.put(
    "/{agent_id}",
    tags=["agents"],
)
async def update_agent(agent_id: str):
    agent: Dict[str, Any] = await agents_service.update_agent(account_id, agent_id)

    return Response(
        status_code=status.HTTP_202_ACCEPTED,
    )

@agents_router.post(
    "/{agent_id}/ap/v1/agent/tasks",
    tags=["agent", "agents"],
)
async def create_agent_task(
    agent_id: str,
    input: Optional[StrictStr]="Write 'Hello world!' to hi.txt.",
    additional_input: Optional[Dict[str, Any]] = None
):
    task = await agents_service.create_agent_task(agent_id, input, additional_input)

    return {
        "task": task,
    }

@agents_router.get(
    "/{agent_id}/ap/v1/agent/tasks",
    tags=["agent", "agents"],
)
async def list_agent_tasks(
    agent_id: str,
) -> TaskListResponse:
    return await agents_service.list_agent_tasks(agent_id)

@agents_router.get(
    "/{agent_id}/ap/v1/agent/tasks/{task_id}",
    tags=["agent", "agents"],
)
async def get_agent_task(
    agent_id: str,
    task_id: str,
):
    return await agents_service.get_agent_task(agent_id, task_id)

@agents_router.get(
    "/{agent_id}/ap/v1/agent/tasks/{task_id}/steps",
    response_model=TaskStepsListResponse,
    tags=["agent", "agents"],
)
async def list_agent_task_steps(
    agent_id: str, task_id: str, page_size: int = 10, current_page: int = 1
) -> List[str]:
    """
    List all steps for the specified task.
    """
    return await agents_service.list_agent_task_steps(agent_id, task_id, page_size, current_page)

@agents_router.post(
    "/{agent_id}/ap/v1/agent/tasks/{task_id}/steps",
    response_model=Step,
    tags=["agent", "agents"],
)
async def execute_agent_task_step(
    agent_id: str,
    task_id: str,
    body: StepRequestBody | None = None,
) -> Step:
    """
    Execute a step in the specified agent task.
    """
    return await agents_service.execute_agent_task_step(agent_id, task_id, body)

@agents_router.get(
    "/{agent_id}/ap/v1/agent/tasks/{task_id}/steps/{step_id}",
    response_model=Step,
    tags=["agent", "agents"],
)
async def get_agent_task_step(self, agent_id: str, task_id: str, step_id: str) -> Step:
    """
    Get details about a specified task step.
    """
    return await agents_service.get_agent_task_step(agent_id, task_id, step_id)
