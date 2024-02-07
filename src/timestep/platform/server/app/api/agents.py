from typing import Annotated, Any, Dict, List, Optional

from agent_protocol import Artifact, Step, StepRequestBody, Task, TaskRequestBody
from agent_protocol.models import (
    Task as APITask,
)
from agent_protocol.models import (
    TaskListResponse,
    TaskStepsListResponse,
)
from fastapi import (
    APIRouter,
    File,
    Form,
    Response,
    UploadFile,
    status,
)
from fastapi.responses import FileResponse
from pydantic import StrictStr

from app.services import agents as agents_service

DEFAULT_ACCOUNT_ID = "f215cf48-7458-4596-9aa5-2159fc6a3caf" # Temporary; same as S3_ROOT_FOLDER in NhostConstruct  # noqa: E5010
DEFAULT_AGENT_NAME = "agent" # TODO: Make this an environment variable

available_agent_names = ("agent", "gpt-4-vision-preview")

agents_router = APIRouter()

@agents_router.post(
    "",
    status_code=status.HTTP_202_ACCEPTED,
    tags=["agents"],
)
async def create_agent(agent_name: str):
    if agent_name not in available_agent_names:
        return Response(
            content=f"Please an agent name from {available_agent_names}.",
            status_code=status.HTTP_400_BAD_REQUEST,
        )

    agents = await agents_service.get_agents(DEFAULT_ACCOUNT_ID)

    if agent_name in [agent["name"] for agent in agents]:
        return Response(
            content=f"Agent with name '{agent_name}' already exists.",
            status_code=status.HTTP_409_CONFLICT,
        )

    await agents_service.create_agent(
        account_id=DEFAULT_ACCOUNT_ID,
        agent_name=agent_name
    )

    return Response(
        status_code=status.HTTP_202_ACCEPTED,
    )

@agents_router.delete(
    "/{agent_id}",
    status_code=status.HTTP_202_ACCEPTED,
    tags=["agents"],
)
async def delete_agent(agent_id: str):
    if agent_id == "default":
        agents = await agents_service.get_agents(DEFAULT_ACCOUNT_ID)
        agent_id = [
            agent["id"] for agent in agents if agent["name"] == DEFAULT_AGENT_NAME
        ][0]

    await agents_service.delete_agent(DEFAULT_ACCOUNT_ID, agent_id)

    return Response(
        status_code=status.HTTP_202_ACCEPTED,
    )

@agents_router.get(
    "/{agent_id}",
    tags=["agents"],
)
async def get_agent(agent_id: str):
    if agent_id == "default":
        agents = await agents_service.get_agents(DEFAULT_ACCOUNT_ID)
        agent_id = [
            agent["id"] for agent in agents if agent["name"] == DEFAULT_AGENT_NAME
        ][0]

    agent: Dict[str, Any] = await agents_service.get_agent(DEFAULT_ACCOUNT_ID, agent_id)

    return {
        "agent": agent,
    }

@agents_router.get(
    "/{agent_id}/livez",
    tags=["agents"],
)
async def get_agent_livez(agent_id: str):
    if agent_id == "default":
        agents = await agents_service.get_agents(DEFAULT_ACCOUNT_ID)
        agent_id = [
            agent["id"] for agent in agents if agent["name"] == DEFAULT_AGENT_NAME
        ][0]

    return await agents_service.get_agent_livez(DEFAULT_ACCOUNT_ID, agent_id)

@agents_router.get(
    "/{agent_id}/readyz",
    tags=["agents"],
)
async def get_agent_readyz(agent_id: str):
    if agent_id == "default":
        agents = await agents_service.get_agents(DEFAULT_ACCOUNT_ID)
        agent_id = [
            agent["id"] for agent in agents if agent["name"] == DEFAULT_AGENT_NAME
        ][0]

    return await agents_service.get_agent_readyz(DEFAULT_ACCOUNT_ID, agent_id)

@agents_router.get(
    "",
    tags=["agents"],
)
async def list_agents():
    agents: List[Dict[str, Any]] = await agents_service.get_agents(DEFAULT_ACCOUNT_ID)

    return {
        "agents": agents,
    }

@agents_router.put(
    "/{agent_id}",
    tags=["agents"],
)
async def update_agent(agent_id: str):
    if agent_id == "default":
        agents = await agents_service.get_agents(DEFAULT_ACCOUNT_ID)
        agent_id = [
            agent["id"] for agent in agents if agent["name"] == DEFAULT_AGENT_NAME
        ][0]

    await agents_service.update_agent(DEFAULT_ACCOUNT_ID, agent_id)

    return Response(
        status_code=status.HTTP_202_ACCEPTED,
    )

@agents_router.post(
    "/{agent_id}/ap/v1/agent/tasks",
    response_model=Task,
    tags=["agent", "agents"],
)
async def create_agent_task(
    agent_id: str,
    body: TaskRequestBody | None = None
) -> Task:
    """
    Creates a task for the agent.
    """
    if agent_id == "default":
        agents = await agents_service.get_agents(DEFAULT_ACCOUNT_ID)
        agent_id = [
            agent["id"] for agent in agents if agent["name"] == DEFAULT_AGENT_NAME
        ][0]

    return await agents_service.create_agent_task(agent_id, body)

@agents_router.get(
    "/{agent_id}/ap/v1/agent/tasks",
    response_model=TaskListResponse,
    tags=["agent", "agents"],
)
async def list_agent_tasks_ids(
    agent_id: str,
    current_page: int = 1,
    page_size: int = 10,
) -> List[str]:
    """
    List all tasks that have been created for the agent.
    """
    if agent_id == "default":
        agents = await agents_service.get_agents(DEFAULT_ACCOUNT_ID)
        agent_id = [
            agent["id"] for agent in agents if agent["name"] == DEFAULT_AGENT_NAME
        ][0]

    return await agents_service.list_agent_tasks_ids(agent_id, current_page, page_size)

@agents_router.get(
    "/{agent_id}/ap/v1/agent/tasks/{task_id}",
    response_model=Task,
    tags=["agent", "agents"],
)
async def get_agent_task(
    agent_id: str,
    task_id: str,
) -> Task:
    """
    Get details about a specified agent task.
    """
    if agent_id == "default":
        agents = await agents_service.get_agents(DEFAULT_ACCOUNT_ID)
        agent_id = [
            agent["id"] for agent in agents if agent["name"] == DEFAULT_AGENT_NAME
        ][0]

    return await agents_service.get_agent_task(agent_id, task_id)

@agents_router.get(
    "/{agent_id}/ap/v1/agent/tasks/{task_id}/artifacts",
    response_model=List[Artifact],
    tags=["agent", "agents"],
)
async def list_agent_task_artifacts(
    agent_id: str,
    task_id: str,
    current_page: int = 1,
    page_size: int = 10,
) -> List[Artifact]:
    """
    List all artifacts for the specified task.
    """
    if agent_id == "default":
        agents = await agents_service.get_agents(DEFAULT_ACCOUNT_ID)
        agent_id = [
            agent["id"] for agent in agents if agent["name"] == DEFAULT_AGENT_NAME
        ][0]

    return await agents_service.list_agent_task_artifacts(
        agent_id=agent_id,
        task_id=task_id,
        current_page=current_page,
        page_size=page_size,
    )

@agents_router.post(
    "/{agent_id}/ap/v1/agent/tasks/{task_id}/artifacts",
    response_model=Artifact,
    tags=["agent", "agents"],
)
async def upload_agent_task_artifacts(
    agent_id: str,
    task_id: str,
    file: Annotated[UploadFile, File()],
    relative_path: Annotated[Optional[str], Form()] = None,
) -> Artifact:
    """
    Upload an artifact for the specified task.
    """
    if agent_id == "default":
        agents = await agents_service.get_agents(DEFAULT_ACCOUNT_ID)
        agent_id = [
            agent["id"] for agent in agents if agent["name"] == DEFAULT_AGENT_NAME
        ][0]

    return await agents_service.upload_agent_task_artifacts(
        agent_id=agent_id,
        task_id=task_id,
        file=file,
        relative_path=relative_path,
    )

@agents_router.get(
    "/{agent_id}/ap/v1/agent/tasks/{task_id}/artifacts/{artifact_id}",
    tags=["agent", "agents"],
)
async def download_agent_task_artifacts(
    agent_id: str,
    task_id: str,
    artifact_id: str
) -> FileResponse:
    """
    Download the specified artifact.
    """
    if agent_id == "default":
        agents = await agents_service.get_agents(DEFAULT_ACCOUNT_ID)
        agent_id = [
            agent["id"] for agent in agents if agent["name"] == DEFAULT_AGENT_NAME
        ][0]

    return await agents_service.download_agent_task_artifacts(
        agent_id=agent_id,
        task_id=task_id,
        artifact_id=artifact_id,
    )

@agents_router.get(
    "/{agent_id}/ap/v1/agent/tasks/{task_id}/steps",
    response_model=TaskStepsListResponse,
    tags=["agent", "agents"],
)
async def list_agent_task_steps(
    agent_id: str, task_id: str, current_page: int = 1, page_size: int = 10,
) -> List[str]:
    """
    List all steps for the specified task.
    """
    if agent_id == "default":
        agents = await agents_service.get_agents(DEFAULT_ACCOUNT_ID)
        agent_id = [
            agent["id"] for agent in agents if agent["name"] == DEFAULT_AGENT_NAME
        ][0]

    return await agents_service.list_agent_task_steps(
        agent_id=agent_id,
        current_page=current_page,
        page_size=page_size,
        task_id=task_id,
    )

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
    if agent_id == "default":
        agents = await agents_service.get_agents(DEFAULT_ACCOUNT_ID)
        agent_id = [
            agent["id"] for agent in agents if agent["name"] == DEFAULT_AGENT_NAME
        ][0]

    return await agents_service.execute_agent_task_step(agent_id, task_id, body)

@agents_router.get(
    "/{agent_id}/ap/v1/agent/tasks/{task_id}/steps/{step_id}",
    response_model=Step,
    tags=["agent", "agents"],
)
async def get_agent_task_step(agent_id: str, task_id: str, step_id: str) -> Step:
    """
    Get details about a specified task step.
    """
    if agent_id == "default":
        agents = await agents_service.get_agents(DEFAULT_ACCOUNT_ID)
        agent_id = [
            agent["id"] for agent in agents if agent["name"] == DEFAULT_AGENT_NAME
        ][0]

    return await agents_service.get_agent_task_step(agent_id, task_id, step_id)
