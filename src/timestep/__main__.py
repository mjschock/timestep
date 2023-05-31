import os

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

    def build_element(self, *args, **kwargs) -> TerraformElement:
        raise NotImplementedError()


class TerraformProviderFactory(TerraformElementFactory):
    def build_element(self) -> TerraformProvider:
        if self.config.target.env == "local":
            provider = MultipassTerraformProvider(
                id=f"{self.stack_id}-provider",
                scope=self.scope,
            )

        elif self.config.target.env == "prod":
            provider = DigitaloceanTerraformProvider(
                id=f"{self.stack_id}-provider",
                scope=self.scope,
                token=self.config.target.do_token,
            )

        else:
            raise ValueError(f"Unknown env: {self.config.target.env}")

        assert isinstance(provider, TerraformProvider)
        return provider


class TerraformResourceFactory(TerraformElementFactory):
    def build_element(self, provider: TerraformProvider) -> TerraformResource:
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

        else:
            raise ValueError(f"Unknown env: {self.config.target.env}")

        assert isinstance(resource, TerraformResource)
        return resource


class TerraformDataSourceFactory(TerraformElementFactory):
    def build_element(self, provider: TerraformProvider, resource: TerraformResource) -> TerraformDataSource:
        if self.config.target.env == "local":
            data_source = MultipassTerraformDataSource(
                id=f"{self.stack_id}-data_source",
                name=resource.name,
                provider=provider,
                scope=self.scope,
            )

        elif self.config.target.env == "prod":
            data_source = DigitaloceanTerraformDataSource(
                id_=f"{self.stack_id}-data_source",
                name=resource.name,
                provider=provider,
                scope=self.scope,
            )

        else:
            raise ValueError(f"Unknown env: {self.config.target.env}")

        assert isinstance(data_source, TerraformDataSource)
        return data_source


class TerraformOutputFactory(TerraformElementFactory):
    def build_element(self, data_source: TerraformDataSource) -> TerraformOutput:
        if self.config.target.env == "local":
            output = TerraformOutput(
                id=f"{self.stack_id}-output-ipv4",
                value=data_source.ipv4,
                scope=self.scope,
            )

        elif self.config.target.env == "prod":
            output = TerraformOutput(
                id=f"{self.stack_id}-output-ipv4",
                value=data_source.ipv4_address,
                scope=self.scope,
            )

        else:
            raise ValueError(f"Unknown env: {self.config.target.env}")

        assert isinstance(output, TerraformOutput)
        return output


class MainTerraformStack(TerraformStack):
    def __init__(self, scope: Construct, id: str, config: DictConfig, **kwargs) -> None:
        super().__init__(scope, id)

        provider: TerraformProvider = TerraformProviderFactory(scope=self, stack_id=id, config=config).build_element()
        assert isinstance(provider, TerraformElement)

        resource: TerraformResource = TerraformResourceFactory(scope=self, stack_id=id, config=config).build_element(provider=provider)
        assert isinstance(resource, TerraformElement)

        data_source: TerraformDataSource = TerraformDataSourceFactory(scope=self, stack_id=id, config=config).build_element(provider=provider, resource=resource)
        assert isinstance(data_source, TerraformElement)

        output: TerraformOutput = TerraformOutputFactory(scope=self, stack_id=id, config=config).build_element(data_source=data_source)
        assert isinstance(output, TerraformElement)


@hydra.main(config_name="config", config_path="conf", version_base=None)
def main(config: DictConfig) -> None:
    app_name = config.target.app_name
    env = config.target.env
    id = f"{app_name}-{env}"

    app = App()

    MainTerraformStack(scope=app, id=id, config=config)

    app.synth()


if __name__ == "__main__":
    main()
