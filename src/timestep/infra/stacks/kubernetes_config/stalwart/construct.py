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


class StalwartConstruct(Construct):
    def __init__(
        self,
        scope: Construct,
        id: str,
        config: Settings,
        helm_provider: HelmProvider,
    ) -> None:
        super().__init__(scope, id)

        minio_root_password = config.minio_root_password.get_secret_value()
        minio_root_user = config.minio_root_user

        postgres_database = "postgres"
        postgres_hostname = "postgresql-postgresql-ha-pgpool.default.svc.cluster.local"
        postgres_password = config.postgresql_password.get_secret_value()
        postgres_username = "postgres"

        self.stalwart_mail_server_deployment_resource = DeploymentV1(
            id_="stalwart_mail_server_deployment_resource",
            metadata=DeploymentV1Metadata(
                labels={
                    "app": "stalwart-mail-server",
                },
                name="stalwart-mail-server",
                namespace="default",
            ),
            spec=DeploymentV1Spec(
                # replicas="1",
                selector=DeploymentV1SpecSelector(
                    match_labels={
                        "app": "stalwart-mail-server",
                    }
                ),
                template=DeploymentV1SpecTemplate(
                    metadata=DeploymentV1SpecTemplateMetadata(
                        labels={
                            "app": "stalwart-mail-server",
                        },
                    ),
                    spec=DeploymentV1SpecTemplateSpec(
                        container=[
                            DeploymentV1SpecTemplateSpecContainer(
                                env=[
                                ],
                                image="stalwartlabs/mail-server:latest",
                                image_pull_policy="IfNotPresent",
                                name="stalwart-mail-server",
                                port=[
                                    # DeploymentV1SpecTemplateSpecContainerPort(
                                    #     container_port=25,
                                    #     name="smtp",
                                    # ),
                                    # DeploymentV1SpecTemplateSpecContainerPort(
                                    #     container_port=143,
                                    #     name="imap",
                                    # ),
                                    # # DeploymentV1SpecTemplateSpecContainerPort(
                                    # #     container_port=443,
                                    # #     name="https",
                                    # # ),
                                    # DeploymentV1SpecTemplateSpecContainerPort(
                                    #     container_port=465,
                                    #     name="submissions", # TLS encrypted SMTP submissions
                                    # ),
                                    # DeploymentV1SpecTemplateSpecContainerPort(
                                    #     container_port=587, # SMTP submissions
                                    #     name="submission",
                                    # ),
                                    # DeploymentV1SpecTemplateSpecContainerPort(
                                    #     container_port=993,
                                    #     name="imaps",
                                    # ),
                                    # DeploymentV1SpecTemplateSpecContainerPort(
                                    #     container_port=4190,
                                    #     name="sieve",
                                    # ),
                                ],
                            )
                        ],
                    ),
                ),
            ),
            scope=self,
        )

        # self.stalwart_mail_server_service_resource = ServiceV1(
        #     depends_on=[self.stalwart_mail_server_deployment_resource],
        #     id_="stalwart_mail_server_service_resource",
        #     metadata=ServiceV1Metadata(
        #         labels={
        #             "app": "stalwart-mail-server",
        #         },
        #         name="stalwart-mail-server",
        #         namespace="default",
        #     ),
        #     spec=ServiceV1Spec(
        #         port=[
        #             # ServiceV1SpecPort(
        #             #     port=443,
        #             #     protocol="TCP",
        #             # )
        #         ],
        #         selector={
        #             "app": "stalwart-mail-server"
        #         },
        #         type="ClusterIP",
        #     ),
        #     scope=self,
        # )
