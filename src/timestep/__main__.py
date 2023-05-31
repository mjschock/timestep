import os
from typing import Dict, List

from constructs import Construct
from cdktf import App, TerraformDataSource, TerraformElement, TerraformOutput, TerraformProvider, TerraformResource, TerraformStack

from omegaconf import DictConfig, OmegaConf
import hydra

from timestep.infra.imports.digitalocean.provider import DigitaloceanProvider as DigitaloceanTerraformProvider
from timestep.infra.imports.digitalocean.droplet import Droplet as DigitaloceanTerraformResource
from timestep.infra.imports.digitalocean.data_digitalocean_droplet import DataDigitaloceanDroplet as DigitaloceanTerraformDataSource
from timestep.infra.imports.multipass.provider import MultipassProvider as MultipassTerraformProvider
from timestep.infra.imports.multipass.instance import Instance as MultipassTerraformResource
from timestep.infra.imports.multipass.data_multipass_instance import DataMultipassInstance as MultipassTerraformDataSource


class TerraformElementFactory():
    def __init__(self, scope: Construct, stack_id: str, config: DictConfig) -> None:
        self.scope = scope
        self.stack_id = stack_id
        self.config = config

    def build(self, *args, **kwargs) -> Dict[str, TerraformElement]:
        raise NotImplementedError()


class TerraformProviderFactory(TerraformElementFactory):
    def build(self) -> Dict[str, TerraformProvider]:
        providers = {}

        if self.config.target.env == "local":
            provider = MultipassTerraformProvider(
                id=f"{self.stack_id}-provider",
                scope=self.scope,
            )

            providers["multipass"] = provider

        elif self.config.target.env == "prod":
            provider = DigitaloceanTerraformProvider(
                id=f"{self.stack_id}-provider",
                scope=self.scope,
                token=self.config.target.do_token,
            )

            providers["digitalocean"] = provider

        else:
            raise ValueError(f"Unknown env: {self.config.target.env}")

        for provider in providers:
            assert isinstance(providers[provider], TerraformProvider)

        return providers


class TerraformResourceFactory(TerraformElementFactory):
    def build(self, providers: Dict[str, TerraformProvider]) -> Dict[str, TerraformResource]:
        resources = {}
        cwd = os.getcwd()
        cloudinit_file = f"{cwd}/src/timestep/conf/base/cloud-config.yaml"

        if self.config.target.env == "local":
            resource = MultipassTerraformResource(
                cloudinit_file=cloudinit_file,
                cpus=2,
                disk="40G",
                id=f"{self.stack_id}-resource",
                image="22.04",
                name=f"{self.stack_id}",
                provider=provider,
                scope=self.scope,
            )

            resources["multipass"] = resource

        elif self.config.target.env == "prod":
            resource = DigitaloceanTerraformResource(
                id_=f"{self.stack_id}-resource",
                image="ubuntu-22-04-x64",
                name=f"{self.stack_id}",
                provider=provider,
                region='sfo3',
                scope=self.scope,
                size='s-1vcpu-512mb-10gb',
                user_data=cloudinit_file,
            )

            resources["digitalocean"] = resource

        else:
            raise ValueError(f"Unknown env: {self.config.target.env}")

        for resource in resources:
            assert isinstance(resources[resource], TerraformResource)
        
        return resources


class TerraformDataSourceFactory(TerraformElementFactory):
    def build(self, providers: Dict[str, TerraformProvider], resources: Dict[str, TerraformResource]) -> Dict[str, TerraformDataSource]:
        data_sources = {}

        if self.config.target.env == "local":
            data_source = MultipassTerraformDataSource(
                id=f"{self.stack_id}-data_source",
                name=resource.name,
                provider=provider,
                scope=self.scope,
            )

            data_sources["multipass"] = data_source

        elif self.config.target.env == "prod":
            data_source = DigitaloceanTerraformDataSource(
                id_=f"{self.stack_id}-data_source",
                name=resource.name,
                provider=provider,
                scope=self.scope,
            )

            data_sources["digitalocean"] = data_source

        else:
            raise ValueError(f"Unknown env: {self.config.target.env}")

        for data_source in data_sources:
            assert isinstance(data_sources[data_source], TerraformDataSource)

        return data_sources


class TerraformOutputFactory(TerraformElementFactory):
    def build(self, data_sources: Dict[str, TerraformDataSource]) -> Dict[str, TerraformOutput]:
        outputs = {}

        if self.config.target.env == "local":
            output = TerraformOutput(
                id=f"{self.stack_id}-output-ipv4",
                value=data_source.ipv4,
                scope=self.scope,
            )

            outputs["multipass"] = output

        elif self.config.target.env == "prod":
            output = TerraformOutput(
                id=f"{self.stack_id}-output-ipv4",
                value=data_source.ipv4_address,
                scope=self.scope,
            )

            outputs["digitalocean"] = output

        else:
            raise ValueError(f"Unknown env: {self.config.target.env}")

        for output in outputs:
            assert isinstance(outputs[output], TerraformOutput)
  
        return outputs


class MainTerraformStack(TerraformStack):
    def __init__(self, scope: Construct, id: str, config: DictConfig, **kwargs) -> None:
        super().__init__(scope, id)

        providers = TerraformProviderFactory(scope=self, stack_id=id, config=config).build()

        for provider in providers:
            assert isinstance(providers[provider], TerraformElement)
            assert isinstance(providers[provider], TerraformProvider)

        resources = TerraformResourceFactory(scope=self, stack_id=id, config=config).build(providers=providers)

        for resource in resources:        
            assert isinstance(resources[resource], TerraformElement)
            assert isinstance(resources[resource], TerraformResource)

        data_sources = TerraformDataSourceFactory(scope=self, stack_id=id, config=config).build(providers=providers, resources=resources)

        for data_source in data_sources:
            assert isinstance(data_sources[data_source], TerraformElement)
            assert isinstance(data_sources[data_source], TerraformDataSource)

        outputs = TerraformOutputFactory(scope=self, stack_id=id, config=config).build(data_sources=data_sources)

        for output in outputs:
            assert isinstance(outputs[output], TerraformElement)
            assert isinstance(output[output], TerraformOutput)


@hydra.main(config_name="config", config_path="conf", version_base=None)
def main(config: DictConfig) -> None:
    print(f"config: {config}")

    app_name = config.target.app_name
    env = config.target.env
    id = f"{app_name}-{env}"

    app = App()

    MainTerraformStack(scope=app, id=id, config=config)

    app.synth()


if __name__ == "__main__":
    main()
