import os
import pathlib
from typing import Any, Dict, List, Type

from cdktf import (
    LocalExecProvisioner,
    TerraformDataSource,
    TerraformElement,
    TerraformOutput,
    TerraformProvider,
    TerraformResource,
    TerraformStack,
    Token,
)
from cloud_init_gen import CloudInitDoc
from constructs import Construct
from prefect import flow, get_run_logger, task
from prefect.filesystems import LocalFileSystem
from prefect.futures import PrefectFuture
from prefect.task_runners import SequentialTaskRunner
from prefect_shell import ShellOperation
from pydantic import BaseModel

from timestep.conf.blocks import AppConfig
from timestep.infra.imports.cloudinit.data_cloudinit_config import (
    DataCloudinitConfig as CloudInitConfigTerraformDataSource,
)
from timestep.infra.imports.digitalocean.data_digitalocean_domain import (
    DataDigitaloceanDomain as DigitaloceanDomainTerraformDataSource,
)
from timestep.infra.imports.digitalocean.data_digitalocean_droplet import (
    DataDigitaloceanDroplet as DigitaloceanDropletTerraformDataSource,
)
from timestep.infra.imports.digitalocean.domain import (
    Domain as DigitaloceanDomainTerraformResource,
)
from timestep.infra.imports.digitalocean.droplet import (
    Droplet as DigitaloceanDropletTerraformResource,
)
from timestep.infra.imports.digitalocean.provider import (
    DigitaloceanProvider as DigitaloceanTerraformProvider,
)
from timestep.infra.imports.external.data_external import (
    DataExternal as ExternalTerraformDataSource,
)
from timestep.infra.imports.helm.provider import HelmProvider as HelmTerraformProvider
from timestep.infra.imports.helm.provider import HelmProviderKubernetes
from timestep.infra.imports.helm.release import Release as HelmReleaseTerraformResource
from timestep.infra.imports.helm.release import ReleaseSet, ReleaseSetListStruct
from timestep.infra.imports.kubernetes.deployment import Deployment
from timestep.infra.imports.kubernetes.ingress import (
    Ingress,
    IngressMetadata,
    IngressSpec,
    IngressSpecBackend,
    IngressSpecRule,
    IngressSpecRuleHttp,
    IngressSpecRuleHttpPath,
    IngressSpecRuleHttpPathBackend,
    IngressSpecTls,
)
from timestep.infra.imports.kubernetes.ingress_class_v1 import (
    IngressClassV1,
    IngressClassV1Metadata,
    IngressClassV1Spec,
    IngressClassV1SpecParameters,
)
from timestep.infra.imports.kubernetes.ingress_v1 import (
    IngressV1,
    IngressV1Metadata,
    IngressV1Spec,
    IngressV1SpecDefaultBackend,
    IngressV1SpecDefaultBackendResource,
    IngressV1SpecDefaultBackendService,
    IngressV1SpecDefaultBackendServicePort,
    IngressV1SpecRule,
    IngressV1SpecRuleHttp,
    IngressV1SpecRuleHttpPath,
    IngressV1SpecRuleHttpPathBackend,
    IngressV1SpecRuleHttpPathBackendResource,
    IngressV1SpecRuleHttpPathBackendService,
    IngressV1SpecRuleHttpPathBackendServicePort,
    IngressV1SpecTls,
)
from timestep.infra.imports.kubernetes.namespace import (
    Namespace as KubernetesNamespaceTerraformResource,
)
from timestep.infra.imports.kubernetes.namespace import NamespaceMetadata
from timestep.infra.imports.kubernetes.provider import (
    KubernetesProvider as KubernetesTerraformProvider,
)
from timestep.infra.imports.kubernetes.service import Service
from timestep.infra.imports.local.data_local_file import (
    DataLocalFile as LocalFileTerraformDataSource,
)
from timestep.infra.imports.local.file import File as LocalFileTerraformResource
from timestep.infra.imports.local.provider import (
    LocalProvider as LocalTerraformProvider,
)
from timestep.infra.imports.multipass.data_multipass_instance import (
    DataMultipassInstance as MultipassInstanceTerraformDataSource,
)
from timestep.infra.imports.multipass.instance import (
    Instance as MultipassInstanceTerraformResource,
)
from timestep.infra.imports.multipass.provider import (
    MultipassProvider as MultipassTerraformProvider,
)
from timestep.infra.imports.namecheap.domain_records import (
    DomainRecords as NamecheapDomainRecordsTerraformResource,
)
from timestep.infra.imports.namecheap.provider import (
    NamecheapProvider as NamecheapTerraformProvider,
)
from timestep.infra.imports.null.data_null_data_source import (
    DataNullDataSource as NullTerraformDataSource,
)
from timestep.infra.imports.null.provider import NullProvider as NullTerraformProvider
from timestep.infra.imports.null.resource import Resource as NullTerraformResource


class KubernetesClusterConstruct(Construct):
    def __init__(self, scope: Construct, id: str, config: AppConfig) -> None:
        # def __init__(self, id: str, scope: Construct) -> None:
        super().__init__(id=id, scope=scope)
        logger = get_run_logger()

        kubernetes_provider = KubernetesTerraformProvider(
            config_context=scope.kube_config_construct.outputs.get(
                "config_context"
            ).value,
            config_path=scope.kube_config_construct.outputs.get("config_path").value,
            id="kubernetes_provider",
            scope=scope,
        )

        helm_provider = HelmTerraformProvider(
            id="helm_provider",
            kubernetes=HelmProviderKubernetes(
                # config_context=config.KUBE_CONTEXT,
                # config_path=config.KUBE_CONFIG_PATH,
                config_context=kubernetes_provider.config_context,
                config_path=kubernetes_provider.config_path,
            ),
            scope=scope,
        )

        caddy_ingress_controller_helm_release_resource = HelmReleaseTerraformResource(
            id_="caddy_ingress_controller_helm_release_resource",
            atomic=True,
            chart="caddy-ingress-controller",
            # chart=config.CADDY_INGRESS_CONTROLLER_CHART_PATH,
            # chart="ingress/charts/caddy-ingress-controller",
            # chart="/home/mjschock/Projects/timestep-ai/timestep/src/timestep/infra/stacks/base/constructs/kubernetes_cluster/ingress/charts/caddy-ingress-controller",
            create_namespace=True,
            name="caddy-ingress-controller",
            namespace="caddy-system",
            repository="https://caddyserver.github.io/ingress",
            provider=helm_provider,
            set=[
                # | Key | Type | Default | Description |
                # |-----|------|---------|-------------|
                # | affinity | object | `{}` |  |
                # | fullnameOverride | string | `""` |  |
                # | image.pullPolicy | string | `"IfNotPresent"` |  |
                # | image.repository | string | `"caddy/ingress"` |  |
                # | image.tag | string | `"latest"` |  |
                # | imagePullSecrets | list | `[]` |  |
                # | ingressController.config.acmeCA | string | `""` |  |
                # | ingressController.config.acmeEABKeyId | string | `""` |  |
                # | ingressController.config.acmeEABMacKey | string | `""` |  |
                # | ingressController.config.debug | bool | `false` |  |
                # | ingressController.config.email | string | `""` |  |
                # | ingressController.config.metrics | bool | `true` |  |
                # | ingressController.config.onDemandTLS | bool | `false` |  |
                # | ingressController.config.proxyProtocol | bool | `false` |  |
                # | ingressController.rbac.create | bool | `true` |  |
                # | ingressController.verbose | bool | `false` |  |
                # | ingressController.leaseId | string | `""` |  |
                # | ingressController.watchNamespace | string | `""` |  |
                # | minikube | bool | `false` |  |
                # | nameOverride | string | `""` |  |
                # | nodeSelector | object | `{}` |  |
                # | podAnnotations | object | `{}` |  |
                # | podDisruptionBudget.maxUnavailable | string | `nil` |  |
                # | podDisruptionBudget.minAvailable | int | `1` |  |
                # | podSecurityContext | object | `{}` |  |
                # | replicaCount | int | `2` |  |
                # | resources | object | `{}` |  |
                # | securityContext.allowPrivilegeEscalation | bool | `true` |  |
                # | securityContext.capabilities.add[0] | string | `"NET_BIND_SERVICE"` |  |
                # | securityContext.capabilities.drop[0] | string | `"ALL"` |  |
                # | securityContext.runAsGroup | int | `0` |  |
                # | securityContext.runAsUser | int | `0` |  |
                # | serviceAccount.annotations | object | `{}` |  |
                # | serviceAccount.create | bool | `true` |  |
                # | serviceAccount.name | string | `"caddy-ingress-controller"` |  |
                # | tolerations | list | `[]` |  |
                ReleaseSet(
                    name="ingressController.config.acmeCA",
                    value="https://acme-staging-v02.api.letsencrypt.org/directory",
                ),
                ReleaseSet(
                    name="ingressController.config.email",
                    value="m@mjschock.com",
                ),
                ReleaseSet(
                    name="ingressController.config.onDemandTLS",
                    value="true",
                ),
                ReleaseSet(
                    name="ingressController.verbose",
                    value="false",
                ),
            ],
            scope=scope,
        )

        # default_namespace = KubernetesNamespaceTerraformResource(
        #     scope=scope,
        #     id_="default_namespace",
        #     metadata={
        #         'name': 'default'
        #     }
        # )

        # helm install cert-manager jetstack/cert-manager --namespace cert-manager --version v1.10.1 --set installCRDs=true
        # cert_manager_helm_release_resource = HelmReleaseTerraformResource(
        #     id_="cert_manager_helm_release_resource",
        #     atomic=True,
        #     chart="cert-manager",
        #     name="cert-manager",
        #     namespace=caddy_ingress_controller_helm_release_resource.namespace, # cert-manager?
        #     repository="https://charts.jetstack.io",
        #     provider=helm_provider,
        #     set=[
        #         {
        #             "name": "installCRDs",
        #             "value": "true",
        #         },
        #     ],
        #     scope=scope,
        # )

        # cert_manager_cluster_issuer_resource = ClusterIssuer

        docker_registry_helm_release_resource = HelmReleaseTerraformResource(
            id_="docker_registry_helm_release_resource",
            atomic=True,
            chart="docker-registry",
            name="docker-registry",
            namespace=caddy_ingress_controller_helm_release_resource.namespace,
            repository="https://helm.twun.io",
            provider=helm_provider,
            set=[  # https://github.com/twuni/docker-registry.helm#configuration
                ReleaseSet(
                    name="ingress.annotations.kubernetes\\.io/ingress\\.class",
                    value="caddy",
                ),
                ReleaseSet(
                    name="ingress.className",
                    value="caddy",
                ),
                ReleaseSet(
                    name="ingress.enabled",
                    value="false",
                ),
                # {
                #     "name": "ingress.labels",
                #     "value": {},
                # },
                ReleaseSet(
                    name="ingress.path",
                    value="/",
                )
                # {
                #     "name": "ingress.tls",
                #     "value": []
                # }
                # {
                #     "name": "persistence.enabled",
                #     "value": "false",
                # },
                # {
                #     "name": "secrets.htpasswd",
                #     "value": "admin:$2y$05$Z3Z1Z3Z1Z3Z1Z3Z",
                #     # "value": "",
                # },
            ],
            set_list=[
                ReleaseSetListStruct(
                    name="ingress.hosts",
                    value=[f"registry.{config.variables.get('primary_domain_name')}"],
                ),
                # {
                #     "name": "ingress.tls",
                #     "value": [
                #         {
                #             "hosts": [
                #                 "registry.timestep.local"
                #             ],
                #             "secretName": "ssl-registry.timestep.local"
                #         }
                #     ],
                # },
            ],
            scope=scope,
        )

        # ingress_class = IngressClassV1(
        #     id_="ingress_class",
        #     metadata=IngressClassV1Metadata(
        #         # annotations={
        #         #     "ingressclass.kubernetes.io/is-default-class": "true",
        #         # },
        #         # labels={
        #         #     "app.kubernetes.io/managed-by": "Helm",
        #         # },
        #         # name="caddy",

        #     ),
        #     scope=scope,
        #     spec=IngressClassV1Spec(
        #         # controller="caddy.ingress.kubernetes.io",
        #         # controller=None,
        #         # parameters=[
        #         #     # IngressClassV1SpecParameters(
        #         #     #     api_group=None,
        #         #     #     kind=None,
        #         #     #     name=None,
        #         #     # )
        #         # ]
        #     )
        # )

        docker_registry_ingress_resource = IngressV1(
            scope=scope,
            id_="docker_registry_ingress_resource",
            metadata=IngressV1Metadata(
                annotations={
                    "kubernetes.io/ingress.class": "caddy",
                    # "cert-manager.io/cluster-issuer": "letsencrypt-staging",
                },
                name=docker_registry_helm_release_resource.name,
                namespace=docker_registry_helm_release_resource.namespace,
            ),
            spec=IngressV1Spec(
                # default_backend=IngressV1SpecDefaultBackend(
                #     resource=IngressV1SpecDefaultBackendResource(
                #         api_group=ingress_class.api_group,
                #         kind=ingress_class.kind,
                #         name=ingress_class.name,
                #     ),
                #     service=IngressV1SpecDefaultBackendService(
                #         port=IngressV1SpecDefaultBackendServicePort(
                #             name="http",
                #             number=5000,
                #         )
                #     )
                # ),
                ingress_class_name="caddy",
                rule=[
                    IngressV1SpecRule(
                        host=f"registry.{config.variables.get('primary_domain_name')}",
                        http=IngressV1SpecRuleHttp(
                            path=[
                                IngressV1SpecRuleHttpPath(
                                    backend=IngressV1SpecRuleHttpPathBackend(
                                        # resource=IngressV1SpecRuleHttpPathBackendResource(
                                        #     api_group=docker_registry_helm_release_resource.api_group,
                                        #     kind=docker_registry_helm_release_resource.kind,
                                        #     name=docker_registry_helm_release_resource.name,
                                        # ),
                                        service=IngressV1SpecRuleHttpPathBackendService(
                                            name="docker-registry",
                                            port=IngressV1SpecRuleHttpPathBackendServicePort(
                                                # name="http",
                                                number=5000,
                                            ),
                                        )
                                    ),
                                    path="/",
                                    path_type="Prefix",
                                )
                            ]
                        ),
                    )
                ],
                # tls=[
                #     IngressV1SpecTls(
                #         hosts=[
                #             "registry.timestep.local"
                #         ],
                #         secret_name="ssl-registry.timestep.local"
                #     )
                # ],
            ),
        )

        app_name = "caddy-server"

        caddy_server_deployment_resource = Deployment(
            scope=self,
            id_="caddy_server_deployment_resource",
            metadata={
                "name": app_name,
                "namespace": caddy_ingress_controller_helm_release_resource.namespace,
                "labels": {"app": app_name},
            },
            spec={
                #    'replicas': 2,
                "selector": {"match_labels": {"app": app_name}},
                "template": {
                    "metadata": {"labels": {"app": app_name}},
                    "spec": {
                        "container": [
                            {
                                "image": "caddy",
                                "name": app_name,
                                "ports": [
                                    {"containerPort": 80},
                                    {"containerPort": 443},
                                ],
                            }
                        ]
                    },
                },
            },
        )

        caddy_server_service_resource = Service(
            scope=self,
            id_="caddy_server_service_resource",
            metadata={
                "name": app_name,
                "namespace": caddy_ingress_controller_helm_release_resource.namespace,
            },
            spec={
                "selector": {"app": app_name},
                "port": [
                    {"name": "http", "port": 80, "target_port": 80},
                    {"name": "https", "port": 443, "target_port": 443},
                ],
            },
        )

        # caddy_server_ingress_resource = Ingress(
        #     scope=self,
        #     id_='caddy_server_ingress_resource',
        #     metadata={
        #         'name': app_name,
        #         'namespace': caddy_ingress_controller_helm_release_resource.namespace,
        #         'annotations': {
        #             'kubernetes.io/ingress.class': 'caddy',
        #         }
        #     },
        #     spec={
        #         'rule': [{
        #             'host': config.variables.get('primary_domain_name'),
        #             'http': {
        #                 'path': [{
        #                     'path': '/',
        #                     'backend': {
        #                         'serviceName': app_name,
        #                         'servicePort': 80
        #                     }
        #                 }]
        #             }
        #         }]
        #     }
        # )

        caddy_server_ingress_resource = IngressV1(
            scope=scope,
            id_="docker_registry_ingcaddy_server_ingress_resourceress_resource",
            metadata=IngressV1Metadata(
                annotations={
                    "kubernetes.io/ingress.class": "caddy",
                    # "cert-manager.io/cluster-issuer": "letsencrypt-staging",
                },
                # name=docker_registry_helm_release_resource.name,
                # namespace=docker_registry_helm_release_resource.namespace,
                name=app_name,
                namespace=caddy_ingress_controller_helm_release_resource.namespace,
            ),
            spec=IngressV1Spec(
                default_backend=IngressV1SpecDefaultBackend(
                    # resource=IngressV1SpecDefaultBackendResource(
                    #     api_group=ingress_class.api_group,
                    #     kind=ingress_class.kind,
                    #     name=ingress_class.name,
                    # ),
                    service=IngressV1SpecDefaultBackendService(
                        name=app_name,
                        port=IngressV1SpecDefaultBackendServicePort(
                            # name="http",
                            number=443,
                        ),
                    )
                ),
                ingress_class_name="caddy",
                rule=[
                    IngressV1SpecRule(
                        host=f"{config.variables.get('primary_domain_name')}",
                        http=IngressV1SpecRuleHttp(
                            path=[
                                IngressV1SpecRuleHttpPath(
                                    backend=IngressV1SpecRuleHttpPathBackend(
                                        # resource=IngressV1SpecRuleHttpPathBackendResource(
                                        #     api_group=docker_registry_helm_release_resource.api_group,
                                        #     kind=docker_registry_helm_release_resource.kind,
                                        #     name=docker_registry_helm_release_resource.name,
                                        # ),
                                        service=IngressV1SpecRuleHttpPathBackendService(
                                            name=app_name,
                                            port=IngressV1SpecRuleHttpPathBackendServicePort(
                                                # name="http",
                                                number=80,
                                            ),
                                        )
                                    ),
                                    path="/",
                                    path_type="Prefix",
                                )
                            ]
                        ),
                    )
                ],
                # tls=[
                #     IngressV1SpecTls(
                #         hosts=[
                #             "registry.timestep.local"
                #         ],
                #         secret_name="ssl-registry.timestep.local"
                #     )
                # ],
            ),
        )

        # platform_helm_release_resource = HelmReleaseTerraformResource(
        #     id_="platform_helm_release_resource",
        #     atomic=True,
        #     chart=config.PLATFORM_CHART_PATH,
        #     # name="timestep-ai-platform",
        #     name="platform",
        #     namespace="default",
        #     provider=helm_provider,
        #     scope=self,
        # )
