import base64
import logging
import os

import kubernetes
import reflex as rx
import yaml

logger = logging.getLogger(__name__)

try:
    import sky
    import sky.check
    import sky.exceptions
    import sky.clouds.kubernetes
    import sky.serve.core

except PermissionError as e:
    logger.error(f"Permission error: {e}")

def create_sky_config(overwrite=False):
    # # ~/.sky/config.yaml
    # kubernetes:
    #     remote_identity: skypilot-service-account   # Or your service account name

    sky_config_path = os.path.expanduser("~/.sky/config.yaml")

    if overwrite or not os.path.exists(sky_config_path):
        sky_config = {
            "kubernetes": {
                "networking": "nodeport",
                "ports": "ingress",
                "remote_identity": "LOCAL_CREDENTIALS",
            }
        }

        # Create ~/.sky directory if it doesn't exist
        sky_dir = os.path.dirname(sky_config_path)
        os.makedirs(sky_dir, exist_ok=True)

        # Save the sky config dictionary to ~/.sky/config.yaml
        with open(sky_config_path, "w") as outfile:
            yaml.dump(sky_config, outfile, default_flow_style=False)

        if not os.path.exists(sky_config_path):
            raise RuntimeError(f"{sky_config_path} file has not been generated.")


def load_kubeconfig(overwrite=False):
    kubernetes.config.load_incluster_config()

    kubeconfig_path = os.path.expanduser(sky.clouds.kubernetes.CREDENTIAL_PATH)

    if overwrite or not os.path.exists(kubeconfig_path):
        cluster_name = os.getenv("PRIMARY_DOMAIN_NAME")
        kubecontext = os.getenv("KUBECONTEXT")
        kubernetes_service_host = os.getenv("KUBERNETES_SERVICE_HOST")
        kubernetes_service_port = os.getenv("KUBERNETES_SERVICE_PORT")
        user_account_name = os.getenv("PRIMARY_DOMAIN_NAME")
        # user_account_name = "skypilot-service-account-role"
        # user_account_name = "default"
        # user_account_name = "system:serviceaccount:default:default"
        # user_account_name = "system:serviceaccount:default:
        # user_account_name = "skypilot-service-account"
        # user_account_name = "ubuntu"

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
                        "user": user_account_name,
                    },
                    "name": kubecontext,
                }
            ],
            "current-context": kubecontext,
            "preferences": {},
            "users": [
                {
                    "name": user_account_name,
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

async def serve():
    logger.debug("debug message")
    logger.info("info message")
    logger.warning("warn message")
    logger.error("error message")
    logger.critical("critical message")

    # load_kubeconfig(overwrite=True)
    # create_sky_config(overwrite=True)

    try:
        import sky
        import sky.check
        import sky.exceptions
        import sky.clouds.kubernetes
        import sky.serve.core

    except PermissionError as e:
        logger.error(f"Permission error: {e}")

        return

    try:
        sky.check.check(
            clouds=None,
            quiet=False,
            verbose=True,
        )

    except SystemExit as e:
        logger.error(f"System exit: {e}")

        return

    try:
        cluster_statuses = sky.status(refresh=True)
        logger.info(f"Cluster statuses: {cluster_statuses}")

    except Exception as e:
        logger.error(f"type: {type(e)}")
        logger.error(f"Exception: {e}")

        return

    try:
        service_statuses = sky.serve.core.status()
        logger.info(f"Service statuses: {service_statuses}")

    except sky.exceptions.ClusterNotUpError as e:
        logger.error(f"Cluster not up: {e}")

        # return

    try:
        # TODO: move this to a Dag
        # TODO: run this as a cron job w/ Prefect
        # task = sky.Task(
        #     run="python train.py",
        #     setup="pip install -r requirements.txt",
        #     workdir=f"{os.getcwd()}/app/api/services/ray_train",
        # ).set_resources(
        #     [
        #         sky.Resources(
        #             cloud=sky.clouds.Kubernetes(),
        #             cpus="1+",
        #             memory="0.1+",
        #         ),
        #     ]
        # )

        # job_id, handle = sky.launch(
        #     task,
        #     cluster_name="sky-train-cluster",  # "sky-serve-cluster",
        #     detach_setup=True,
        #     detach_run=True,
        #     down=True,
        # )

        # logger.info(f"Job ID: {job_id}")
        # logger.info(f"Handle: {handle}")

        # logger.debug(f"cwd: {os.getcwd()}")

        # TODO: run service as ClusterIP instead of LoadBalancer and proxy via Caddy
        ray_serve_task = (
            sky.Task(
                run="serve run serve:app --host 0.0.0.0",
                setup="pip install -r requirements.txt",
                workdir=f"{os.getcwd()}/timestep/services/serve",
            )
            .set_resources(
                [
                    sky.Resources(
                        cloud=sky.clouds.Kubernetes(),
                        cpus="1+",
                        memory="0.1+",
                        ports=[8000],
                    ),
                ]
            )
            .set_service(
                service=sky.serve.SkyServiceSpec(
                    initial_delay_seconds=3,
                    min_replicas=1,
                    readiness_path="/",
                    readiness_timeout_seconds=30,
                )
            )
        )

        ray_serve_job_id, ray_serve_handle = sky.launch(
            ray_serve_task,
            cluster_name="sky-serve-cluster",
            detach_run=True,
            detach_setup=True,
        )

        logger.info(f"Ray Serve Job ID: {ray_serve_job_id}")
        logger.info(f"Ray Serve Handle: {ray_serve_handle}")

        return ray_serve_job_id

    except RuntimeError as e:
        logger.error(f"Runtime error: {e}")

        return

    except sky.exceptions.ResourcesUnavailableError as e:
        logger.error(f"Resources unavailable: {e}")

        return

    except Exception as e:
        logger.error(f"type: {type(e)}")
        logger.error(f"Exception: {e}")

    return

def train():
    return
