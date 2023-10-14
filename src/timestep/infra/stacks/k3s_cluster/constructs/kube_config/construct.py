import datetime

from cdktf import LocalExecProvisioner
from cdktf_cdktf_provider_local.data_local_file import DataLocalFile
from cdktf_cdktf_provider_local.provider import LocalProvider
from cdktf_cdktf_provider_null.provider import NullProvider
from cdktf_cdktf_provider_null.resource import Resource
from constructs import Construct
from timestep.config import CloudInstanceProvider, Settings
from timestep.infra.stacks.k3s_cluster.constructs.cloud_instance.construct import (
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
        local_kube_config_path = f"{config.base_path}/secrets/kubeconfig"
        username = config.cloud_instance_user
        ssh_private_key_path = config.ssh_private_key_path

        kube_config_provider = NullProvider(
            alias="kube_config_provider",
            id="kube_config_provider",
            scope=scope,
        )

        kube_config_resource = Resource(  # noqa: F841
            depends_on=[cloud_instance_construct.data_source],  # noqa: F841
            id="kube_config_resource",
            provider=kube_config_provider,
            provisioners=[
                LocalExecProvisioner(
                    command=f"k3sup install --context {kubecontext} --ip {ipv4} --local-path {local_kube_config_path} --skip-install --ssh-key {ssh_private_key_path} --user {username}",  # noqa: E501
                    type="local-exec",
                    when="create",
                ),
                LocalExecProvisioner(
                    command=f"rm {local_kube_config_path} || true",
                    type="local-exec",
                    when="destroy",
                ),
            ],
            scope=scope,
            triggers={
                "always": str(datetime.datetime.now()),
                "ipv4": ipv4,
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
            filename=local_kube_config_path,
            scope=scope,
            provider=kube_config_local_provider,
        )
