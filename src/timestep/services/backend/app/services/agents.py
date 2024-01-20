import os
from typing import Any, Dict, List, Optional

import httpx
import sky
from agent_protocol import Step, Task
from agent_protocol.models import (
    StepRequestBody,
    TaskListResponse,
    TaskRequestBody,
    TaskStepsListResponse,
)
from agent_protocol_client import (
    AgentApi,
    ApiClient,
    Configuration,
)
from prefect.deployments.deployments import run_deployment
from prefect_shell import ShellOperation
from pydantic import StrictStr

from app.services.utils import (
    create_minio_bucket,
    create_minio_storage_block,
    deploy_agent,
    load_cloud_credentials,
    sky_check_task,
    sky_queue_task,
    sky_status_task,
    upload_directory_to_minio,
)

DEFAULT_BUCKET_NAME="default"


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
        local_path=f"{os.getcwd()}/app/workflows/agents/{agent_name}",
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
            timeout=0,
        )

async def create_agent_task(
    agent_id,
    input: Optional[StrictStr],
    additional_input: Optional[Dict[str, Any]]
) -> Task:
    agent: Dict[str, Any] = {
        "id": agent_id,
    }
    memo: Dict[str, Any] = {}

    memo = await load_cloud_credentials(memo)
    memo = await sky_check_task(memo)
    memo = await sky_status_task(memo)

    for cluster_status in memo["cluster_statuses"]:

        if cluster_status["cluster_hash"] == agent_id:
            agent["name"] = cluster_status["name"]
            head_ip = cluster_status["handle"].head_ip

            break

    configuration = Configuration(host=f"http://{head_ip}:8000")

    async with ApiClient(configuration) as api_client:
        api_instance = AgentApi(api_client)
        task_request_body = TaskRequestBody(
            input=input,
            additional_input=additional_input,
        )
        task: Task = await api_instance.create_agent_task(
            task_request_body=task_request_body
        )

    return task

async def list_agent_tasks(agent_id: str) -> TaskListResponse:
    agent: Dict[str, Any] = {
        "id": agent_id,
    }
    memo: Dict[str, Any] = {}

    memo = await load_cloud_credentials(memo)
    memo = await sky_check_task(memo)
    memo = await sky_status_task(memo)

    for cluster_status in memo["cluster_statuses"]:

        if cluster_status["cluster_hash"] == agent_id:
            agent["name"] = cluster_status["name"]
            head_ip = cluster_status["handle"].head_ip

            break

    configuration = Configuration(host=f"http://{head_ip}:8000")

    async with ApiClient(configuration) as api_client:
        api_instance = AgentApi(api_client)
        tasks = await api_instance.list_agent_tasks()

    return tasks

async def get_agent_task(agent_id: str, task_id: str) -> Task:
    agent: Dict[str, Any] = {
        "id": agent_id,
    }
    memo: Dict[str, Any] = {}

    memo = await load_cloud_credentials(memo)
    memo = await sky_check_task(memo)
    memo = await sky_status_task(memo)

    for cluster_status in memo["cluster_statuses"]:

        if cluster_status["cluster_hash"] == agent_id:
            agent["name"] = cluster_status["name"]
            head_ip = cluster_status["handle"].head_ip

            break

    configuration = Configuration(host=f"http://{head_ip}:8000")

    async with ApiClient(configuration) as api_client:
        api_instance = AgentApi(api_client)
        task = await api_instance.get_agent_task(task_id=task_id)

    return task

async def list_agent_task_steps(
        agent_id: str,
        task_id: str,
        page_size: int = 10,
        current_page: int = 1
) -> Task:
    agent: Dict[str, Any] = {
        "id": agent_id,
    }
    memo: Dict[str, Any] = {}

    memo = await load_cloud_credentials(memo)
    memo = await sky_check_task(memo)
    memo = await sky_status_task(memo)

    for cluster_status in memo["cluster_statuses"]:

        if cluster_status["cluster_hash"] == agent_id:
            agent["name"] = cluster_status["name"]
            head_ip = cluster_status["handle"].head_ip

            break

    configuration = Configuration(host=f"http://{head_ip}:8000")

    async with ApiClient(configuration) as api_client:
        api_instance = AgentApi(api_client)
        task_steps_list_response: TaskStepsListResponse = await api_instance.list_agent_task_steps(  # noqa: E501
            task_id=task_id,
            page_size=page_size,
            current_page=current_page,
        )

    return task_steps_list_response

async def execute_agent_task_step(
        agent_id: str,
        task_id: str,
        body: StepRequestBody | None = None
) -> Step:
    agent: Dict[str, Any] = {
        "id": agent_id,
    }
    memo: Dict[str, Any] = {}

    memo = await load_cloud_credentials(memo)
    memo = await sky_check_task(memo)
    memo = await sky_status_task(memo)

    for cluster_status in memo["cluster_statuses"]:

        if cluster_status["cluster_hash"] == agent_id:
            agent["name"] = cluster_status["name"]
            head_ip = cluster_status["handle"].head_ip

            break

    configuration = Configuration(host=f"http://{head_ip}:8000")

    async with ApiClient(configuration) as api_client:
        api_instance = AgentApi(api_client)
        step: Step = await api_instance.execute_agent_task_step(
            task_id=task_id,
            step_request_body=body
        )

    return step

async def get_agent_task_step(agent_id: str, task_id: str, step_id: str) -> Step:
    agent: Dict[str, Any] = {
        "id": agent_id,
    }
    memo: Dict[str, Any] = {}

    memo = await load_cloud_credentials(memo)
    memo = await sky_check_task(memo)
    memo = await sky_status_task(memo)

    for cluster_status in memo["cluster_statuses"]:
        if cluster_status["cluster_hash"] == agent_id:
            agent["name"] = cluster_status["name"]
            head_ip = cluster_status["handle"].head_ip

            break

    configuration = Configuration(host=f"http://{head_ip}:8000")

    async with ApiClient(configuration) as api_client:
        api_instance = AgentApi(api_client)
        step: Step = await api_instance.get_agent_task_step(task_id=task_id, step_id=step_id)

    return step

async def delete_agent(account_id: str, agent_id: str) -> Dict[str, Any]:
    agent: Dict[str, Any] = {
        "id": agent_id,
    }
    deployment_id = "serve-agent-flow/serve-agent-flow-deployment"

    await run_deployment(
        deployment_id,
        parameters={
            "account_id": account_id,
            "operation": "delete",
        },
    )

    return agent

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
    cluster_statuses = sky.core.status(refresh=True)

    for cluster_status in cluster_statuses:
        if cluster_status["cluster_hash"] == agent_id:
            head_ip = cluster_status["handle"].head_ip

            async with httpx.AsyncClient() as client:
                resp = await client.get(f"http://{head_ip}:8000/livez")
                assert resp.json() == "ok", f"{resp.json()} != ok"
                return resp.json()

    raise Exception(f"Agent {agent_id} not found")

async def get_agent_readyz(account_id: str, agent_id: str):
    cluster_statuses = sky.core.status(refresh=True)

    for cluster_status in cluster_statuses:
        if cluster_status["cluster_hash"] == agent_id:
            head_ip = cluster_status["handle"].head_ip

            async with httpx.AsyncClient() as client:
                resp = await client.get(f"http://{head_ip}:8000/readyz")
                assert resp.json() == "ok", f"{resp.json()} != ok"

            async with ShellOperation(
                commands=[
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

async def get_agents(account_id: str) -> Dict[str, Any]:
    agents: List[Dict[str, Any]] = []
    memo: Dict[str, Any] = {}

    memo = await load_cloud_credentials(memo)
    memo = await sky_check_task(memo)
    memo = await sky_status_task(memo)

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

async def update_agent(account_id: str, agent_id: str) -> dict[str, Any]:
    agent = await get_agent(account_id, agent_id)
    agent_name = agent["name"]
    bucket_name: str = await create_minio_bucket(DEFAULT_BUCKET_NAME, ignore_exists=True)
    minio_storage_block = await create_minio_storage_block(
        bucket_folder=account_id,
        bucket_name=bucket_name,
    )
    await upload_directory_to_minio(
        minio_storage_block=minio_storage_block,
        local_path=f"{os.getcwd()}/app/workflows/agents/{agent_name}",
        to_path=f"agents/{agent_name}"
    )

    deployment_id = "serve-agent-flow/serve-agent-flow-deployment"

    await run_deployment(
        deployment_id,
        parameters={
            "account_id": account_id,
            "operation": "update",
        },
        timeout=0,
    )

    return agent
