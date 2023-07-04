from typing import Dict

from cdktf import (
    TerraformDataSource,
    TerraformOutput,
    TerraformProvider,
    TerraformResource,
)
from constructs import Construct
from prefect import get_run_logger
from prefect.blocks.kubernetes import KubernetesClusterConfig
from prefect.futures import PrefectFuture

from timestep.conf.blocks import AppConfig
from timestep.infra.stacks.base.constructs.cloud_instance.blocks import (
    CloudInstanceConstruct,
)
from timestep.infra.stacks.base.constructs.kube_config.tasks import (
    get_kube_config_data_source,
    get_kube_config_outputs,
    get_kube_config_provider,
    get_kube_config_resource,
)


class KubeConfigConstruct(Construct):
    def __init__(
        self,
        scope: Construct,
        id: str,
        config: AppConfig,
        cloud_instance_construct: CloudInstanceConstruct,
    ) -> None:
        super().__init__(scope, id)
        get_run_logger()

        self.kube_config_provider_future: PrefectFuture[
            TerraformProvider
        ] = get_kube_config_provider.submit(
            scope=scope,
            config=config,
            cloud_instance_construct=cloud_instance_construct,
        )
        self.kube_config_resource_future: PrefectFuture[
            TerraformResource
        ] = get_kube_config_resource.submit(
            scope=scope,
            config=config,
            cloud_instance_construct=cloud_instance_construct,
            kube_config_provider=self.kube_config_provider_future,
        )
        self.kube_config_data_source_future: PrefectFuture[
            TerraformDataSource
        ] = get_kube_config_data_source.submit(
            scope=scope,
            config=config,
            cloud_instance_construct=cloud_instance_construct,
            kube_config_resource=self.kube_config_resource_future,
        )
        self.kube_config_outputs_future: PrefectFuture[
            Dict[str, TerraformOutput]
        ] = get_kube_config_outputs.submit(
            scope=scope,
            config=config,
            cloud_instance_construct=cloud_instance_construct,
            kube_config_data_source=self.kube_config_data_source_future,
        )

        self.provider = self.kube_config_provider_future.result()
        self.resource = self.kube_config_resource_future.result()
        self.data_source = self.kube_config_data_source_future.result()
        self.outputs = self.kube_config_outputs_future.result()

        try:
            kube_config_block = KubernetesClusterConfig.load("kube-config")

        except ValueError:
            kube_config_block = KubernetesClusterConfig.from_file(
                path=config.variables.get("kubeconfig"),
                context_name=config.variables.get("kubecontext"),
            )

            kube_config_block.save(
                name="kube-config",
                overwrite=False,
            )
