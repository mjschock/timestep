import logging
import os
from typing import Any, Dict, List, Optional

import httpx
import kubernetes
import sky
from agent_protocol import Step, Task
from agent_protocol.models import (
    StepRequestBody,
    Task,
    TaskListResponse,
    TaskRequestBody,
    TaskStepsListResponse,
)
from agent_protocol_client import (
    AgentApi,
    ApiClient,
    Configuration,
    StepRequestBody,
    TaskRequestBody,
)
from prefect import flow, get_run_logger, task
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
    # load_kubeconfig,
    upload_directory_to_minio,
)

DEFAULT_BUCKET_NAME="default"


# @flow(
#     log_prints=True,
#     timeout_seconds=10,
# )
async def create_agent(account_id: str, agent_name: str) -> dict[str, Any]:
    # logger: logging.Logger = get_run_logger()
    # agent: Dict[str, Any] = {
    #     "name": name,
    # }
    # memo: Dict[str, Any] = {}

    # memo = await load_cloud_credentials(memo)
    # memo = await sky_check_task(memo)
    # memo = await sky_status_task(memo)

    # agent_cluster_is_already_deployed = False

    # for cluster_status in memo["cluster_statuses"]:
    #     if cluster_status["name"] == name:
    #         agent_cluster_is_already_deployed = True

    #         break

    # if agent_cluster_is_already_deployed:
    #     logger.info("Agent cluster is already deployed")

    # else:
    #     logger.info("Launching agent cluster")
    #     memo = await sky_launch_task(name, memo)

    # memo = await sky_status_task(memo)

    # for cluster_status in memo["cluster_statuses"]:
    #     if cluster_status["name"] == name:
    #         agent["id"] = cluster_status["cluster_hash"] # TODO: use db to store agent id instead of cluster hash
    #         agent["cluster_status"] = cluster_status

    #         break

    # return agent

    bucket_name: str = await create_minio_bucket(DEFAULT_BUCKET_NAME, ignore_exists=True)
    minio_storage_block = await create_minio_storage_block(
        bucket_folder=account_id,
        bucket_name=bucket_name,
    )
    # print('local_path')
    # print(f"{os.getcwd()}/app/workflows/agents/{name}")
    uploaded_file_count: int = await upload_directory_to_minio(
        minio_storage_block=minio_storage_block,
        local_path=f"{os.getcwd()}/app/workflows/agents/{agent_name}",
        to_path=f"agents/{agent_name}"
    )
    # print('uploaded_file_count: ')
    # print(uploaded_file_count)
    deployment_ids: list = await deploy_agent(
        uploaded_file_count,
        account_id,
        agent_name,
        bucket_name,
    )

    for deployment_id in deployment_ids:
        print(f"Deployment ID: {deployment_id}")
        print("Running deployment, not waiting for completion")
        await run_deployment(
            deployment_id,
            timeout=0,
        )


# @flow(
#     log_prints=True,
# )
# async def create_agent_task(
#     agent_id,
#     input: Optional[StrictStr],
#     additional_input: Optional[Dict[str, Any]]
# # ) -> Dict[str, Any]:
# ) -> Task:
#     logger: logging.Logger = get_run_logger()
#     agent: Dict[str, Any] = {
#         "id": agent_id,
#     }
#     memo: Dict[str, Any] = {}
#     # task: Dict[str, Any] = {}

#     memo = await load_cloud_credentials(memo)
#     memo = await sky_check_task(memo)
#     memo = await sky_status_task(memo)

#     for cluster_status in memo["cluster_statuses"]:
#         # logger.info(cluster_status)

#         if cluster_status["cluster_hash"] == agent_id:
#             agent["name"] = cluster_status["name"]
#             # cluster_name_on_cloud = cluster_status["handle"].cluster_name_on_cloud
#             head_ip = cluster_status["handle"].head_ip

#             async with httpx.AsyncClient() as client:
#                 logger.info(f"GET http://{head_ip}:8000/livez") # TODO: move to it's own endpoint
#                 resp = await client.get(f"http://{head_ip}:8000/livez")
#                 assert resp.json() == "ok", f"{resp.json()} != ok"

#             async with httpx.AsyncClient() as client:
#                 logger.info(f"GET http://{head_ip}:8000/readyz") # TODO: move to it's own endpoint
#                 resp = await client.get(f"http://{head_ip}:8000/readyz")
#                 assert resp.json() == "ok", f"{resp.json()} != ok"

#             break

#     configuration = Configuration(host=f"http://{head_ip}:8000")

#     async with ApiClient(configuration) as api_client:
#         api_instance = AgentApi(api_client)

#         task_request_body = TaskRequestBody(
#             input=input,
#             additional_input=additional_input,
#         )

#         logger.info(f"POST http://{head_ip}:8000/ap/v1/agent/tasks")
#         task: Task = await api_instance.create_agent_task(
#             task_request_body=task_request_body
#         )

#     # async with httpx.AsyncClient(timeout=httpx.Timeout(None)) as client:
#     #     logger.info(f"GET http://{head_ip}:8000/v1/chat/completions")
#     #     resp = await client.get(f"http://{head_ip}:8000/v1/chat/completions")
#     #     logger.info("resp.json():")
#     #     logger.info(resp.json())

#         # assert resp.json() == "ok", f"{resp.json()} != ok"

#     return task


# @flow
# async def list_agent_tasks(agent_id: str) -> TaskListResponse:
#     logger: logging.Logger = get_run_logger()
#     agent: Dict[str, Any] = {
#         "id": agent_id,
#     }
#     memo: Dict[str, Any] = {}
#     # task: Dict[str, Any] = {}

#     memo = await load_cloud_credentials(memo)
#     memo = await sky_check_task(memo)
#     memo = await sky_status_task(memo)

#     for cluster_status in memo["cluster_statuses"]:
#         # logger.info(cluster_status)

#         if cluster_status["cluster_hash"] == agent_id:
#             agent["name"] = cluster_status["name"]
#             # cluster_name_on_cloud = cluster_status["handle"].cluster_name_on_cloud
#             head_ip = cluster_status["handle"].head_ip

#             break

#     configuration = Configuration(host=f"http://{head_ip}:8000")

#     async with ApiClient(configuration) as api_client:
#         api_instance = AgentApi(api_client)
#         logger.info(f"GET http://{head_ip}:8000/ap/v1/agent/tasks")
#         tasks = await api_instance.list_agent_tasks()

#     logger.info("tasks:")
#     logger.info(tasks)

#     return tasks


# @flow
# async def get_agent_task(agent_id: str, task_id: str) -> Task:
#     logger: logging.Logger = get_run_logger()
#     agent: Dict[str, Any] = {
#         "id": agent_id,
#     }
#     memo: Dict[str, Any] = {}
#     # task: Dict[str, Any] = {}

#     memo = await load_cloud_credentials(memo)
#     memo = await sky_check_task(memo)
#     memo = await sky_status_task(memo)

#     for cluster_status in memo["cluster_statuses"]:
#         # logger.info(cluster_status)

#         if cluster_status["cluster_hash"] == agent_id:
#             agent["name"] = cluster_status["name"]
#             # cluster_name_on_cloud = cluster_status["handle"].cluster_name_on_cloud
#             head_ip = cluster_status["handle"].head_ip

#             break

#     configuration = Configuration(host=f"http://{head_ip}:8000")

#     async with ApiClient(configuration) as api_client:
#         api_instance = AgentApi(api_client)

#         logger.info(f"GET http://{head_ip}:8000/ap/v1/agent/tasks/{task_id}")
#         task = await api_instance.get_agent_task(task_id=task_id)

#     logger.info("task:")
#     logger.info(task)

#     return task

# @flow
# async def list_agent_task_steps(agent_id: str, task_id: str, page_size: int = 10, current_page: int = 1) -> Task:
#     logger: logging.Logger = get_run_logger()
#     agent: Dict[str, Any] = {
#         "id": agent_id,
#     }
#     memo: Dict[str, Any] = {}
#     # task: Dict[str, Any] = {}

#     memo = await load_cloud_credentials(memo)
#     memo = await sky_check_task(memo)
#     memo = await sky_status_task(memo)

#     for cluster_status in memo["cluster_statuses"]:
#         # logger.info(cluster_status)

#         if cluster_status["cluster_hash"] == agent_id:
#             agent["name"] = cluster_status["name"]
#             # cluster_name_on_cloud = cluster_status["handle"].cluster_name_on_cloud
#             head_ip = cluster_status["handle"].head_ip

#             break

#     configuration = Configuration(host=f"http://{head_ip}:8000")

#     async with ApiClient(configuration) as api_client:
#         api_instance = AgentApi(api_client)

#         logger.info(f"GET http://{head_ip}:8000/ap/v1/agent/tasks/{task_id}/steps")
#         task_steps_list_response: TaskStepsListResponse = await api_instance.list_agent_task_steps(task_id=task_id, page_size=page_size, current_page=current_page)

#     logger.info("task_steps_list_response:")
#     logger.info(task_steps_list_response)

#     return task_steps_list_response

# @flow
# async def execute_agent_task_step(agent_id: str, task_id: str, body: StepRequestBody | None = None) -> Step:
#     logger: logging.Logger = get_run_logger()
#     agent: Dict[str, Any] = {
#         "id": agent_id,
#     }
#     memo: Dict[str, Any] = {}
#     # task: Dict[str, Any] = {}

#     memo = await load_cloud_credentials(memo)
#     memo = await sky_check_task(memo)
#     memo = await sky_status_task(memo)

#     for cluster_status in memo["cluster_statuses"]:
#         # logger.info(cluster_status)

#         if cluster_status["cluster_hash"] == agent_id:
#             agent["name"] = cluster_status["name"]
#             # cluster_name_on_cloud = cluster_status["handle"].cluster_name_on_cloud
#             head_ip = cluster_status["handle"].head_ip

#             break

#     configuration = Configuration(host=f"http://{head_ip}:8000")

#     async with ApiClient(configuration) as api_client:
#         api_instance = AgentApi(api_client)

#         logger.info(f"POST http://{head_ip}:8000/ap/v1/agent/tasks/{task_id}/steps")
#         step: Step = await api_instance.execute_agent_task_step(task_id=task_id, step_request_body=body)

#     logger.info("step:")
#     logger.info(step)

#     return step

# @flow
# async def get_agent_task_step(agent_id: str, task_id: str, step_id: str) -> Step:
#     logger: logging.Logger = get_run_logger()
#     agent: Dict[str, Any] = {
#         "id": agent_id,
#     }
#     memo: Dict[str, Any] = {}
#     # task: Dict[str, Any] = {}

#     memo = await load_cloud_credentials(memo)
#     memo = await sky_check_task(memo)
#     memo = await sky_status_task(memo)

#     for cluster_status in memo["cluster_statuses"]:
#         # logger.info(cluster_status)

#         if cluster_status["cluster_hash"] == agent_id:
#             agent["name"] = cluster_status["name"]
#             # cluster_name_on_cloud = cluster_status["handle"].cluster_name_on_cloud
#             head_ip = cluster_status["handle"].head_ip

#             break

#     configuration = Configuration(host=f"http://{head_ip}:8000")

#     async with ApiClient(configuration) as api_client:
#         api_instance = AgentApi(api_client)

#         logger.info(f"GET http://{head_ip}:8000/ap/v1/agent/tasks/{task_id}/steps/{step_id}")
#         step: Step = await api_instance.get_agent_task_step(task_id=task_id, step_id=step_id)

#     logger.info("step:")
#     logger.info(step)

#     return step

# @flow
async def delete_agent(account_id: str, agent_id: str) -> Dict[str, Any]:
    agent: Dict[str, Any] = {
        "id": agent_id,
    }
    memo: Dict[str, Any] = {}

    # memo = await load_cloud_credentials(memo)
    # memo = await sky_check_task(memo)
    # memo = await sky_status_task(memo)

    # for cluster_status in memo["cluster_statuses"]:

    #     if cluster_status["cluster_hash"] == agent_id:
    #         agent["name"] = cluster_status["name"]

    #         memo = await sky_down_task(agent["name"], memo)

    #         break

    # memo = await sky_status_task(memo)

    # return agent

    deployment_id = "serve-agent-flow/serve-agent-flow-deployment"

    resp = await run_deployment(
        deployment_id,
        # timeout=0,
        parameters={
            "account_id": account_id,
            # "agent_id": agent_id,
            "operation": "delete",
        },
    )

    # logger.info("resp:")
    # logger.info(resp)
    print("resp:")
    print(resp)

    return agent

# @flow
async def get_agent(account_id: str, agent_id: str) -> Dict[str, Any]:
    # logger: logging.Logger = get_run_logger()
    # agent: Dict[str, Any] = {
    #     "id": agent_id,
    # }
    memo: Dict[str, Any] = {}

    # memo = await load_cloud_credentials(memo)
    # memo = await sky_check_task(memo)
    # memo = await sky_status_task(memo)

    # for cluster_status in memo["cluster_statuses"]:
    #     logger.info(cluster_status)

    #     if cluster_status["cluster_hash"] == agent_id:
    #         agent["name"] = cluster_status["name"]
    #         agent["cluster_status"] = cluster_status
    #         agent["links"] = {
    #             "tasks": f"/api/agents/{agent_id}/ap/v1/agent/tasks",
    #         }

    #         break

    # memo = await sky_queue_task(agent["name"], memo)
    # agent["cluster_queue"] = memo["cluster_queue"]

    # logger.info(memo)

    # return agent

    # deployment_id = "serve-agent-flow/serve-agent-flow-deployment"

    # resp = await run_deployment(
    #     deployment_id,
    #     # timeout=0,
    #     parameters={
    #         "account_id": account_id,
    #         # "agent_id": agent_id,
    #         "operation": "read",
    #     },
    # )

    # # logger.info("resp:")
    # # logger.info(resp)
    # print("resp:")
    # print(resp)

    # return agent

    agents = await get_agents(account_id)

    for agent in agents:
        if agent["id"] == agent_id:
            agent_name = agent["name"]
            memo = await sky_queue_task(agent_name, memo)

            # agent["cluster_queue"] = memo["cluster_queue"]
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

            # async with httpx.AsyncClient() as client:
            #     resp = await client.get(f"http://{head_ip}:8000/readyz")
            #     assert resp.json() == "ok", f"{resp.json()} != ok"

    raise Exception(f"Agent {agent_id} not found")

# @flow
async def get_agent_readyz(account_id: str, agent_id: str):
    cluster_statuses = sky.core.status(refresh=True)

    for cluster_status in cluster_statuses:
        if cluster_status["cluster_hash"] == agent_id:
            head_ip = cluster_status["handle"].head_ip

            async with httpx.AsyncClient() as client:
                resp = await client.get(f"http://{head_ip}:8000/readyz")
                assert resp.json() == "ok", f"{resp.json()} != ok"
                # return resp.json()

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
                    # print(e)
                    return "not ok"

                return "ok"
                # return await sky_op_process.fetch_result()

            # async with httpx.AsyncClient() as client:
            #     resp = await client.get(f"http://{head_ip}:8000/readyz")
            #     assert resp.json() == "ok", f"{resp.json()} != ok"

    #     async with ShellOperation(
    #         commands=[
    #             # f'URL=http://{head_ip}:8000 bash -c "$(curl -fsSL https://agentprotocol.ai/test.sh)"',
    #             # f"URL=http://{head_ip}:8000 bash -c test.sh",
    #             # f"URL=http://{head_ip}:8000 ls -al",
    #             # "ls -al /bin",
    #             # f"URL=http://{head_ip}:8000 bash test.sh",
    #             "curl -fsSL https://agentprotocol.ai/test.sh > test.sh",
    #             "dos2unix test.sh",
    #             f"URL=http://{head_ip}:8000 bash test.sh",
    #         ],
    #         shell="bash",
    #         # working_dir=f"{os.getcwd()}/app/workflows",
    #         # working_dir=f"{os.getcwd()}/tests",
    #         working_dir="/tmp",
    #     ) as sky_op:
    #         sky_op_process = await sky_op.trigger()
    #         await sky_op_process.wait_for_completion()

    # memo = await load_cloud_credentials(memo)
    # memo = await sky_check_task(memo)
    # memo = await sky_status_task(memo)

    # for cluster_status in memo["cluster_statuses"]:
    #     logger.info(cluster_status)

    #     if cluster_status["cluster_hash"] == agent_id:
    #         agent["name"] = cluster_status["name"]
    #         agent["cluster_status"] = cluster_status
    #         agent["links"] = {
    #             "tasks": f"/api/agents/{agent_id}/ap/v1/agent/tasks",
    #         }

    #         break

    # memo = await sky_queue_task(agent["name"], memo)
    # agent["cluster_queue"] = memo["cluster_queue"]

    # logger.info(memo)

    # return agent

    # deployment_id = "serve-agent-flow/serve-agent-flow-deployment"

    # resp = await run_deployment(
    #     deployment_id,
    #     # timeout=0,
    #     parameters={
    #         "account_id": account_id,
    #         "ap_check": True,
    #         # "agent_id": agent_id,
    #         "operation": "read",
    #     },
    # )

    # return resp

    # logger.info("resp:")
    # logger.info(resp)
    # print("resp:")
    # print(resp)

    # raise Exception(f"Agent {agent_id} not found")

#     agent: Dict[str, Any] = {
#         "id": agent_id,
#     }
#     memo: Dict[str, Any] = {}
#     # task: Dict[str, Any] = {}

#     memo = await load_cloud_credentials(memo)
#     memo = await sky_check_task(memo)
#     memo = await sky_status_task(memo)

#     for cluster_status in memo["cluster_statuses"]:
#         if cluster_status["cluster_hash"] == agent_id:
#             agent["name"] = cluster_status["name"]
#             head_ip = cluster_status["handle"].head_ip

#             break

#     # async with httpx.AsyncClient() as client:
#     #     logger.info(f"GET http://{head_ip}:8000/readyz") # TODO: move to it's own endpoint
#     #     resp = await client.get(f"http://{head_ip}:8000/readyz")
#     #     assert resp.json() == "ok", f"{resp.json()} != ok"

#     # URL=http://localhost:8000 bash -c "$(curl -fsSL https://agentprotocol.ai/test.sh)"

#     async with ShellOperation(
#         commands=[
#             # f'URL=http://{head_ip}:8000 bash -c "$(curl -fsSL https://agentprotocol.ai/test.sh)"',
#             # f"URL=http://{head_ip}:8000 bash -c test.sh",
#             # f"URL=http://{head_ip}:8000 ls -al",
#             # "ls -al /bin",
#             # f"URL=http://{head_ip}:8000 bash test.sh",
#             "curl -fsSL https://agentprotocol.ai/test.sh > test.sh",
#             "dos2unix test.sh",
#             f"URL=http://{head_ip}:8000 bash test.sh",
#         ],
#         shell="bash",
#         # working_dir=f"{os.getcwd()}/app/workflows",
#         # working_dir=f"{os.getcwd()}/tests",
#         working_dir="/tmp",
#     ) as sky_op:
#         sky_op_process = await sky_op.trigger()
#         await sky_op_process.wait_for_completion()

#     return agent

# @flow
async def get_agents(account_id: str) -> Dict[str, Any]:
    # logger: logging.Logger = get_run_logger()
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

# @flow
async def update_agent(account_id: str, agent_id: str) -> Dict[str, Any]:
    # logger: logging.Logger = get_run_logger()
    # agent: Dict[str, Any] = {
    #     "id": agent_id,
    # }
    # memo: Dict[str, Any] = {}

    # memo = await load_cloud_credentials(memo)
    # memo = await sky_check_task(memo)
    # memo = await sky_status_task(memo)

    # for cluster_status in memo["cluster_statuses"]:
    #     if cluster_status["cluster_hash"] == agent_id:
    #         agent["name"] = cluster_status["name"]

    #         break

    # logger.info("Updating agent cluster")
    # memo = await sky_exec_task(agent["name"], memo)
    # memo = await sky_status_task(memo)

    # for cluster_status in memo["cluster_statuses"]:
    #     if cluster_status["cluster_hash"] == agent_id:
    #         agent["cluster_status"] = cluster_status

    #         break

    # return agent

    # agent: Dict[str, Any] = {
    #     "id": agent_id,
    # }
    # memo: Dict[str, Any] = {}

    # memo = await load_cloud_credentials(memo)
    # memo = await sky_check_task(memo)
    # memo = await sky_status_task(memo)

    # for cluster_status in memo["cluster_statuses"]:

    #     if cluster_status["cluster_hash"] == agent_id:
    #         agent["name"] = cluster_status["name"]

    #         memo = await sky_down_task(agent["name"], memo)

    #         break

    # memo = await sky_status_task(memo)

    # return agent

    agent = await get_agent(account_id, agent_id)

    agent_name = agent["name"]

    bucket_name: str = await create_minio_bucket(DEFAULT_BUCKET_NAME, ignore_exists=True)
    minio_storage_block = await create_minio_storage_block(
        bucket_folder=account_id,
        bucket_name=bucket_name,
    )
    # print('local_path')
    # print(f"{os.getcwd()}/app/workflows/agents/{name}")
    uploaded_file_count: int = await upload_directory_to_minio(
        minio_storage_block=minio_storage_block,
        local_path=f"{os.getcwd()}/app/workflows/agents/{agent_name}",
        to_path=f"agents/{agent_name}"
    )

    deployment_id = "serve-agent-flow/serve-agent-flow-deployment"

    resp = await run_deployment(
        deployment_id,
        # timeout=0,
        parameters={
            "account_id": account_id,
            # "agent_id": agent_id,
            "operation": "update",
        },
        timeout=0,
    )

    # logger.info("resp:")
    # logger.info(resp)
    # print("resp:")
    # print(resp)

    return agent

# @task
# async def load_cloud_credentials(memo: Dict[str, Any]):
#     logger = get_run_logger()

#     try:
#         kubernetes.config.load_incluster_config()
#         memo = load_kubeconfig(memo)

#     except kubernetes.config.config_exception.ConfigException as e:
#         logger.info(e)

#     return memo

# @task
# async def sky_cancel_task(
#     name: str,
#     all_jobs: bool = False,
#     job_ids: Optional[List[int]] = None,
#     memo: Dict[str, Any] = None
# ):
#     sky.core.cancel(cluster_name=name, all=all_jobs, job_ids=job_ids)  # noqa: E501

#     return memo

# @task
# async def sky_check_task(memo: Dict[str, Any]):
#     logger = get_run_logger()

#     sky.check.check()

#     enabled_clouds: List[sky.clouds.Cloud] = sky.global_user_state.get_enabled_clouds()
#     enabled_storage_clouds: List[
#         str
#     ] = sky.global_user_state.get_enabled_storage_clouds()

#     logger.info("enabled_clouds: %s", enabled_clouds)
#     logger.info("enabled_storage_clouds: %s", enabled_storage_clouds)

#     # memo["enabled_clouds"] = enabled_clouds
#     # memo["enabled_storage_clouds"] = enabled_storage_clouds

#     return memo

# @task
# async def sky_status_task(memo: Dict[str, Any]):
#     # logger: logging.Logger = get_run_logger()

#     # async with ShellOperation(
#     #     commands=[
#     #         f"sky status",
#     #     ],
#     #     # working_dir="workflows",
#     #     # working_dir=f"{cwd}/app/api/routers/workflows",
#     # ) as sky_op:
#     #     sky_op_process = await sky_op.trigger()
#     #     await sky_op_process.wait_for_completion()

#     memo["cluster_statuses"]: List[Dict[str, Any]] = sky.core.status(refresh=True)

#     return memo

# @task
# async def sky_launch_task(name: str, memo: Dict[str, Any]):
#     minio_endpoint = os.environ["MINIO_ENDPOINT"]
#     minio_root_user = os.environ["MINIO_ROOT_USER"]
#     minio_root_password = os.environ["MINIO_ROOT_PASSWORD"]
#     openai_api_key = os.environ["OPENAI_API_KEY"]

#     async with ShellOperation(
#         commands=[
#             f"""sky launch \
#                 --cluster {name} \
#                 --detach-setup \
#                 --detach-run \
#                 --env MINIO_ENDPOINT={minio_endpoint} \
#                 --env MINIO_ROOT_USER={minio_root_user} \
#                 --env MINIO_ROOT_PASSWORD={minio_root_password} \
#                 --env OPENAI_API_KEY={openai_api_key} \
#                 --yes agents/{name}/serve.yaml
#             """,
#         ],
#         working_dir=f"{os.getcwd()}/app/workflows",
#     ) as sky_op:
#         sky_op_process = await sky_op.trigger()
#         await sky_op_process.wait_for_completion()

#     return memo

# @task
# async def sky_exec_task(name: str, memo: Dict[str, Any]):
#     minio_endpoint = os.environ["MINIO_ENDPOINT"]
#     minio_root_user = os.environ["MINIO_ROOT_USER"]
#     minio_root_password = os.environ["MINIO_ROOT_PASSWORD"]
#     openai_api_key = os.environ["OPENAI_API_KEY"]

#     sky.core.cancel(cluster_name=name, all=True)

#     async with ShellOperation(
#         commands=[
#             f"""sky exec {name} \
#                 --detach-run \
#                 --env MINIO_ENDPOINT={minio_endpoint} \
#                 --env MINIO_ROOT_USER={minio_root_user} \
#                 --env MINIO_ROOT_PASSWORD={minio_root_password} \
#                 --env OPENAI_API_KEY={openai_api_key} \
#                 agents/{name}/serve.yaml
#             """,
#         ],
#         working_dir=f"{os.getcwd()}/app/workflows",
#     ) as sky_op:
#         sky_op_process = await sky_op.trigger()
#         await sky_op_process.wait_for_completion()

#     return memo

# @task
# async def sky_down_task(name: str, memo: Dict[str, Any]):
#     async with ShellOperation(
#         commands=[
#             f"sky down {name} --purge --yes"
#         ],
#         working_dir=f"{os.getcwd()}/app/workflows",
#     ) as sky_op:
#         sky_op_process = await sky_op.trigger()
#         await sky_op_process.wait_for_completion()

#     return memo

# @task
# async def sky_queue_task(name: str, memo: Dict[str, Any]):
#     memo["cluster_queue"]: List[dict] = sky.core.queue(cluster_name=name)  # noqa: E501

#     return memo
