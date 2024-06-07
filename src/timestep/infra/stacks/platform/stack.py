from cdktf import (
    HttpBackend,
    LocalBackend,
    TerraformStack,
)
from cdktf_cdktf_provider_helm.provider import HelmProvider, HelmProviderKubernetes
from cdktf_cdktf_provider_kubernetes.provider import KubernetesProvider
from constructs import Construct

from timestep.config import CloudInstanceProvider, Settings
from timestep.infra.stacks.platform.litellm_proxy.construct import LiteLLMProxyConstruct
from timestep.infra.stacks.platform.timestep_ai.construct import TimestepAIConstruct


class PlatformStack(TerraformStack):
    id: str

    def __init__(self, scope: Construct, id: str, config: Settings, kube_config=None):
        super().__init__(scope, id)
        self.id = id

        self.kubernetes_provider = KubernetesProvider(
            id="kubernetes_provider",
            config_context=config.kubecontext,
            config_path=f"{config.base_path}/secrets/kubeconfig",
            scope=self,
        )

        self.helm_provider = HelmProvider(
            id="helm_provider",
            kubernetes=HelmProviderKubernetes(
                config_context=self.kubernetes_provider.config_context,
                config_path=self.kubernetes_provider.config_path,
            ),
            scope=self,
        )

        if config.litellm_proxy_is_enabled:
            self.litellm_proxy_construct: LiteLLMProxyConstruct = LiteLLMProxyConstruct(
                config=config,
                id="litellm_proxy_construct",
                helm_provider=self.helm_provider,
                scope=self,
            )

        if config.timestep_ai_is_enabled:
            self.timestep_ai_construct: TimestepAIConstruct = TimestepAIConstruct(
                config=config,
                id="timestep_ai_construct",
                helm_provider=self.helm_provider,
                scope=self,
            )

        if config.cloud_instance_provider == CloudInstanceProvider.MULTIPASS:
            LocalBackend(
                path=f"{config.dist_path}/terraform.{self.id}.tfstate",
                scope=self,
                workspace_dir=None,
            )

        else:
            HttpBackend(
                address=f"{config.tf_http_address}/{self.id}",
                lock_address=f"{config.tf_http_address}/{self.id}/lock",
                lock_method="POST",
                password=config.tf_api_token.get_secret_value(),
                retry_wait_min=5,
                scope=self,
                unlock_address=f"{config.tf_http_address}/{self.id}/lock",
                unlock_method="DELETE",
                username=config.tf_username,
            )
