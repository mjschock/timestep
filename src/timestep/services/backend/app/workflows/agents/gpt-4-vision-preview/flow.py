import base64
import logging
import os
from typing import Any, Dict, List

import kubernetes
import sky
import yaml
from prefect import flow, get_run_logger, task
from prefect_shell import ShellOperation


def load_kubeconfig(overwrite=True, memo: Dict[str, Any] = {}):
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
async def load_cloud_credentials(memo: Dict[str, Any]):
    logger = get_run_logger()

    try:
        kubernetes.config.load_incluster_config()
        memo = load_kubeconfig(memo)

    except kubernetes.config.config_exception.ConfigException as e:
        logger.info(e)

    return memo


@task
async def litestream_restore_task(account_id: str, memo: Dict[str, Any]):
    logger = get_run_logger()
    cwd = os.getcwd()
    logger.info(f"cwd: {cwd}")

    # ["-c", "litestream restore -if-db-not-exists -if-replica-exists /home/ubuntu/.sky/benchmark.db; litestream restore -if-db-not-exists -if-replica-exists /home/ubuntu/.sky/jobs.db; litestream restore -if-db-not-exists -if-replica-exists /home/ubuntu/.sky/spot_jobs.db; litestream restore -if-db-not-exists -if-replica-exists /home/ubuntu/.sky/state.db;"]

    async with ShellOperation(
        commands=[
            "echo 'hello world'",
            "pwd",
            "ls -al",
            f"litestream restore -config litestream.yml -if-db-not-exists -if-replica-exists /home/ubuntu/.sky/benchmark.db",
            f"litestream restore -config litestream.yml -if-db-not-exists -if-replica-exists /home/ubuntu/.sky/jobs.db",
            f"litestream restore -config litestream.yml -if-db-not-exists -if-replica-exists /home/ubuntu/.sky/spot_jobs.db",
            f"litestream restore -config litestream.yml -if-db-not-exists -if-replica-exists /home/ubuntu/.sky/state.db",
        ],
        env={
            "ACCOUNT_ID": account_id,
            "LITESTREAM_ACCESS_KEY_ID": os.getenv("MINIO_ROOT_USER"),
            "LITESTREAM_SECRET_ACCESS_KEY": os.getenv("MINIO_ROOT_PASSWORD"),
        },
        # working_dir=f"{os.getcwd()}/app/workflows",
    ) as sky_op:
        sky_op_process = await sky_op.trigger()
        await sky_op_process.wait_for_completion()

    return memo


@task
async def litestream_replicate_task(account_id: str, memo: Dict[str, Any]):
    logger = get_run_logger()
    cwd = os.getcwd()
    logger.info(f"cwd: {cwd}")

    async with ShellOperation(
        commands=[
            "echo 'hello world'",
            "pwd",
            "ls -al",
            f"litestream replicate -config litestream.yml",
        ],
        env={
            "ACCOUNT_ID": account_id,
            "LITESTREAM_ACCESS_KEY_ID": os.getenv("MINIO_ROOT_USER"),
            "LITESTREAM_SECRET_ACCESS_KEY": os.getenv("MINIO_ROOT_PASSWORD"),
        },
        # working_dir=f"{os.getcwd()}/app/workflows",
    ) as sky_op:
        sky_op_process = await sky_op.trigger()
        await sky_op_process.wait_for_completion()

    return memo


@task
async def sky_launch_task(name: str, memo: Dict[str, Any]):
    minio_endpoint = os.environ["MINIO_ENDPOINT"]
    minio_root_user = os.environ["MINIO_ROOT_USER"]
    minio_root_password = os.environ["MINIO_ROOT_PASSWORD"]
    openai_api_key = os.environ["OPENAI_API_KEY"]

    cwd = os.getcwd()
    print(f"cwd: {cwd}")

    async with ShellOperation(
        commands=[
            f"""sky launch \
                --cluster {name} \
                --env MINIO_ENDPOINT={minio_endpoint} \
                --env MINIO_ROOT_USER={minio_root_user} \
                --env MINIO_ROOT_PASSWORD={minio_root_password} \
                --env OPENAI_API_KEY={openai_api_key} \
                --yes serve.yaml
            """,
        ],
        # working_dir=f"{os.getcwd()}/app/workflows",
    ) as sky_op:
        sky_op_process = await sky_op.trigger()
        await sky_op_process.wait_for_completion()

    return memo


@task
async def sky_check_task(memo: Dict[str, Any]):
    logger = get_run_logger()

    sky.check.check()

    enabled_clouds: List[sky.clouds.Cloud] = sky.global_user_state.get_enabled_clouds()
    enabled_storage_clouds: List[
        str
    ] = sky.global_user_state.get_enabled_storage_clouds()

    logger.info("enabled_clouds: %s", enabled_clouds)
    logger.info("enabled_storage_clouds: %s", enabled_storage_clouds)

    # memo["enabled_clouds"] = enabled_clouds
    # memo["enabled_storage_clouds"] = enabled_storage_clouds

    return memo

@task
async def sky_status_task(memo: Dict[str, Any]):
    # logger: logging.Logger = get_run_logger()

    # async with ShellOperation(
    #     commands=[
    #         f"sky status",
    #     ],
    #     # working_dir="workflows",
    #     # working_dir=f"{cwd}/app/api/routers/workflows",
    # ) as sky_op:
    #     sky_op_process = await sky_op.trigger()
    #     await sky_op_process.wait_for_completion()

    memo["cluster_statuses"]: List[Dict[str, Any]] = sky.core.status(refresh=True)

    return memo


@flow(
    log_prints=True,
)
async def serve_agent_flow(account_id: str, name: str):
    logger: logging.Logger = get_run_logger()
    # agent: Dict[str, Any] = {
    #     "name": name,
    # }
    memo: Dict[str, Any] = {}

    memo = await litestream_restore_task(account_id, memo)

    memo = await load_cloud_credentials(memo)
    memo = await sky_check_task(memo)
    memo = await sky_status_task(memo)

    agent_cluster_is_already_deployed = False

    for cluster_status in memo["cluster_statuses"]:
        if cluster_status["name"] == name:
            agent_cluster_is_already_deployed = True

            break

    if agent_cluster_is_already_deployed:
        logger.info("Agent cluster is already deployed")

    else:
        logger.info("Launching agent cluster")
        memo = await sky_launch_task(name, memo)

    # memo = await sky_status_task(memo)

    # for cluster_status in memo["cluster_statuses"]:
    #     if cluster_status["name"] == name:
    #         agent["id"] = cluster_status["cluster_hash"] # TODO: use db to store agent id instead of cluster hash
    #         agent["cluster_status"] = cluster_status

    #         break

    # return agent

    memo = await litestream_replicate_task(account_id, memo)
