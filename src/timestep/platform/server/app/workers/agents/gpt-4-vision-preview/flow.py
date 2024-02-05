import base64
import logging
import os
from typing import Any

import kubernetes
import sky
import yaml
from prefect import flow, get_run_logger, task
from prefect_shell import ShellOperation


def load_kubeconfig(overwrite=False, memo: dict[str, Any] = {}):
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

    # memo["kubeconfig_path"] = kubeconfig_path

    return memo

@task
async def load_cloud_credentials(memo: dict[str, Any]):
    logger = get_run_logger()

    try:
        kubernetes.config.load_incluster_config()
        memo = load_kubeconfig(memo)

    except kubernetes.config.config_exception.ConfigException as e:
        logger.info(e)

    return memo

@task
async def sky_check_task(memo: dict[str, Any]):
    sky.check.check()

    enabled_clouds: list[sky.clouds.Cloud] = sky.global_user_state.get_enabled_clouds()
    enabled_storage_clouds: list[
        str
    ] = sky.global_user_state.get_enabled_storage_clouds()

    memo["enabled_clouds"] = enabled_clouds
    memo["enabled_storage_clouds"] = enabled_storage_clouds

    return memo

@task
async def sky_status_task(memo: dict[str, Any]):
    memo["cluster_statuses"]: list[dict[str, Any]] = sky.core.status(refresh=True)

    return memo

@task
async def sky_launch_task(agent_name: str, memo: dict[str, Any]):
    minio_endpoint = os.environ["MINIO_ENDPOINT"]
    minio_root_user = os.environ["MINIO_ROOT_USER"]
    minio_root_password = os.environ["MINIO_ROOT_PASSWORD"]
    # openai_api_key = os.environ["OPENAI_API_KEY"]

    async with ShellOperation(
        commands=[
            f"""sky launch \
                --cluster {agent_name} \
                --detach-run \
                --env MINIO_ENDPOINT={minio_endpoint} \
                --env MINIO_ROOT_USER={minio_root_user} \
                --env MINIO_ROOT_PASSWORD={minio_root_password} \
                --yes launch.yaml
            """,
        ],
    ) as sky_op:
        sky_op_process = await sky_op.trigger()
        await sky_op_process.wait_for_completion()

    return memo

@task
async def sky_down_task(agent_name: str, memo: dict[str, Any]):
    async with ShellOperation(
        commands=[
            f"sky down {agent_name} --purge --yes"
        ],
    ) as sky_op:
        sky_op_process = await sky_op.trigger()
        await sky_op_process.wait_for_completion()

    return memo

@task
async def sky_queue_task(agent_name: str, memo: dict[str, Any]):
    memo["cluster_queue"]: list[dict] = sky.core.queue(cluster_name=agent_name)

    return memo

@task
async def sky_exec_task(
    agent_name: str,
    memo: dict[str, Any],
    task_yaml_name: str = "serve.yaml",
    cancel_all: bool = False,
):
    minio_endpoint = os.environ["MINIO_ENDPOINT"]
    minio_root_user = os.environ["MINIO_ROOT_USER"]
    minio_root_password = os.environ["MINIO_ROOT_PASSWORD"]
    # openai_api_key = os.environ["OPENAI_API_KEY"]

    if cancel_all:
        sky.core.cancel(cluster_name=agent_name, all=True) # TODO: Make this configurable

    async with ShellOperation(
        commands=[
            f"""sky exec {agent_name} \
                --detach-run \
                --env MINIO_ENDPOINT={minio_endpoint} \
                --env MINIO_ROOT_USER={minio_root_user} \
                --env MINIO_ROOT_PASSWORD={minio_root_password} \
                {task_yaml_name}
            """,
        ],
    ) as sky_op:
        sky_op_process = await sky_op.trigger()
        await sky_op_process.wait_for_completion()

    return memo

@flow
async def serve_agent_flow(account_id: str, agent_name: str, operation: str = "create"):
    logger: logging.Logger = get_run_logger()
    logger.info(f"account_id: {account_id}")
    logger.info(f"agent_name: {agent_name}")
    logger.info(f"operation: {operation}")
    memo: dict[str, Any] = {}

    memo = await load_cloud_credentials(memo)
    memo = await sky_check_task(memo)
    memo = await sky_status_task(memo)

    agent_cluster_is_already_deployed = False

    for cluster_status in memo["cluster_statuses"]:
        if cluster_status["name"] == agent_name:
            logger.info(f"cluster_status: {cluster_status}")
            agent_cluster_is_already_deployed = True

            break

    if operation == "create":
        if agent_cluster_is_already_deployed:
            raise Exception(f"Agent cluster {agent_name} is already deployed")

        memo = await sky_launch_task(agent_name, memo)
        memo = await sky_exec_task(agent_name, memo, task_yaml_name="serve.yaml", cancel_all=True)
        memo = await sky_exec_task(agent_name, memo, task_yaml_name="jupyter_lab.yaml", cancel_all=False)
        # memo = await sky_exec_task(agent_name, memo, task_yaml_name="jupyter_lab.yaml", cancel_all=True)

    elif operation == "delete":
        memo = await sky_down_task(agent_name, memo)

    elif operation == "read":
        try:
            memo = await sky_queue_task(agent_name, memo)

            return memo

        except sky.exceptions.ClusterNotUpError as e:
            logger.info(e)

            # memo = await sky_start_task(name, memo)

    elif operation == "update":
        memo = await sky_exec_task(agent_name, memo, task_yaml_name="serve.yaml", cancel_all=True)
        memo = await sky_exec_task(agent_name, memo, task_yaml_name="jupyter_lab.yaml", cancel_all=False)
        # memo = await sky_exec_task(agent_name, memo, task_yaml_name="jupyter_lab.yaml", cancel_all=True)

    memo = await sky_status_task(memo)

    return memo
