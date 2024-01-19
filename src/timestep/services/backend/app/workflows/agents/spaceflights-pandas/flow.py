import base64
import logging
import os
from typing import Any, Dict, List
import httpx

import kubernetes
import minio
from prefect_aws import AwsClientParameters, MinIOCredentials, S3Bucket
from pydantic import SecretStr
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


# @task
# async def litestream_restore_task(account_id: str, memo: Dict[str, Any]):
#     logger = get_run_logger()
#     cwd = os.getcwd()
#     logger.info(f"cwd: {cwd}")

#     # ["-c", "litestream restore -if-db-not-exists -if-replica-exists /home/ubuntu/.sky/benchmark.db; litestream restore -if-db-not-exists -if-replica-exists /home/ubuntu/.sky/jobs.db; litestream restore -if-db-not-exists -if-replica-exists /home/ubuntu/.sky/spot_jobs.db; litestream restore -if-db-not-exists -if-replica-exists /home/ubuntu/.sky/state.db;"]

#     async with ShellOperation(
#         commands=[
#             "echo 'hello world'",
#             "pwd",
#             "ls -al",
#             f"litestream restore -config litestream.yml -if-db-not-exists -if-replica-exists /home/ubuntu/.sky/benchmark.db",
#             f"litestream restore -config litestream.yml -if-db-not-exists -if-replica-exists /home/ubuntu/.sky/jobs.db",
#             f"litestream restore -config litestream.yml -if-db-not-exists -if-replica-exists /home/ubuntu/.sky/spot_jobs.db",
#             f"litestream restore -config litestream.yml -if-db-not-exists -if-replica-exists /home/ubuntu/.sky/state.db",
#         ],
#         env={
#             "ACCOUNT_ID": account_id,
#             "LITESTREAM_ACCESS_KEY_ID": os.getenv("MINIO_ROOT_USER"),
#             "LITESTREAM_SECRET_ACCESS_KEY": os.getenv("MINIO_ROOT_PASSWORD"),
#         },
#         # working_dir=f"{os.getcwd()}/app/workflows",
#     ) as sky_op:
#         sky_op_process = await sky_op.trigger()
#         await sky_op_process.wait_for_completion()

#     return memo



# @task
# async def sqlite_restore_task(account_id: str, memo: dict[str, Any]):
#     logger = get_run_logger()
#     cwd = os.getcwd()
#     logger.info(f"cwd: {cwd}")

#     # ["-c", "litestream restore -if-db-not-exists -if-replica-exists /home/ubuntu/.sky/benchmark.db; litestream restore -if-db-not-exists -if-replica-exists /home/ubuntu/.sky/jobs.db; litestream restore -if-db-not-exists -if-replica-exists /home/ubuntu/.sky/spot_jobs.db; litestream restore -if-db-not-exists -if-replica-exists /home/ubuntu/.sky/state.db;"]

#     async with ShellOperation(
#         commands=[
#             "echo 'Restore sqlite databases'",
#             "pwd",
#             "ls -al",
#             "ls -al ~/.sky",
#             # f"litestream restore -config litestream.yml -if-db-not-exists -if-replica-exists /home/ubuntu/.sky/benchmark.db",
#             # f"litestream restore -config litestream.yml -if-db-not-exists -if-replica-exists /home/ubuntu/.sky/jobs.db",
#             # f"litestream restore -config litestream.yml -if-db-not-exists -if-replica-exists /home/ubuntu/.sky/spot_jobs.db",
#             # f"litestream restore -config litestream.yml -if-db-not-exists -if-replica-exists /home/ubuntu/.sky/state.db",
#             # "sqlite3 /home/ubuntu/.sky/benchmark.db \"VACUUM INTO '/home/ubuntu/.sky/benchmark.db.backup'\"",
#             # "gzip /home/ubuntu/.sky/benchmark.db.backup",
#             # "ls -al",
#         ],
#         env={
#             "ACCOUNT_ID": account_id,
#             "LITESTREAM_ACCESS_KEY_ID": os.getenv("MINIO_ROOT_USER"),
#             "LITESTREAM_SECRET_ACCESS_KEY": os.getenv("MINIO_ROOT_PASSWORD"),
#         },
#         # working_dir=f"{os.getcwd()}/app/workflows",
#     ) as sky_op:
#         sky_op_process = await sky_op.trigger()
#         await sky_op_process.wait_for_completion()

#     return memo


# @task
# async def litestream_replicate_task(account_id: str, memo: Dict[str, Any]):
#     logger = get_run_logger()
#     cwd = os.getcwd()
#     logger.info(f"cwd: {cwd}")

#     async with ShellOperation(
#         commands=[
#             "echo 'hello world'",
#             "pwd",
#             "ls -al",
#             f"litestream replicate -config litestream.yml",
#         ],
#         env={
#             "ACCOUNT_ID": account_id,
#             "LITESTREAM_ACCESS_KEY_ID": os.getenv("MINIO_ROOT_USER"),
#             "LITESTREAM_SECRET_ACCESS_KEY": os.getenv("MINIO_ROOT_PASSWORD"),
#         },
#         # working_dir=f"{os.getcwd()}/app/workflows",
#     ) as sky_op:
#         sky_op_process = await sky_op.trigger()
#         await sky_op_process.wait_for_completion()

#     return memo

# @task
# async def sqlite_replicate_task(account_id: str, memo: dict[str, Any]):
#     logger = get_run_logger()
#     cwd = os.getcwd()
#     logger.info(f"cwd: {cwd}")

#     async with ShellOperation(
#         commands=[
#             "echo 'Replicate sqlite databases'",
#             "pwd",
#             "ls -al",
#             # f"litestream replicate -config litestream.yml",
#             "sqlite3 /home/ubuntu/.sky/state.db \"VACUUM INTO '/home/ubuntu/.sky/state.db.backup'\"",
#             "gzip /home/ubuntu/.sky/state.db.backup",
#             "ls -al ~/.sky",
#             "minio "
#         ],
#         env={
#             "ACCOUNT_ID": account_id,
#             "LITESTREAM_ACCESS_KEY_ID": os.getenv("MINIO_ROOT_USER"),
#             "LITESTREAM_SECRET_ACCESS_KEY": os.getenv("MINIO_ROOT_PASSWORD"),
#         },
#         # working_dir=f"{os.getcwd()}/app/workflows",
#     ) as sky_op:
#         sky_op_process = await sky_op.trigger()
#         await sky_op_process.wait_for_completion()

#     return memo


@task(
    timeout_seconds=600,
)
async def sky_launch_task(name: str, memo: dict[str, Any]):
    minio_endpoint = os.environ["MINIO_ENDPOINT"]
    minio_root_user = os.environ["MINIO_ROOT_USER"]
    minio_root_password = os.environ["MINIO_ROOT_PASSWORD"]
    openai_api_key = os.environ["OPENAI_API_KEY"]

    cwd = os.getcwd()
    print(f"cwd: {cwd}")

    async with ShellOperation(
        commands=[
            "ls -al ~/.sky",
            f"""sky launch \
                --cluster {name} \
                --detach-run \
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
async def sky_start_task(name: str, memo: dict[str, Any]):
    async with ShellOperation(
        commands=[
            f"""sky start \
                {name} \
                --yes
            """,
        ],
    ) as sky_op:
        sky_op_process = await sky_op.trigger()
        await sky_op_process.wait_for_completion()

    return memo

def sky_exec_task_on_failure(task, old_state, new_state):
    logger = get_run_logger()
    logger.info(f"sky_exec_task_on_failure: {task} {old_state} {new_state}")


@task(
    on_failure=[sky_exec_task_on_failure]
)
async def sky_exec_task(name: str, memo: dict[str, Any]):
    minio_endpoint = os.environ["MINIO_ENDPOINT"]
    minio_root_user = os.environ["MINIO_ROOT_USER"]
    minio_root_password = os.environ["MINIO_ROOT_PASSWORD"]
    openai_api_key = os.environ["OPENAI_API_KEY"]

    cwd = os.getcwd()
    print(f"cwd: {cwd}")

    sky.core.cancel(cluster_name=name, all=True)

    async with ShellOperation(
        commands=[
            f"""sky exec {name} \
                --detach-run \
                --env MINIO_ENDPOINT={minio_endpoint} \
                --env MINIO_ROOT_USER={minio_root_user} \
                --env MINIO_ROOT_PASSWORD={minio_root_password} \
                --env OPENAI_API_KEY={openai_api_key} \
                serve.yaml
            """,
        ],
        # working_dir=f"{os.getcwd()}/app/workflows",
    ) as sky_op:
        sky_op_process = await sky_op.trigger()
        await sky_op_process.wait_for_completion()

    return memo

@task
async def sky_queue_task(name: str, memo: dict[str, Any]):
    memo["cluster_queue"]: list[dict] = sky.core.queue(cluster_name=name)  # noqa: E501

    return memo

@task
async def sky_check_task(memo: dict[str, Any]):
    logger = get_run_logger()

    sky.check.check()

    enabled_clouds: list[sky.clouds.Cloud] = sky.global_user_state.get_enabled_clouds()
    enabled_storage_clouds: list[
        str
    ] = sky.global_user_state.get_enabled_storage_clouds()

    logger.info("enabled_clouds: %s", enabled_clouds)
    logger.info("enabled_storage_clouds: %s", enabled_storage_clouds)

    # memo["enabled_clouds"] = enabled_clouds
    # memo["enabled_storage_clouds"] = enabled_storage_clouds

    return memo

@task
async def sky_status_task(memo: dict[str, Any]):
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

    memo["cluster_statuses"]: list[dict[str, Any]] = sky.core.status(refresh=True)

    return memo


async def create_minio_storage_block(
    bucket_folder: str,
    bucket_name: str,
):
    # minio_endpoint_url = f'http://{os.getenv("MINIO_ENDPOINT")}'
    # minio_storage_block = S3Bucket(
    #     bucket_folder=bucket_folder,
    #     bucket_name=bucket_name,
    #     credentials=MinIOCredentials(
    #         aws_client_parameters=AwsClientParameters(
    #             endpoint_url=minio_endpoint_url,
    #             verify=False,
    #             use_ssl=False,
    #         ),
    #         minio_root_user=os.getenv("MINIO_ROOT_USER"),
    #         minio_root_password=SecretStr(os.getenv("MINIO_ROOT_PASSWORD")),
    #     ),
    # )

    # await minio_storage_block.save("minio-storage", overwrite=True)

    return await S3Bucket.load("minio-storage")

async def upload_directory_to_minio(
    minio_storage_block: S3Bucket,
    local_path: str,
    to_path: str,
) -> int:
    return await minio_storage_block.put_directory(
        local_path=local_path,
        to_path=to_path,
    )

@task
async def load_sky_data(account_id: str, name: str, memo: dict[str, Any]):
    # logger = get_run_logger()

    # minio_endpoint = os.getenv("MINIO_ENDPOINT")
    # minio_client = minio.Minio(
    #     minio_endpoint,
    #     access_key=os.getenv("MINIO_ROOT_USER"),
    #     secret_key=os.getenv("MINIO_ROOT_PASSWORD"),
    #     secure=False,
    # )

    # sky_data_folder = "/home/ubuntu/.sky"

    # minio_storage_block = await create_minio_storage_block(
    #     bucket_folder=account_id,
    #     bucket_name="default",
    # )
    # print('local_path')
    # print(f"{os.getcwd()}/app/workflows/agents/{name}")
    # uploaded_file_count: int = await upload_directory_to_minio(
    #     minio_storage_block=minio_storage_block,
    #     # local_path=f"{os.getcwd()}/app/workflows/agents/{name}",
    #     local_path="/home/ubuntu/.sky",
    #     # to_path=f"agents/{name}"
    #     to_path=f"agents/{name}/.sky",
    # )

    # await minio_storage_block.get_directory(
    #     local_path="/home/ubuntu/.sky",
    #     from_path=f"agents/{name}/.sky",
    # )

    async with ShellOperation(
        commands=[
            "yes | cp -rf .sky /home/ubuntu/",
            "yes | cp -rf .ssh /home/ubuntu/",
        ],
        # working_dir=f"{os.getcwd()}/app/workflows",
    ) as sky_op:
        sky_op_process = await sky_op.trigger()
        await sky_op_process.wait_for_completion()

    # logger.info(f"uploaded_file_count: {uploaded_file_count}")

    return memo

@task
async def save_sky_data(account_id: str, name: str, memo: dict[str, Any]):
    logger = get_run_logger()

    minio_storage_block = await create_minio_storage_block(
        bucket_folder=account_id,
        bucket_name="default",
    )

    uploaded_file_count: int = await upload_directory_to_minio(
        minio_storage_block=minio_storage_block,
        local_path="/home/ubuntu/.sky",
        to_path=f"agents/{name}/.sky",
    )

    logger.info(f"uploaded_file_count: {uploaded_file_count}")

    uploaded_file_count: int = await upload_directory_to_minio(
        minio_storage_block=minio_storage_block,
        local_path="/home/ubuntu/.ssh",
        to_path=f"agents/{name}/.ssh",
    )

    return memo

@task
async def sky_down_task(name: str, memo: dict[str, Any]):
    async with ShellOperation(
        commands=[
            f"sky down {name} --purge --yes"
        ],
    ) as sky_op:
        sky_op_process = await sky_op.trigger()
        await sky_op_process.wait_for_completion()

    return memo

@flow(
    log_prints=True,
)
async def serve_agent_flow(account_id: str, name: str, operation: str = "create", ap_check=False):
    logger: logging.Logger = get_run_logger()
    logger.info(f"account_id: {account_id}")
    logger.info(f"ap_check: {ap_check}")
    logger.info(f"name: {name}")
    logger.info(f"operation: {operation}")
    # agent: Dict[str, Any] = {
    #     "name": name,
    # }
    memo: dict[str, Any] = {}

    # memo = await load_sky_data(account_id, name, memo)

    # memo = await litestream_restore_task(account_id, memo)
    # memo = await sqlite_restore_task(account_id, memo)

    memo = await load_cloud_credentials(memo)
    memo = await sky_check_task(memo)
    memo = await sky_status_task(memo)

    agent_cluster_is_already_deployed = False

    for cluster_status in memo["cluster_statuses"]:
        if cluster_status["name"] == name:
            logger.info(f"cluster_status: {cluster_status}")
            agent_cluster_is_already_deployed = True

            break

    if ap_check:
        head_ip = cluster_status["handle"].head_ip
        async with ShellOperation(
            commands=[
                # f'URL=http://{head_ip}:8000 bash -c "$(curl -fsSL https://agentprotocol.ai/test.sh)"',
                # f"URL=http://{head_ip}:8000 bash -c test.sh",
                # f"URL=http://{head_ip}:8000 ls -al",
                # "ls -al /bin",
                # f"URL=http://{head_ip}:8000 bash test.sh",
                "curl -fsSL https://agentprotocol.ai/test.sh > test.sh",
                "dos2unix test.sh",
                f"URL=http://{head_ip}:8000 bash test.sh",
            ],
            shell="bash",
            # working_dir=f"{os.getcwd()}/app/workflows",
            # working_dir=f"{os.getcwd()}/tests",
            working_dir="/tmp",
        ) as sky_op:
            sky_op_process = await sky_op.trigger()
            await sky_op_process.wait_for_completion()
            return await sky_op_process.fetch_result()

    if operation == "create":
        if agent_cluster_is_already_deployed:
            raise Exception(f"Agent cluster {name} is already deployed")

        memo = await sky_launch_task(name, memo)

    elif operation == "read":
        try:
            memo = await sky_queue_task(name, memo)

            return memo

        except sky.exceptions.ClusterNotUpError as e:
            logger.info(e)

            memo = await sky_start_task(name, memo)

    elif operation == "delete":
        memo = await sky_down_task(name, memo)

    elif operation == "update":
        memo = await sky_exec_task(name, memo)

    # logger.info(f"agent_cluster_is_already_deployed: {agent_cluster_is_already_deployed}")

    # if agent_cluster_is_already_deployed:
    #     logger.info("Agent cluster is already deployed")
    #     memo = await sky_exec_task(name, memo)

    # else:
    #     logger.info("Launching agent cluster")
    #     memo = await sky_launch_task(name, memo)

    memo = await sky_status_task(memo)

    for cluster_status in memo["cluster_statuses"]:
        if cluster_status["name"] == name:
    # #         agent["id"] = cluster_status["cluster_hash"] # TODO: use db to store agent id instead of cluster hash
    # #         agent["cluster_status"] = cluster_status
            logger.info(f"cluster_status: {cluster_status}")

            if operation in ("create", "update"):
            #     logger.info(f"Waiting for agent cluster {name} to be ready")

                assert cluster_status["status"] == sky.ClusterStatus.UP, f"{cluster_status['status']} != {sky.ClusterStatus.UP}"

            #     head_ip = cluster_status["handle"].head_ip

            #     async with httpx.AsyncClient() as client:
            #         logger.info(f"GET http://{head_ip}:8000/livez")
            #         resp = await client.get(f"http://{head_ip}:8000/livez")
            #         assert resp.json() == "ok", f"{resp.json()} != ok"

            #     async with httpx.AsyncClient() as client:
            #         logger.info(f"GET http://{head_ip}:8000/readyz")
            #         resp = await client.get(f"http://{head_ip}:8000/readyz")
            #         assert resp.json() == "ok", f"{resp.json()} != ok"

            break

    # return agent

    # memo = await litestream_replicate_task(account_id, memo)
    # memo = await sqlite_replicate_task(account_id, memo)
    # memo = await save_sky_data(account_id, name, memo)

    return memo
