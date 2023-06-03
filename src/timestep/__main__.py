import os

from constructs import Construct
from cdktf import App, TerraformDataSource, TerraformElement, TerraformOutput, TerraformProvider, TerraformResource, TerraformStack

from omegaconf import DictConfig
import hydra

from timestep.infra.imports.digitalocean.provider import DigitaloceanProvider as DigitaloceanTerraformProvider
from timestep.infra.imports.digitalocean.domain import Domain as DigitaloceanDomainTerraformResource
from timestep.infra.imports.digitalocean.droplet import Droplet as DigitaloceanDropletTerraformResource
from timestep.infra.imports.digitalocean.data_digitalocean_droplet import DataDigitaloceanDroplet as DigitaloceanDropletTerraformDataSource
from timestep.infra.imports.digitalocean.data_digitalocean_domain import DataDigitaloceanDomain as DigitaloceanDomainTerraformDataSource
from timestep.infra.imports.helm.provider import HelmProvider as HelmTerraformProvider, HelmProviderKubernetes
from timestep.infra.imports.helm.data_helm_template import DataHelmTemplate as HelmTerraformDataSource
from timestep.infra.imports.helm.release import Release as HelmReleaseTerraformResource
from timestep.infra.imports.multipass.provider import MultipassProvider as MultipassTerraformProvider
from timestep.infra.imports.multipass.instance import Instance as MultipassInstanceTerraformResource
from timestep.infra.imports.multipass.data_multipass_instance import DataMultipassInstance as MultipassInstanceTerraformDataSource
from timestep.infra.imports.kubernetes.provider import KubernetesProvider as KubernetesTerraformProvider
from timestep.infra.imports.kubernetes.namespace import Namespace as KubernetesNamespaceTerraformResource, NamespaceMetadata
from timestep.infra.imports.kubernetes.ingress import Ingress as KubernetesIngressTerraformResource


class TerraformElementFactory():
    def __init__(self, scope: Construct, config: DictConfig) -> None:
        self.scope = scope
        self.config = config

    def build(self, *args, **kwargs) -> dict[str, TerraformElement]:
        raise NotImplementedError()


class TerraformProviderFactory(TerraformElementFactory):
    def build(self) -> dict[str, TerraformProvider]:
        providers = {}

        if self.config.target.env == "local":
            multipass_provider = MultipassTerraformProvider(
                id="multipass_provider",
                scope=self.scope,
            )

            providers["multipass"] = multipass_provider

        elif self.config.target.env == "prod":
            digitalocean_provider = DigitaloceanTerraformProvider(
                id="digitalocean_provider",
                scope=self.scope,
                token=self.config.target.do_token,
            )

            providers["digitalocean"] = digitalocean_provider

        else:
            raise ValueError(f"Unknown env: {self.config.target.env}")

        for provider in providers:
            assert isinstance(providers[provider], TerraformProvider)

        return providers


class TerraformResourceFactory(TerraformElementFactory):
    def build(self, providers: dict[str, TerraformProvider]) -> dict[str, TerraformResource]:
        resources = {}
        cwd = os.getcwd()
        cloudinit_file = f"{cwd}/src/timestep/conf/base/cloud-config.yaml"

        if self.config.target.env == "local":
            multipass_instance_resource = MultipassInstanceTerraformResource(
                cloudinit_file=cloudinit_file,
                cpus=self.config.target.multipass_instance_cpus,
                disk=self.config.target.multipass_instance_disk,
                id="multipass_instance_resource",
                image=self.config.target.multipass_instance_image,
                name=self.config.target.multipass_instance_name,
                provider=providers["multipass"],
                scope=self.scope,
            )

            resources["multipass_instance"] = multipass_instance_resource

        elif self.config.target.env == "prod":
            digitalocean_droplet_resource = DigitaloceanDropletTerraformResource(
                id="digitalocean_droplet_resource",
                image=self.config.target.do_droplet_image,
                name=self.config.target.do_droplet_name,
                provider=providers["digitalocean"],
                region=self.config.target.do_droplet_region,
                scope=self.scope,
                size=self.config.target.do_droplet_size,
                user_data=cloudinit_file,
            )

            resources["digitalocean_droplet"] = digitalocean_droplet_resource

            digitalocean_domain_resource = DigitaloceanDomainTerraformResource(
                id="digitalocean_domain_resource",
                ip_address=digitalocean_droplet_resource.ipv4_address,
                name=self.config.target.domain,
                provider=providers["digitalocean"],
                scope=self.scope,
            )

            resources["digitalocean_domain"] = digitalocean_domain_resource

        else:
            raise ValueError(f"Unknown env: {self.config.target.env}")

        for resource in resources:
            assert isinstance(resources[resource], TerraformResource)

        return resources


class TerraformDataSourceFactory(TerraformElementFactory):
    def build(self, providers: dict[str, TerraformProvider], resources: dict[str, TerraformResource]) -> dict[str, TerraformDataSource]:
        data_sources = {}

        if self.config.target.env == "local":
            multipass_instance_data_source = MultipassInstanceTerraformDataSource(
                id="multipass_instance_data_source",
                name=resources["multipass_instance"].name,
                provider=providers["multipass"],
                scope=self.scope,
            )

            data_sources["multipass_instance"] = multipass_instance_data_source

        elif self.config.target.env == "prod":
            digitalocean_droplet_data_source = DigitaloceanDropletTerraformDataSource(
                id="digitalocean_droplet_data_source",
                name=resources["digitalocean_droplet"].name,
                provider=providers["digitalocean"],
                scope=self.scope,
            )

            data_sources["digitalocean_droplet"] = digitalocean_droplet_data_source

            digitalocean_domain_data_source = DigitaloceanDomainTerraformDataSource(
                id="digitalocean_domain_data_source",
                name=resources["digitalocean_domain"].name,
                provider=providers["digitalocean"],
                scope=self.scope,
            )

            data_sources["digitalocean_domain"] = digitalocean_domain_data_source

        else:
            raise ValueError(f"Unknown env: {self.config.target.env}")

        for data_source in data_sources:
            assert isinstance(data_sources[data_source], TerraformDataSource)

        return data_sources


class TerraformOutputFactory(TerraformElementFactory):
    def build(self, data_sources: dict[str, TerraformDataSource]) -> dict[str, TerraformOutput]:
        outputs = {}

        if self.config.target.env == "local":
            multipass_instance_ipv4_output = TerraformOutput(
                id="multipass_instance_ipv4_output",
                value=data_sources["multipass_instance"].ipv4,
                scope=self.scope,
            )

            outputs["multipass_instance_ipv4"] = multipass_instance_ipv4_output

        elif self.config.target.env == "prod":
            digitalocean_droplet_ipv4_output = TerraformOutput(
                id="digitalocean_droplet_ipv4_output",
                value=data_sources["digitalocean_droplet"].ipv4_address,
                scope=self.scope,
            )

            outputs["digitalocean_droplet_ipv4"] = digitalocean_droplet_ipv4_output

            digitalocean_domain_zone_file_output = TerraformOutput(
                id="digitalocean_domain_zone_file_output",
                value=data_sources["digitalocean_domain"].zone_file,
                scope=self.scope,
            )

            outputs["digitalocean_domain_zone_file"] = digitalocean_domain_zone_file_output

        else:
            raise ValueError(f"Unknown env: {self.config.target.env}")

        for output in outputs:
            assert isinstance(outputs[output], TerraformOutput)
  
        return outputs


class CloudTerraformStack(TerraformStack):
    def __init__(self, scope: Construct, id: str, config: DictConfig, **kwargs) -> None:
        super().__init__(scope, id)

        providers = TerraformProviderFactory(scope=self, config=config).build()

        for provider in providers:
            assert isinstance(providers[provider], TerraformElement)
            assert isinstance(providers[provider], TerraformProvider)

        resources = TerraformResourceFactory(scope=self, config=config).build(providers=providers)

        for resource in resources:        
            assert isinstance(resources[resource], TerraformElement)
            assert isinstance(resources[resource], TerraformResource)

        data_sources = TerraformDataSourceFactory(scope=self, config=config).build(providers=providers, resources=resources)

        for data_source in data_sources:
            assert isinstance(data_sources[data_source], TerraformElement)
            assert isinstance(data_sources[data_source], TerraformDataSource)

        self.outputs = TerraformOutputFactory(scope=self, config=config).build(data_sources=data_sources)

        for output in self.outputs:
            assert isinstance(self.outputs[output], TerraformElement)
            assert isinstance(self.outputs[output], TerraformOutput)


class KubernetesStackConfig:
    host: str

    def __init__(self, config: DictConfig, cloud_stack: CloudTerraformStack) -> None:
        if config.target.env == "local":
            self.host=cloud_stack.outputs["multipass_instance_ipv4"].value

        elif config.target.env == "prod":
            self.host=cloud_stack.outputs["digitalocean_droplet_ipv4"].value

        else:
            raise ValueError(f"Unknown env: {self.config.target.env}")

class KubernetesTerraformStack(TerraformStack):
    def __init__(self, scope: Construct, id: str, config: DictConfig, kube_stack_config: KubernetesStackConfig, **kwargs) -> None:
        super().__init__(scope, id)

        kubernetes_provider = KubernetesTerraformProvider(
            id="kubernetes_provider",
            config_context="timestep-ai-k3s-cluster",
            config_path = "~/.kube/config",
            scope=self,
        )

        metadata = NamespaceMetadata(
            name="caddy-system",
        )

        kubernetes_namespace = KubernetesNamespaceTerraformResource(
            id_="kubernetes_namespace",
            metadata=metadata,
            provider=kubernetes_provider,
            scope=self,
        )

        kubernetes = HelmProviderKubernetes(
            config_context=kubernetes_provider.config_context,
            config_path=kubernetes_provider.config_path,
        )

        helm_provider = HelmTerraformProvider(
            id="helm_provider",
            kubernetes=kubernetes,
            scope=self,
        )

        helm_release_resource = HelmReleaseTerraformResource(
            id_="helm_release_resource",
            atomic=True,
            chart="caddy-ingress-controller",
            name="timestep-ai",
            namespace=metadata.name,
            repository="https://caddyserver.github.io/ingress",
            provider=helm_provider,
            scope=self,
        )


class TimestepAIStack(TerraformStack):
    def __init__(self, scope: Construct, id: str, config: DictConfig, **kwargs) -> None:
        super().__init__(scope, id)


@hydra.main(config_name="config", config_path="conf", version_base=None)
def main(config: DictConfig) -> None:
    print(f"config: {config}")

    app_name = config.target.app_name
    env = config.target.env
    id = f"{app_name}-{env}"

    app = App()

    cloud_stack = CloudTerraformStack(scope=app, id=f"{app_name}-{env}", config=config) # aka "base" stack or BareMetalStack

    # TODO: Run prefect shell script to load kubeconfig from cloud instance
    kube_stack_config = KubernetesStackConfig(config=config, cloud_stack=cloud_stack) # aka KubernetesClusterStack
    k8s_stack = KubernetesTerraformStack(scope=app, id=f"{app_name}-{env}-k8s-stack", config=config, kube_stack_config=kube_stack_config)

    # TimestepAIStack(scope=app, id=f"{app_name}-{env}-?", config=config) # aka TimestepAIPlatformStack

    app.synth()


if __name__ == "__main__":
    main()
