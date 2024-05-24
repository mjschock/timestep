import json
import os

from cdktf_cdktf_provider_helm.provider import HelmProvider
from cdktf_cdktf_provider_helm.release import (
    Release,
    ReleaseSet,
    ReleaseSetListStruct,
    ReleaseSetSensitive,
)
from cdktf_cdktf_provider_kubernetes.cluster_role_binding_v1 import (
    ClusterRoleBindingV1,
    ClusterRoleBindingV1Metadata,
    ClusterRoleBindingV1RoleRef,
    ClusterRoleBindingV1Subject,
)
from cdktf_cdktf_provider_kubernetes.cluster_role_v1 import (
    ClusterRoleV1,
    ClusterRoleV1Metadata,
    ClusterRoleV1Rule,
)
from cdktf_cdktf_provider_kubernetes.role_binding_v1 import (
    RoleBindingV1,
    RoleBindingV1Metadata,
    RoleBindingV1RoleRef,
    RoleBindingV1Subject,
)
from cdktf_cdktf_provider_kubernetes.role_v1 import (
    RoleV1,
    RoleV1Metadata,
    RoleV1Rule,
)
from cdktf_cdktf_provider_kubernetes.secret_v1 import SecretV1, SecretV1Metadata
from cdktf_cdktf_provider_kubernetes.service_account_v1 import (
    ServiceAccountV1,
    ServiceAccountV1ImagePullSecret,
    ServiceAccountV1Metadata,
)
from constructs import Construct

from timestep.config import Settings


class PrefectConstruct(Construct):
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
        postgres_connection_string = f"postgresql+asyncpg://{postgres_username}:{postgres_password}@{postgres_hostname}/{postgres_database}"

        self.prefect_server_postgresql_connection_secret_resource = SecretV1(
            id_="prefect_server_postgresql_connection_secret_resource",
            data={
                "connection-string": postgres_connection_string,
                "password": postgres_password,
            },
            metadata=SecretV1Metadata(
                name="prefect-server-postgresql-connection",
                namespace="default",
            ),
            scope=self,
        )

        self.prefect_server_helm_release_resource = Release(
            id_="prefect_server_helm_release_resource",
            atomic=True,
            chart="prefect-server",
            create_namespace=True,
            name="prefect-server",
            namespace="default",
            repository="https://prefecthq.github.io/prefect-helm",
            provider=helm_provider,
            set=[
                ReleaseSet(
                    name="postgresql.auth.database",
                    value=postgres_database,
                ),
                ReleaseSet(
                    name="postgresql.auth.username",
                    value=postgres_username,
                ),
                ReleaseSet(
                    name="postgresql.enabled",
                    value="true",
                ),
                ReleaseSet(
                    name="postgresql.useSubChart",
                    value="false",
                ),
                ReleaseSet(
                    name="server.image.prefectTag",
                    value=f"{config.prefect_server_version}-python3.11-kubernetes",
                ),
                ReleaseSet(
                    name="server.image.repository",
                    value="prefecthq/prefect",
                ),
            ],
            set_sensitive=[
                ReleaseSetSensitive(
                    name="postgresql.auth.existingSecret",
                    value=self.prefect_server_postgresql_connection_secret_resource.metadata.name,
                )
            ],
            scope=self,
            version="2024.1.12",
        )

        # sidecar_container = DeploymentV1SpecTemplateSpecContainer(
        #     command=["sh", "-c", "while true; do sleep 30; done;"],
        #     image="alpine:latest",
        #     name="sidecar",
        # )

        # base_job_template_values_asset = TerraformAsset(
        #     id="base_job_template_values_asset",
        #     path=os.path.join(os.path.dirname(__file__), "base-job-template.json"),
        #     scope=self,
        #     type=AssetType.FILE,
        # )

        with open(
            os.path.join(os.path.dirname(__file__), "base-job-template.json"), "r"
        ) as f:  # noqa: E501
            # base_job_template = f.read()
            base_job_template_json = json.load(f)

        self.prefect_default_worker_helm_release_resource = Release(
            depends_on=[self.prefect_server_helm_release_resource],
            id_="prefect_default_worker_helm_release_resource",
            atomic=True,
            chart="prefect-worker",
            name="prefect-worker",
            namespace=self.prefect_server_helm_release_resource.namespace,
            repository="https://prefecthq.github.io/prefect-helm",
            provider=helm_provider,
            set=[
                ReleaseSet(
                    name="worker.apiConfig",
                    value="server",
                ),
                ReleaseSet(
                    name="worker.config.limit",
                    value="1",
                ),
                ReleaseSet(
                    name="worker.config.workPool",
                    value="default-worker-pool",
                ),
                ReleaseSet(
                    name="worker.image.debug",
                    value="true",
                ),
                ReleaseSet(
                    name="worker.image.prefectTag",
                    value=f"{config.prefect_server_version}-python3.11-kubernetes",
                ),
                ReleaseSet(
                    name="worker.serverApiConfig.apiUrl",
                    value=f"http://prefect-server.{self.prefect_server_helm_release_resource.namespace}.svc.cluster.local:4200/api",  # noqa: E501
                ),
            ],
            set_list=[
                # ReleaseSetListStruct(
                #     # -- additional sidecar containers
                #     name="worker.extraContainers",
                #     # value=["\\{\"timeout\": \"30s\"\\}"],
                #     value=[sidecar_container.metadata.name],
                # ),
                # ReleaseSetListStruct(
                #     # -- array with extra volumes for the worker pod
                #     name="worker.extraVolumes",
                #     value=[
                #         {
                #             "name": "extra-volume",
                #             "emptyDir": {},
                #         }
                #     ],
                # ),
                # ReleaseSetListStruct(
                #     # -- array with extra volumeMounts for the worker pod
                #     name="worker.extraVolumeMounts",
                #     value=[
                #         {
                #             "name": "extra-volume",
                #             "mountPath": "/extra-volume",
                #         }
                #     ],
                # ),
                ReleaseSetListStruct(
                    name="worker.image.pullSecrets",
                    value=["regcred"],
                ),
            ],
            scope=self,
            values=[
                f"""worker:
  config:
    baseJobTemplate: |
        {json.dumps(base_job_template_json)}
"""
                #                 """worker:
                #   extraVolumes:
                #     - name: cache-volume
                #       emptyDir:
                #         sizeLimit: 500Mi
                #   extraVolumeMounts:
                #     - name: cache-volume
                #       mountPath: /cache
                #             """
            ],
        )

        # Create prefect-worker-job service account, role, and role binding
        self.prefect_worker_job_service_account = ServiceAccountV1(
            depends_on=[
                self.prefect_default_worker_helm_release_resource,
            ],
            id_="prefect_worker_job_service_account",
            image_pull_secret=[
                ServiceAccountV1ImagePullSecret(
                    name="regcred",
                ),
            ],
            metadata=ServiceAccountV1Metadata(
                name="prefect-worker-job-service-account",
                namespace=self.prefect_default_worker_helm_release_resource.namespace,
            ),
            scope=self,
        )

        self.prefect_worker_job_cluster_role = ClusterRoleV1(
            depends_on=[
                self.prefect_worker_job_service_account,
            ],
            id_="prefect_worker_job_cluster_role",
            metadata=ClusterRoleV1Metadata(
                name="prefect-worker-job-cluster-role",
            ),
            rule=[
                ClusterRoleV1Rule(
                    api_groups=[""],
                    resources=["nodes"],
                    verbs=["list"],
                )
            ],
            scope=self,
        )

        self.prefect_worker_job_role = RoleV1(
            depends_on=[
                self.prefect_worker_job_service_account,
            ],
            id_="prefect_worker_job_role",
            metadata=RoleV1Metadata(
                name="prefect-worker-job-role",
                namespace=self.prefect_worker_job_service_account.metadata.namespace,
            ),
            rule=[
                RoleV1Rule(
                    api_groups=[""],
                    resources=["pods"],
                    verbs=["create", "delete", "get", "list"],
                ),
                RoleV1Rule(
                    api_groups=[""],
                    resources=["pods/exec"],
                    verbs=["create", "delete", "get", "list"],
                ),
                RoleV1Rule(
                    api_groups=[""],
                    resources=["pods/status"],
                    verbs=["create", "delete", "get", "list"],
                ),
                RoleV1Rule(
                    api_groups=["rbac.authorization.k8s.io"],
                    resources=["rolebindings"],
                    verbs=["create", "list"],
                ),
                RoleV1Rule(
                    api_groups=["rbac.authorization.k8s.io"],
                    resources=["roles"],
                    verbs=["create", "list"],
                ),
                RoleV1Rule(
                    api_groups=[""],
                    resources=["secrets"],
                    verbs=["create"],
                ),
                RoleV1Rule(
                    api_groups=[""],
                    resources=["services"],
                    verbs=["create", "delete", "get", "list", "patch"],
                ),
                RoleV1Rule(
                    api_groups=[""],
                    resources=["serviceaccounts"],
                    verbs=["create", "list"],
                ),
                RoleV1Rule(  # TODO: Figure out why this is needed, it seems like a security risk!  # noqa: E501
                    api_groups=["*"],
                    resources=["*"],
                    verbs=["*"],
                ),
            ],
            scope=self,
        )

        self.prefect_worker_job_cluster_role_binding = ClusterRoleBindingV1(
            depends_on=[
                self.prefect_worker_job_service_account,
                self.prefect_worker_job_cluster_role,
            ],
            id_="prefect_worker_job_cluster_role_binding",
            metadata=ClusterRoleBindingV1Metadata(
                name="prefect-worker-job-cluster-role-binding",
            ),
            subject=[
                ClusterRoleBindingV1Subject(
                    kind="ServiceAccount",
                    name=self.prefect_worker_job_service_account.metadata.name,
                    api_group="",
                )
            ],
            role_ref=ClusterRoleBindingV1RoleRef(
                kind="ClusterRole",
                name=f"{self.prefect_worker_job_cluster_role.metadata.name}",
                api_group="rbac.authorization.k8s.io",
            ),
            scope=self,
        )

        self.prefect_worker_job_role_binding = RoleBindingV1(
            depends_on=[
                self.prefect_worker_job_service_account,
                self.prefect_worker_job_role,
            ],
            id_="prefect_worker_job_role_binding",
            metadata=RoleBindingV1Metadata(
                name="prefect-worker-job-role-binding",
                namespace=self.prefect_worker_job_service_account.metadata.namespace,
            ),
            subject=[
                RoleBindingV1Subject(
                    kind="ServiceAccount",
                    name=self.prefect_worker_job_service_account.metadata.name,
                    api_group="",
                )
            ],
            role_ref=RoleBindingV1RoleRef(
                kind="Role",
                name=f"{self.prefect_worker_job_role.metadata.name}",
                api_group="rbac.authorization.k8s.io",
            ),
            scope=self,
        )

        self.prefect_worker_event_lister_role = RoleV1(
            depends_on=[
                self.prefect_default_worker_helm_release_resource,
            ],
            id_="prefect_worker_event_lister_role",
            metadata=RoleV1Metadata(
                name="event-lister",
                namespace=self.prefect_default_worker_helm_release_resource.namespace,
            ),
            rule=[
                RoleV1Rule(
                    api_groups=[""],
                    resources=["events"],
                    verbs=["list"],
                )
            ],
            scope=self,
        )

        RoleBindingV1(
            depends_on=[
                self.prefect_default_worker_helm_release_resource,
            ],
            id_="prefect_worker_list_events_role_binding",
            metadata=RoleBindingV1Metadata(
                name="list-events",
                namespace=self.prefect_default_worker_helm_release_resource.namespace,
            ),
            subject=[
                RoleBindingV1Subject(
                    kind="ServiceAccount",
                    name=self.prefect_default_worker_helm_release_resource.name,
                    api_group="",
                )
            ],
            role_ref=RoleBindingV1RoleRef(
                kind="Role",
                name=self.prefect_worker_event_lister_role.metadata.name,
                api_group="rbac.authorization.k8s.io",
            ),
            scope=self,
        )
