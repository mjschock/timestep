from cdktf_cdktf_provider_helm.provider import HelmProvider
from cdktf_cdktf_provider_helm.release import (
    Release,
    ReleaseSet,
    ReleaseSetSensitive,
)
from cdktf_cdktf_provider_kubernetes.namespace_v1 import (
    NamespaceV1,
    NamespaceV1Metadata,
)
from cdktf_cdktf_provider_kubernetes.secret_v1 import SecretV1, SecretV1Metadata
from constructs import Construct

from timestep.config import Settings


class LiteLLMProxyConstruct(Construct):
    def __init__(
        self,
        scope: Construct,
        id: str,
        config: Settings,
        helm_provider: HelmProvider,
    ) -> None:
        super().__init__(scope, id)

        postgres_hostname = config.postgres_hostname
        postgres_password = config.postgres_password.get_secret_value()
        postgres_username = config.postgres_username

        self.litellm_proxy_namespace = NamespaceV1(
            id_="litellm_proxy_namespace",
            metadata=NamespaceV1Metadata(
                name="litellm-proxy",
            ),
            scope=self,
        )

        self.litellm_proxy_postgres_secret_resource = SecretV1(
            depends_on=[self.litellm_proxy_namespace],
            id_="litellm_proxy_postgres_secret_resource",
            data={
                "username": postgres_username,  # db.secret.usernameKey
                "password": postgres_password,  # db.secret.passwordKey
            },
            metadata=SecretV1Metadata(
                name="postgres",  # db.secret.name
                namespace=self.litellm_proxy_namespace.metadata.name,
            ),
            scope=self,
        )

        # See https://github.com/BerriAI/litellm/tree/main/deploy/charts/litellm-helm for more info # noqa E501
        self.litellm_proxy_helm_release_resource = Release(
            id_="litellm_proxy_helm_release_resource",
            atomic=True,
            chart="litellm-helm",
            cleanup_on_fail=True,
            create_namespace=True,
            depends_on=[self.litellm_proxy_postgres_secret_resource],
            name="litellm-proxy",
            namespace=self.litellm_proxy_namespace.metadata.name,
            repository="https://berriai.github.io/litellm/",
            provider=helm_provider,
            set=[
                ReleaseSet(
                    name="image.repository",
                    # value="ghcr.io/berriai/litellm-database",
                    value="docker.io/mschock/litellm-database",
                ),
                ReleaseSet(
                    name="image.tag",
                    # value="main-v1.40.3-stable",
                    value="latest",
                ),
                ReleaseSet(
                    name="db.database",
                    value="litellm",
                ),
                ReleaseSet(
                    name="db.deployStandalone",
                    value="false",
                ),
                ReleaseSet(
                    name="db.endpoint",
                    value=postgres_hostname,
                ),
                ReleaseSet(
                    name="db.secret.name",
                    value=self.litellm_proxy_postgres_secret_resource.metadata.name,
                ),
                ReleaseSet(
                    name="db.secret.passwordKey",
                    value="password",
                ),
                ReleaseSet(
                    name="db.secret.usernameKey",
                    value="username",
                ),
                ReleaseSet(
                    name="db.useExisting",
                    value="true",
                ),
            ],
            set_sensitive=[
                ReleaseSetSensitive(
                    name="masterkey",
                    value=config.litellm_master_key.get_secret_value(),
                ),
            ],
            scope=self,
            values=[
                """
proxy_config:
  model_list:
    # At least one model must exist for the proxy to start.
    - model_name: gpt-3.5-turbo
      litellm_params:
        model: gpt-3.5-turbo
        api_key: eXaMpLeOnLy
    - model_name: fake-openai-endpoint
      litellm_params:
        model: openai/fake
        api_key: fake-key
        api_base: https://test-production.up.railway.app/
    - model_name: llava-phi3
      litellm_params:
        model: ollama/llava-phi3:3.8b
        api_base: http://ollama.ollama.svc.cluster.local:11434
  general_settings:
    master_key: os.environ/PROXY_MASTER_KEY
"""
            ],
            version="0.2.0",
        )
