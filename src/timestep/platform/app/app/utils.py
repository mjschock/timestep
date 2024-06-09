import base64
import os

import kubernetes
import sky
import sky.clouds.kubernetes
import yaml


def create_sky_config(overwrite=False):
    # # ~/.sky/config.yaml
    # kubernetes:
    #     remote_identity: skypilot-service-account   # Or your service account name

    sky_config_path = os.path.expanduser("~/.sky/config.yaml")

    if overwrite or not os.path.exists(sky_config_path):
        sky_config = {
            "kubernetes": {
                # "remote_identity": "default",
                # "remote_identity": "skypilot-service-account",
                # "remote_identity": "LOCAL_CREDENTIALS",
                "remote_identity": "SERVICE_ACCOUNT",
                # Activated account: timestep.local_timestep.local_default
                # "remote_identity": "timestep.local_timestep.local_default",
                # TODO: try skypilot-service-account-role
                # "remote_identity": "skypilot-service-account-role",
                # "remote_identity": "default",
                # "remote_identity": "system:serviceaccount:default:default",
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
