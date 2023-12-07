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
)
from cdktf_cdktf_provider_kubernetes.service_v1 import (
    ServiceV1,
    ServiceV1Metadata,
    ServiceV1Spec,
    ServiceV1SpecPort,
)
from constructs import Construct

from timestep.config import Settings


class HasuraConstruct(Construct):
    def __init__(
        self,
        scope: Construct,
        id: str,
        config: Settings,
        helm_provider: HelmProvider,
    ) -> None:
        super().__init__(scope, id)

        postgres_database = "postgres"
        postgres_hostname = "postgresql-postgresql-ha-pgpool.default.svc.cluster.local"
        postgres_password = config.postgresql_password.get_secret_value()
        postgres_username = "postgres"

        self.hasura_graphql_engine_deployment_resource = DeploymentV1(
            id_="hasura_graphql_engine_deployment_resource",
            metadata=DeploymentV1Metadata(
                labels={
                    "app": "hasura-graphql-engine",
                },
                name="hasura-graphql-engine",
                namespace="default",
            ),
            spec=DeploymentV1Spec(
                replicas="1",
                selector=DeploymentV1SpecSelector(
                    match_labels={
                        "app": "hasura-graphql-engine",
                    }
                ),
                template=DeploymentV1SpecTemplate(
                    metadata=DeploymentV1SpecTemplateMetadata(
                        labels={
                            "app": "hasura-graphql-engine",
                        },
                    ),
                    spec=DeploymentV1SpecTemplateSpec(
                        container=[
                            DeploymentV1SpecTemplateSpecContainer(
                                env=[
                                    DeploymentV1SpecTemplateSpecContainerEnv(
                                        name="HASURA_GRAPHQL_ADMIN_SECRET",
                                        value=config.hasura_graphql_admin_secret.get_secret_value(),
                                    ),
                                    DeploymentV1SpecTemplateSpecContainerEnv(
                                        name="HASURA_GRAPHQL_DEV_MODE",
                                        value="true",
                                    ),
                                    DeploymentV1SpecTemplateSpecContainerEnv(
                                        name="HASURA_GRAPHQL_DATABASE_URL",
                                        value=f"postgres://{postgres_username}:{postgres_password}@{postgres_hostname}/{postgres_database}",
                                    ),
                                    DeploymentV1SpecTemplateSpecContainerEnv(
                                        name="HASURA_GRAPHQL_ENABLE_CONSOLE",
                                        value="true",
                                    ),
                                    DeploymentV1SpecTemplateSpecContainerEnv(
                                        name="HASURA_GRAPHQL_JWT_SECRET",
                                        value=f'{{"type": "HS256", "key": "{config.hasura_graphql_jwt_secret_key.get_secret_value()}", "issuer": "hasura-auth"}}',  # noqa: E501
                                    ),
                                    DeploymentV1SpecTemplateSpecContainerEnv(
                                        name="HASURA_GRAPHQL_LOG_LEVEL",
                                        value="debug",
                                    ),
                                    DeploymentV1SpecTemplateSpecContainerEnv(
                                        name="HASURA_GRAPHQL_UNAUTHORIZED_ROLE",
                                        value="public",
                                    ),
                                ],
                                image="hasura/graphql-engine:latest",
                                image_pull_policy="IfNotPresent",
                                name="hasura-graphql-engine",
                                port=[
                                    DeploymentV1SpecTemplateSpecContainerPort(
                                        container_port=8080,
                                        name="http",
                                        protocol="TCP",
                                    )
                                ],
                            )
                        ],
                    ),
                ),
            ),
            scope=self,
        )

        self.hasura_graphql_engine_service_resource = ServiceV1(
            depends_on=[self.hasura_graphql_engine_deployment_resource],
            id_="hasura_graphql_engine_service_resource",
            metadata=ServiceV1Metadata(
                labels={
                    "app": "hasura-graphql-engine",
                },
                name="hasura-graphql-engine",
                namespace="default",
            ),
            spec=ServiceV1Spec(
                port=[
                    ServiceV1SpecPort(
                        port=8080,
                        protocol="TCP",
                    )
                ],
                selector={
                    "app": "hasura-graphql-engine",
                },
                type="ClusterIP",
            ),
            scope=self,
        )
