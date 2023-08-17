from cdktf import (
    TerraformStack,
)
from cdktf_cdktf_provider_helm.provider import HelmProvider, HelmProviderKubernetes
from cdktf_cdktf_provider_kubernetes.provider import KubernetesProvider
from constructs import Construct

from timestep.infra.stacks.kubernetes_config.constructs.kubernetes_cluster_ingress.construct import (  # noqa: E501
    KubernetesClusterIngressConstruct,
)
from timestep.infra.stacks.kubernetes_config.constructs.timestep_ai.construct import (
    TimestepAIConstruct,
)


class KubernetesConfigStack(TerraformStack):
    id: str = None

    def __init__(self, scope: Construct, id: str, config: dict[str, str], kube_config):
        super().__init__(scope, id)
        self.id = id

        self.kubernetes_provider = KubernetesProvider(
            id="kubernetes_provider",
            config_context=config.kubecontext,
            config_path=kube_config,
            scope=self,
        )

        self.helm_provider = HelmProvider(
            id="helm_provider",
            kubernetes=HelmProviderKubernetes(
                config_context=self.kubernetes_provider.config_context,
                config_path=kube_config,
            ),
            scope=self,
        )

        self.kubernetes_cluster_ingress_construct: KubernetesClusterIngressConstruct = (
            KubernetesClusterIngressConstruct(
                config=config,
                id="kubernetes_cluster_ingress_construct",
                helm_provider=self.helm_provider,
                scope=self,
            )
        )

        self.timestep_ai_contruct: TimestepAIConstruct = TimestepAIConstruct(
            config=config,
            id="timestep_ai_contruct",
            helm_provider=self.helm_provider,
            scope=self,
        )
