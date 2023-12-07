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


class NhostConstruct(Construct):
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

        self.nhost_hasura_auth_deployment_resource = DeploymentV1(
            id_="nhost_hasura_auth_deployment_resource",
            metadata=DeploymentV1Metadata(
                labels={
                    "app": "nhost-hasura-auth",
                },
                name="nhost-hasura-auth",
                namespace="default",
            ),
            spec=DeploymentV1Spec(
                replicas="1",
                selector=DeploymentV1SpecSelector(
                    match_labels={
                        "app": "nhost-hasura-auth",
                    }
                ),
                template=DeploymentV1SpecTemplate(
                    metadata=DeploymentV1SpecTemplateMetadata(
                        labels={
                            "app": "nhost-hasura-auth",
                        },
                    ),
                    spec=DeploymentV1SpecTemplateSpec(
                        container=[
                            DeploymentV1SpecTemplateSpecContainer(
                                env=[
                                    DeploymentV1SpecTemplateSpecContainerEnv(
                                        name="AUTH_CLIENT_URL",
                                        value=f"https://www.{config.primary_domain_name}",
                                    ),
                                    DeploymentV1SpecTemplateSpecContainerEnv(
                                        name="AUTH_MFA_ENABLED",
                                        value="true",
                                    ),
                                    DeploymentV1SpecTemplateSpecContainerEnv(
                                        name="AUTH_PASSWORD_HIBP_ENABLED",
                                        value="true",
                                    ),
                                    DeploymentV1SpecTemplateSpecContainerEnv(
                                        name="AUTH_PASSWORD_MIN_LENGTH",
                                        value="14",  # https://bitwarden.com/blog/how-long-should-my-password-be/
                                    ),
                                    DeploymentV1SpecTemplateSpecContainerEnv(
                                        name="AUTH_SERVER_URL",
                                        value=f"https://www.{config.primary_domain_name}/v1/auth",
                                    ),
                                    DeploymentV1SpecTemplateSpecContainerEnv(
                                        name="AUTH_SMTP_HOST",
                                        value="smtp.gmail.com",  # The sending limit is 2,000 messages per day.  # noqa: E501
                                    ),
                                    DeploymentV1SpecTemplateSpecContainerEnv(
                                        name="AUTH_SMTP_PASS",
                                        value=config.smtp_password.get_secret_value(),
                                    ),
                                    DeploymentV1SpecTemplateSpecContainerEnv(
                                        name="AUTH_SMTP_PORT",
                                        value="587",
                                    ),
                                    DeploymentV1SpecTemplateSpecContainerEnv(
                                        name="AUTH_SMTP_SENDER",
                                        value=config.smtp_sender,
                                    ),
                                    DeploymentV1SpecTemplateSpecContainerEnv(
                                        name="AUTH_SMTP_USER",
                                        value="agent@timestep.ai",
                                        # value="Timestep AI Agent"
                                    ),
                                    DeploymentV1SpecTemplateSpecContainerEnv(
                                        name="HASURA_GRAPHQL_ADMIN_SECRET",
                                        value=config.hasura_graphql_admin_secret.get_secret_value(),
                                    ),
                                    DeploymentV1SpecTemplateSpecContainerEnv(
                                        name="HASURA_GRAPHQL_DATABASE_URL",
                                        value=f"postgres://{postgres_username}:{postgres_password}@{postgres_hostname}/{postgres_database}",
                                    ),
                                    DeploymentV1SpecTemplateSpecContainerEnv(
                                        name="HASURA_GRAPHQL_GRAPHQL_URL",
                                        value="http://hasura-graphql-engine.default.svc.cluster.local:8080/v1/graphql",  # noqa: E501
                                    ),
                                    DeploymentV1SpecTemplateSpecContainerEnv(
                                        name="HASURA_GRAPHQL_JWT_SECRET",
                                        value=f'{{"type": "HS256", "key": "{config.hasura_graphql_jwt_secret_key.get_secret_value()}", "issuer": "hasura-auth"}}',  # noqa: E501
                                    ),
                                ],
                                image="nhost/hasura-auth:latest",
                                name="nhost-hasura-auth",
                                port=[
                                    DeploymentV1SpecTemplateSpecContainerPort(
                                        container_port=4000,
                                        name="http",
                                    )
                                ],
                            )
                        ],
                    ),
                ),
            ),
            scope=self,
        )

        self.nhost_hasura_auth_service_resource = ServiceV1(
            depends_on=[
                self.hasura_graphql_engine_service_resource,
                self.nhost_hasura_auth_deployment_resource,
            ],
            id_="nhost_hasura_auth_service_resource",
            metadata=ServiceV1Metadata(
                labels={
                    "app": "nhost-hasura-auth",
                },
                name="nhost-hasura-auth",
                namespace="default",
            ),
            spec=ServiceV1Spec(
                port=[
                    ServiceV1SpecPort(
                        port=4000,
                        protocol="TCP",
                    )
                ],
                selector={
                    "app": "nhost-hasura-auth",
                },
                type="ClusterIP",
            ),
            scope=self,
        )
