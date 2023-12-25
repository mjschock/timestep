import base64
import os

import kubernetes
import sky
import yaml

# from llama_index.llms import Ollama
# from ray import serve
from sky import clouds, skypilot_config

# from sky.adaptors.minio import MINIO_CREDENTIALS_PATH, MINIO_PROFILE_NAME
from sky.check import check as sky_check

# from sky.data.storage import MINIOStore, StoreType
from sky.data.storage import StoreType
from sky.serve import service_spec
from sky.serve.core import up as sky_serve_up
from sky.skypilot_config import CONFIG_PATH, _try_load_config

# from web.app.workflows.agents import delete_agent_flow, query_agent_flow, serve_agent_flow  # noqa: E501

# @task
# async def process(x):
#     return x + 1


# @flow(task_runner=RayTaskRunner(
#         address=None,
#         init_kwargs=None,
# ))
# async def my_flow():
#     # equivalent to setting @ray.remote(num_cpus=4, num_gpus=2)
#     with remote_options(num_cpus=4, num_gpus=2):
#         await process.submit(42)

# @task
# async def print_values(values):
#     for value in values:
#         await asyncio.sleep(1) # yield
#         print(value, end=" ")

# @flow
# async def async_flow():
#     await print_values([1, 2])  # runs immediately
#     coros = [print_values("abcd"), print_values("6789")]

#     # asynchronously gather the tasks
#     await asyncio.gather(*coros)


# @task(retries=3)
# async def pull_model(model_name):
#     print(f'Pulling model {model_name}...')
#     # url = f"http://ollama.ollama.svc.cluster.local:80/api/pull"
#     # api_response = httpx.post(url, json={
#     #     "insecure": True,
#     #     # "name": "llama2",
#     #     # "name": "orca-mini:3b",
#     #     "name": model_name,
#     #     # "timeout": 60,
#     # })
#     # api_response.raise_for_status()
#     # repo_info = api_response.json()
#     # print('repo_info', repo_info)

#     async with httpx.AsyncClient() as client:
#         url = f"http://ollama.ollama.svc.cluster.local:80/api/pull"
#         api_response = await client.post(url, json={
#             "insecure": True,
#             # "name": "llama2",
#             # "name": "orca-mini:3b",
#             "name": model_name,
#             # "timeout": 60,
#         })
#         api_response.raise_for_status()
#         repo_info = api_response.json()
#         print('repo_info', repo_info)


# @flow(log_prints=True)
# async def llama_flow():
#     model_name = 'llava'

#     # await pull_model(model_name)

#     print('Loading model...')
#     llm = Ollama(
#         base_url="http://ollama.ollama.svc.cluster.local:80",
#         # model="llama2"
#         # model="orca-mini:3b",
#         model=model_name,
#     )

#     print('Running model inference...')
#     # resp = llm.complete("Who is Paul Graham?")
#     resp = llm.predict("Why is the sky blue?")
#     print(resp)


# # The result of this task will be cached in the configured result storage
# # @task(cache_key_fn=task_input_hash)
# @task()
# async def say_hello(name: str) -> None:
#     logger = get_run_logger()
#     # This log statement will print only on the first run. Subsequent runs will be cached.  # noqa: E501
#     logger.info(f"hello {name}!")
#     return name


# runtime_env = RuntimeEnv(
#     pip=[
#         "accelerate>=0.16.0",
#         f"cloudpickle=={cloudpickle.__version__}",
#         "numpy<1.24",  # remove when mlflow updates beyond 2.2
#         f"prefect_ray=={prefect_ray.__version__}",
#         "torch",
#         "transformers>=4.26.0",
#     ],
#     env_vars={"ONEDNN_MAX_CPU_ISA": "AVX512_CORE_AMX"}
# )


# @task
# async def serve_agent(model_id: str, revision: str = None):
#     print('Starting Ray Serve...')
#     import typing

#     import starlette

#     # @serve.deployment(ray_actor_options={"num_gpus": 0})
#     # @serve.deployment(num_replicas=2, ray_actor_options={"num_cpus": 0.2, "num_gpus": 0})  # noqa: E501
#     @serve.deployment(num_replicas=1, ray_actor_options={
#         "memory": 0.5 * 1024 * 1024 * 1024,  # 0.5 GB
#         "num_cpus": 0.2,
#         "num_gpus": 0,
#     })
#     class PredictDeployment:
#         def __init__(self, model_id: str, revision: str = None, msg: str = None):
#             from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
#             import torch

#             self._msg = msg
#             # self.model = pipeline("translation_en_to_fr", model="t5-small")
#             # self.model = AutoModelForCausalLM.from_pretrained(
#             #     model_id,
#             #     # revision=revision,
#             #     # torch_dtype=torch.float16,
#             #     # low_cpu_mem_usage=True,
#             #     # device_map="auto",  # automatically makes use of all GPUs available to the Actor  # noqa: E501
#             #     trust_remote_code=True,
#             # )
#             # self.tokenizer = AutoTokenizer.from_pretrained(model_id)
#             # self.tokenizer.pad_token = self.tokenizer.eos_token

#         # def translate(self, text: str) -> str:
#         #     # Run inference
#         #     model_output = self.model(text)

#         #     # Post-process output to return only the translation text
#         #     translation = model_output[0]["translation_text"]

#         #     return translation

#         # async def __call__(self, http_request: starlette.requests.Request) -> str:
#         #     english_text: str = await http_request.json()
#         #     return self.translate(english_text)

#         def __call__(self, request: starlette.requests.Request) -> typing.Dict:
#             del request  # unused
#             return {'result': self._msg}

#         # def generate(self, text: str) -> pd.DataFrame:
#         #     input_ids = self.tokenizer(text, return_tensors="pt").input_ids.to(
#         #         self.model.device
#         #     )

#         #     gen_tokens = self.model.generate(
#         #         input_ids,
#         #         do_sample=True,
#         #         temperature=0.9,
#         #         max_length=100,
#         #     )
#         #     return pd.DataFrame(
#         #         self.tokenizer.batch_decode(gen_tokens), columns=["responses"]
#         #     )

#         # async def __call__(self, http_request: starlette.requests.Request) -> str:
#         #     json_request: str = await http_request.json()
#         #     prompts = []
#         #     for prompt in json_request:
#         #         text = prompt["text"]
#         #         if isinstance(text, list):
#         #             prompts.extend(text)
#         #         else:
#         #             prompts.append(text)
#         #     return self.generate(prompts)

#     print('model_id', model_id)
#     print('Binding deployment...')
#     deployment = PredictDeployment.bind(model_id=model_id, revision=revision, msg="Hello Ray Serve!")  # noqa: E501
#     print('Starting deployment...')
#     handle = serve.run(deployment)


# @flow(
#     log_prints=True,
#     task_runner=RayTaskRunner(
#         # address="ray://<instance_public_ip_address>:10001",
#         address="ray://ray-cluster-kuberay-head-svc.default.svc.cluster.local:10001",
#         init_kwargs={
#             "runtime_env": runtime_env,
#         }
#     ),
#     # Using an S3 block that has already been created via the Prefect UI
#     # result_storage="s3/my-result-storage",
# )
# async def greetings(names: List[str]) -> None:
#     # print('names', names)
#     # print('Greetings!')

#     # for name in names:
#     #     # say_hello.submit(name)
#     #     with remote_options(num_cpus=0.1, num_gpus=0):
#     #         await process.submit(42)

#     model_id = "tiiuae/falcon-7b"
#     revision = None

#     with remote_options(num_cpus=0.1, num_gpus=0):
#         await serve_agent.submit(model_id, revision)

# async def ray_flow():
#     await greetings(["Alice", "Bob", "Charlie", "Delta" ])


class AgentsService:
    # def __init__(self, q: str | None = None, skip: int = 0, limit: int = 100):
    #     self.q = q
    #     self.skip = skip
    #     self.limit = limit

    def __init__(self):
        # self.q = q
        # self.skip = skip
        # self.limit = limit
        pass

    async def create_agent(self):
        cloud_info = {}
        job_id = None

        # from llama_index.llms import MistralAI

        # job_id = await my_flow()
        # job_id = await async_flow()

        # job_id = await llama_flow()
        # job_id = await ray_flow()
        # job_id = await serve_agent_flow(
        #     names=["Alice", "Bob"]
        # )

        return {
            "job_id": job_id,
        }

        for cloud_name, cloud in sky.clouds.CLOUD_REGISTRY.items():
            cloud_info[cloud_name] = {
                "enabled": False,
                "name": str(cloud),
            }

        data = {
            "cloud_info": cloud_info,
            # "commit": sky.__commit__,
            # "version": sky.__version__,
            # "root_dir": sky.__root_dir__,
        }

        # return {
        #     "job_id": job_id,
        #     "sky": data,
        # }

        print("=== load_cloud_credentials? ===")
        load_cloud_credentials()

        try:
            sky_check(
                quiet=False,
                verbose=True,
            )

            enabled_clouds = sky.global_user_state.get_enabled_clouds()

            for cloud in enabled_clouds:
                data["cloud_info"][str(cloud).lower()]["enabled"] = True

        except SystemExit:
            data["error"] = {
                "type": "SystemExit",
            }

            # ).set_service(
            #     service_spec.SkyServiceSpec(
            #         initial_delay_seconds=5,
            #         min_replicas=1,
            #         readiness_path='/',
            #     )

        return {
            "job_id": job_id,
            "sky": data,
            "workdir": os.getcwd(),
        }

        # with sky.Dag() as dag:
        #     # The working directory contains all code and will be synced to remote.
        #     # workdir = os.getcwd()

        #     # The setup command.  Will be run under the working directory.
        #     # setup = 'pip install "ray[serve]"'

        #     # The command to run.  Will be run under the working directory.
        #     run = 'echo hello SkyPilot'

        #     task = sky.Task(
        #         run=run,
        #     )

        #     task.set_resources(
        #         sky.Resources(
        #             cloud=clouds.Kubernetes(),
        #             cpus="1",
        #             disk_size=1,
        #             memory="1",
        #         )
        #     )

        # job_id, handle = sky.launch(dag)

        task = sky.Task(
            run="echo hello SkyPilot",
        )

        task.set_resources(
            sky.Resources(
                cloud=clouds.Kubernetes(),
                cpus="1",
                disk_size=1,
                memory="1",
            )
        )

        job_id, handle = sky.launch(
            cluster_name="sky-47ed-ubuntu",
            detach_run=True,
            task=task,
        )

        return {
            "job_id": job_id,
            "sky": data,
            "workdir": os.getcwd(),
        }

        # Kubernetes(cpus=4+, disk_size=200, ports=['30001-30100'])
        resources = sky.Resources(
            cloud=clouds.Kubernetes(),
            # cpus="1",
            cpus="1",
            # cpus='4+',
            disk_size=1,
            memory="1",
            # ports=8000,
            # ports="30001-30100",
            # ports=[30001, 30002, 30003, 30004, 30005, 30006, 30007, 30008, 30009, 30010],  # noqa: E501
            ports=[30001],
            # ports=[port]
            # ports=['30001', '30002'],
        )

        service = service_spec.SkyServiceSpec(
            initial_delay_seconds=5,
            max_replicas=1,
            min_replicas=1,
            readiness_path="/",
        )

        store = MINIOStore(  # noqa: F821
            name="minio-store-name",
            source="minio-store-data-source",
        )

        sky.Storage(
            name="my-bucket",
            source=f"{os.getcwd()}/src/web/app/storage",
            stores={
                StoreType.MINIO: store,
            },
        )

        task = sky.Task(
            run="serve run serve:app --host 0.0.0.0",
            setup='pip install "ray[serve]"',
            # workdir='examples/serve/ray_serve',
            # workdir='.',
        )

        # task.set_file_mounts(file_mounts=file_mounts)
        task.set_resources(resources=resources)
        task.set_service(service=service)
        # task.set_storage_mounts(storage_mounts=storage_mounts)

        try:
            sky_serve_up(
                # service_name=f'sky-service-{uuid.uuid4().hex[:4]}',
                service_name="sky-service-agent-5cf0",
                task=task,
            )

        except Exception as e:
            print("e", e)
            data["error"] = {
                "type": "Exception",
                "message": str(e),
            }

        return {
            "job_id": job_id,
            "sky": data,
        }

        # store = storage.Storage(

        # TEST_BUCKET_NAME = 'skypilot-workdir-ubuntu-b0670fb3'
        # LOCAL_SOURCE_PATH = '/home/ubuntu/app/src/web/examples/serve/ray_serve'
        # storage_1 = storage.Storage(name=TEST_BUCKET_NAME, source=LOCAL_SOURCE_PATH)
        # # storage_1.add_store(StoreType.S3)  # Transfers data from local to S3
        # storage_1.add_store(StoreType.MINIO)

        # storages = sky.core.storage_ls()
        # print('storages', storages)

        task = (
            sky.Task(
                run='echo "Hello, how are you?',
                # run='serve run serve:app --host 0.0.0.0',
                setup='echo "Running setup."',
                # setup='pip install "ray[serve]"',
                workdir=".",
                # workdir=f'{os.getcwd()}/src/web/examples/serve/ray_serve',
            )
            .set_file_mounts(
                {
                    "/dataset-demo": "minio://sky-demo-dataset",
                }
            )
            .set_resources(
                sky.Resources(
                    cloud=clouds.Kubernetes(),
                    cpus="1",
                    # cpus='2+',
                    memory="2",
                    # ports='8000',
                )
                # ).set_service(
                #     service_spec.SkyServiceSpec(
                #         initial_delay_seconds=5,
                #         min_replicas=1,
                #         readiness_path='/',
                #     )
            )
        )
        # ).set_storage_mounts( #  Workdir '/home/ubuntu/app/src/web/examples/serve/ray_serve' will be synced to cloud storage 'skypilot-workdir-ubuntu-b0670fb3'.  # noqa: E501
        #     {
        #         f"{mount_path}": sky.Storage(
        #             name="skypilot-workdir-ubuntu-b0670fb3",
        #             source="/home/ubuntu/app/src/web/examples/serve/ray_serve",
        #         )
        #     }

        # # sky serve up examples/serve/ray_serve/ray_serve.yaml
        # sky_serve_up(
        #     service_name=None,
        #     task=task,
        # )

        job_id, handle = sky.launch(
            cluster_name="sky-5cf0-ubuntu",
            task=task,
        )

        return {
            "job_id": job_id,
            "sky": data,
        }

    async def delete_agent(self, agent_id: str):
        await delete_agent_flow(agent_id)  # noqa: F821

        return {
            "agent_id": agent_id,
        }

    async def query_agent(self, query: str):
        resp = await query_agent_flow(query)  # noqa: F821

        return {
            "resp": resp,
        }


# async def get_agent_service(q: str | None = None, skip: int = 2, limit: int = 100):
async def get_agent_service():
    # return AgentsService(q=q, skip=skip, limit=limit)
    return AgentsService()


def load_cloud_credentials(overwrite=True):
    load_kubeconfig(overwrite)
    # load_minio_credentials(overwrite)


def load_kubeconfig(overwrite=True):
    kubeconfig_path = os.path.expanduser(sky.clouds.kubernetes.CREDENTIAL_PATH)

    if overwrite or not os.path.exists(kubeconfig_path):
        kubecontext = os.getenv("KUBECONTEXT", "timestep.local")
        kubernetes_service_host = os.getenv("KUBERNETES_SERVICE_HOST")
        kubernetes_service_port = os.getenv("KUBERNETES_SERVICE_PORT")

        ca_certificate_path = "/var/run/secrets/kubernetes.io/serviceaccount/ca.crt"
        namespace_path = "/var/run/secrets/kubernetes.io/serviceaccount/namespace"
        service_account_token_path = (
            "/var/run/secrets/kubernetes.io/serviceaccount/token"  # noqa: E501
        )

        with open(namespace_path, "r") as file:
            namespace = file.read()

        print("before load_incluster_config")
        kubernetes.config.load_incluster_config()
        config = kubernetes.client.Configuration.get_default_copy()

        # kube_config_loader = kubernetes.config.kube_config.KubeConfigLoader(
        #     config_dict=config.to_dict()
        # )

        print("config", config)
        # kube_config_contexts = kubernetes.config.list_kube_config_contexts()
        # print('kube_config_contexts', kube_config_contexts)

        # kube_config = kubernetes.config.load_kube_config(
        #     client_configuration=config,
        # )
        # print('kube_config', kube_config)

        api_key = config.api_key
        print("api_key", api_key)

        auth = config.auth_settings()
        print("auth", auth)

        api_key_prefix = config.api_key_prefix
        print("api_key_prefix", api_key_prefix)

        cert_file = config.cert_file
        print("cert_file", cert_file)

        key_file = config.key_file
        print("key_file", key_file)

        username = config.username
        print("username", username)

        password = config.password
        print("password", password)

        server = config.host
        print("server", server)
        assert (
            server == f"https://{kubernetes_service_host}:{kubernetes_service_port}"
        ), f"{server} != https://{kubernetes_service_host}:{kubernetes_service_port}"

        ssl_ca_cert = config.ssl_ca_cert
        print("ssl_ca_cert", ssl_ca_cert)
        assert (
            ssl_ca_cert == ca_certificate_path
        ), f"{ssl_ca_cert} != {ca_certificate_path}"

        # Load CA certificate and encode it in base64
        with open(ssl_ca_cert, "rb") as ssl_ca_cert_file:
            certificate_authority_data = base64.b64encode(
                ssl_ca_cert_file.read()
            ).decode("utf-8")

        # Load service account token
        with open(service_account_token_path, "rb") as token_file:
            service_account_token = token_file.read()

        cluster_name = "timestep.local"
        user_name = "ubuntu"

        # Create kubeconfig dictionary
        kubeconfig = {
            "apiVersion": "v1",
            "kind": "Config",
            "clusters": [
                {
                    "cluster": {
                        "certificate-authority-data": certificate_authority_data,
                        "server": server,
                    },
                    "name": cluster_name,
                }
            ],
            "contexts": [
                {
                    "context": {
                        "cluster": cluster_name,
                        "namespace": namespace,
                        "user": user_name,
                    },
                    "name": kubecontext,
                }
            ],
            "current-context": kubecontext,
            "preferences": {},
            "users": [
                {
                    "name": user_name,
                    "user": {
                        # "client-certificate-data": client_certificate_data,
                        # "client-key-data": client_key_data,
                        "token": service_account_token
                        # "token-data": service_account_token,
                        # "token": token_file,
                    },
                }
            ],
        }

        # Create ~/.kube directory if it doesn't exist
        kube_dir = os.path.dirname(kubeconfig_path)
        os.makedirs(kube_dir, exist_ok=True)

        # Save the kubeconfig dictionary to ~/.kube/config
        with open(kubeconfig_path, "w") as outfile:
            yaml.dump(kubeconfig, outfile, default_flow_style=False)

        if not os.path.exists(kubeconfig_path):
            raise RuntimeError(f"{kubeconfig_path} file has not been generated.")

        print(f"{kubeconfig_path} file has been generated.")

        with open(kubeconfig_path, "r") as file:
            content = file.read()
            print(f"{kubeconfig_path}:")
            print(content)


def load_minio_credentials(overwrite=True):
    minio_credentials_path = os.path.expanduser(MINIO_CREDENTIALS_PATH)  # noqa: F821
    minio_credentials = f"""[{MINIO_PROFILE_NAME}]
aws_access_key_id={os.getenv("MINIO_ROOT_USER")}
aws_secret_access_key={os.getenv("MINIO_ROOT_PASSWORD")}
"""  # noqa: F821

    if overwrite or not os.path.exists(minio_credentials_path):
        minio_credentials_dir = os.path.dirname(minio_credentials_path)
        os.makedirs(minio_credentials_dir, exist_ok=True)

        with open(minio_credentials_path, "w") as outfile:
            outfile.write(minio_credentials)
        if not os.path.exists(minio_credentials_path):
            raise RuntimeError(
                f"{minio_credentials_path} file has not been generated."
            )  # noqa: E501

        with open(minio_credentials_path, "r") as file:
            content = file.read()
            print(f"{minio_credentials_path}:")
            print(content)

    aws_credentials_path = os.path.expanduser("~/.aws/credentials")
    aws_credentials = f"""[default]
aws_access_key_id={os.getenv("AWS_ACCESS_KEY_ID")}
aws_secret_access_key={os.getenv("AWS_SECRET_ACCESS_KEY")}

{minio_credentials}
"""

    if overwrite or not os.path.exists(aws_credentials_path):
        aws_credentials_dir = os.path.dirname(aws_credentials_path)
        os.makedirs(aws_credentials_dir, exist_ok=True)

        with open(aws_credentials_path, "w") as outfile:
            outfile.write(aws_credentials)
        if not os.path.exists(aws_credentials_path):
            raise RuntimeError(f"{aws_credentials_path} file has not been generated.")

        with open(aws_credentials_path, "r") as file:
            content = file.read()
            print(f"{aws_credentials_path}:")
            print(content)

    config_path = os.path.expanduser(CONFIG_PATH)
    config = f"""{MINIO_PROFILE_NAME}:
    endpoint: "http://minio.default.svc.cluster.local:9000"
"""  # noqa: F821

    if overwrite or not os.path.exists(config_path):
        config_dir = os.path.dirname(config_path)
        os.makedirs(config_dir, exist_ok=True)

        with open(config_path, "w") as outfile:
            outfile.write(config)
        if not os.path.exists(config_path):
            raise RuntimeError(f"{config_path} file has not been generated.")

        with open(config_path, "r") as file:
            content = file.read()
            print(f"{config_path}:")
            print(content)

    _try_load_config()

    if not skypilot_config.get_nested(("minio", "endpoint"), None):
        raise Exception(f"minio endpoint is not set in {config_path}")
