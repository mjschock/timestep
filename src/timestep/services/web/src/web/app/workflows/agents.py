import asyncio
import base64
import os
from logging import Logger

import httpx
import kubernetes
import sky
import yaml
from llama_index import ServiceContext
from prefect import Flow, State, Task, flow, task
from prefect.blocks.kubernetes import KubernetesClusterConfig
from prefect.flows import FlowRun
from prefect.logging import get_run_logger
from prefect.tasks import TaskRun
from prefect.utilities.annotations import quote
from prefect_kubernetes.credentials import KubernetesCredentials
from prefect_shell import ShellOperation

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
        namespace_path = "/var/run/secrets/kubernetes.io/serviceaccount/namespace"
        service_account_token_path = (
            "/var/run/secrets/kubernetes.io/serviceaccount/token"
        )

        with open(namespace_path, "r") as file:
            file.read()

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

        print(f"{kubeconfig_path} file has been generated.")


@task
async def load_cloud_credentials():
    load_kubeconfig()


@task
async def sky_check_task():
    get_run_logger()

    async with ShellOperation(
        commands=[
            "sky check",
        ],
        # working_dir=f"data/{today}",
    ) as sky_check_operation:
        # trigger runs the process in the background
        sky_check_operation_process = await sky_check_operation.trigger()

        # then do other things here in the meantime, like download another file
        # logger.info("=== sky_check_operation_process ===")

        # when you're ready, wait for the process to finish
        await sky_check_operation_process.wait_for_completion()

        # if you'd like to get the output lines, you can use the `fetch_result` method
        # output_lines = await sky_check_operation_process.fetch_result()

        # logger.info("output_lines: %s", output_lines)

        # return await sky_check_operation.close()


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


def sky_launch_task_on_failure_hook(task: Task, task_run: TaskRun, state: State):
    get_run_logger()


@task(
    log_prints=True,
    on_failure=[
        sky_launch_task_on_failure_hook,
    ],
)
async def sky_launch_task():
    get_run_logger()

    async with ShellOperation(
        commands=[
            "sky launch --cluster min --yes examples/minimal.yaml",
        ],
        working_dir="workflows",
    ) as sky_launch_operation:
        sky_launch_operation_process = await sky_launch_operation.trigger()
        await sky_launch_operation_process.wait_for_completion()


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
            "ssh --help",  # ssh is needed
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
    logger: Logger = get_run_logger()
    in_cluster = True

    try:
        kubernetes.config.load_incluster_config()

    except kubernetes.config.config_exception.ConfigException as e:
        logger.debug(e)
        in_cluster = False

    if in_cluster:
        await load_cloud_credentials()

    await sky_check_task()

    local_model_ids = await ollama_list_local_models_task()

    logger.debug("local_model_ids: %s", local_model_ids)
    logger.debug("model_ids: %s", model_ids)

    for model_id in model_ids:
        if model_id not in local_model_ids:
            await ollama_pull_model_task(model_id=model_id)

    for model_id in model_ids:
        service_context = await create_service_context_task(model_id=model_id)
        await create_index_task(service_context=quote(service_context))

    # print ~/.kube/config
    logger.debug("=== ~/.kube/config ===")
    with open(os.path.expanduser("~/.kube/config"), "r") as file:
        logger.debug(file.read())

    k8s_config: KubernetesClusterConfig = KubernetesClusterConfig.from_file(
        context_name=os.getenv("KUBECONTEXT"), path="~/.kube/config"
    )

    logger.debug("k8s_config.config: %s", k8s_config.config)

    k8s_credentials = KubernetesCredentials(cluster_config=k8s_config)

    try:
        with k8s_credentials.get_client("core") as core_v1_client:
            for pod in core_v1_client.list_namespaced_pod(namespace="default"):
                logger.debug("pod.metadata.name: %s", pod.metadata.name)

        # for namespace in v1_core_client.list_namespace().items:
        #     logger.debug(namespace.metadata.name)

        # v1_deployment_metadata = await create_namespaced_deployment(
        #     # kubernetes_credentials=KubernetesCredentials.load("k8s-creds"),
        #     kubernetes_credentials=k8s_credentials,
        #     namespace='default',
        #     new_deployment=V1Deployment(metadata={"name": "test-agent-deployment"}),
        # )

        # logger.debug('v1_deployment_metadata: %s', v1_deployment_metadata)

        # v1_deployment_list = await list_namespaced_deployment(
        #     # kubernetes_credentials=KubernetesCredentials.load("k8s-creds")
        #     kubernetes_credentials=k8s_credentials,
        #     namespace='default',
        # )

        # logger.debug('v1_deployment_list: %s', v1_deployment_list)

        # v1_deployment_updates = convert_manifest_to_model(
        #     manifest="workflows/agent-deployment.yaml",
        #     v1_model_name="V1Deployment",
        # )

        # v1_deployment = patch_namespaced_deployment(
        #     # kubernetes_credentials=KubernetesCredentials.load("k8s-creds"),
        #     kubernetes_credentials=k8s_credentials,
        #     deployment_name="my-deployment",
        #     deployment_updates=v1_deployment_updates,
        #     namespace="my-namespace"
        # )

    except kubernetes.client.exceptions.ApiException as e:
        logger.debug(e)

    try:
        await sky_launch_task()  # TODO: sky launch -c min minimal.yaml
    except Exception as e:
        logger.debug(e)

    # await sky_serve_up_task()


if __name__ == "__main__":
    asyncio.run(
        deploy_agent_flow(
            model_ids=[47],
        )
    )
