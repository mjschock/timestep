from cdktf_cdktf_provider_helm.provider import HelmProvider
from cdktf_cdktf_provider_helm.release import Release, ReleaseSet
from constructs import Construct
from timestep.config import Settings


class TimestepAIConstruct(Construct):
    def __init__(
        self,
        scope: Construct,
        id: str,
        config: Settings,
        # kubernetes_cluster_ingress_construct: KubernetesClusterIngressConstruct,
        helm_provider: HelmProvider,
    ) -> None:
        super().__init__(scope, id)

        self.release_resource = Release(
            # depends_on=[kubernetes_cluster_ingress_construct],
            id_="timestep_ai_helm_release_resource",
            atomic=True,
            # chart="timestep-ai",
            # chart=f"{os.getcwd()}/timestep-ai",
            chart=f"{config.base_path}/timestep-ai",
            create_namespace=True,
            lint=True,
            # force_update=True,
            name="timestep-ai",
            # namespace="registry",
            namespace="default",
            # repository="https://charts.bitnami.com/bitnami",
            # provider=kubernetes_cluster_ingress_construct.helm_provider,
            provider=helm_provider,
            set=[
                ReleaseSet(
                    name="app.kubernetes.io\\/managed-by",
                    value="Helm",
                ),
                ReleaseSet(
                    name="meta.helm.sh\\/release-name",
                    value="timestep-ai",
                ),
                # ReleaseSet(
                #     name="externalURL",
                #     value=f"https://registry.{config.primary_domain_name}",
                # ),
                # ReleaseSet(
                #     name="exposureType",
                #     value="proxy",
                # ),
                # ReleaseSet(
                #     name="ingress.core.annotations.kubernetes\\.io/ingress\\.class",
                #     value="caddy",
                # ),
                # ReleaseSet(
                #     name="ingress.core.hostname",
                #     value=f"registry.{config.primary_domain_name}",
                # ),
                # ReleaseSet(
                #     name="ingress.core.ingressClassName",
                #     value="caddy",
                # ),
                # ReleaseSet(
                #     name="ingress.core.pathType",
                #     value="Prefix",
                # ),
                # ReleaseSet(
                #     name="ingress.core.selfSigned",
                #     value="true",
                # ),
                # ReleaseSet(
                #     name="ingress.core.tls",
                #     value="true",
                # ),
                # ReleaseSet(
                #     name="ingress.notary.annotations.kubernetes\\.io/ingress\\.class",
                #     value="caddy",
                # ),
                # ReleaseSet(
                #     name="ingress.notary.hostname",
                #     value=f"notary.{config.primary_domain_name}",
                # ),
                # ReleaseSet(
                #     name="ingress.notary.ingressClassName",
                #     value="caddy",
                # ),
                # ReleaseSet(
                #     name="ingress.notary.pathType",
                #     value="Prefix",
                # ),
                # ReleaseSet(
                #     name="ingress.notary.selfSigned",
                #     value="true",
                # ),
                # ReleaseSet(
                #     name="ingress.notary.tls",
                #     value="true",
                # ),
                # ReleaseSet(
                #     name="service.type",
                #     value="ClusterIP",
                # ),
            ],
            set_sensitive=[
                # ReleaseSetSensitive(
                #     name="adminPassword",
                #     value=config.registry_admin_password.get_secret_value(),
                # )
            ],
            scope=self,
        )

        # kubernetes_cluster_ingress_construct.create_ingress_resource(
        #     config=config,
        #     depends_on=[self.release_resource],
        #     helm_release_chart_version=self.release_resource.version,
        #     helm_release_name=self.release_resource.name,
        #     helm_release_namespace=self.release_resource.namespace,
        #     host=f"registry.{config.primary_domain_name}",
        #     id="registry_ingress_resource",
        #     ingress_class="caddy",
        #     # ingress_name="registry-ingress", # harbor-ingress
        #     ingress_name=f"{self.release_resource.name}-ingress",
        #     namespace="registry",
        #     paths=[
        #         {
        #             "path": "/api/",
        #             "path_type": "Prefix",
        #             "service_name": "harbor-core",
        #             "service_port_name": "http",
        #             "service_port_number": None,
        #         },
        #         {
        #             "path": "/service/",
        #             "path_type": "Prefix",
        #             "service_name": "harbor-core",
        #             "service_port_name": "http",
        #             "service_port_number": None,
        #         },
        #         {
        #             "path": "/v2",
        #             "path_type": "Prefix",
        #             "service_name": "harbor-core",
        #             "service_port_name": "http",
        #             "service_port_number": None,
        #         },
        #         {
        #             "path": "/chartrepo/",
        #             "path_type": "Prefix",
        #             "service_name": "harbor-core",
        #             "service_port_name": "http",
        #             "service_port_number": None,
        #         },
        #         {
        #             "path": "/c/",
        #             "path_type": "Prefix",
        #             "service_name": "harbor-core",
        #             "service_port_name": "http",
        #             "service_port_number": None,
        #         },
        #         {
        #             "path": "/",
        #             "path_type": "Prefix",
        #             "service_name": "harbor-portal",
        #             "service_port_name": "http",
        #             "service_port_number": None,
        #         },
        #     ],
        # )

        # kubernetes_cluster_ingress_construct.create_ingress_resource(
        #     config=config,
        #     depends_on=[self.release_resource],
        #     helm_release_chart_version=self.release_resource.version,
        #     helm_release_name=self.release_resource.name,
        #     helm_release_namespace=self.release_resource.namespace,
        #     host=f"notary.{config.primary_domain_name}",
        #     id="registry_ingress_notary_resource",
        #     ingress_class="caddy",
        #     # ingress_name="registry-ingress-notary", # harbor-ingress-notary
        #     ingress_name=f"{self.release_resource.name}-ingress-notary",
        #     namespace="registry",
        #     paths=[
        #         {
        #             "path": "/",
        #             "path_type": "Prefix",
        #             "service_name": "harbor-notary-server",
        #             "service_port_name": "notary-server",
        #             "service_port_number": None,
        #         },
        #     ],
        # )

        # self.release_resource = Release(
        #     depends_on=[kubernetes_cluster_ingress_construct],
        #     id_="registry_helm_release_resource",
        #     atomic=True,
        #     chart="docker-registry",
        #     create_namespace=True,
        #     name="docker-registry",
        #     namespace="default",
        #     repository="https://helm.twun.io",
        #     provider=kubernetes_cluster_ingress_construct.helm_provider,
        #     set=[
        #         # ReleaseSet(
        #         #     name="externalURL",
        #         #     value=f"https://registry.{config.primary_domain_name}",
        #         # ),
        #         # ReleaseSet(
        #         #     name="exposureType",
        #         #     value="proxy",
        #         # ),
        #         # ReleaseSet(
        #         #     name="ingress.core.annotations.kubernetes\\.io/ingress\\.class",
        #         #     value="caddy",
        #         # ),
        #         # ReleaseSet(
        #         #     name="ingress.core.hostname",
        #         #     value=f"registry.{config.primary_domain_name}",
        #         # ),
        #         # ReleaseSet(
        #         #     name="ingress.core.ingressClassName",
        #         #     value="caddy",
        #         # ),
        #         # ReleaseSet(
        #         #     name="ingress.core.pathType",
        #         #     value="Prefix",
        #         # ),
        #         # ReleaseSet(
        #         #     name="ingress.core.selfSigned",
        #         #     value="true",
        #         # ),
        #         # ReleaseSet(
        #         #     name="ingress.core.tls",
        #         #     value="true",
        #         # ),
        #         # ReleaseSet(
        #         #     name="ingress.notary.annotations.kubernetes\\.io/ingress\\.class",  # noqa: E501
        #         #     value="caddy",
        #         # ),
        #         # ReleaseSet(
        #         #     name="ingress.notary.hostname",
        #         #     value=f"notary.{config.primary_domain_name}",
        #         # ),
        #         # ReleaseSet(
        #         #     name="ingress.notary.ingressClassName",
        #         #     value="caddy",
        #         # ),
        #         # ReleaseSet(
        #         #     name="ingress.notary.pathType",
        #         #     value="Prefix",
        #         # ),
        #         # ReleaseSet(
        #         #     name="ingress.notary.selfSigned",
        #         #     value="true",
        #         # ),
        #         # ReleaseSet(
        #         #     name="ingress.notary.tls",
        #         #     value="true",
        #         # ),
        #         # ReleaseSet(
        #         #     name="service.type",
        #         #     value="ClusterIP",
        #         # ),
        #     ],
        #     set_sensitive=[
        #         ReleaseSetSensitive(
        #             name="secrets.htpasswd",
        #             value=config.htpasswd.get_secret_value()
        #         )
        #     ],
        #     scope=self,
        # )

        # kubernetes_cluster_ingress_construct.create_ingress_resource(
        #     config=config,
        #     depends_on=[self.release_resource],
        #     helm_release_chart_version=self.release_resource.version,
        #     helm_release_name=self.release_resource.name,
        #     helm_release_namespace=self.release_resource.namespace,
        #     host=f"registry.{config.primary_domain_name}",
        #     id="registry_ingress_resource",
        #     ingress_class="caddy",
        #     ingress_name=f"{self.release_resource.name}-ingress",
        #     # namespace="registry",
        #     namespace=self.release_resource.namespace,
        #     paths=[
        #         {
        #             "path": "/",
        #             "path_type": "Prefix",
        #             "service_name": "docker-registry",
        #             # "service_port_name": "http",
        #             "service_port_name": "http-5000",
        #             "service_port_number": None,
        #         },
        #     ],
        # )
