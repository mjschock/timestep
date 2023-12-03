import base64
import json

from cdktf_cdktf_provider_helm.provider import HelmProvider
from cdktf_cdktf_provider_kubernetes.secret_v1 import SecretV1, SecretV1Metadata
from constructs import Construct

from timestep.config import Settings


class ContainerRegistryConstruct(Construct):
    def __init__(
        self,
        scope: Construct,
        id: str,
        config: Settings,
        helm_provider: HelmProvider,
    ) -> None:
        super().__init__(scope, id)

        # self.release_resource = Release(
        #     id_="registry_helm_release_resource",
        #     atomic=True,
        #     chart="harbor",
        #     create_namespace=True,
        #     name="harbor",
        #     namespace="default",
        #     repository="https://charts.bitnami.com/bitnami",
        #     provider=helm_provider,
        #     set=[],
        #     set_sensitive=[
        #         ReleaseSetSensitive(
        #             name="adminPassword",
        #             value=config.registry_admin_password.get_secret_value(),
        #         )
        #     ],
        #     scope=self,
        # )

        docker_registry_email = config.docker_registry_email
        docker_registry_password = config.docker_registry_password.get_secret_value()
        docker_registry_username = config.docker_registry_username
        docker_registry_server = config.docker_registry_server

        docker_config_json = {
            "auths": {
                docker_registry_server: {
                    "auth": base64.b64encode(
                        f"{docker_registry_username}:{docker_registry_password}".encode(
                            "utf-8"
                        )
                    ).decode("utf-8"),
                    "email": docker_registry_email,
                    "password": docker_registry_password,
                    "username": docker_registry_username,
                }
            }
        }

        self.regcred_secret = SecretV1(
            id_="regcred_secret",
            data={
                ".dockerconfigjson": json.dumps(docker_config_json),
            },
            metadata=SecretV1Metadata(
                name="regcred",
                namespace="default",
            ),
            scope=self,
            type="kubernetes.io/dockerconfigjson",
        )
