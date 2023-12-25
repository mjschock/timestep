import typing
from typing import List

import cloudpickle
import prefect_ray
import starlette
from prefect import flow, task
from prefect_ray.context import remote_options
from prefect_ray.task_runners import RayTaskRunner
from ray import serve
from ray.runtime_env import RuntimeEnv
from ray.serve.handle import DeploymentHandle, DeploymentResponse

runtime_env = RuntimeEnv(
    pip=[
        "accelerate>=0.16.0",
        f"cloudpickle=={cloudpickle.__version__}",
        "einops",
        "numpy<1.24",  # remove when mlflow updates beyond 2.2
        f"prefect_ray=={prefect_ray.__version__}",
        "torch",
        "transformers>=4.26.0",
    ],
    env_vars={"ONEDNN_MAX_CPU_ISA": "AVX512_CORE_AMX"},
)


# @serve.deployment(ray_actor_options={"num_gpus": 0})
# @serve.deployment(num_replicas=2, ray_actor_options={"num_cpus": 0.2, "num_gpus": 0})
@serve.deployment(
    num_replicas=1,
    ray_actor_options={
        # "memory": 0.25 * 1024 * 1024 * 1024,  # 0.25 GB
        # "num_cpus": 0.1,
        "num_gpus": 0,
    },
)
class AgentDeployment:
    def __init__(self, model_id: str, revision: str = None, msg: str = None):
        import torch
        from transformers import AutoModelForCausalLM, AutoTokenizer

        self._msg = msg
        # self.model = pipeline("translation_en_to_fr", model="t5-small")
        # self.model = AutoModelForCausalLM.from_pretrained(
        #     model_id,
        #     # revision=revision,
        #     # torch_dtype=torch.float16,
        #     # low_cpu_mem_usage=True,
        #     # device_map="auto",  # automatically makes use of all GPUs available to the Actor  # noqa: E501
        #     trust_remote_code=True,
        # )
        # self.tokenizer = AutoTokenizer.from_pretrained(model_id)
        # self.tokenizer.pad_token = self.tokenizer.eos_token

        import torch  # noqa: F811
        from transformers import AutoModelForCausalLM, AutoTokenizer  # noqa: F811

        # torch.set_default_device("cuda")

        # model = AutoModelForCausalLM.from_pretrained("microsoft/phi-2", torch_dtype="auto", trust_remote_code=True)  # noqa: E501
        print("Loading model...")
        self.model = AutoModelForCausalLM.from_pretrained(
            "microsoft/phi-2",
            torch_dtype=torch.float32,
            device_map="cpu",
            trust_remote_code=True,
        )  # noqa: E501
        print("Loading tokenizer...")
        self.tokenizer = AutoTokenizer.from_pretrained(
            "microsoft/phi-2", trust_remote_code=True
        )  # noqa: E501
        print("Done loading model and tokenizer.")

        # inputs = tokenizer('''def print_prime(n):
        # """
        # Print all primes between 1 and n
        # """''', return_tensors="pt", return_attention_mask=False)

        # outputs = model.generate(**inputs, max_length=200)
        # text = tokenizer.batch_decode(outputs)[0]
        # print(text)

    # def translate(self, text: str) -> str:
    #     # Run inference
    #     model_output = self.model(text)

    #     # Post-process output to return only the translation text
    #     translation = model_output[0]["translation_text"]

    #     return translation

    # async def __call__(self, http_request: starlette.requests.Request) -> str:
    #     english_text: str = await http_request.json()
    #     return self.translate(english_text)

    def __call__(self, request: starlette.requests.Request) -> typing.Dict:
        del request  # unused
        return {"result": self._msg}

    # def generate(self, text: str) -> pd.DataFrame:
    #     input_ids = self.tokenizer(text, return_tensors="pt").input_ids.to(
    #         self.model.device
    #     )

    #     gen_tokens = self.model.generate(
    #         input_ids,
    #         do_sample=True,
    #         temperature=0.9,
    #         max_length=100,
    #     )
    #     return pd.DataFrame(
    #         self.tokenizer.batch_decode(gen_tokens), columns=["responses"]
    #     )

    # async def __call__(self, http_request: starlette.requests.Request) -> str:
    #     json_request: str = await http_request.json()
    #     prompts = []
    #     for prompt in json_request:
    #         text = prompt["text"]
    #         if isinstance(text, list):
    #             prompts.extend(text)
    #         else:
    #             prompts.append(text)
    #     return self.generate(prompts)


# model_id = "tiiuae/falcon-7b"
# revision = None

# print('model_id', model_id)
# print('Binding deployment...')

# deployment = PredictDeployment.bind(
#     model_id=model_id,
#     revision=revision,
#     msg="Hello Ray Serve!")


@task
async def serve_agent_task(model_id: str, revision: str = None):
    print("Starting Ray Serve...")
    # import typing

    # import starlette

    # # @serve.deployment(ray_actor_options={"num_gpus": 0})
    # # @serve.deployment(num_replicas=2, ray_actor_options={"num_cpus": 0.2, "num_gpus": 0})  # noqa: E501
    # @serve.deployment(num_replicas=1, ray_actor_options={
    #     "memory": 0.5 * 1024 * 1024 * 1024,  # 0.5 GB
    #     "num_cpus": 0.2,
    #     "num_gpus": 0,
    # })
    # class PredictDeployment:
    #     def __init__(self, model_id: str, revision: str = None, msg: str = None):
    #         from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
    #         import torch

    #         self._msg = msg
    #         # self.model = pipeline("translation_en_to_fr", model="t5-small")
    #         # self.model = AutoModelForCausalLM.from_pretrained(
    #         #     model_id,
    #         #     # revision=revision,
    #         #     # torch_dtype=torch.float16,
    #         #     # low_cpu_mem_usage=True,
    #         #     # device_map="auto",  # automatically makes use of all GPUs available to the Actor  # noqa: E501
    #         #     trust_remote_code=True,
    #         # )
    #         # self.tokenizer = AutoTokenizer.from_pretrained(model_id)
    #         # self.tokenizer.pad_token = self.tokenizer.eos_token

    #     # def translate(self, text: str) -> str:
    #     #     # Run inference
    #     #     model_output = self.model(text)

    #     #     # Post-process output to return only the translation text
    #     #     translation = model_output[0]["translation_text"]

    #     #     return translation

    #     # async def __call__(self, http_request: starlette.requests.Request) -> str:
    #     #     english_text: str = await http_request.json()
    #     #     return self.translate(english_text)

    #     def __call__(self, request: starlette.requests.Request) -> typing.Dict:
    #         del request  # unused
    #         return {'result': self._msg}

    #     # def generate(self, text: str) -> pd.DataFrame:
    #     #     input_ids = self.tokenizer(text, return_tensors="pt").input_ids.to(
    #     #         self.model.device
    #     #     )

    #     #     gen_tokens = self.model.generate(
    #     #         input_ids,
    #     #         do_sample=True,
    #     #         temperature=0.9,
    #     #         max_length=100,
    #     #     )
    #     #     return pd.DataFrame(
    #     #         self.tokenizer.batch_decode(gen_tokens), columns=["responses"]
    #     #     )

    #     # async def __call__(self, http_request: starlette.requests.Request) -> str:
    #     #     json_request: str = await http_request.json()
    #     #     prompts = []
    #     #     for prompt in json_request:
    #     #         text = prompt["text"]
    #     #         if isinstance(text, list):
    #     #             prompts.extend(text)
    #     #         else:
    #     #             prompts.append(text)
    #     #     return self.generate(prompts)

    # print('model_id', model_id)
    # print('Binding deployment...')

    # deployment = PredictDeployment.bind(
    #     model_id=model_id,
    #     revision=revision,
    #     msg="Hello Ray Serve!")

    model_id = "tiiuae/falcon-7b"
    revision = None

    print("model_id", model_id)
    print("Binding deployment...")

    deployment = AgentDeployment.bind(
        model_id=model_id, revision=revision, msg="Hello Ray Serve v3!"
    )

    print("Starting deployment...")
    serve.run(deployment)
    # ray.get(handle.remote())


# @serve.deployment(
#     ray_actor_options={"num_gpus": 0},
# )
# # @serve.ingress(router)
# class AgentsDeployment:
#     def __init__(self) -> None:
#         print("AgentsDeployment init")

#     @router.get(
#         "/{agent_id}",
#         responses={
#             200: {"description": "Agent query successful"},
#             403: {"description": "Operation forbidden"},
#         },
#     )
#     async def query_agent(
#         self,
#         agent_service: Annotated[AgentsService, Depends(get_agent_service)],
#         agent_id: str,
#     ):
#         print("query_agent")
#         resp = await agent_service.query_agent(agent_id=agent_id)

#         print('resp', resp)

#         return resp

# app = AgentsDeployment.bind()


@flow(
    log_prints=True,
    task_runner=RayTaskRunner(
        # address="ray://<instance_public_ip_address>:10001",
        address="ray://ray-cluster-kuberay-head-svc.default.svc.cluster.local:10001",
        init_kwargs={
            "runtime_env": runtime_env,
        },
    ),
    # Using an S3 block that has already been created via the Prefect UI
    # result_storage="s3/my-result-storage",
)
async def serve_agent_flow(names: List[str]) -> None:
    # print('names', names)
    # print('Greetings!')

    # for name in names:
    #     # say_hello.submit(name)
    #     with remote_options(num_cpus=0.1, num_gpus=0):
    #         await process.submit(42)

    model_id = "tiiuae/falcon-7b"
    revision = None

    with remote_options(num_cpus=0.1, num_gpus=0):
        await serve_agent_task.submit(model_id, revision)


@task(
    log_prints=True,
)
async def delete_agent_task(agent_id: str = "default"):
    print("delete_agent_task")
    print("agent_id: ", agent_id)

    # handle: DeploymentHandle = serve.get_deployment_handle("AgentDeployment", app_name=agent_id)  # noqa: E501
    # response: DeploymentResponse = handle.remote("world")
    # handle.delete.remote()
    serve.delete(name=agent_id)

    # return agent_id


@flow(
    log_prints=True,
    task_runner=RayTaskRunner(
        # address="ray://<instance_public_ip_address>:10001",
        address="ray://ray-cluster-kuberay-head-svc.default.svc.cluster.local:10001",
        init_kwargs={
            "runtime_env": runtime_env,
        },
    ),
)
async def delete_agent_flow(agent_id: str) -> None:
    print("delete_agent_flow")
    print("agent_id: ", agent_id)

    await delete_agent_task.submit(agent_id)


# @flow(
#     log_prints=True,
# )
# async def query_agent_flow(query: str) -> None:
#     print('query', query)

#     return query

# response = requests.get("http://127.0.0.1:8000/", json=query)
# response_text = response.text

# print('response_text', response_text)
# print(requests.get("http://localhost:8000/", params={"text": query}).json())
# handle = serve.get_handle("PredictDeployment")

# model_id = "tiiuae/falcon-7b"
# revision = None

# print('model_id', model_id)
# print('Binding deployment...')

# deployment = PredictDeployment.bind(
#     model_id=model_id,
#     revision=revision,
#     msg="Hello Ray Serve!")

# handle = deployment.get_handle()
# print('handle', handle)


@task(log_prints=True)
async def query_agent_task(query: str):
    model_id = "tiiuae/falcon-7b"
    revision = None

    # deployment = PredictDeployment.bind(
    #     model_id=model_id,
    #     revision=revision,
    #     msg="Hello Ray Serve!")

    # print('Starting deployment...')
    # handle = serve.run(deployment)
    # ray.get(handle.remote())

    response_text = None

    try:
        # response = requests.post("http://127.0.0.1:8000/", json=query)

        # print('response', response)
        # print('response.text', response.text)
        # response_text = response.text

        handle: DeploymentHandle = serve.get_deployment_handle(
            "AgentDeployment", app_name="default"
        )  # noqa: E501
        response: DeploymentResponse = handle.remote("world")
        response_text = await response

    except Exception as e:
        print("e", e)
        response_text = str(e)

    return {
        "model_id": model_id,
        "revision": revision,
        "msg": "Hello Ray Serve!",
        "query": query,
        "response_text": response_text,
    }


query_agent_runtime_env = RuntimeEnv(
    pip=[
        # "accelerate>=0.16.0",
        f"cloudpickle=={cloudpickle.__version__}",
        # "numpy<1.24",  # remove when mlflow updates beyond 2.2
        f"prefect_ray=={prefect_ray.__version__}",
        # "torch",
        # "transformers>=4.26.0",
    ],
    # env_vars={"ONEDNN_MAX_CPU_ISA": "AVX512_CORE_AMX"}
)


@flow(
    log_prints=True,
    task_runner=RayTaskRunner(
        #     # address="ray://<instance_public_ip_address>:10001",
        address="ray://ray-cluster-kuberay-head-svc.default.svc.cluster.local:10001",
        init_kwargs={
            "runtime_env": query_agent_runtime_env,
        },
    ),
    # Using an S3 block that has already been created via the Prefect UI
    # result_storage="s3/my-result-storage",
)
async def query_agent_flow(query: str) -> None:
    # print('names', names)
    # print('Greetings!')

    # for name in names:
    #     # say_hello.submit(name)
    #     with remote_options(num_cpus=0.1, num_gpus=0):
    #         await process.submit(42)

    # model_id = "tiiuae/falcon-7b"
    # revision = None

    # with remote_options(num_cpus=0.1, num_gpus=0):
    #     await query_agent_task.submit(query)

    resp = await query_agent_task.submit(query)

    # print('resp', resp)
    # print('resp.result()', resp.result())

    result = await resp.result()

    print("result", result)

    return result
