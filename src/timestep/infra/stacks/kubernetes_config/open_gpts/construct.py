from cdktf_cdktf_provider_helm.provider import HelmProvider
from cdktf_cdktf_provider_kubernetes.config_map_v1 import (
    ConfigMapV1,
    ConfigMapV1Metadata,
)
from cdktf_cdktf_provider_kubernetes.deployment_v1 import (
    DeploymentV1,
    DeploymentV1Metadata,
    DeploymentV1Spec,
    DeploymentV1SpecSelector,
    DeploymentV1SpecTemplate,
    DeploymentV1SpecTemplateMetadata,
    DeploymentV1SpecTemplateSpec,
    DeploymentV1SpecTemplateSpecContainer,
    DeploymentV1SpecTemplateSpecContainerEnvFrom,
    DeploymentV1SpecTemplateSpecContainerEnvFromConfigMapRef,
    DeploymentV1SpecTemplateSpecContainerEnvFromSecretRef,
    DeploymentV1SpecTemplateSpecContainerPort,
    DeploymentV1SpecTemplateSpecContainerResources,
    DeploymentV1SpecTemplateSpecInitContainer,
    DeploymentV1SpecTemplateSpecInitContainerEnvFrom,
    DeploymentV1SpecTemplateSpecInitContainerEnvFromConfigMapRef,
    DeploymentV1SpecTemplateSpecInitContainerEnvFromSecretRef,
)
from cdktf_cdktf_provider_kubernetes.namespace_v1 import (
    NamespaceV1,
    NamespaceV1Metadata,
)
from cdktf_cdktf_provider_kubernetes.secret_v1 import SecretV1, SecretV1Metadata
from cdktf_cdktf_provider_kubernetes.service_v1 import (
    ServiceV1,
    ServiceV1Metadata,
    ServiceV1Spec,
    ServiceV1SpecPort,
)
from constructs import Construct

from timestep.config import Settings


class OpenGPTsConstruct(Construct):
    def __init__(
        self,
        scope: Construct,
        id: str,
        config: Settings,
        helm_provider: HelmProvider,
    ) -> None:
        super().__init__(scope, id)

        # self.open_gpts_helm_release_resource = Release(
        #     id_="open_gpts_helm_release_resource",
        #     atomic=True,
        #     chart="open-gpts",
        #     create_namespace=True,
        #     name="open-gpts",
        #     namespace="default",
        #     repository="https://langchain-ai.github.io/helm/",
        #     provider=helm_provider,
        #     set=[
        #         ReleaseSet(
        #             name="backend.service.type",
        #             value="ClusterIP",
        #         ),
        #     ],
        #     set_sensitive=[
        #         ReleaseSetSensitive(
        #             name="config.openaiApiKey",
        #             value=config.openai_api_key.get_secret_value(),
        #         ),
        #     ],
        #     scope=self,
        #     version="0.1.2",
        # )

        open_gpts_namespace = NamespaceV1(
            id_="open_gpts_namespace",
            metadata=NamespaceV1Metadata(
                name="open-gpts",
            ),
            scope=self,
        )

        open_gpts_config_map = ConfigMapV1(
            id_="open_gpts_config_map",
            data={
                "OLLAMA_MODEL": "llava-phi3:3.8b",
                "OLLAMA_BASE_URL": "http://ollama.ollama.svc.cluster.local:11434",
                "POSTGRES_DB": "open_gpts",
                "POSTGRES_HOST": config.postgres_hostname,
                "POSTGRES_PORT": config.postgres_port,
                "POSTGRES_USER": config.postgres_username,
            },
            metadata=ConfigMapV1Metadata(
                name="open-gpts-config-map",
                namespace=open_gpts_namespace.metadata.name,
            ),
            scope=self,
        )

        open_gpts_secret_data = {
            "POSTGRES_PASSWORD": config.postgres_password.get_secret_value(),
        }

        if config.anthropic_api_key:
            open_gpts_secret_data[
                "ANTHROPIC_API_KEY"
            ] = config.anthropic_api_key.get_secret_value()

        if config.langchain_api_key:
            open_gpts_secret_data[
                "LANGCHAIN_API_KEY"
            ] = config.langchain_api_key.get_secret_value()
            open_gpts_secret_data["LANGCHAIN_TRACING_V2"] = "true"

        if config.openai_api_key:
            open_gpts_secret_data[
                "OPENAI_API_KEY"
            ] = config.openai_api_key.get_secret_value()

        open_gpts_secret = SecretV1(
            id_="open_gpts_secret",
            data=open_gpts_secret_data,
            metadata=SecretV1Metadata(
                name="open-gpts-secret",
                namespace=open_gpts_namespace.metadata.name,
            ),
            scope=self,
        )

        self.open_gpts_backend_deployment_resource = DeploymentV1(
            id_="open_gpts_backend_deployment_resource",
            metadata=DeploymentV1Metadata(
                labels={
                    "app": "open-gpts-backend",
                },
                name="open-gpts-backend",
                namespace=open_gpts_namespace.metadata.name,
            ),
            spec=DeploymentV1Spec(
                replicas="1",
                selector=DeploymentV1SpecSelector(
                    match_labels={
                        "app": "open-gpts-backend",
                    }
                ),
                template=DeploymentV1SpecTemplate(
                    metadata=DeploymentV1SpecTemplateMetadata(
                        labels={
                            "app": "open-gpts-backend",
                        },
                    ),
                    spec=DeploymentV1SpecTemplateSpec(
                        container=[
                            DeploymentV1SpecTemplateSpecContainer(
                                env_from=[
                                    DeploymentV1SpecTemplateSpecContainerEnvFrom(
                                        config_map_ref=DeploymentV1SpecTemplateSpecContainerEnvFromConfigMapRef(
                                            name=open_gpts_config_map.metadata.name,
                                        ),
                                    ),
                                    DeploymentV1SpecTemplateSpecContainerEnvFrom(
                                        secret_ref=DeploymentV1SpecTemplateSpecContainerEnvFromSecretRef(
                                            name=open_gpts_secret.metadata.name,
                                        ),
                                    ),
                                ],
                                image="docker.io/mschock/open-gpts:latest",
                                image_pull_policy="IfNotPresent",
                                name="open-gpts-backend",
                                port=[
                                    DeploymentV1SpecTemplateSpecContainerPort(
                                        container_port=8000,
                                        name="http",
                                        protocol="TCP",
                                    )
                                ],
                                resources=DeploymentV1SpecTemplateSpecContainerResources(
                                    limits={
                                        "cpu": "4000m",
                                        "memory": "8Gi",
                                    },
                                    requests={
                                        "cpu": "100m",
                                        "memory": "128Mi",
                                    },
                                ),
                            )
                        ],
                        init_container=[
                            DeploymentV1SpecTemplateSpecInitContainer(
                                command=[
                                    "make",
                                    "migrate",
                                ],
                                env_from=[
                                    DeploymentV1SpecTemplateSpecInitContainerEnvFrom(
                                        config_map_ref=DeploymentV1SpecTemplateSpecInitContainerEnvFromConfigMapRef(
                                            name=open_gpts_config_map.metadata.name,
                                        ),
                                    ),
                                    DeploymentV1SpecTemplateSpecInitContainerEnvFrom(
                                        secret_ref=DeploymentV1SpecTemplateSpecInitContainerEnvFromSecretRef(
                                            name=open_gpts_secret.metadata.name,
                                        ),
                                    ),
                                ],
                                image="docker.io/mschock/open-gpts:latest",
                                image_pull_policy="IfNotPresent",
                                name="postgres-setup",
                            ),
                        ],
                    ),
                ),
            ),
            scope=self,
        )

        self.open_gpts_backend_service_resource = ServiceV1(
            depends_on=[self.open_gpts_backend_deployment_resource],
            id_="open_gpts_backend_service_resource",
            metadata=ServiceV1Metadata(
                labels={
                    "app": self.open_gpts_backend_deployment_resource.metadata.name,
                },
                name="open-gpts-backend",
                namespace=open_gpts_namespace.metadata.name,
            ),
            spec=ServiceV1Spec(
                port=[
                    ServiceV1SpecPort(
                        port=8000,
                        protocol="TCP",
                    )
                ],
                selector={
                    "app": self.open_gpts_backend_deployment_resource.metadata.name,
                },
                type="ClusterIP",
            ),
            scope=self,
        )
