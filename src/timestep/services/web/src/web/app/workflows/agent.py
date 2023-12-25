# import logging
# import os

# from prefect import flow
# from prefect_aws import MinIOCredentials, S3Bucket
# # from web.services.storage import StorageService

# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)


# @flow(log_prints=True)
# def create_agent_flow():
#     print("Creating agent...")


# def deploy_flow():
#     print("Deploying flow...")

#     # storage_service = StorageService()
#     # storage_service.create_bucket("default")

#     minio_endpoint_url = f'http://{os.getenv("MINIO_ENDPOINT")}'
#     minio_credentials_block = MinIOCredentials(
#         aws_client_parameters={
#             "endpoint_url": minio_endpoint_url,
#             "verify": False,
#             "use_ssl": False,
#         },
#         minio_root_user=os.getenv("MINIO_ROOT_USER"),
#         minio_root_password=os.getenv("MINIO_ROOT_PASSWORD"),
#     )

#     minio_credentials_block.save("minio-credentials", overwrite=True)

#     minio_storage_block = S3Bucket(
#         bucket_name="default",
#         # bucket_folder="workflows",
#         credentials=minio_credentials_block,
#     )

#     minio_storage_block.save("minio-storage", overwrite=True)

#     # cwd = os.getcwd()
#     # print(f"cwd: {cwd}")

#     # print('contents of cwd', os.listdir(cwd))
#     # print('contents of workflows', os.listdir(f"{cwd}/src/web/app/workflows"))

#     # uploaded_file_count = minio_storage_block.put_directory(
#     #     # local_path="src/timestep/services/web/src/web/app/workflows",
#     #     local_path=f"{os.getcwd()}/src/web/app/workflows",
#     #     to_path="workflows",
#     #     # ignore_file=ignore_file, to_path=self.path
#     # )

#     # print(f"Uploaded {uploaded_file_count} files")

#     # flow.from_source(
#     #     source=minio_storage_block,
#     #     entrypoint="agent.py:create_agent_flow",
#     # ).deploy(
#     #     name="my-first-deployment",
#     #     build=False,
#     #     # image=DeploymentImage(
#     #     #     name="prefecthq/prefect",
#     #     #     tag="2.14.6-python3.11-kubernetes",
#     #     #     # dockerfile="Dockerfile"
#     #     # ),
#     #     push=False,
#     #     work_pool_name="default-worker-pool",
#     # )

#     # return buy.deploy(
#     #     name="my-code-baked-into-an-image-deployment",
#     #     build=False,
#     #     image="prefecthq/prefect:2.14.6-python3.11-kubernetes",
#     #     push=False,
#     #     work_pool_name="default-worker-pool",
#     # )

#     # logger.info("Deploying flow")

#     # minio_endpoint_url = f'http://{os.getenv("MINIO_ENDPOINT")}'
#     # minio_credentials = MinIOCredentials(
#     #     aws_client_parameters={
#     #         "endpoint_url": minio_endpoint_url,
#     #         # "use_ssl": False,
#     #     },
#     #     minio_root_user=os.getenv("MINIO_ROOT_USER"),
#     #     minio_root_password=os.getenv("MINIO_ROOT_PASSWORD"),
#     # )

#     # minio_credentials.save("minio-credentials", overwrite=True)

#     # logger.info("Saved minio credentials")

#     # # s3_client = minio_credentials.get_boto3_session().client(
#     # #     service="s3",
#     # #     endpoint_url=minio_endpoint_url,
#     # # )

#     # minio_block = S3Bucket(
#     #     bucket_name="default",
#     #     bucket_folder="test",
#     #     credentials=minio_credentials,
#     # )

#     # # minio_block = RemoteFileSystem(
#     # #     # basepath="s3://default",
#     # #     # basepath="s3://my-bucket",
#     # #     basepath="minio://my-bucket",
#     # #     settings={
#     # #         "key": os.getenv("MINIO_ROOT_USER"),
#     # #         "secret": os.getenv("MINIO_ROOT_PASSWORD"),
#     # #         "client_kwargs": {"endpoint_url": minio_endpoint_url},
#     # #     },
#     # # )
#     # minio_block.save("minio", overwrite=True)

#     # logger.info("Saved minio block")

#     # uploaded_file_count = minio_block.put_directory(
#     #     # ignore_file=ignore_file, to_path=self.path
#     # )

#     # logger.info("Saved minio block")

#     # deployment = Deployment.build_from_flow(
#     #     flow=buy,
#     #     apply=False,
#     #     # infrastructure="kubernetes",
#     #     name="my-code-baked-into-an-image-deployment",
#     #     skip_upload=True,
#     #     # storage=minio_block,
#     #     work_pool_name="default-worker-pool",
#     #     work_queue_name="default",
#     # )

#     # logger.info("Built deployment")

#     # id = deployment.apply(upload=False)

#     # logger.info(f"Applied deployment {id}")

#     # file_count = deployment.upload_to_storage(storage_block='s3-bucket/minio')

#     # logger.info(f"Uploaded {uploaded_file_count} files")

#     # return deployment

#     # return deploy(
#     #     buy.to_deployment(
#     #         name="my-code-baked-into-an-image-deployment",
#     #     ),
#     #     build=False,
#     #     image="prefecthq/prefect:2.14.6-python3.11-kubernetes",
#     #     push=False,
#     #     work_pool_name="default-worker-pool",
#     # )


# if __name__ == "__main__":
#     deploy_flow()

# Filename: local_dev.py
# import torch
import time

import cloudpickle
import prefect_ray
from fastapi import FastAPI
from prefect import Flow, State, flow, task
from prefect.flows import FlowRun
from prefect_ray import RayTaskRunner
from prefect_ray.context import remote_options
from ray import serve
from ray.runtime_env import RuntimeEnv

# from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

print("=== agent.py ===")

runtime_env = RuntimeEnv(
    pip=[
        "accelerate==0.25.0",
        # "accelerate>=0.16.0",
        f"cloudpickle=={cloudpickle.__version__}",
        "datasets==2.16.0",
        "einops==0.7.0",
        # f"einops=={einops.__version__}",
        # "numpy<1.24",  # remove when mlflow updates beyond 2.2
        f"prefect-ray=={prefect_ray.__version__}",
        # f"pydantic=={pydantic.__version__}",
        # f"torch=={torch.__version__.replace('+cpu', '')}",
        # f"transformers=={transformers.__version__}",
        "transformers[torch]==4.35.2",
    ],
    # env_vars={"ONEDNN_MAX_CPU_ISA": "AVX512_CORE_AMX"}
)

#     # https://docs.ray.io/en/releases-2.9.0/ray-core/api/doc/ray.init.html
#     # TODO: use RAY_ADDRESS
#     client_context: ClientContext = ray.init(
#         address="ray://ray-cluster-kuberay-head-svc.default.svc.cluster.local:10001",
#         runtime_env=runtime_env,
#     )
#     # TODO: storage (RAY_STORAGE)
#     # todo: _temp_dir

# app = FastAPI()


# @serve.deployment
# @serve.ingress(app)
# class AgentDeployment:
#     def __init__(self):
#         # pass

#         # https://huggingface.co/docs/transformers/big_models
#         # https://huggingface.co/docs/transformers/main_classes/model#large-model-loading
#         import torch
#         # from accelerate import Accelerator
#         # from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
#         # from transformers.modeling_utils import load_sharded_checkpoint

#         # self._classifier = pipeline("sentiment-analysis")

#         # self.model = AutoModelForCausalLM.from_pretrained(
#         #     "microsoft/phi-2",
#         #     torch_dtype=torch.float32,
#         #     device_map="cpu",
#         #     trust_remote_code=True,
#         #     low_cpu_mem_usage=True,
#         # )

#         # self.model = AutoModelForCausalLM.from_pretrained(
#         #     "microsoft/phi-2",
#         #     device_map="auto",
#         #     torch_dtype="auto",
#         #     trust_remote_code=True,
#         # )

#         # self.tokenizer = AutoTokenizer.from_pretrained(
#         #     "microsoft/phi-2",
#         #     trust_remote_code=True,
#         #     low_cpu_mem_usage=True,
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


# agent_deployment = AgentDeployment.bind()


@task
async def process(x):
    return x + 1


# @flow(task_runner=RayTaskRunner(
#         address=None,
#         init_kwargs=None,
# ))
# async def my_flow():
#     # equivalent to setting @ray.remote(num_cpus=4, num_gpus=2)
#     with remote_options(num_cpus=4, num_gpus=2):
#         await process.submit(42)

# @flow(log_prints=True)
# def deploy_agent():
#     print("Creating agent...")

#     result = process(42)
#     print(result)

# if __name__ == "__main__":
#     deploy_agent()


@task
def shout(number):
    time.sleep(0.5)
    print(f"#{number}")


def my_failure_hook(task, task_run, state):
    print("Task run failed!")


@task(log_prints=True, on_failure=[my_failure_hook])
async def dep_check():
    import accelerate

    print("accelerate version", accelerate.__version__)

    import datasets

    print("datasets version", datasets.__version__)

    import transformers

    print("transformers version", transformers.__version__)

    import torch

    print("torch version", torch.__version__)


def serve_agent_on_failure_hook(task, task_run, state):
    print("Serve agent deployment failed!")


def serve_agent_on_crashed_hook(task, task_run, state):
    print("Serve agent deployment crashed!")


@task(
    log_prints=True,
    on_failure=[
        serve_agent_on_failure_hook,
    ],
)
async def serve_agent():
    print("Serving agent deployment...")

    app = FastAPI()

    @serve.deployment(
        # ray_actor_options: Options to pass to the Ray Actor decorator, such as
        # resource requirements. Valid options are: `accelerator_type`, `memory`,
        # `num_cpus`, `num_gpus`, `object_store_memory`, `resources`,
        # and `runtime_env`.
        ray_actor_options={
            "memory": 0.1 * 1024 * 1024 * 1024,  # 0.1 GB
            "num_cpus": 0.2,
            "num_gpus": 0,
        },
    )
    @serve.ingress(app)
    class AgentDeployment:
        def __init__(self):
            # pass

            # https://huggingface.co/docs/transformers/big_models
            # https://huggingface.co/docs/transformers/main_classes/model#large-model-loading
            # https://huggingface.co/docs/transformers/perf_infer_cpu#bettertransformer
            import accelerate
            import datasets
            import torch
            import transformers
            from transformers import AutoModelForCausalLM, AutoTokenizer

            self.accelerator_version = accelerate.__version__
            self.datasets_version = datasets.__version__
            self.transformers_version = transformers.__version__
            self.torch_version = torch.__version__

            # self._classifier = pipeline("sentiment-analysis")

            # self.model = AutoModelForCausalLM.from_pretrained(
            #     "microsoft/phi-2",
            #     torch_dtype=torch.float32,
            #     device_map="cpu",
            #     trust_remote_code=True,
            #     low_cpu_mem_usage=True,
            # )

            # self.model = AutoModelForCausalLM.from_pretrained(
            #     "microsoft/phi-2",
            #     device_map="auto",
            #     torch_dtype="auto",
            #     trust_remote_code=True,
            # )

            self.model = AutoModelForCausalLM.from_pretrained(
                "microsoft/phi-2",
                device_map="cpu",
                low_cpu_mem_usage=True,
                torch_dtype=torch.float32,
                trust_remote_code=True,
            )

            # self.tokenizer = AutoTokenizer.from_pretrained(
            #     "microsoft/phi-2",
            #     device_map="auto",
            #     torch_dtype="auto",
            #     trust_remote_code=True,
            # )

            # self.tokenizer = AutoTokenizer.from_pretrained(
            #     "microsoft/phi-2",
            #     trust_remote_code=True,
            # )

            self.tokenizer = AutoTokenizer.from_pretrained(
                "microsoft/phi-2",
                device_map="cpu",
                low_cpu_mem_usage=True,
                torch_dtype=torch.float32,
                trust_remote_code=True,
            )

        # FastAPI will automatically parse the HTTP request for us.
        @app.get("/")
        def say_hello(self, name: str) -> str:
            # return f"Hello {name}! (accelerate version: {self.accelerator_version}, datasets version: {self.datasets_version}, transformers version: {self.transformers_version}, torch version: {self.torch_version})"  # noqa: E501

            # return self._classifier(name)[0]["label"]

            inputs = self.tokenizer(
                name,
                return_tensors="pt",
                return_attention_mask=False,
            )
            outputs = self.model.generate(
                **inputs,
                max_length=200,
            )
            text = self.tokenizer.batch_decode(outputs)[0]

            return text

    agent_deployment = AgentDeployment.bind()

    print("Agent deployment bound.")

    serve.shutdown()

    serve.run(agent_deployment, _blocking=False, host="0.0.0.0")

    # handle: DeploymentHandle = serve.run(agent_deployment, host="0.0.0.0")
    print("Agent deployment served.")

    # print('Testing agent deployment...')
    # response: DeploymentResponse = handle.say_hello.remote(name="Ray")
    # result = await response
    # print('Received response from agent deployment: ', result)


def my_flow_hook(flow: Flow, flow_run: FlowRun, state: State):
    """This is the required signature for a flow run state
    change hook. This hook can only be passed into flows.
    """
    print("Flow run failed!")


@flow(
    log_prints=True,
    task_runner=RayTaskRunner(
        address="ray://ray-cluster-kuberay-head-svc.default.svc.cluster.local:10001",
        init_kwargs={
            "runtime_env": runtime_env,
        },
    ),
    on_crashed=[
        my_flow_hook,
    ],
    # Using an S3 block that has already been created via the Prefect UI
    # result_storage="s3/my-result-storage",
)
async def deploy_agent(highest_number):
    # with remote_options(num_cpus=0.1, num_gpus=0):
    #     for number in range(highest_number):
    #         shout.submit(number)

    # current_remote_options = RemoteOptionsContext.get().current_remote_options
    # print('current_remote_options', current_remote_options)

    #    # equivalent to setting @ray.remote(num_cpus=4, num_gpus=2)
    # with remote_options(num_cpus=0.1, num_gpus=0):
    #     await process.submit(42)

    # with remote_options(num_cpus=0.5, num_gpus=0):
    #     await dep_check.submit()

    with remote_options(
        memory=0.1 * 1024 * 1024 * 1024,  # 0.1 GB
        num_cpus=0.6,
        # num_gpus=0
    ):
        await serve_agent.submit()

    # print('Serving agent deployment...')
    # handle: DeploymentHandle = serve.run(agent_deployment, host="0.0.0.0")
    # print('Agent deployment served.')

    # print('Testing agent deployment...')
    # response: DeploymentResponse = handle.say_hello.remote(name="Ray")
    # result = await response
    # print('Received response from agent deployment: ', result)


# if __name__ == "__main__":
#     deploy_agent(10)
