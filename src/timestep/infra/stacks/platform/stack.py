from constructs import Construct
from cdktf import TerraformStack

from omegaconf import DictConfig

from timestep.infra.imports.helm.provider import HelmProvider as HelmTerraformProvider, HelmProviderKubernetes
from timestep.infra.imports.helm.release import Release as HelmReleaseTerraformResource
from timestep.infra.imports.kubernetes.provider import KubernetesProvider as KubernetesTerraformProvider
from timestep.infra.stacks.kubernetes.stack import KubernetesTerraformStack


class PlatformTerraformStackConfig:
    def __init__(self, config: DictConfig, k8s_stack: KubernetesTerraformStack) -> None:
        pass

class PlatformTerraformStack(TerraformStack):
    def __init__(self, scope: Construct, id: str, config: PlatformTerraformStackConfig, **kwargs) -> None:
        super().__init__(scope, id)

        platform_kubernetes_provider = KubernetesTerraformProvider(
            id="platform_kubernetes_provider",
            config_context="timestep-ai-k3s-cluster",
            config_path = "~/.kube/config",
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
            chart="/home/mjschock/Projects/timestep-ai/timestep/dist/deploy/k8s/charts/timestep-ai-platform",
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
