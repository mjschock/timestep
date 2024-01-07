import asyncio
import base64
import os
from logging import Logger
from typing import Any, Dict, List

import httpx
import kubernetes

# from sky.check import check as sky_check
import sky
import yaml
from llama_index import ServiceContext
from prefect import Flow, State, Task, flow, runtime, task
from prefect.blocks.system import Secret
from prefect.flows import FlowRun
from prefect.logging import get_run_logger
from prefect.tasks import TaskRun
from prefect_aws import MinIOCredentials
from prefect_shell import ShellOperation
from prefect_sqlalchemy import (
    ConnectionComponents,
    SqlAlchemyConnector,
    SyncDriver,
)

from .utils.index import get_index, get_service_context


def load_kubeconfig(overwrite=True):
    kubeconfig_path = os.path.expanduser(sky.clouds.kubernetes.CREDENTIAL_PATH)

    if overwrite or not os.path.exists(kubeconfig_path):
        cluster_name = os.getenv("PRIMARY_DOMAIN_NAME")
        kubecontext = os.getenv("KUBECONTEXT")
        kubernetes_service_host = os.getenv("KUBERNETES_SERVICE_HOST")
        kubernetes_service_port = os.getenv("KUBERNETES_SERVICE_PORT")
        user_name = os.getenv("PRIMARY_DOMAIN_NAME")

        ca_certificate_path = "/var/run/secrets/kubernetes.io/serviceaccount/ca.crt"
        # namespace_path = "/var/run/secrets/kubernetes.io/serviceaccount/namespace"
        service_account_token_path = (
            "/var/run/secrets/kubernetes.io/serviceaccount/token"
        )

        kubernetes.config.load_incluster_config()
        config = kubernetes.client.Configuration.get_default_copy()

        server = config.host

        assert (
            server == f"https://{kubernetes_service_host}:{kubernetes_service_port}"
        ), f"{server} != https://{kubernetes_service_host}:{kubernetes_service_port}"

        ssl_ca_cert = config.ssl_ca_cert

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
                        # "namespace": namespace,
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
                    "user": {"token": service_account_token},
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

        # print(f"{kubeconfig_path} file has been generated.")


@task
async def load_cloud_credentials(memo: Dict[str, Any]):
    logger = get_run_logger()

    try:
        kubernetes.config.load_incluster_config()
        load_kubeconfig()

    except kubernetes.config.config_exception.ConfigException as e:
        logger.debug(e)

    return memo


@task
async def backup_sqlite_db_task():
    db_path = os.path.expanduser(sky.core.global_user_state._DB_PATH)
    # https://litestream.io/alternatives/cron/
    # #!/bin/bash -x

    # # Ensure script stops when commands fail.
    # set -e

    # # Backup & compress our database to the temp directory.
    # sqlite3 /path/to/db "VACUUM INTO '/path/to/backup'"
    # gzip /tmp/db

    # # Upload backup to S3 using a rolling daily naming scheme.
    # aws s3 cp /tmp/db.gz s3://mybucket/db-`date +%d`.gz

    # async with ShellOperation(
    #     commands=[
    #         # "ssh --help",  # ssh is needed
    #         # "sky serve up --yes examples/serve/ray_serve/ray_serve.yaml",
    #         f"sqlite3 {db_path} 'VACUUM INTO {db_path}.backup'",
    #         f"gzip {db_path}.backup",
    #         f"aws s3 cp {db_path}.backup.gz s3://default/sky_db-`date +%d`.gz",
    #     ],
    #     # working_dir="workflows",
    # ) as shell_op:
    #     shell_op_process = await shell_op.trigger()
    #     await shell_op_process.wait_for_completion()

    # connector = SqlAlchemyConnector(
    #     connection_info=ConnectionComponents(
    #         driver=SyncDriver.SQLITE_PYSQLITE,
    #         database=db_path,
    #     )
    # )

    # connector.save('sky-pilot-db', overwrite=True)

    # with SqlAlchemyConnector.load('sky-pilot-db') as connector:
    #     connector.execute(f'VACUUM INTO {db_path}.backup')

    with SqlAlchemyConnector(
        connection_info=ConnectionComponents(
            driver=SyncDriver.SQLITE_PYSQLITE,
            # database="prefect.db"
            database=db_path,
        )
    ) as database:
        database.execute(f"VACUUM INTO {db_path}.backup")

    # async with SqlAlchemyConnector.load('sky-pilot-db') as connector:
    # await connector.execute(f'VACUUM INTO {db_path}.backup')

    async with ShellOperation(
        commands=[
            "pwd",
            "ls -al",
            "ls -al workflows",
            "ls -al /home/ubuntu/.sky",
            "gzip --version",
            f"gzip {db_path}.backup",
        ],
        # working_dir="workflows",
    ) as shell_op:
        shell_op_process = await shell_op.trigger()
        await shell_op_process.wait_for_completion()

    # async with S3Bucket.load("default") as s3_bucket:
    #     await s3_bucket.upload_from_path(f"{db_path}.backup.gz", "sky_db-`date +%d`.gz")  # noqa: E501

    # minio_root_user_secret_block = await Secret.load('minio-root-user')
    # minio_root_password_secret_block = await Secret.load('minio-root-password')

    # minio_credentials = MinIOCredentials(
    #     minio_root_user=minio_root_user_secret_block.get(),
    #     minio_root_password=minio_root_password_secret_block.get(),
    # )
    # s3_client = minio_credentials.get_boto3_session().client(
    #     service_name="s3",
    #     endpoint_url=f'http://{os.getenv("MINIO_ENDPOINT")}',
    # )

    # with open(db_path, "rb") as f:
    #     s3_client.upload_fileobj(f, "default", "sky_db")
    #     # f.close()


@task
async def sky_db_task():
    # sky.global_user_state._DB_PATH
    # from sky.core import global_user_state
    SQL_LITE_DB_PATH = os.path.expanduser(  # noqa: N806
        sky.core.global_user_state._DB_PATH
    )  # noqa: N806, E501

    # minio_storage_block = await S3Bucket.load("minio-storage")

    # s3_bucket_block.download_file(
    #     key="sky_db",
    #     path=SQL_LITE_DB_PATH,
    # )

    # await minio_storage_block.download_object_to_path(
    #     from_path="my_folder/notes.txt",
    #     to_path=SQL_LITE_DB_PATH
    # )

    minio_root_user_secret_block = await Secret.load("minio-root-user")
    minio_root_password_secret_block = await Secret.load("minio-root-password")

    minio_credentials = MinIOCredentials(
        minio_root_user=minio_root_user_secret_block.get(),
        minio_root_password=minio_root_password_secret_block.get(),
    )
    s3_client = minio_credentials.get_boto3_session().client(
        service_name="s3",
        endpoint_url=f'http://{os.getenv("MINIO_ENDPOINT")}',
    )
    # s3_client.download_file(
    #     'BUCKET_NAME', 'OBJECT_NAME', 'FILE_NAME'
    # )
    response = s3_client.list_buckets()

    logger = get_run_logger()

    logger.debug("response: %s", response)

    for bucket in response["Buckets"]:
        logger.debug(f"Bucket Name: {bucket['Name']}")

    # bucket_name = "default"

    try:
        with open(SQL_LITE_DB_PATH, "wb") as f:
            s3_client.download_fileobj("default", "sky_db", f)
            f.close()

    except Exception as e:
        logger.debug(e)

    with open(SQL_LITE_DB_PATH, "rb") as f:
        s3_client.upload_fileobj(f, "default", "sky_db")
        f.close()

    with open(SQL_LITE_DB_PATH, "wb") as f:
        s3_client.download_fileobj("default", "sky_db", f)
        f.close()

    # s3_client.download_file(
    #     'BUCKET_NAME', 'OBJECT_NAME', 'FILE_NAME'
    # )
    # await s3_bucket.upload_from_path("notes.txt", "my_folder/notes.txt")

    # storage = RemoteStorage(
    #     url="s3://my-bucket/my-folder",
    #     # Use Secret blocks to keep credentials out of your code
    #     key=Secret.load("my-aws-access-key"),
    #     secret=Secret.load("my-aws-secret-key"),
    # )

    # await storage.pull_code()

    # connector = SqlAlchemyConnector(
    #     connection_info=ConnectionComponents(
    #         driver=AsyncDriver.SQLITE_AIOSQLITE,
    #         database=SQL_LITE_DB_PATH,
    #     )
    # )

    # connector.save("sky_db", overwrite=True)

    # all_rows = []
    # with SqlAlchemyConnector.load(block_name) as connector:
    #     while True:
    #         # Repeated fetch* calls using the same operation will
    #         # skip re-executing and instead return the next set of results
    #         new_rows = connector.fetch_many("SELECT * FROM customers", size=2)
    #         if len(new_rows) == 0:
    #             break
    #         all_rows.append(new_rows)

    # return all_rows


@task
async def sky_check_task(memo: Dict[str, Any]):
    logger = get_run_logger()

    # async with ShellOperation(
    #     commands=[
    #         "sky check",
    #     ],
    #     # working_dir=f"data/{today}",
    # ) as sky_check_operation:
    #     # trigger runs the process in the background
    #     sky_check_operation_process = await sky_check_operation.trigger()

    #     # then do other things here in the meantime, like download another file
    #     # logger.info("=== sky_check_operation_process ===")

    #     # when you're ready, wait for the process to finish
    #     await sky_check_operation_process.wait_for_completion()

    #     # if you'd like to get the output lines, you can use the `fetch_result` method
    #     # output_lines = await sky_check_operation_process.fetch_result()

    #     # logger.info("output_lines: %s", output_lines)

    #     # return await sky_check_operation.close()

    sky.check.check()

    enabled_clouds: List[sky.clouds.Cloud] = sky.global_user_state.get_enabled_clouds()
    enabled_storage_clouds: List[
        str
    ] = sky.global_user_state.get_enabled_storage_clouds()  # noqa: E501

    logger.debug("enabled_clouds: %s", enabled_clouds)
    logger.debug("enabled_storage_clouds: %s", enabled_storage_clouds)

    # return enabled_clouds, enabled_storage_clouds

    memo["enabled_clouds"] = enabled_clouds
    memo["enabled_storage_clouds"] = enabled_storage_clouds

    return memo


@task
async def ollama_list_local_models_task():
    logger = get_run_logger()
    logger.debug("ollama_list_local_models_task")

    url = "http://ollama.default.svc.cluster.local:80/api/tags"
    # response = httpx.post(
    #     url,
    #     json={
    #         "name": model_id,
    #     },

    # repo = response.json()

    local_model_ids = []

    response = httpx.get(url)

    # logger.debug(response)
    # logger.debug(response.json())

    # client = httpx.AsyncClient()

    local_models = response.json().get("models", [])

    logger.debug(local_models)

    local_model_ids = [local_model["name"] for local_model in local_models]

    # async with client.stream('GET', url) as response:
    #     logger.debug(response.status_code)
    #     logger.debug(response.headers['content-type'])

    #     async for chunk in response.aiter_bytes():
    #         logger.debug(chunk)

    # async with client.get(url) as response:
    #     logger.debug(response)

    # await client.aclose()

    return local_model_ids


@task
async def ollama_pull_model_task(model_id: str):
    logger = get_run_logger()

    url = "http://ollama.default.svc.cluster.local:80/api/pull"
    # response = httpx.post(
    #     url,
    #     json={
    #         "name": model_id,
    #     },

    # repo = response.json()

    client = httpx.AsyncClient()

    async with client.stream("POST", url, json={"name": model_id}) as response:
        logger.debug(response.status_code)
        logger.debug(response.headers["content-type"])

        async for chunk in response.aiter_bytes():
            logger.debug(chunk)

    await client.aclose()


@task
async def create_service_context_task(model_id: str) -> ServiceContext:
    logger = get_run_logger()

    logger.debug("Creating service context for model_id: %s", model_id)

    service_context = await get_service_context()

    logger.debug("service_context: %s", service_context)

    return service_context


@task
async def create_index_task(service_context: ServiceContext):
    logger = get_run_logger()

    logger.debug("Creating index for service_context: %s", service_context)

    index = await get_index(service_context)

    logger.debug("index: %s", index)

    return index


def sky_status_task_on_failure_hook(task: Task, task_run: TaskRun, state: State):
    get_run_logger()


@task(
    on_failure=[
        sky_status_task_on_failure_hook,
    ],
)
async def sky_status_task(memo: Dict[str, Any]):
    logger = get_run_logger()

    # async with ShellOperation(
    #     commands=[
    #         "sky status",
    #     ],
    #     working_dir="workflows",
    # ) as sky_status_operation:
    #     sky_status_operation_process = await sky_status_operation.trigger()
    #     await sky_status_operation_process.wait_for_completion()

    cluster_statuses: List[Dict[str, Any]] = sky.status(
        cluster_names=None,
        refresh=True,
    )

    logger.debug("cluster_statuses: %s", cluster_statuses)

    memo["cluster_statuses"] = cluster_statuses

    return memo

    # return cluster_statuses


def sky_launch_task_on_failure_hook(task: Task, task_run: TaskRun, state: State):
    get_run_logger()


@task(
    log_prints=True,
    on_failure=[
        sky_launch_task_on_failure_hook,
    ],
)
async def sky_launch_task(memo: Dict[str, Any]):
    get_run_logger()

    runtime.flow_run.get_id()

    # AGENT_ID ?= 58648f86-a691-11ee-b5cf-2bc42583c635
    AGENT_ID = "58648f86-a691-11ee-b5cf-2bc42583c635"  # noqa: N806
    # AGENT_ID_SHORT_HASH ?= $(shell echo ${AGENT_ID} | cut -c1-8)
    AGENT_ID_SHORT_HASH = AGENT_ID[:8]  # noqa: N806

    async with ShellOperation(
        commands=[
            # "sky launch --cluster min --yes examples/minimal.yaml",
            f"sky launch --cluster agent-cluster-{AGENT_ID_SHORT_HASH} --yes agents/{AGENT_ID}/serve.yaml"  # noqa: E501
        ],
        working_dir="workflows",
    ) as sky_launch_operation:
        sky_launch_operation_process = await sky_launch_operation.trigger()
        await sky_launch_operation_process.wait_for_completion()

    # task = sky.Task(
    #     run='echo hello SkyPilot',
    #     setup='echo Running setup',
    # )

    # logger.debug("os.getenv('PREFECT_API_URL'): %s", os.getenv("PREFECT_API_URL"))

    # task = sky.Task(
    #     envs={
    #         "FLOW_RUN_ID": flow_run_id,
    #         "PREFECT_API_URL": os.getenv("PREFECT_API_URL"),
    #     },
    #     # event_callback=event_callback,
    #     run='python train.py',
    #     setup='pip install -r requirements.txt',
    #     workdir='workflows/examples/serve/ray_serve',
    # )

    # task.set_resources(
    #    sky.Resources(
    #        cloud=sky.Kubernetes(),
    #        cpus='1+',
    #        memory='0.5+',
    #     #    ports=8000,
    #     )
    # )

    # # (job_id, handle): Tuple[
    # #     Optional[int],
    # #     Optional[sky.backends.ResourceHandle]
    # # ] = sky.launch(
    # #     cluster_name="timestep-ai-k8s-cluster",
    # #     task=task,
    # # )

    # sky_launch_tuple: Tuple[
    #     Optional[int],
    #     Optional[sky.backends.ResourceHandle]
    # ] = sky.launch(
    #     cluster_name="timestep-ai-k8s-cluster",
    #     # down=True,
    #     stream_logs=True,
    #     task=task,
    # )

    # job_id = sky_launch_tuple[0]
    # handle = sky_launch_tuple[1]

    # logger.debug("job_id: %s", job_id)
    # logger.debug("handle: %s", handle)

    # memo["job_id"] = job_id
    # memo["handle"] = handle

    # cluster_yaml = handle.cluster_yaml

    # Read generated cluster yaml
    # with open(handle.cluster_yaml, "r") as file:
    # logger.debug(f"handle.cluster_yaml: {file.read()}")

    return memo


@task
async def sky_exec_task():
    # logger = get_run_logger()

    async with ShellOperation(
        commands=[
            "sky exec timestep-ai-k8s-cluster examples/minimal.yaml",
        ],
        working_dir="workflows",
    ) as sky_op:
        sky_op_process = await sky_op.trigger()
        await sky_op_process.wait_for_completion()

    # task = sky.Task(
    #     run='echo hello SkyPilot!',
    #     setup='echo Running setup',
    # )

    # task.set_resources(
    #    sky.Resources(
    #        cloud=sky.Kubernetes(),
    #        cpus='1+',
    #        memory='0.5+'
    #     ))

    # sky_exec_tuple: Tuple[
    #     Optional[int],
    #     Optional[sky.backends.ResourceHandle]
    # ] = sky.exec(
    #     cluster_name="timestep-ai-k8s-cluster",
    #     task=task,
    # )

    # job_id = sky_exec_tuple[0]
    # handle = sky_exec_tuple[1]

    # logger.debug("job_id: %s", job_id)
    # logger.debug("handle: %s", handle)


@task
async def sky_down_task():
    sky.down(
        cluster_name="timestep-ai-k8s-cluster",
    )


def sky_serve_up_task_on_failure_hook(task: Task, task_run: TaskRun, state: State):
    get_run_logger()


@task(
    log_prints=True,
    on_failure=[
        sky_serve_up_task_on_failure_hook,
    ],
)
async def sky_serve_up_task():
    get_run_logger()

    async with ShellOperation(
        commands=[
            "sky serve up --yes examples/serve/ray_serve/ray_serve.yaml",
        ],
        working_dir="workflows",
    ) as sky_serve_up_operation:
        sky_serve_up_operation_process = await sky_serve_up_operation.trigger()
        await sky_serve_up_operation_process.wait_for_completion()


def deploy_agent_flow_on_crashed_hook(flow: Flow, flow_run: FlowRun, state: State):
    get_run_logger()


@flow(
    log_prints=True,
    on_crashed=[
        deploy_agent_flow_on_crashed_hook,
    ],
)
async def deploy_agent_flow(model_ids: list = None):
    # logger: Logger = get_run_logger()
    # in_cluster = True

    # try:
    #     kubernetes.config.load_incluster_config()

    # except kubernetes.config.config_exception.ConfigException as e:
    #     logger.debug(e)
    #     in_cluster = False

    # if in_cluster:
    #     await load_cloud_credentials()

    # # await sky_db_task()

    # enabled_clouds, enabled_storage_clouds = await sky_check_task()

    # await sky_status_task()

    logger: Logger = get_run_logger()
    memo: Dict[str, Any] = {}

    memo = await load_cloud_credentials(memo)
    memo = await sky_check_task(memo)
    memo = await sky_launch_task(memo)

    logger.info(f"memo: {memo}")

    # cluster_statuses = await sky_status_task()

    # await sky_launch_task()

    # cluster_statuses = await sky_status_task()

    # # await sky_exec_task()

    # # cluster_statuses = await sky_status_task()

    # await sky_down_task()

    # cluster_statuses = await sky_status_task()

    # await sky_serve_up_task()

    # await backup_sqlite_db_task()

    # local_model_ids = await ollama_list_local_models_task()

    # logger.debug("local_model_ids: %s", local_model_ids)
    # logger.debug("model_ids: %s", model_ids)

    # for model_id in model_ids:
    #     if model_id not in local_model_ids:
    #         await ollama_pull_model_task(model_id=model_id)

    # for model_id in model_ids:
    #     service_context = await create_service_context_task(model_id=model_id)
    #     await create_index_task(service_context=quote(service_context))

    # print ~/.kube/config
    # logger.debug("=== ~/.kube/config ===")
    # with open(os.path.expanduser("~/.kube/config"), "r") as file:
    #     logger.debug(file.read())

    # k8s_config: KubernetesClusterConfig = KubernetesClusterConfig.from_file(
    #     context_name=os.getenv("KUBECONTEXT"), path="~/.kube/config"
    # )

    # logger.debug("k8s_config.config: %s", k8s_config.config)

    # k8s_credentials = KubernetesCredentials(cluster_config=k8s_config)

    # try:
    #     with k8s_credentials.get_client("core") as core_v1_client:
    #         for pod in core_v1_client.list_namespaced_pod(namespace="default"):
    #             logger.debug("pod.metadata.name: %s", pod.metadata.name)

    #     # for namespace in v1_core_client.list_namespace().items:
    #     #     logger.debug(namespace.metadata.name)

    #     # v1_deployment_metadata = await create_namespaced_deployment(
    #     #     # kubernetes_credentials=KubernetesCredentials.load("k8s-creds"),
    #     #     kubernetes_credentials=k8s_credentials,
    #     #     namespace='default',
    #     #     new_deployment=V1Deployment(metadata={"name": "test-agent-deployment"}),
    #     # )

    #     # logger.debug('v1_deployment_metadata: %s', v1_deployment_metadata)

    #     # v1_deployment_list = await list_namespaced_deployment(
    #     #     # kubernetes_credentials=KubernetesCredentials.load("k8s-creds")
    #     #     kubernetes_credentials=k8s_credentials,
    #     #     namespace='default',
    #     # )

    #     # logger.debug('v1_deployment_list: %s', v1_deployment_list)

    #     # v1_deployment_updates = convert_manifest_to_model(
    #     #     manifest="workflows/agent-deployment.yaml",
    #     #     v1_model_name="V1Deployment",
    #     # )

    #     # v1_deployment = patch_namespaced_deployment(
    #     #     # kubernetes_credentials=KubernetesCredentials.load("k8s-creds"),
    #     #     kubernetes_credentials=k8s_credentials,
    #     #     deployment_name="my-deployment",
    #     #     deployment_updates=v1_deployment_updates,
    #     #     namespace="my-namespace"
    #     # )

    # except kubernetes.client.exceptions.ApiException as e:
    #     logger.debug(e)

    # try:
    #     await sky_launch_task()  # TODO: sky launch -c min minimal.yaml
    # except Exception as e:
    #     logger.debug(e)

    # await sky_serve_up_task()


if __name__ == "__main__":
    asyncio.run(
        deploy_agent_flow(
            model_ids=[47],
        )
    )
