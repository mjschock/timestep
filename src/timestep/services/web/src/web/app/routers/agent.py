import requests
from fastapi import APIRouter, Response

# from web.app.local_dev import app as local_dev
# from ..services.agent import app as agent_deployment
from starlette.background import BackgroundTask

# from ..workflows.agent import deploy_flow
# from ..services import agent_deployment
# from ..services.agent import deploy_create_agent_flow
from ..services import agent as agent_service

router = APIRouter(
    prefix="/api/agents",
    tags=["agents"],
    # dependencies=[Depends(get_current_user)],
    responses={404: {"description": "Not found"}},
)


# @flow(log_prints=True)
# def get_repo_info(repo_name: str = "PrefectHQ/prefect"):
#     url = f"https://api.github.com/repos/{repo_name}"
#     response = httpx.get(url)
#     response.raise_for_status()
#     repo = response.json()
#     print(f"{repo_name} repository statistics 🤓:")
#     print(f"Stars 🌠 : {repo['stargazers_count']}")
#     print(f"Forks 🍴 : {repo['forks_count']}")

# async def create_agent_flow(agent_config: AgentConfig, agent_service: AgentsService):
# @flow
# def deploy_create_agent_flow():
#     print("create_agent_flow")

#     # deploy_flow()

# print('agent_config: ', agent_config)
# agent_id = await agent_service.create_agent()

# minio_endpoint_url = f'http://{os.getenv("MINIO_ENDPOINT")}'
# minio_credentials_block = MinIOCredentials(
#     aws_client_parameters={
#         "endpoint_url": minio_endpoint_url,
#         # "use_ssl": False,
#     },
#     minio_root_user=os.getenv("MINIO_ROOT_USER"),
#     minio_root_password=os.getenv("MINIO_ROOT_PASSWORD"),
# )

# minio_credentials_block.save("minio-credentials", overwrite=True)

# minio_storage_block = S3Bucket(
#     bucket_name="default",
#     bucket_folder="test",
#     credentials=minio_credentials_block,
# )

# minio_storage_block.save("minio-storage", overwrite=True)

# # uploaded_file_count = minio_storage_block.put_directory(
# #     # ignore_file=ignore_file, to_path=self.path
# # )

# flow.from_source(
#     source=minio_storage_block,
#     entrypoint="flows.py:my_flow",
# ).deploy(
#     name="my-first-deployment",
#     build=False,
#     # image=DeploymentImage(
#     #     name="prefecthq/prefect",
#     #     tag="2.14.6-python3.11-kubernetes",
#     #     # dockerfile="Dockerfile"
#     # ),
#     push=False,
#     work_pool_name="default-worker-pool",
# )

# get_repo_info.deploy(
#     name="my-first-deployment",
#     build=False,
#     # image=DeploymentImage(
#     #     name="prefecthq/prefect",
#     #     tag="2.14.6-python3.11-kubernetes",
#     #     # dockerfile="Dockerfile"
#     # ),
#     push=False,
#     work_pool_name="default-worker-pool",
# )

# await deploy(
#     buy.to_deployment(
#         name="create-agent-deployment",
#     ),
#     build=False,
#     # image="prefecthq/prefect:2.14.6-python3.11-kubernetes",
#     push=False,
#     work_pool_name="default-worker-pool",
# )

#     runtime_env = RuntimeEnv(
#         pip=[
#             # "accelerate>=0.16.0",
#             f"cloudpickle=={cloudpickle.__version__}",
#             f"einops=={einops.__version__}",
#             # "numpy<1.24",  # remove when mlflow updates beyond 2.2
#             # f"prefect_ray=={prefect_ray.__version__}",
#             f"pydantic=={pydantic.__version__}",
#             f"torch=={torch.__version__.replace('+cpu', '')}",
#             f"transformers=={transformers.__version__}",
#         ],
#         # env_vars={"ONEDNN_MAX_CPU_ISA": "AVX512_CORE_AMX"}
#     )

# #     # https://docs.ray.io/en/releases-2.9.0/ray-core/api/doc/ray.init.html
# #     # TODO: use RAY_ADDRESS
#     client_context: ClientContext = ray.init(
#         address="ray://ray-cluster-kuberay-head-svc.default.svc.cluster.local:10001",
#         runtime_env=runtime_env,
#     )

#     # return agent_id
#     print('Creating agent deployment...')
#     handle: DeploymentHandle = serve.run(agent_deployment, host="0.0.0.0")
#     print('Agent deployment created.')

#     print('Testing agent deployment...')
#     response: DeploymentResponse = handle.say_hello.remote(name="Ray")
#     result = await response
#     print('Received response from agent deployment: ', result)


@router.post(
    "",
    responses={
        202: {"description": "Agent created"},
        403: {"description": "Operation forbidden"},
    },
)
async def create_agent(
    # agent_config: AgentConfig,
    # agent_service: Annotated[AgentsService, Depends(get_agent_service)],
):
    background_task: BackgroundTask = BackgroundTask(
        # func=deploy_create_agent_flow,
        func=agent_service.create_agent,
        # agent_config=agent_config,
        # agent_service=agent_service,
    )

    return Response(
        background=background_task,
        status_code=202,
    )


@router.get("/hello2")
async def hello2(name: str = "Ray"):
    response = requests.get(
        "http://ray-cluster-kuberay-head-svc.default.svc.cluster.local:8000/",
        params={"name": name},  # noqa: E501
    ).json()

    return {
        "message": response,
    }
