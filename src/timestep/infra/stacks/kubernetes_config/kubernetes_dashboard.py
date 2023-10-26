from cdktf_cdktf_provider_helm.provider import HelmProvider
from cdktf_cdktf_provider_helm.release import Release, ReleaseSet
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
from constructs import Construct

from timestep.config import Settings


class KubernetesDashboardConstruct(Construct):
    def __init__(
        self,
        scope: Construct,
        id: str,
        config: Settings,
        helm_provider: HelmProvider,
    ) -> None:
        super().__init__(scope, id)

        self.kubernetes_dashboard_helm_release_resource = Release(
            id_="kubernetes_dashboard_helm_release_resource",
            atomic=True,
            chart="kubernetes-dashboard",
            create_namespace=True,
            name="kubernetes-dashboard",
            namespace="kubernetes-dashboard",
            repository="https://kubernetes.github.io/dashboard",
            provider=helm_provider,
            set=[
                ReleaseSet(
                    name="app.ingress.enabled",
                    value="false",
                ),
                ReleaseSet(
                    name="cert-manager.enabled",
                    value="false",
                ),
                ReleaseSet(
                    name="nginx.enabled",
                    value="false",
                ),
            ],
            scope=self,
        )

        IngressV1(
            depends_on=[
                self.kubernetes_dashboard_helm_release_resource,
            ],
            id_="kubernetes_dashboard_ingress",
            metadata=IngressV1Metadata(
                annotations={
                    "kubernetes.io/ingress.class": "caddy",
                },
                name="kubernetes-dashboard",
                namespace="kubernetes-dashboard",
            ),
            scope=self,
            spec=IngressV1Spec(
                rule=[
                    IngressV1SpecRule(
                        host=f"kubernetes-dashboard.{config.primary_domain_name}",
                        http=IngressV1SpecRuleHttp(
                            path=[
                                IngressV1SpecRuleHttpPath(
                                    backend=IngressV1SpecRuleHttpPathBackend(
                                        service=IngressV1SpecRuleHttpPathBackendService(
                                            name="kubernetes-dashboard",
                                            port=IngressV1SpecRuleHttpPathBackendServicePort(
                                                number=443,  # https://artifacthub.io/packages/helm/k8s-dashboard/kubernetes-dashboard#networkpolicy
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
