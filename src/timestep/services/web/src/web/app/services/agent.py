# # Filename: local_dev.py
# from starlette.requests import Request

# from ray import serve
# from ray.serve.handle import DeploymentHandle, DeploymentResponse


# @serve.deployment
# class Doubler:
#     def double(self, s: str):
#         return s + " " + s


# @serve.deployment
# class HelloDeployment:
#     def __init__(self, doubler: DeploymentHandle):
#         self.doubler = doubler

#     async def say_hello_twice(self, name: str):
#         return await self.doubler.double.remote(f"Hello, {name}!")

#     async def __call__(self, request: Request):
#         return await self.say_hello_twice(request.query_params["name"])


# app = HelloDeployment.bind(Doubler.bind())

# Filename: local_dev.py
# from fastapi import FastAPI

# from ray import serve
# from ray.serve.handle import DeploymentHandle, DeploymentResponse
# import torch

# from transformers import pipeline
# from transformers import AutoModelForCausalLM, AutoTokenizer

# app = FastAPI()


# @serve.deployment
# @serve.ingress(app)
# class FastAPIDeployment:
#     def __init__(self):
#         pass

#         # self._classifier = pipeline("sentiment-analysis")

#         # self.model = AutoModelForCausalLM.from_pretrained(
#         #     "microsoft/phi-2",
#         #     torch_dtype=torch.float32,
#         #     device_map="cpu",
#         #     trust_remote_code=True,
#         # )
#         # self.tokenizer = AutoTokenizer.from_pretrained(
#         #     "microsoft/phi-2",
#         #     trust_remote_code=True,
#         # )

#     # FastAPI will automatically parse the HTTP request for us.
#     @app.get("/")
#     def say_hello(self, name: str) -> str:
#         return f"Hello {name}!"

#         # return self._classifier(name)[0]["label"]

#         # inputs = self.tokenizer(
#         #     name,
#         #     return_tensors="pt",
#         #     return_attention_mask=False,
#         # )
#         # outputs = self.model.generate(
#         #     **inputs,
#         #     max_length=200,
#         # )
#         # text = self.tokenizer.batch_decode(outputs)[0]

#         # return text

# app = FastAPIDeployment.bind()

import asyncio
import os

import fastapi
import prefect_aws
import prefect_shell
import s3fs
import sky
from minio import Minio
from prefect import deploy, flow, task
from prefect.deployments.runner import DeploymentImage
from prefect.runner.runner import RunnerDeployment
from prefect.runner.storage import RemoteStorage
from prefect_aws import AwsClientParameters, MinIOCredentials, S3Bucket
from pydantic import SecretStr

# import transformers


@task
async def print_values(values):
    for value in values:
        await asyncio.sleep(1)  # yield
        print(value, end=" ")


@task
async def create_minio_bucket(bucket_name: str, ignore_exists: bool = False) -> str:
    minio_endpoint = os.getenv("MINIO_ENDPOINT")
    minio_client = Minio(
        minio_endpoint,
        access_key=os.getenv("MINIO_ROOT_USER"),
        secret_key=os.getenv("MINIO_ROOT_PASSWORD"),
        secure=False,
    )

    if minio_client.bucket_exists(bucket_name):
        if ignore_exists:
            return bucket_name

        else:
            raise Exception(f"Bucket {bucket_name} already exists")

    minio_client.make_bucket(bucket_name)

    return bucket_name

    # return await create_link_artifact(
    #     key="minio-bucket",
    #     link=f"{minio_endpoint}/{bucket_name}",
    #     description="MinIO bucket",
    # )


# @task(log_prints=True)
# async def create_minio_credentials_block():
#     minio_endpoint_url = f'http://{os.getenv("MINIO_ENDPOINT")}'
#     minio_credentials_block = MinIOCredentials(
#         aws_client_parameters=AwsClientParameters(
#             endpoint_url=minio_endpoint_url,
#             verify=False,
#             use_ssl=False,
#         ),
#         minio_root_user=os.getenv("MINIO_ROOT_USER"),
#         minio_root_password=SecretStr(os.getenv("MINIO_ROOT_PASSWORD")),
#     )

#     await minio_credentials_block.save("minio-credentials", overwrite=True)

#     print('minio_credentials_block (before): ', minio_credentials_block)

#     # return minio_credentials_block

#     minio_credentials_block =  await MinIOCredentials.load("minio-credentials")

#     print('minio_credentials_block (after): ', minio_credentials_block)

#     return minio_credentials_block


@task(log_prints=True)
async def create_minio_storage_block(
    bucket_folder: str,
    bucket_name: str,
    # minio_credentials_block: MinIOCredentials
):
    minio_endpoint_url = f'http://{os.getenv("MINIO_ENDPOINT")}'
    minio_storage_block = S3Bucket(
        bucket_folder=bucket_folder,
        bucket_name=bucket_name,
        credentials=MinIOCredentials(
            aws_client_parameters=AwsClientParameters(
                endpoint_url=minio_endpoint_url,
                verify=False,
                use_ssl=False,
            ),
            minio_root_user=os.getenv("MINIO_ROOT_USER"),
            minio_root_password=SecretStr(os.getenv("MINIO_ROOT_PASSWORD")),
        ),
    )

    await minio_storage_block.save("minio-storage", overwrite=True)

    print("minio_storage_block (before): ", minio_storage_block)

    minio_storage_block = await S3Bucket.load("minio-storage")

    print("minio_storage_block (after): ", minio_storage_block)

    return minio_storage_block


@task(log_prints=True)
async def upload_directory_to_minio(
    minio_storage_block: S3Bucket,
    local_path: str,
    to_path: str,
) -> int:
    print("minio_storage_block (again): ", minio_storage_block)

    uploaded_file_count = await minio_storage_block.put_directory(
        # local_path="src/timestep/services/web/src/web/app/workflows",
        local_path=f"{os.getcwd()}/src/web/app/workflows",
        to_path="workflows",
        # ignore_file=ignore_file, to_path=self.path
    )

    print(f"Uploaded {uploaded_file_count} files")

    return uploaded_file_count


@task(
    log_prints=True,
    timeout_seconds=10,
)
async def deploy_agent(
    # minio_storage_block: S3Bucket,
    uploaded_file_count: int,
):
    # my_flow = await flow.from_source(
    #     source=minio_storage_block,
    #     entrypoint="workflows/agent.py:deploy_agent",
    # )

    # await my_flow.deploy(
    #     name="agent-deployment",
    #     build=False,
    #     job_variables={
    #         "env": {
    #             "EXTRA_PIP_PACKAGES": f"prefect-aws=={prefect_aws.__version__}",
    #         },
    #     },
    #     push=False,
    #     work_pool_name="default-worker-pool",
    # )

    # print('creating storage adapter')
    # storage = BlockStorageAdapter(minio_storage_block)
    # # await storage.pull_code()
    # print('storage adapter created')

    #     minio_endpoint_url = f'http://{os.getenv("MINIO_ENDPOINT")}'
    #     minio_credentials_block = MinIOCredentials(
    #         aws_client_parameters=AwsClientParameters(
    #             endpoint_url=minio_endpoint_url,
    #             verify=False,
    #             use_ssl=False,
    #         ),
    #         minio_root_user=os.getenv("MINIO_ROOT_USER"),
    #         minio_root_password=SecretStr(os.getenv("MINIO_ROOT_PASSWORD")),
    #     )

    minio_endpoint = os.getenv("MINIO_ENDPOINT")
    minio_endpoint_url = f"http://{minio_endpoint}"
    # minio_client = Minio(
    #     minio_endpoint,
    #     access_key=os.getenv("MINIO_ROOT_USER"),
    #     secret_key=os.getenv("MINIO_ROOT_PASSWORD"),
    #     secure=False,
    # )

    print("Creating storage")
    storage = RemoteStorage(
        # url="s3://my-bucket/my-folder",
        # url=f"s3://{minio_endpoint}/default/agent",
        url="s3://default/agent",
        # Use Secret blocks to keep credentials out of your code
        # key=Secret.load("my-aws-access-key"),
        # key=SecretStr(os.getenv("MINIO_ROOT_USER")),
        # secret=Secret.load("my-aws-secret-key"),
        # secret=SecretStr(os.getenv("MINIO_ROOT_PASSWORD")),
        # token=?
        # minio_root_user=os.getenv("MINIO_ROOT_USER"),
        key=os.getenv("MINIO_ROOT_USER"),
        # minio_root_password=SecretStr(os.getenv("MINIO_ROOT_PASSWORD")),
        secret=os.getenv("MINIO_ROOT_PASSWORD"),
        client_kwargs={
            "endpoint_url": minio_endpoint_url,
            "verify": False,
            "use_ssl": False,
        },
    )

    # await storage.pull_code()

    # print('Getting flow from source')
    # my_flow = await flow.from_source(
    # my_flow = Flow.from_source(
    #     # source=minio_storage_block,
    #     # source=await S3Bucket.load("minio-storage"),
    #     source=storage,
    #     entrypoint="workflows/agent.py:deploy_agent",
    # )

    print("Deploying flow")
    # await my_flow.deploy(
    #     name="agent-deployment",
    #     build=False,
    #     job_variables={
    #         "env": {
    #             "EXTRA_PIP_PACKAGES": f"""
    #                 fastapi=={fastapi.__version__}
    #                 prefect-aws=={prefect_aws.__version__}
    #                 prefect-ray=={prefect_ray.__version__}
    #                 s3fs=={s3fs.__version__}
    #             """,
    #         },
    #     },
    #     push=False,
    #     work_pool_name="default-worker-pool",
    # )

    # print('transformers.__version__: ', transformers.__version__)

    # deployment: RunnerDeployment = RunnerDeployment(
    #     flow_name="agent-flow",
    #     # entrypoint="agent.py:deploy_agent",
    #     entrypoint="workflows/agent.py:deploy_agent",
    #     job_variables={
    #         "env": {
    #             "EXTRA_PIP_PACKAGES": f"""
    #                 fastapi=={fastapi.__version__}
    #                 prefect-aws=={prefect_aws.__version__}
    #                 prefect-ray=={prefect_ray.__version__}
    #                 s3fs=={s3fs.__version__}
    #             """,
    #         },
    #     },
    #     name="agent-flow-deployment",
    #     # path="workflows",
    #     parameters={
    #         "highest_number": 1,
    #     },
    #     storage=storage,
    #     work_pool_name="default-worker-pool",
    #     work_queue_name="default",
    # )

    deployment: RunnerDeployment = RunnerDeployment(
        flow_name="agent-flow",
        # entrypoint="agent.py:deploy_agent",
        entrypoint="workflows/agent2.py:deploy_agent_flow",
        job_variables={
            "env": {
                # "IMAGE_TO_DEPLOY": "registry.gitlab.com/timestep-ai/timestep/web",
                "EXTRA_PIP_PACKAGES": f"""
                    fastapi=={fastapi.__version__}
                    prefect-aws=={prefect_aws.__version__}
                    prefect-shell=={prefect_shell.__version__}
                    s3fs=={s3fs.__version__}
                    skypilot-nightly[kubernetes]=={sky.__version__}
                """,
            },
            # "image_pull_secrets": "regcred",
            "service_account_name": "prefect-worker-job-service-account",
        },
        name="agent-flow-deployment",
        # path="workflows",
        parameters={
            "model_ids": ["microsoft/phi-2"],
        },
        storage=storage,
        work_pool_name="default-worker-pool",
        work_queue_name="default",
    )

    await deploy(
        # local_flow.to_deployment(name="example-deploy-local-flow"),
        # flow.from_source(
        #     # source="https://github.com/org/repo.git",
        #     # entrypoint="flows.py:my_flow",
        #     source=storage,
        #     entrypoint="workflows/agent.py:deploy_agent",
        # ).to_deployment(
        #     # name="example-deploy-remote-flow",
        #     name="agent-deployment",
        # ),
        deployment,
        build=False,
        # job_variables={
        #     "env": {
        #         "EXTRA_PIP_PACKAGES": f"""
        #             fastapi=={fastapi.__version__}
        #             prefect-aws=={prefect_aws.__version__}
        #             prefect-ray=={prefect_ray.__version__}
        #             s3fs=={s3fs.__version__}
        #         """,
        #     },
        # },
        # image="berkeleyskypilot/skypilot-nightly",
        image=DeploymentImage(
            # name="berkeleyskypilot/skypilot-nightly",
            name="registry.gitlab.com/timestep-ai/timestep/web",
            # tag="latest",
            tag="tilt-96f6965e55017bbc",  # TODO: https://docs.tilt.dev/custom_resource#advanced-pod-creation
        ),
        push=False,
        work_pool_name="default-worker-pool",
        # image="my-registry/my-image:dev",
    )


@flow(
    timeout_seconds=10,
)
async def create_agent_flow(bucket_folder="agent", bucket_name="default"):
    # await print_values([1, 2])  # runs immediately
    # coros = [print_values("abcd"), print_values("6789")]

    # asynchronously gather the tasks
    # await asyncio.gather(*coros)

    await asyncio.sleep(1)  # yield

    bucket_name: str = await create_minio_bucket(bucket_name, ignore_exists=True)
    # minio_credentials_block = await create_minio_credentials_block()
    minio_storage_block = await create_minio_storage_block(
        bucket_folder=bucket_folder,
        bucket_name=bucket_name,
        # minio_credentials_block=minio_credentials_block,
    )

    uploaded_file_count: int = await upload_directory_to_minio(
        minio_storage_block=minio_storage_block,
        local_path=f"{os.getcwd()}/src/web/app/workflows",
        to_path="agent",
    )

    await deploy_agent(
        # minio_storage_block=minio_storage_block,
        uploaded_file_count,
    )


def create_agent():
    print("async create_agent_flow")

    asyncio.run(create_agent_flow())

    # deploy_flow()
