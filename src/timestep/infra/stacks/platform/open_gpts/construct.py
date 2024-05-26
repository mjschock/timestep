from cdktf_cdktf_provider_helm.provider import HelmProvider
from cdktf_cdktf_provider_kubernetes.deployment_v1 import (
    DeploymentV1,
    DeploymentV1Metadata,
    DeploymentV1Spec,
    DeploymentV1SpecSelector,
    DeploymentV1SpecTemplate,
    DeploymentV1SpecTemplateMetadata,
    DeploymentV1SpecTemplateSpec,
    DeploymentV1SpecTemplateSpecContainer,
    DeploymentV1SpecTemplateSpecContainerEnv,
    DeploymentV1SpecTemplateSpecContainerPort,
    DeploymentV1SpecTemplateSpecContainerResources,
    DeploymentV1SpecTemplateSpecInitContainer,
    DeploymentV1SpecTemplateSpecInitContainerEnv,
)
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

        env = [
            DeploymentV1SpecTemplateSpecContainerEnv(
                name="POSTGRES_DB",
                value=config.postgres_database,
            ),
            DeploymentV1SpecTemplateSpecContainerEnv(
                name="POSTGRES_HOST",
                value=config.postgres_hostname,
            ),
            DeploymentV1SpecTemplateSpecContainerEnv(
                name="POSTGRES_PASSWORD",  # TODO: move to secret # noqa: E501
                value=config.postgres_password.get_secret_value(),
            ),
            DeploymentV1SpecTemplateSpecContainerEnv(
                name="POSTGRES_PORT",
                value=config.postgres_port,
            ),
            DeploymentV1SpecTemplateSpecContainerEnv(
                name="POSTGRES_USER",
                value=config.postgres_username,
            ),
        ]

        if config.anthropic_api_key:
            env.append(
                DeploymentV1SpecTemplateSpecContainerEnv(
                    name="ANTHROPIC_API_KEY",
                    value=config.anthropic_api_key.get_secret_value(),
                )
            )

        if config.langchain_api_key:
            env.append(
                DeploymentV1SpecTemplateSpecContainerEnv(
                    name="LANGCHAIN_API_KEY",
                    value=config.langchain_api_key.get_secret_value(),
                )
            )
            env.append(
                DeploymentV1SpecTemplateSpecContainerEnv(
                    name="LANGCHAIN_TRACING_V2",
                    value="true",
                )
            )

        if config.openai_api_key:
            env.append(
                DeploymentV1SpecTemplateSpecContainerEnv(
                    name="OPENAI_API_KEY",  # TODO: move to secret
                    value=config.openai_api_key.get_secret_value(),
                )
            )

        self.open_gpts_backend_deployment_resource = DeploymentV1(
            id_="open_gpts_backend_deployment_resource",
            metadata=DeploymentV1Metadata(
                labels={
                    "app": "open-gpts-backend",
                },
                name="open-gpts-backend",
                namespace="default",  # TODO: open-gpts
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
                                env=env,
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
                                env=[
                                    DeploymentV1SpecTemplateSpecInitContainerEnv(
                                        name="POSTGRES_DB",
                                        value=config.postgres_database,
                                    ),
                                    DeploymentV1SpecTemplateSpecInitContainerEnv(
                                        name="POSTGRES_HOST",
                                        value=config.postgres_hostname,
                                    ),
                                    DeploymentV1SpecTemplateSpecInitContainerEnv(
                                        name="POSTGRES_PASSWORD",  # TODO: move to secret # noqa: E501
                                        value=config.postgres_password.get_secret_value(),
                                    ),
                                    DeploymentV1SpecTemplateSpecInitContainerEnv(
                                        name="POSTGRES_PORT",
                                        value=config.postgres_port,
                                    ),
                                    DeploymentV1SpecTemplateSpecInitContainerEnv(
                                        name="POSTGRES_USER",
                                        value=config.postgres_username,
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
                    "app": "open-gpts-backend",
                },
                name="open-gpts-backend",
                namespace="default",
            ),
            spec=ServiceV1Spec(
                port=[
                    ServiceV1SpecPort(
                        port=8000,
                        protocol="TCP",
                    )
                ],
                selector={
                    "app": "open-gpts-backend",
                },
                type="ClusterIP",
            ),
            scope=self,
        )
