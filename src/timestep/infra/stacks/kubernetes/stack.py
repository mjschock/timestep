import os

from constructs import Construct
from cdktf import TerraformStack
from pydantic import BaseModel

from timestep.infra.imports.helm.provider import HelmProvider as HelmTerraformProvider, HelmProviderKubernetes
from timestep.infra.imports.helm.release import Release as HelmReleaseTerraformResource
from timestep.infra.imports.kubernetes.provider import KubernetesProvider as KubernetesTerraformProvider
from timestep.infra.imports.kubernetes.namespace import Namespace as KubernetesNamespaceTerraformResource, NamespaceMetadata
from timestep.infra.stacks.base.stack import BaseTerraformStack, BaseTerraformStackConfig


class KubernetesTerraformStackConfig(BaseTerraformStackConfig):
    pass


class KubernetesTerraformStack(TerraformStack):
    def __init__(self, scope: Construct, id: str, config: KubernetesTerraformStackConfig, **kwargs) -> None:
        super().__init__(scope, id)

        cwd = os.getcwd()
        KUBECONFIG = os.getenv('KUBECONFIG')

        self.kubernetes_provider = KubernetesTerraformProvider(
            id="kubernetes_provider",
            config_context="timestep-ai-k3s-cluster",
            config_path=f"{cwd}/{KUBECONFIG}",
            scope=self,
        )

        self.metadata = NamespaceMetadata(
            name="caddy-system",
        )

        self.kubernetes_namespace = KubernetesNamespaceTerraformResource(
            id_="kubernetes_namespace",
            metadata=self.metadata,
            provider=self.kubernetes_provider,
            scope=self,
        )

        self.kubernetes = HelmProviderKubernetes(
            config_context=self.kubernetes_provider.config_context,
            config_path=self.kubernetes_provider.config_path,
        )

        self.helm_provider = HelmTerraformProvider(
            id="helm_provider",
            kubernetes=self.kubernetes,
            scope=self,
        )

        self.helm_release_resource = HelmReleaseTerraformResource(
            id_="helm_release_resource",
            atomic=True,
            chart="caddy-ingress-controller",
            name="timestep-ai",
            namespace=self.metadata.name,
            repository="https://caddyserver.github.io/ingress",
            provider=self.helm_provider,
            scope=self,
        )
