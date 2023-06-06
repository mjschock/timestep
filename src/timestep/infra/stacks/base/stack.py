import os
import yaml

from constructs import Construct
from cdktf import TerraformDataSource, TerraformElement, TerraformOutput, TerraformProvider, TerraformResource, TerraformStack
from cloud_init_gen import CloudInitDoc
from omegaconf import DictConfig
from pydantic import BaseModel

from timestep.infra.imports.digitalocean.provider import DigitaloceanProvider as DigitaloceanTerraformProvider
from timestep.infra.imports.digitalocean.domain import Domain as DigitaloceanDomainTerraformResource
from timestep.infra.imports.digitalocean.droplet import Droplet as DigitaloceanDropletTerraformResource
from timestep.infra.imports.digitalocean.data_digitalocean_droplet import DataDigitaloceanDroplet as DigitaloceanDropletTerraformDataSource
from timestep.infra.imports.digitalocean.data_digitalocean_domain import DataDigitaloceanDomain as DigitaloceanDomainTerraformDataSource
from timestep.infra.imports.multipass.provider import MultipassProvider as MultipassTerraformProvider
from timestep.infra.imports.multipass.instance import Instance as MultipassInstanceTerraformResource
from timestep.infra.imports.multipass.data_multipass_instance import DataMultipassInstance as MultipassInstanceTerraformDataSource


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
        # cloudinit_file = f"{cwd}/src/timestep/conf/base/cloud-config.yaml"
        cloudinit_file = f"{cwd}/dist/cloud-config.yaml"

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


class TargetConfig(BaseModel):
    app_name: str
    domain: str
    env: str
    ssh_authorized_key_path: str


class MultipassTargetConfig(TargetConfig):
    multipass_instance_cpus: int
    multipass_instance_disk: str
    multipass_instance_image: str
    multipass_instance_name: str


class DigitaloceanTargetConfig(TargetConfig):
    do_droplet_image: str
    do_droplet_name: str
    do_droplet_region: str
    do_droplet_size: str
    do_token: str # TODO: Use secret


class BaseTerraformStackConfig(BaseModel):
    target: MultipassTargetConfig | DigitaloceanTargetConfig


class BaseTerraformStack(TerraformStack):
    def __init__(self, scope: Construct, id: str, config: BaseTerraformStackConfig) -> None:
        super().__init__(scope, id)

        self.config = config

        user_data = CloudInitDoc()

        with open(self.config.target.ssh_authorized_key_path, "r") as file:
            ssh_authorized_key = file.read().strip()

        cloud_cfg = dict(
            disable_root = True,
            package_reboot_if_required = True,
            package_update = True,
            package_upgrade = True,
            packages = [
                "build-essential",
                "curl",
                "default-jdk",
                "direnv",
                "figlet",
                "jq",
                "libbz2-dev",
                "libffi-dev",
                "liblzma-dev",
                "libncursesw5-dev",
                "libreadline-dev",
                "libsqlite3-dev",
                "libssl-dev",
                "libxml2-dev",
                "libxmlsec1-dev",
                "net-tools",
                "tk-dev",
                "unzip",
                "xz-utils",
                "zlib1g-dev",
            ],
            runcmd = [
                ["runuser", "-l", "ubuntu", "-c", 'bash -c "$(curl -fsSL https://raw.githubusercontent.com/ohmybash/oh-my-bash/master/tools/install.sh)"'],
                ["runuser", "-l", "ubuntu", "-c", 'echo "" >> $HOME/.oh-my-bash/custom/example.sh'],
                ["runuser", "-l", "ubuntu", "-c", 'echo OSH_THEME=\"zork\" >> $HOME/.oh-my-bash/custom/example.sh'],
                ["runuser", "-l", "ubuntu", "-c", 'echo "" >> $HOME/.bashrc'],
                # "runuser -l ubuntu -c 'echo \"eval \\\"\$(direnv hook bash)\\\"\" >> $HOME/.bashrc'",
                ["runuser", "-l", "ubuntu", "-c", 'echo \"eval \\\"\$(direnv hook bash)\\\"\" >> $HOME/.bashrc'],
                ["runuser", "-l", "ubuntu", "-c", 'git clone https://github.com/anyenv/anyenv ~/.anyenv'],
                ["runuser", "-l", "ubuntu", "-c", 'echo "" >> $HOME/.bashrc'],
                ["runuser", "-l", "ubuntu", "-c", 'echo export PATH=\$HOME/.anyenv/bin:\$PATH >> $HOME/.bashrc'],
                # "runuser -l ubuntu -c 'echo \"eval \\\"\$(anyenv init -)\\\"\" >> $HOME/.bashrc'",
                ["runuser", "-l", "ubuntu", "-c", 'echo \"eval \\\"\$(anyenv init -)\\\"\" >> $HOME/.bashrc'],
                ["runuser", "-l", "ubuntu", "-c", '$HOME/.anyenv/bin/anyenv install --force-init'],
                ["runuser", "-l", "ubuntu", "-c", '$HOME/.anyenv/bin/anyenv install jenv'],
                ["runuser", "-l", "ubuntu", "-c", '$HOME/.anyenv/bin/anyenv install nodenv'],
                ["runuser", "-l", "ubuntu", "-c", '$HOME/.anyenv/bin/anyenv install goenv'],
                ["runuser", "-l", "ubuntu", "-c", '$HOME/.anyenv/bin/anyenv install pyenv'],
                ["runuser", "-l", "ubuntu", "-c", 'curl -sLS https://get.arkade.dev | sudo sh'],
                ["runuser", "-l", "ubuntu", "-c", 'echo "" >> $HOME/.bashrc'],
                ["runuser", "-l", "ubuntu", "-c", 'echo export PATH=\$HOME/.arkade/bin:\$PATH >> $HOME/.bashrc'],
                ["runuser", "-l", "ubuntu", "-c", 'arkade get k3sup'],
                ["runuser", "-l", "ubuntu", "-c", 'mkdir $HOME/.kube'],
                ["runuser", "-l", "ubuntu", "-c", '$HOME/.arkade/bin/k3sup install --context timestep-ai-k3s-cluster --k3s-extra-args "--disable traefik" --local --local-path $HOME/.kube/config --user ubuntu'],
            ],
            users = [
                "default",
                {
                    "groups": "sudo",
                    "name": "ubuntu",
                    "shell": "/bin/bash",
                    "ssh_authorized_keys": [
                        ssh_authorized_key,
                    ],
                    "sudo": "ALL=(ALL) NOPASSWD:ALL",
                }
            ],
            write_files = [
                {
                    "content": f"""\
#!/bin/sh
[ -r /etc/lsb-release ] && . /etc/lsb-release

if [ -z \"$DISTRIB_DESCRIPTION\" ] && [ -x /usr/bin/lsb_release ]; then
        # Fall back to using the very slow lsb_release utility
        DISTRIB_DESCRIPTION=$(lsb_release -s -d)
fi

printf \"Welcome to \n%s\nv%s\nrunning on %s (%s %s %s).\n\" \"$(figlet Timestep AI)\" \"$(date +'%Y.%m.%d')\" \"$DISTRIB_DESCRIPTION\" \"$(uname -o)\" \"$(uname -r)\" \"$(uname -m)\"
                    """,
                    "path": "/etc/update-motd.d/00-header",
                    "permissions": "\"0o755\"",
                },
            ],
                # content = f"""\
            # - content: |
            #     mirrors:
            #         registry.localhost:
            #         endpoint:
            #             - "http://registry:5000"
            #     path: /etc/rancher/k3s/registries.yaml
            #     permissions: "0o644"
        )

        user_data.add(cloud_cfg)  # will be rendered as yaml with implicit MIME type text/cloud-config

        print(f"Final user-data (text):\n====================\n{user_data.render()}\n====================")
        print(f"Final user-data (base64):\n====================\n{user_data.render_base64()}\n====================")

        with open("dist/cloud-config.yaml", "w") as file:
            file.write(user_data.render())

        providers = TerraformProviderFactory(scope=self, config=self.config).build()

        for provider in providers:
            assert isinstance(providers[provider], TerraformElement)
            assert isinstance(providers[provider], TerraformProvider)

        resources = TerraformResourceFactory(scope=self, config=self.config).build(providers=providers)

        for resource in resources:        
            assert isinstance(resources[resource], TerraformElement)
            assert isinstance(resources[resource], TerraformResource)

        data_sources = TerraformDataSourceFactory(scope=self, config=self.config).build(providers=providers, resources=resources)

        for data_source in data_sources:
            assert isinstance(data_sources[data_source], TerraformElement)
            assert isinstance(data_sources[data_source], TerraformDataSource)

        self.outputs = TerraformOutputFactory(scope=self, config=self.config).build(data_sources=data_sources)

        for output in self.outputs:
            assert isinstance(self.outputs[output], TerraformElement)
            assert isinstance(self.outputs[output], TerraformOutput)
