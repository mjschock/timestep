import os
from tempfile import NamedTemporaryFile
from typing import Annotated, Any, Dict, List, Optional

import httpx
import sky
from agent_protocol import Artifact, Task
from agent_protocol.models import (
    Step as APIStep,
)
from agent_protocol.models import (
    StepRequestBody,
    TaskListResponse,
    TaskRequestBody,
    TaskStepsListResponse,
)
from agent_protocol.models import (
    Task as APITask,
)
from agent_protocol_client import (
    AgentApi,
    ApiClient,
    Configuration,
)
from agent_protocol_client.models.task_artifacts_list_response import (
    TaskArtifactsListResponse,
)
from fastapi import File, Form, UploadFile
from fastapi.responses import FileResponse
from prefect.deployments.deployments import run_deployment
from prefect_shell import ShellOperation
from pydantic import StrictBytes, StrictStr

from app.services.utils import (
    create_minio_bucket,
    create_minio_storage_block,
    deploy_agent,
    get_agent_deployment_idempotency_key,
    load_cloud_credentials,
    sky_check_task,
    sky_queue_task,
    sky_status_task,
    upload_directory_to_minio,
)

DEFAULT_ACCOUNT_ID = "f215cf48-7458-4596-9aa5-2159fc6a3caf" # Temporary; same as S3_ROOT_FOLDER in NhostConstruct  # noqa: E501
DEFAULT_AGENT_NAME = "agent" # TODO: Make this an environment variable
DEFAULT_BUCKET_NAME = "default"

async def create_agent(account_id: str, agent_name: str) -> dict[str, Any]:
    bucket_name: str = await create_minio_bucket(
        DEFAULT_BUCKET_NAME,
        ignore_exists=True,
    )
    minio_storage_block = await create_minio_storage_block(
        account_id=account_id,
        agent_name=agent_name,
        bucket_folder=account_id,
        bucket_name=bucket_name,
    )
    uploaded_file_count: int = await upload_directory_to_minio(
        minio_storage_block=minio_storage_block,
        local_path=f"{os.getcwd()}/app/workers/agents/{agent_name}",
        to_path=f"agents/{agent_name}"
    )
    deployment_ids: list = await deploy_agent(
        uploaded_file_count,
        account_id,
        agent_name,
        bucket_name,
    )

    for deployment_id in deployment_ids:
        await run_deployment(
            deployment_id,
            idempotency_key=get_agent_deployment_idempotency_key(
                local_path=f"{os.getcwd()}/app/workers/agents/{agent_name}",
            ),
            timeout=0,
        )

async def create_agent_task(
    agent_id,
    body: TaskRequestBody | None = None,
) -> APITask:
    """
    Creates a task for the agent.
    """
    agent: Dict[str, Any] = {
        "id": agent_id,
    }
    memo: Dict[str, Any] = {}
    memo = await sky_status_task(memo, refresh=False)

    for cluster_status in memo["cluster_statuses"]:
        if cluster_status["cluster_hash"] == agent_id:
            agent["name"] = cluster_status["name"]
            head_ip = cluster_status["handle"].head_ip

            break

    configuration = Configuration(host=f"http://{head_ip}:8000")

    async with ApiClient(configuration) as api_client:
        api_instance = AgentApi(api_client)

        task: APITask = await api_instance.create_agent_task(
            task_request_body=body,
        )

    return task

async def list_agent_tasks_ids(
    agent_id: str,
    current_page: int = 1,
    page_size: int = 10,
) -> TaskListResponse:
    """
    List all tasks that have been created for the agent.
    """
    agent: Dict[str, Any] = {
        "id": agent_id,
    }
    memo: Dict[str, Any] = {}
    memo = await sky_status_task(memo, refresh=False)

    for cluster_status in memo["cluster_statuses"]:
        if cluster_status["cluster_hash"] == agent_id:
            agent["name"] = cluster_status["name"]
            head_ip = cluster_status["handle"].head_ip

            break

    configuration = Configuration(host=f"http://{head_ip}:8000")

    async with ApiClient(configuration) as api_client:
        api_instance = AgentApi(api_client)
        tasks_list_response: TaskListResponse = await api_instance.list_agent_tasks(
            current_page=current_page,
            page_size=page_size,
        )

    return tasks_list_response

async def get_agent_task(agent_id: str, task_id: str) -> Task:
    """
    Get details about a specified agent task.
    """
    agent: Dict[str, Any] = {
        "id": agent_id,
    }
    memo: Dict[str, Any] = {}
    memo = await sky_status_task(memo, refresh=False)

    for cluster_status in memo["cluster_statuses"]:
        if cluster_status["cluster_hash"] == agent_id:
            agent["name"] = cluster_status["name"]
            head_ip = cluster_status["handle"].head_ip

            break

    configuration = Configuration(host=f"http://{head_ip}:8000")

    async with ApiClient(configuration) as api_client:
        api_instance = AgentApi(api_client)
        task: Task = await api_instance.get_agent_task(task_id=task_id)

    return task

async def list_agent_task_artifacts(
    agent_id: str,
    task_id: str,
    current_page: int = 1,
    page_size: int = 10,
) ->  List[Artifact]:
    """
    List all artifacts for the specified task.
    """
    agent: Dict[str, Any] = {
        "id": agent_id,
    }
    memo: Dict[str, Any] = {}
    memo = await sky_status_task(memo, refresh=False)

    for cluster_status in memo["cluster_statuses"]:
        if cluster_status["cluster_hash"] == agent_id:
            agent["name"] = cluster_status["name"]
            head_ip = cluster_status["handle"].head_ip

            break

    configuration = Configuration(host=f"http://{head_ip}:8000")

    async with ApiClient(configuration) as api_client:
        api_instance = AgentApi(api_client)

        tasks_artifacts_list_response: TaskArtifactsListResponse = \
            await api_instance.list_agent_task_artifacts(
                task_id=task_id,
                current_page=current_page,
                page_size=page_size,
            )

    return tasks_artifacts_list_response.artifacts

async def list_agent_task_steps(
    agent_id: str,
    task_id: str,
    current_page: int = 1,
    page_size: int = 10,
) -> TaskStepsListResponse:
    """
    List all steps for the specified task.
    """
    agent: Dict[str, Any] = {
        "id": agent_id,
    }
    memo: Dict[str, Any] = {}
    memo = await sky_status_task(memo, refresh=False)

    for cluster_status in memo["cluster_statuses"]:
        if cluster_status["cluster_hash"] == agent_id:
            agent["name"] = cluster_status["name"]
            head_ip = cluster_status["handle"].head_ip

            break

    configuration = Configuration(host=f"http://{head_ip}:8000")

    async with ApiClient(configuration) as api_client:
        api_instance = AgentApi(api_client)

        task_steps_list_response: TaskStepsListResponse = \
            await api_instance.list_agent_task_steps(
                task_id=task_id,
                page_size=page_size,
                current_page=current_page,
            )

    return task_steps_list_response

async def upload_agent_task_artifacts(
    agent_id: str,
    task_id: str,
    file: Annotated[UploadFile, File()],
    relative_path: Annotated[Optional[str], Form()] = None,
) -> Artifact:
    """
    Upload an artifact for the specified task.
    """
    agent: Dict[str, Any] = {
        "id": agent_id,
    }
    memo: Dict[str, Any] = {}
    memo = await sky_status_task(memo, refresh=False)

    for cluster_status in memo["cluster_statuses"]:
        if cluster_status["cluster_hash"] == agent_id:
            agent["name"] = cluster_status["name"]
            head_ip = cluster_status["handle"].head_ip

            break

    configuration = Configuration(host=f"http://{head_ip}:8000")

    async with ApiClient(configuration) as api_client:
        api_instance = AgentApi(api_client)

        try:
            # Save the file to a temporary location
            with NamedTemporaryFile(delete=False) as temp_file:
                temp_file.write(await file.read())
                temp_file_path = temp_file.name

            # Call the function with the temporary file path
            artifact: Artifact = await api_instance.upload_agent_task_artifacts(
                task_id=task_id,
                file=temp_file_path,
                relative_path=relative_path,
            )

        finally:
            # Cleanup the temporary file
            if temp_file_path:
                os.unlink(temp_file_path)

    return artifact

async def execute_agent_task_step(
    agent_id: str,
    task_id: str,
    body: StepRequestBody | None = None
) -> APIStep:
    agent: Dict[str, Any] = {
        "id": agent_id,
    }
    memo: Dict[str, Any] = {}
    memo = await sky_status_task(memo, refresh=False)

    for cluster_status in memo["cluster_statuses"]:

        if cluster_status["cluster_hash"] == agent_id:
            agent["name"] = cluster_status["name"]
            head_ip = cluster_status["handle"].head_ip

            break

    configuration = Configuration(host=f"http://{head_ip}:8000")

    async with ApiClient(configuration) as api_client:
        api_instance = AgentApi(api_client)

        step: APIStep = await api_instance.execute_agent_task_step(
            task_id=task_id,
            step_request_body=body
        )

    return step

async def download_agent_task_artifacts(
    agent_id: str,
    task_id: str,
    artifact_id: str
) -> FileResponse:
    """
    Download the specified artifact.
    """
    agent: Dict[str, Any] = {
        "id": agent_id,
    }
    memo: Dict[str, Any] = {}
    memo = await sky_status_task(memo, refresh=False)

    for cluster_status in memo["cluster_statuses"]:
        if cluster_status["cluster_hash"] == agent_id:
            agent["name"] = cluster_status["name"]
            head_ip = cluster_status["handle"].head_ip

            break

    configuration = Configuration(host=f"http://{head_ip}:8000")

    async with ApiClient(configuration) as api_client:
        api_instance = AgentApi(api_client)

        return await api_instance.download_agent_task_artifact(
            task_id=task_id,
            artifact_id=artifact_id,
        )

async def get_agent_task_step(agent_id: str, task_id: str, step_id: str) -> APIStep:
    agent: Dict[str, Any] = {
        "id": agent_id,
    }
    memo: Dict[str, Any] = {}
    memo = await sky_status_task(memo, refresh=False)

    for cluster_status in memo["cluster_statuses"]:
        if cluster_status["cluster_hash"] == agent_id:
            agent["name"] = cluster_status["name"]
            head_ip = cluster_status["handle"].head_ip

            break

    configuration = Configuration(host=f"http://{head_ip}:8000")

    async with ApiClient(configuration) as api_client:
        api_instance = AgentApi(api_client)
        step: APIStep = await api_instance.get_agent_task_step(
            task_id=task_id,
            step_id=step_id,
        )

    return step

async def delete_agent(account_id: str, agent_id: str):
    agent = await get_agent(account_id, agent_id)
    assert agent["id"] == agent_id, f"{agent['id']} != {agent_id}"

    await run_deployment( # TODO: cleanup minio on delete
        "serve-agent-flow/serve-agent-flow-deployment",
        parameters={
            "account_id": account_id,
            "agent_name": agent["name"],
            "operation": "delete",
        },
        timeout=0,
    )

async def get_agent(account_id: str, agent_id: str) -> Dict[str, Any]:
    memo: Dict[str, Any] = {}
    agents = await get_agents(account_id)

    for agent in agents:
        if agent["id"] == agent_id:
            agent_name = agent["name"]
            memo = await sky_queue_task(agent_name, memo)

            agent["iterations"] = [
                {
                    "id": job["job_id"],
                    "status": job["status"],
                } for job in memo["cluster_queue"]
            ]

            return agent

    raise Exception(f"Agent {agent_id} not found")

async def get_agent_livez(account_id: str, agent_id: str):
    cluster_statuses = sky.core.status(refresh=False)

    for cluster_status in cluster_statuses:
        if cluster_status["cluster_hash"] == agent_id:
            head_ip = cluster_status["handle"].head_ip

            async with httpx.AsyncClient() as client:
                resp = await client.get(f"http://{head_ip}:8000/livez")
                assert resp.json() == "ok", f"{resp.json()} != ok"
                return resp.json()

    raise Exception(f"Agent {agent_id} not found")

async def get_agent_readyz(account_id: str, agent_id: str):
    cluster_statuses = sky.core.status(refresh=False)

    for cluster_status in cluster_statuses:
        if cluster_status["cluster_hash"] == agent_id:
            head_ip = cluster_status["handle"].head_ip

            async with httpx.AsyncClient() as client:
                resp = await client.get(f"http://{head_ip}:8000/readyz")
                assert resp.json() == "ok", f"{resp.json()} != ok"

            async with ShellOperation(
                commands=[
                    "set -e",
                    "curl -fsSL https://agentprotocol.ai/test.sh > test.sh",
                    "dos2unix test.sh",
                    f"URL=http://{head_ip}:8000 bash test.sh",
                ],
                shell="bash",
                working_dir="/tmp",
            ) as sky_op:
                sky_op_process = await sky_op.trigger()

                try:
                    await sky_op_process.wait_for_completion()
                except RuntimeError:
                    return "not ok"

                return "ok"

async def get_agents(account_id: str) -> List[Dict[str, Any]]:
    agents: List[Dict[str, Any]] = []
    memo: Dict[str, Any] = {}
    memo = await sky_status_task(memo, refresh=False)

    for cluster_status in memo["cluster_statuses"]:
        agent_id = cluster_status["cluster_hash"]
        agent = {
            "id": agent_id,
            "name": cluster_status["name"],
            "links": {
                f"/api/agents/{agent_id}/ap/v1/agent/tasks",
            },
            "status": cluster_status["status"],
        }

        agents.append(agent)

    return agents

async def update_agent(account_id: str, agent_id: str):
    agent = await get_agent(account_id, agent_id)
    agent_name = agent["name"]
    bucket_name: str = await create_minio_bucket(DEFAULT_BUCKET_NAME, ignore_exists=True)
    minio_storage_block = await create_minio_storage_block(
        account_id=account_id,
        agent_name=agent_name,
        bucket_folder=account_id,
        bucket_name=bucket_name,
    )

    await upload_directory_to_minio(
        minio_storage_block=minio_storage_block,
        local_path=f"{os.getcwd()}/app/workers/agents/{agent_name}",
        to_path=f"agents/{agent_name}"
    )

    await run_deployment(
        "serve-agent-flow/serve-agent-flow-deployment",
        idempotency_key=get_agent_deployment_idempotency_key(
            local_path=f"{os.getcwd()}/app/workers/agents/{agent_name}",
        ),
        parameters={
            "account_id": account_id,
            "agent_name": agent_name,
            "operation": "update",
        },
        timeout=0,
    )

async def on_startup():
    print(f'\n=== {__name__} on_startup (BEGIN) ===\n')

    # memo: Dict[str, Any] = {}
    # memo = await load_cloud_credentials(memo)
    # memo = await sky_check_task(memo)
    # memo = await sky_status_task(memo, refresh=True)
    # agents = await get_agents(DEFAULT_ACCOUNT_ID)

    # if not agents:
    #     await create_agent(DEFAULT_ACCOUNT_ID, DEFAULT_AGENT_NAME)

    # else:
    #     for agent in agents:
    #         await update_agent(DEFAULT_ACCOUNT_ID, agent["id"])

    print(f'\n=== {__name__} on_startup (END) ===\n')

async def on_shutdown():
    print(f'\n=== {__name__} on_shutdown (BEGIN) ===\n')
    print(f'\n=== {__name__} on_shutdown (END) ===\n')
