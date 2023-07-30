import tempfile

from cdktf import LocalExecProvisioner
from constructs import Construct
from pydantic import SecretStr
from timestep.config import CloudInstanceProvider, Settings
from timestep.infra.imports.local.data_local_file import DataLocalFile
from timestep.infra.imports.local.provider import LocalProvider
from timestep.infra.imports.null.provider import NullProvider
from timestep.infra.imports.null.resource import Resource
from timestep.infra.stacks.main.constructs.cloud_instance.construct import (
    CloudInstanceConstruct,
)


class KubeConfigConstruct(Construct):
    def __init__(
        self,
        scope: Construct,
        id: str,
        config: Settings,
        cloud_instance_construct: CloudInstanceConstruct,
    ) -> None:
        super().__init__(scope, id)

        if config.cloud_instance_provider == CloudInstanceProvider.MULTIPASS:
            ipv4 = (
                cloud_instance_construct.data_source.ipv4
            )  # TODO: can I use the output  # noqa: E501
        else:
            ipv4 = cloud_instance_construct.data_source.ipv4_address

        kubecontext = config.kubecontext
        local_path = "kubeconfig"
        # ssh_private_key: SecretStr = config.secrets.get_secret_value().get(
        #     "ssh_private_key"
        # )
        ssh_private_key: SecretStr = config.ssh_private_key
        username = config.cloud_instance_user

        with tempfile.NamedTemporaryFile(
            delete=False,
            # dir=DIST_PATH,
        ) as fp:
            fp.write(ssh_private_key.get_secret_value().encode())
            fp.flush()

            ssh_key_path = fp.name

            local_exec_provisioner = LocalExecProvisioner(
                command=f"k3sup install --context {kubecontext} --ip {ipv4} --k3s-extra-args '--disable traefik' --local-path {local_path} --skip-install --ssh-key {ssh_key_path} --user {username} && rm {ssh_key_path}",  # noqa: E501
                type="local-exec",
            )

        kube_config_provider = NullProvider(
            alias="kube_config_provider",
            id="kube_config_provider",
            scope=scope,
        )

        kube_config_resource = Resource(  # noqa: F841
            id="kube_config_resource",
            provider=kube_config_provider,
            provisioners=[
                local_exec_provisioner,
            ],
            scope=scope,
            triggers={
                # "ipv4": cloud_instance_construct.data_source.ipv4_address,
                "ipv4": ipv4,
                # "ssh_private_key": config.secrets.get_secret_value().get("ssh_private_key")  # noqa: E501
            },
        )

        kube_config_local_provider = LocalProvider(
            id="kube_config_local_provider",
            scope=scope,
            alias="kube_config_local_provider",
        )

        self.data_source = DataLocalFile(
            depends_on=[kube_config_resource],
            id="kube_config_data_source",
            filename=local_path,
            scope=scope,
            provider=kube_config_local_provider,
        )
