from cdktf_cdktf_provider_helm.provider import HelmProvider
from cdktf_cdktf_provider_helm.release import (
    Release,
    ReleaseSet,
    ReleaseSetListStruct,
    ReleaseSetSensitive,
)
from cdktf_cdktf_provider_kubernetes.ingress_v1 import (
    IngressV1,
    IngressV1Metadata,
    IngressV1Spec,
    IngressV1SpecRule,
    IngressV1SpecRuleHttp,
    IngressV1SpecRuleHttpPath,
    IngressV1SpecRuleHttpPathBackend,
    IngressV1SpecRuleHttpPathBackendService,
    IngressV1SpecRuleHttpPathBackendServicePort,
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

        self.prefect_server_helm_release_resource = Release(
            id_="prefect_server_helm_release_resource",
            atomic=True,
            chart="prefect-server",
            create_namespace=True,
            name="prefect-server",
            # namespace="prefect-system",
            namespace="default",
            repository="https://prefecthq.github.io/prefect-helm",
            provider=helm_provider,
            set=[
                ReleaseSet(
                    name="postgresql.enabled",
                    value="true",
                ),
                ReleaseSet(
                    name="postgresql.useSubChart",
                    value="true",
                ),
                ReleaseSet(
                    name="server.image.prefectTag",
                    value="2.13.7-python3.11",
                ),
                ReleaseSet(
                    name="server.image.repository",
                    value="prefecthq/prefect",
                ),
                ReleaseSet(
                    name="server.publicApiUrl",
                    value=f"https://prefect-server.{config.primary_domain_name}/api",
                ),
            ],
            set_sensitive=[
                ReleaseSetSensitive(
                    name="postgresql.auth.password",
                    value=config.postgresql_password.get_secret_value(),
                )
            ],
            scope=self,
        )

        IngressV1(
            depends_on=[
                self.prefect_server_helm_release_resource,
            ],
            id_="prefect_server_ingress",
            metadata=IngressV1Metadata(
                annotations={
                    "kubernetes.io/ingress.class": "caddy",
                },
                name="prefect-server",
                namespace=self.prefect_server_helm_release_resource.namespace,
            ),
            scope=self,
            spec=IngressV1Spec(
                rule=[
                    IngressV1SpecRule(
                        host=f"prefect-server.{config.primary_domain_name}",
                        http=IngressV1SpecRuleHttp(
                            path=[
                                IngressV1SpecRuleHttpPath(
                                    backend=IngressV1SpecRuleHttpPathBackend(
                                        service=IngressV1SpecRuleHttpPathBackendService(
                                            name="prefect-server",
                                            port=IngressV1SpecRuleHttpPathBackendServicePort(
                                                number=4200,
                                            ),
                                        ),
                                    ),
                                    path="/",
                                    path_type="Prefix",
                                ),
                            ]
                        ),
                    ),
                ],
            ),
        )

        self.prefect_default_agent_helm_release_resource = Release(
            depends_on=[self.prefect_server_helm_release_resource],
            id_="prefect_default_agent_helm_release_resource",
            atomic=True,
            chart="prefect-agent",
            name="prefect-agent",
            namespace=self.prefect_server_helm_release_resource.namespace,
            repository="https://prefecthq.github.io/prefect-helm",
            provider=helm_provider,
            set=[
                ReleaseSet(
                    name="agent.apiConfig",
                    value="server",
                ),
                ReleaseSet(
                    name="agent.config.workPool",
                    value="default-agent-pool",
                ),
                ReleaseSet(
                    name="agent.serverApiConfig.apiUrl",
                    value=f"http://prefect-server.{self.prefect_server_helm_release_resource.namespace}.svc.cluster.local:4200/api",  # noqa: E501
                ),
            ],
            scope=self,
        )

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
                    name="worker.config.workPool",
                    value="default-worker-pool",
                ),
                ReleaseSet(
                    name="worker.image.debug",
                    value="true",
                ),
                # ReleaseSet(
                #     name="worker.image.prefectTag",
                #     value="latest",
                # ),
                # ReleaseSet(
                #     name="worker.image.repository",
                #     value="registry.gitlab.com/timestep-ai/timestep/api",
                # ),
                ReleaseSet(
                    name="worker.serverApiConfig.apiUrl",
                    value=f"http://prefect-server.{self.prefect_server_helm_release_resource.namespace}.svc.cluster.local:4200/api",  # noqa: E501
                ),
            ],
            set_list=[
                ReleaseSetListStruct(
                    name="worker.image.pullSecrets",
                    value=["regcred"],
                ),
            ],
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
