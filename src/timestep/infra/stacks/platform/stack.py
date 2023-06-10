import os
from constructs import Construct
from cdktf import TerraformStack

from omegaconf import DictConfig

from timestep.infra.imports.helm.provider import HelmProvider as HelmTerraformProvider, HelmProviderKubernetes
from timestep.infra.imports.helm.release import Release as HelmReleaseTerraformResource
from timestep.infra.imports.kubernetes.provider import KubernetesProvider as KubernetesTerraformProvider
from timestep.infra.stacks.kubernetes.stack import KubernetesTerraformStack
from timestep.infra.stacks.base.stack import BaseTerraformStack, BaseTerraformStackConfig


class PlatformTerraformStackConfig(BaseTerraformStackConfig):
    pass


class PlatformTerraformStack(TerraformStack):
    def __init__(self, scope: Construct, id: str, config: PlatformTerraformStackConfig, **kwargs) -> None:
        super().__init__(scope, id)

        cwd = os.getcwd()
        KUBECONFIG = os.getenv('KUBECONFIG')
        config_path = f"{cwd}/{KUBECONFIG}"
        chart_path = f"{cwd}/dist/deploy/k8s/charts/timestep-ai-platform"

        platform_kubernetes_provider = KubernetesTerraformProvider(
            id="platform_kubernetes_provider",
            config_context="timestep-ai-k3s-cluster",
            config_path=config_path,
            scope=self,
        )

        # self.metadata = NamespaceMetadata(
        #     name="caddy-system",
        # )

        # self.kubernetes_namespace = KubernetesNamespaceTerraformResource(
        #     id_="kubernetes_namespace",
        #     metadata=self.metadata,
        #     provider=self.kubernetes_provider,
        #     scope=self,
        # )

        platform_kubernetes = HelmProviderKubernetes(
            config_context=platform_kubernetes_provider.config_context,
            config_path=platform_kubernetes_provider.config_path,
        )

        platform_helm_provider = HelmTerraformProvider(
            id="platform_helm_provider",
            kubernetes=platform_kubernetes,
            scope=self,
        )

        platform_helm_release_resource = HelmReleaseTerraformResource(
            id_="platform_helm_release_resource",
            atomic=True,
            chart=chart_path,
            force_update=True,
            name="timestep-ai-platform",
            # namespace=k8s_stack.metadata.name,
            namespace="default",
            # namespace=self.metadata.name,
            # provider=k8s_stack.helm_provider,
            provider=platform_helm_provider,
            replace=True,
            scope=self,
        )
