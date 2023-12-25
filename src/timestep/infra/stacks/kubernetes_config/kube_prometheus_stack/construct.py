import os

from cdktf import AssetType, Fn, TerraformAsset
from cdktf_cdktf_provider_helm.provider import HelmProvider
from cdktf_cdktf_provider_helm.release import (
    Release,
)
from constructs import Construct

from timestep.config import Settings

# https://github.com/ray-project/kuberay/blob/master/install/prometheus/install.sh


class KubePrometheusStackConstruct(Construct):
    def __init__(
        self,
        scope: Construct,
        id: str,
        config: Settings,
        helm_provider: HelmProvider,
    ) -> None:
        super().__init__(scope, id)

        values_asset = TerraformAsset(
            id="kube_prometheus_stack_helm_release_resource_values_asset",
            path=os.path.join(os.path.dirname(__file__), "overrides.yaml"),
            scope=self,
            type=AssetType.FILE,
        )

        self.kube_prometheus_stack_helm_release_resource = Release(
            id_="kube_prometheus_stack_helm_release_resource",
            atomic=True,
            chart="kube-prometheus-stack",
            create_namespace=True,
            name="prometheus",
            namespace="prometheus-system",
            repository="https://prometheus-community.github.io/helm-charts",
            provider=helm_provider,
            scope=self,
            values=[
                # "https://raw.githubusercontent.com/ray-project/kuberay/master/install/prometheus/overrides.yaml",
                # "${file('values.yaml')}"
                # values_asset.path,
                Fn.file(values_asset.path),
            ],
            version="48.2.1",
        )
