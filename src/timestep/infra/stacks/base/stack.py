from cdktf import (
    TerraformDataSource,
    TerraformOutput,
    TerraformProvider,
    TerraformResource,
    TerraformStack,
)
from constructs import Construct
from prefect import get_run_logger
from prefect.futures import PrefectFuture

from timestep.conf.blocks import AppConfig
from timestep.infra.stacks.base.constructs.cloud_init_config.blocks import (
    CloudInitConfigConstruct,
)
from timestep.infra.stacks.base.constructs.cloud_instance.blocks import (
    CloudInstanceConstruct,
)
from timestep.infra.stacks.base.constructs.cloud_instance_domain.blocks import (
    CloudInstanceDomainConstruct,
)
from timestep.infra.stacks.base.constructs.domain_name_registrar.blocks import (
    DomainNameRegistrarConstruct,
)
from timestep.infra.stacks.base.constructs.kube_config.blocks import KubeConfigConstruct
from timestep.infra.stacks.base.constructs.kubernetes_cluster.blocks import (
    KubernetesClusterConstruct,
)


class BaseStack(TerraformStack):
    def __init__(self, scope: Construct, id: str, config: AppConfig) -> None:
        super().__init__(scope, id)
        logger = get_run_logger()

        self.cloud_init_config_construct = CloudInitConfigConstruct(
            config=config,
            id="cloud_init_config_construct",
            scope=self,
        )

        self.cloud_instance_construct = CloudInstanceConstruct(
            cloud_init_config_construct=self.cloud_init_config_construct,
            config=config,
            id="cloud_instance_construct",
            scope=self,
        )

        self.cloud_instance_domain_construct = CloudInstanceDomainConstruct(
            cloud_instance_construct=self.cloud_instance_construct,
            config=config,
            id="cloud_instance_domain_construct",
            scope=self,
        )

        self.domain_name_registar_construct = DomainNameRegistrarConstruct(
            cloud_instance_construct=self.cloud_instance_construct,
            config=config,
            id="domain_name_registar_construct",
            scope=self,
        )

        self.kube_config_construct = KubeConfigConstruct(
            cloud_instance_construct=self.cloud_instance_construct,
            config=config,
            id="kube_config_construct",
            scope=self,
        )

        self.kubernetes_cluster_construct = KubernetesClusterConstruct(
            # cloud_instance_construct=self.cloud_instance_construct,
            config=config,
            id="kubernetes_cluster_construct",
            scope=self,
        )

        # # kubernetes_cluster_ingress = KubernetesClusterIngressConstruct(
        # #     self, "kubernetes_cluster_ingress", config=config, kubernetes_cluster=kubernetes_cluster
        # # )

        # cloud_init_config_provider_future: PrefectFuture[TerraformProvider] = get_cloud_init_config_provider.submit(scope=self, config=config)
        # cloud_init_config_resource_future: PrefectFuture[TerraformResource] = get_cloud_init_config_resource.submit(scope=self, config=config, cloud_init_config_provider=cloud_init_config_provider_future)
        # cloud_init_config_data_source_future: PrefectFuture[TerraformDataSource] = get_cloud_init_config_data_source.submit(scope=self, config=config, cloud_init_config_resource=cloud_init_config_resource_future)

        # cloud_instance_provider_future: PrefectFuture[TerraformProvider] = get_cloud_instance_provider.submit(scope=self, config=config, cloud_init_config_data_source=cloud_init_config_data_source_future)
        # # cloud_instance_resource_future: PrefectFuture[TerraformResource] = get_cloud_instance_resource.submit(scope=scope, config=config, cloud_instance_provider=cloud_instance_provider_future)
        # # cloud_instance_data_source_future: PrefectFuture[TerraformDataSource] = get_cloud_instance_data_source.submit(scope=self, config=config, cloud_instance_resource=cloud_instance_resource_future)

        # cloud_instance_domain_provider_future: PrefectFuture[TerraformProvider] = get_cloud_instance_domain_provider.submit(scope=scope, config=config)
        # cloud_instance_domain_resource_future: PrefectFuture[TerraformResource] = get_cloud_instance_domain_resource.submit(scope=scope, config=config, cloud_instance_domain_provider=cloud_instance_domain_provider_future)
        # cloud_instance_domain_data_source_future: PrefectFuture[TerraformDataSource] = get_cloud_instance_domain_data_source.submit(scope=self, config=config, cloud_instance_domain_resource=cloud_instance_domain_resource_future)

        # domain_name_registar_provider_future: PrefectFuture[TerraformProvider] = get_domain_name_registar_provider.submit(scope=scope, config=config)
        # domain_name_registar_resource_future: PrefectFuture[TerraformResource] = get_domain_name_registar_resource.submit(scope=scope, config=config, domain_name_registar_provider=domain_name_registar_provider_future)
        # domain_name_registar_data_source_future: PrefectFuture[TerraformDataSource] = get_domain_name_registar_data_source.submit(scope=self, config=config, domain_name_registar_resource=domain_name_registar_resource_future)

        # kube_config_provider_future: PrefectFuture[TerraformProvider] = get_kube_config_provider.submit(scope=scope, config=config)
        # kube_config_resource_future: PrefectFuture[TerraformResource] = get_kube_config_resource.submit(scope=scope, config=config, kube_config_provider=kube_config_provider_future)
        # kube_config_data_source_future: PrefectFuture[TerraformDataSource] = get_kube_config_data_source.submit(scope=self, config=config, kube_config_resource=kube_config_resource_future)

        # kubernetes_cluster_provider_future: PrefectFuture[TerraformProvider] = get_kubernetes_cluster_provider.submit(scope=scope, config=config, kube_config_data_source=kube_config_data_source_future)
        # kubernetes_cluster_resource_future: PrefectFuture[TerraformResource] = get_kubernetes_cluster_resource.submit(scope=scope, config=config, kubernetes_cluster_provider=kubernetes_cluster_provider_future)
        # kubernetes_cluster_data_source_future: PrefectFuture[TerraformDataSource] = get_kubernetes_cluster_data_source.submit(scope=self, config=config, kubernetes_cluster_resource=kubernetes_cluster_resource_future)

        # kubernetes_cluster_ingress_provider_future: PrefectFuture[TerraformProvider] = get_kubernetes_cluster_ingress_provider.submit(scope=scope, config=config, kubernetes_cluster_data_source=kubernetes_cluster_data_source_future)
        # kubernetes_cluster_ingress_resource_future: PrefectFuture[TerraformResource] = get_kubernetes_cluster_ingress_resource.submit(scope=scope, config=config, kubernetes_cluster_ingress_provider=kubernetes_cluster_ingress_provider_future)
        # kubernetes_cluster_ingress_data_source_future: PrefectFuture[TerraformDataSource] = get_kubernetes_cluster_ingress_data_source.submit(scope=self, config=config, kubernetes_cluster_ingress_resource=kubernetes_cluster_ingress_resource_future)

        # for construct in self.contructs:
        #     for output in construct.outputs:
        #         out
