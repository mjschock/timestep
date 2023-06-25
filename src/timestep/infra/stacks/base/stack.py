from cdktf import TerraformDataSource, TerraformOutput, TerraformProvider, TerraformResource, TerraformStack
from constructs import Construct
from prefect import get_run_logger
from prefect.futures import PrefectFuture

from timestep.conf import MainConfig
from timestep.infra.stacks.base.constructs.cloud_init_config.construct import CloudInitConfigConstruct, get_cloud_init_config_data_source, get_cloud_init_config_provider, get_cloud_init_config_resource
from timestep.infra.stacks.base.constructs.cloud_instance.construct import CloudInstanceConstruct, get_cloud_instance_provider
from timestep.infra.stacks.base.constructs.cloud_instance_domain.construct import CloudInstanceDomainConstruct
from timestep.infra.stacks.base.constructs.domain_name_registrar.construct import DomainNameRegistrarConstruct


class BaseStack(TerraformStack):
    def __init__(
        self, scope: Construct, id: str, config: MainConfig
    ) -> None:
        super().__init__(scope, id)
        logger = get_run_logger()
        # logger.info(f"config: {config}")

        self.cloud_init_config_construct = CloudInitConfigConstruct(
            scope=self, id="cloud_init_config_construct", config=config
        )

        self.cloud_instance_construct = CloudInstanceConstruct(
            scope=self, id="cloud_instance_construct", config=config, cloud_init_config_construct=self.cloud_init_config_construct
        )

        self.cloud_instance_domain_construct = CloudInstanceDomainConstruct(
            self, "cloud_instance_domain_construct", config=config, cloud_instance_construct=self.cloud_instance_construct
        )

        self.domain_name_registar_construct = DomainNameRegistrarConstruct(
            self, "domain_name_registar", config=config, cloud_instance_construct=self.cloud_instance_construct
        )

        # # kube_config = KubeConfigConstruct(
        # #     self, "kube_config", config=config, cloud_instance=cloud_instance
        # # )

        # # kubernetes_cluster = KubernetesClusterConstruct(
        # #     self, "kubernetes_cluster", config=config, kube_config=kube_config
        # # )

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