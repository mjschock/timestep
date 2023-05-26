import os

from constructs import Construct
from cdktf import App, TerraformDataSource, TerraformOutput, TerraformProvider, TerraformResource, TerraformStack

from omegaconf import DictConfig, OmegaConf
import hydra

from timestep.infra.imports.digitalocean.provider import DigitaloceanProvider as DigitaloceanTerraformProvider
from timestep.infra.imports.digitalocean.droplet import Droplet as DigitaloceanTerraformResource
from timestep.infra.imports.digitalocean.data_digitalocean_droplet import DataDigitaloceanDroplet as DigitaloceanTerraformDataSource
from timestep.infra.imports.multipass.provider import MultipassProvider as MultipassTerraformProvider
from timestep.infra.imports.multipass.instance import Instance as MultipassTerraformResource
from timestep.infra.imports.multipass.data_multipass_instance import DataMultipassInstance as MultipassTerraformDataSource


class MainTerraformStack(TerraformStack):
    def __init__(self, scope: Construct, id: str, target: str):
        super().__init__(scope, id)

        provider = self.get_provider(id, target)

        resource = self.get_resource(id, target, provider)

        data_source = self.get_data_source(id, target, provider, resource)

        output = self.get_output(target, data_source)

    def get_provider(self, id, target):
        if target in ["localhost", "multipass"]:
            provider = MultipassTerraformProvider(
                id=f"{id}-{target}-provider",
                scope=self,
            )

        elif target == "prod":
            do_token = os.environ.get("DO_TOKEN", "")

            provider = DigitaloceanTerraformProvider(
                id=f"{id}-{target}-provider",
                scope=self,
                token=do_token,
            )

        else:
            raise ValueError(f"Unknown target: {target}")

        assert isinstance(provider, TerraformProvider)
        return provider

    def get_resource(self, id, target, provider):
        if target in ["localhost", "multipass"]:
            cwd = os.getcwd()
            cloudinit_file = f"{cwd}/conf/base/cloud.yaml"

            resource = MultipassTerraformResource(
                cloudinit_file=cloudinit_file,
                cpus=2,
                disk="40G",
                id=f"{id}-{target}-resource",
                image="22.04", # "ros2-humble",
                # image="ros2-humble",
                # memory="4G",
                name=f"{id}",
                provider=provider,
                scope=self,
            )

        elif target == "prod":
            cwd = os.getcwd()
            cloudinit_file = f"{cwd}/conf/base/cloud.yaml"

            resource = DigitaloceanTerraformResource(
                id_=f"{id}-{target}-resource",
                image="ubuntu-22-04-x64",
                name=f"{id}",
                provider=provider,
                region='sfo3',
                scope=self,
                size='s-1vcpu-512mb-10gb',
                user_data=cloudinit_file,
            )

        else:
            raise ValueError(f"Unknown target: {target}")

        assert isinstance(resource, TerraformResource)
        return resource

    def get_data_source(self, id, target, provider, resource):
        if target in ["localhost", "multipass"]:
            data_source = MultipassTerraformDataSource(
                id=f"{id}-{target}-data_source",
                name=resource.name,
                provider=provider,
                scope=self,
            )

        elif target == "prod":
            data_source = DigitaloceanTerraformDataSource(
                id_=f"{id}-{target}-data_source",
                name=resource.name,
                provider=provider,
                scope=self,
            )

        else:
            raise ValueError(f"Unknown target: {target}")

        assert isinstance(data_source, TerraformDataSource)
        return data_source

    def get_output(self, target, data_source):
        if target in ["localhost", "multipass"]:
            output = TerraformOutput(
                id=f"{target}-ipv4",
                value=data_source.ipv4,
                scope=self,
            )

        elif target == "prod":
            output = TerraformOutput(
                id=f"{target}-ipv4",
                value=data_source.ipv4_address,
                scope=self,
            )

        else:
            raise ValueError(f"Unknown target: {target}")

        assert isinstance(output, TerraformOutput)
        return output


@hydra.main(config_name="config", config_path="conf", version_base=None)
def main(cfg: DictConfig) -> None:
    app_name = cfg.target.app_name
    env = cfg.target.env

    print(f"Running {app_name} app in {env} mode")

    app = App()

    MainTerraformStack(scope=app, id=app_name, target=env)

    app.synth()


if __name__ == "__main__":
    main()
