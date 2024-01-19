import base64
import logging
import os
from typing import Any, Dict, List

import httpx
import kubernetes
import prefect_aws
import prefect_shell

# import s3fs
import sky
import yaml
from fastapi import APIRouter, Depends, HTTPException, Request, status
from fastapi.responses import StreamingResponse
from llama_index.agent import AgentRunner, OpenAIAgent, Task
from llama_index.chat_engine.types import BaseChatEngine
from llama_index.llms.base import ChatMessage
from llama_index.llms.types import MessageRole
from llama_index.schema import ImageDocument

# from minio import Minio
from prefect import deploy, flow, get_run_logger, task

# from prefect.blocks.system import Secret
# from prefect.deployments.deployments import run_deployment
# from prefect.deployments.runner import DeploymentImage
# from prefect.runner.runner import RunnerDeployment
# from prefect.runner.storage import RemoteStorage
# from prefect_aws import AwsClientParameters, MinIOCredentials, S3Bucket
from prefect_shell import ShellOperation
from pydantic import BaseModel, SecretStr

from app.engine.index import get_chat_engine
from app.utils.index import get_agent, get_chat_agent

logger = logging.getLogger("uvicorn")

chat_router = r = APIRouter()


class _Message(BaseModel):
    role: MessageRole
    content: str


class _ChatData(BaseModel):
    messages: List[_Message]


# @task
# async def create_minio_bucket(bucket_name: str, ignore_exists: bool = False) -> str:
#     minio_endpoint = os.getenv("MINIO_ENDPOINT")
#     minio_client = Minio(
#         minio_endpoint,
#         access_key=os.getenv("MINIO_ROOT_USER"),
#         secret_key=os.getenv("MINIO_ROOT_PASSWORD"),
#         secure=False,
#     )

#     if minio_client.bucket_exists(bucket_name):
#         if ignore_exists:
#             return bucket_name

#         else:
#             raise Exception(f"Bucket {bucket_name} already exists")

#     minio_client.make_bucket(bucket_name)

#     return bucket_name


# # @task
# # async def create_minio_storage_block(
# #     bucket_folder: str,
# #     bucket_name: str,
# # ):
# #     minio_endpoint_url = f'http://{os.getenv("MINIO_ENDPOINT")}'
# #     minio_storage_block = S3Bucket(
# #         bucket_folder=bucket_folder,
# #         bucket_name=bucket_name,
# #         credentials=MinIOCredentials(
# #             aws_client_parameters=AwsClientParameters(
# #                 endpoint_url=minio_endpoint_url,
# #                 verify=False,
# #                 use_ssl=False,
# #             ),
# #             minio_root_user=os.getenv("MINIO_ROOT_USER"),
# #             minio_root_password=SecretStr(os.getenv("MINIO_ROOT_PASSWORD")),
# #         ),
# #     )

# #     await minio_storage_block.save("minio-storage", overwrite=True)

# #     return await S3Bucket.load("minio-storage")

# # @task
# # async def upload_directory_to_minio(
# #     minio_storage_block: S3Bucket,
# #     local_path: str,
# #     to_path: str,
# # ) -> int:
# #     return await minio_storage_block.put_directory(
# #         local_path=f"{os.getcwd()}/src/web/app/workflows",
# #         to_path="workflows",
# #     )

# # @task(
# #     timeout_seconds=10,
# # )
# # async def deploy_agent(
# #     uploaded_file_count: int,
# # ):
# #     minio_endpoint = os.getenv("MINIO_ENDPOINT")
# #     minio_endpoint_url = f"http://{minio_endpoint}"
# #     minio_root_user_secret_block = Secret(value=SecretStr(os.getenv("MINIO_ROOT_USER")))
# #     minio_root_password_secret_block = Secret(
# #         value=SecretStr(os.getenv("MINIO_ROOT_PASSWORD"))
# #     )

# #     await minio_root_user_secret_block.save("minio-root-user", overwrite=True)
# #     await minio_root_password_secret_block.save("minio-root-password", overwrite=True)

# #     storage = RemoteStorage(
# #         url="s3://default/agent",
# #         key=minio_root_user_secret_block,
# #         secret=minio_root_password_secret_block,
# #         client_kwargs={
# #             "endpoint_url": minio_endpoint_url,
# #             "verify": False,
# #             "use_ssl": False,
# #         },
# #     )

# #     deployment: RunnerDeployment = RunnerDeployment(
# #         flow_name="agent-flow",
# #         entrypoint="workflows/agents.py:deploy_agent_flow",
# #         job_variables={
# #             "env": {
# #                 "EXTRA_PIP_PACKAGES": f"""
# #                     fastapi=={fastapi.__version__}
# #                     prefect-aws=={prefect_aws.__version__}
# #                     prefect-shell=={prefect_shell.__version__}
# #                     s3fs=={s3fs.__version__}
# #                     skypilot-nightly[kubernetes]=={sky.__version__}
# #                 """,
# #                 "KUBECONTEXT": os.getenv("KUBECONTEXT"),
# #                 "MINIO_ENDPOINT": os.getenv("MINIO_ENDPOINT"),
# #                 "PRIMARY_DOMAIN_NAME": os.getenv("PRIMARY_DOMAIN_NAME"),
# #             },
# #             "service_account_name": "prefect-worker-job-service-account",
# #         },
# #         name="agent-flow-deployment",
# #         parameters={
# #             "model_ids": ["phi:latest"]
# #         },
# #         storage=storage,
# #         work_pool_name="default-worker-pool",
# #         work_queue_name="default",
# #     )

# #     deployment_ids: list = await deploy(
# #         deployment,
# #         build=False,
# #         image=DeploymentImage(
# #             name="registry.gitlab.com/timestep-ai/timestep/web",
# #             tag="latest",
# #         ),
# #         push=False,
# #         work_pool_name="default-worker-pool",
# #     )

# #     return deployment_ids

# # @flow(
# #     timeout_seconds=10,
# # )
# # async def create_agent(bucket_folder="agent", bucket_name="default"):
# #     bucket_name: str = await create_minio_bucket(bucket_name, ignore_exists=True)
# #     minio_storage_block = await create_minio_storage_block(
# #         bucket_folder=bucket_folder,
# #         bucket_name=bucket_name,
# #     )
# #     uploaded_file_count: int = await upload_directory_to_minio(
# #         minio_storage_block=minio_storage_block,
# #         local_path=f"{os.getcwd()}/src/web/app/workflows",
# #         to_path="agent",
# #     )
# #     deployment_ids: list = await deploy_agent(
# #         uploaded_file_count,
# #     )

# #     for deployment_id in deployment_ids:
# #         print(f"Deployment ID: {deployment_id}")
# #         print("Running deployment, not waiting for completion")
# #         await run_deployment(
# #             deployment_id,
# #             timeout=0,
# #         )

# @r.on_event("startup")
# async def startup():
#     logger = logging.getLogger("uvicorn")
#     logger.warning("Starting up chat router")

# #     # await create_agent()
#     await deploy_agent_flow()

@r.post("")
async def chat(
    request: Request, # request.auth, .session, .user AuthenticationMiddleware and SessionMiddleware
    data: _ChatData,
    # chat_engine: BaseChatEngine = Depends(get_chat_engine),
    # agent: OpenAIAgent = Depends(get_agent),
    # agent: OpenAIAgent = Depends(get_agent),
    # agent: AgentRunner = Depends(get_agent),
    agent: AgentRunner = Depends(get_chat_agent),
):
    # check preconditions and get last message
    if len(data.messages) == 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No messages provided",
        )

    last_message = data.messages.pop()

    if last_message.role != MessageRole.USER:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Last message must be from user",
        )

    # convert messages coming from the request to type ChatMessage
    messages = [
        ChatMessage(
            role=m.role,
            content=m.content,
        )
        for m in data.messages # NOTE: the last message is not included
    ]

    # query chat engine
    logger.info("Querying chat engine")
    # response = chat_engine.stream_chat(last_message.content, messages)
    response = agent.stream_chat(last_message.content, messages)

    # stream response
    async def event_generator():
        queue = agent.callback_manager.handlers[0].queue

        while len(queue) > 0:
            item = queue.pop(0)
            yield item

        for token in response.response_gen:
            # If client closes connection, stop sending events
            if await request.is_disconnected():
                break

            yield token

    return StreamingResponse(event_generator(), media_type="text/plain")

@r.post("/steps")
async def execute(
    request: Request, # request.auth, .session, .user AuthenticationMiddleware and SessionMiddleware
    data: _ChatData,
    # chat_engine: BaseChatEngine = Depends(get_chat_engine),
    # agent: OpenAIAgent = Depends(get_agent),
    # agent: OpenAIAgent = Depends(get_agent),
    agent: AgentRunner = Depends(get_agent),
):
    # check preconditions and get last message
    if len(data.messages) == 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No messages provided",
        )

    last_message = data.messages.pop()

    if last_message.role != MessageRole.USER:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Last message must be from user",
        )

    # convert messages coming from the request to type ChatMessage
    messages = [
        ChatMessage(
            role=m.role,
            content=m.content,
        )
        for m in data.messages # NOTE: the last message is not included
    ]

    query_str = last_message.content
    logger.info(f"query_str: {query_str}")

    image_document = ImageDocument(image_path="data/dev_day.png")

    task = agent.create_task(
        query_str,
        extra_state={"image_docs": [image_document]},
    )

    def execute_step(agent: AgentRunner, task: Task):
        step_output = agent.run_step(task.task_id)
        if step_output.is_last:
            response = agent.finalize_response(task.task_id)
            print(f"> Agent finished: {str(response)}")
            return response
        else:
            return None

    def execute_steps(agent: AgentRunner, task: Task):
        response = execute_step(agent, task)
        while response is None:
            response = execute_step(agent, task)
        return response

    response = execute_step(agent, task)
    logger.info(f"response: {response}")

    return response
