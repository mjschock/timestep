from cdktf import TerraformDataSource, TerraformOutput

# from timestep.config import AppConfig
from cdktf_cdktf_provider_cloudinit.data_cloudinit_config import (
    DataCloudinitConfig,
    DataCloudinitConfigPart,
)
from cdktf_cdktf_provider_cloudinit.provider import CloudinitProvider
from cdktf_cdktf_provider_local.data_local_file import DataLocalFile
from cdktf_cdktf_provider_local.file import File
from cdktf_cdktf_provider_local.provider import LocalProvider
from cdktf_cdktf_provider_null.provider import NullProvider as NullTerraformProvider
from cdktf_cdktf_provider_null.resource import Resource
from cloud_init_gen import CloudInitDoc
from constructs import Construct

from timestep.config import CloudInstanceProvider, Settings


class CloudInitConfigConstruct(Construct):
    def __init__(self, scope: Construct, id: str, config: Settings) -> None:
        super().__init__(scope, id)

        # username = "ubuntu"  # TODO: use config

        # print(config.value)

        if (
            # config.cloud_instance_provider
            # config.string_value
            config.cloud_instance_provider
            == CloudInstanceProvider.MULTIPASS
        ):
            cloud_init_config_provider = LocalProvider(
                id="cloud_init_config_provider",
                scope=scope,
                alias=None,
            )

        else:
            cloud_init_config_provider = CloudinitProvider(
                scope=scope,
                id="cloud_init_config_provider",
                alias=None,
            )

        # if not config.ssh_public_key
        #     "ssh_public_key", None
        # ) or not config.secrets.get_secret_value().get("ssh_private_key", None):
        #     raise Exception("SSH credentials not found")

        cloud_cfg = dict(
            disable_root=True,
            package_reboot_if_required=True,
            package_update=True,
            package_upgrade=True,
            packages=[
                "build-essential",
                "ca-certificates-java",
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
            runcmd=[
                "sed -i -E '/^#?PermitRootLogin/s/^.*$/PermitRootLogin no/' /etc/ssh/sshd_config",  # noqa: E501
                f"sed -i -e '$aAllowUsers {config.cloud_instance_user}' /etc/ssh/sshd_config",  # noqa: E501
                "service ssh restart",
                "curl -sLS https://get.arkade.dev | sudo sh",
                [
                    "runuser",
                    "-l",
                    config.cloud_instance_user,
                    "-c",
                    'echo "\nexport PATH=\\$HOME/.arkade/bin:\\$PATH" >> $HOME/.bashrc',  # noqa: E501
                ],
                # [
                #     "runuser",
                #     "-l",
                #     config.cloud_instance_user,
                #     "-c",
                #     "arkade get caddy k3sup krew",
                # ],  # noqa: E501
                [
                    "runuser",
                    "-l",
                    config.cloud_instance_user,
                    "-c",
                    "arkade get k3sup",
                ],  # noqa: E501
                # [
                #     "runuser",
                #     "-l",
                #     config.cloud_instance_user,
                #     "-c",
                #     'echo "\nexport PATH=\\$HOME/.krew/bin:\\$PATH" >> $HOME/.bashrc',  # noqa: E501
                # ],
                [
                    "runuser",
                    "-l",
                    config.cloud_instance_user,
                    "-c",
                    f"""$HOME/.arkade/bin/k3sup install \
--context {config.kubecontext} \
--k3s-extra-args '--disable traefik' \
--local \
--user {config.cloud_instance_user}""",
                ],
                #                 [
                #                     "runuser",
                #                     "-l",
                #                     config.cloud_instance_user,
                #                     "-c",
                #                     f"""$HOME/.arkade/bin/k3sup install \
                # --context {config.kubecontext} \
                # --local \
                # --user {config.cloud_instance_user}""",
                #                 ],
                #                 [
                #                     "runuser",
                #                     "-l",
                #                     username,
                #                     "-c",
                #                     f"""$HOME/.arkade/bin/k3sup install \
                # --context {config.kubecontext} \
                # --local \
                # --user {username}""",
                #                 ],
                # [
                #     "runuser",
                #     "-l",
                #     config.cloud_instance_user,
                #     "-c",
                #     "$HOME/.arkade/bin/krew install kvaps/build",
                # ],
                # [
                #     "runuser",
                #     "-l",
                #     config.cloud_instance_user,
                #     "-c",
                #     f"$HOME/.arkade/bin/mkcert --install registry.{config.primary_domain_name}",  # noqa: E501
                # ],
                # [
                #     "runuser",
                #     "-l",
                #     config.cloud_instance_user,
                #     "-c",
                #     f"sudo kubectl --kubeconfig /home/{config.cloud_instance_user}/kubeconfig create secret tls registry.{config.primary_domain_name}-tls --key /home/{config.cloud_instance_user}/registry.{config.primary_domain_name}-key.pem --cert /home/{config.cloud_instance_user}/registry.{config.primary_domain_name}.pem",  # noqa: E501
                # ],
                # [
                #     "runuser",
                #     "-l",
                #     username,
                #     "-c",
                #     f"sudo arkade install --kubeconfig /home/{username}/kubeconfig docker-registry --password password --set app.kubernetes.io/managed-by=Helm --set meta.helm.sh/release-name=docker-registry --set meta.helm.sh/release-namespace=default --set persistence.enabled=true --username admin"  # noqa: E501
                # ],
                # [
                #     "runuser",
                #     "-l",
                #     username,
                #     "-c",
                #     f"sudo kubectl -n default create secret generic supabase-jwt --from-literal=anonKey='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.ewogICAgInJvbGUiOiAiYW5vbiIsCiAgICAiaXNzIjogInN1cGFiYXNlIiwKICAgICJpYXQiOiAxNjc1NDAwNDAwLAogICAgImV4cCI6IDE4MzMxNjY4MDAKfQ.ztuiBzjaVoFHmoljUXWmnuDN6QU2WgJICeqwyzyZO88' --from-literal=serviceKey='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.ewogICAgInJvbGUiOiAic2VydmljZV9yb2xlIiwKICAgICJpc3MiOiAic3VwYWJhc2UiLAogICAgImlhdCI6IDE2NzU0MDA0MDAsCiAgICAiZXhwIjogMTgzMzE2NjgwMAp9.qNsmXzz4tG7eqJPh1Y58DbtIlJBauwpqx39UF-MwM8k' --from-literal=secret='abcdefghijklmnopqrstuvwxyz123456'"  # noqa: E501, F541
                # ],
                # [
                #     "runuser",
                #     "-l",
                #     username,
                #     "-c",
                #     f"sudo kubectl -n default create secret generic supabase-smtp --from-literal=username='m@mjschock.com' --from-literal=password='password'"  # noqa: F541, E501
                # ],
                # [
                #     "runuser",
                #     "-l",
                #     username,
                #     "-c",
                #     f"sudo kubectl -n default create secret generic supabase-db --from-literal=username='postgres' --from-literal=password='postgres'"  # noqa: E501, F541
                # ],
                # [
                #     "runuser",
                #     "-l",
                #     username,
                #     "-c",
                #     f"sudo arkade install --kubeconfig /home/{username}/kubeconfig ingress-nginx",  # noqa: E501
                # ],
                # [
                #     "runuser",
                #     "-l",
                #     username,
                #     "-c",
                #     f"sudo arkade install --kubeconfig /home/{username}/kubeconfig chart --namespace caddy-system --repo-name caddyserver/caddy-ingress-controller --repo-url https://caddyserver.github.io/ingress/ --set ingressController.config.acmeCA=https://acme-staging-v02.api.letsencrypt.org/directory --set ingressController.config.debug=true --set ingressController.config.email=m@mjschock.com --set ingressController.config.onDemandTLS=true",  # noqa: E501
                # ],
                # [
                #     "runuser",
                #     "-l",
                #     config.cloud_instance_user,
                #     "-c",
                #     f"sudo arkade install --kubeconfig /home/{config.cloud_instance_user}/kubeconfig cert-manager",  # noqa: E501
                # ],
                [
                    "runuser",
                    "-l",
                    config.cloud_instance_user,
                    "-c",
                    f"sudo kubectl --kubeconfig /home/{config.cloud_instance_user}/kubeconfig create secret docker-registry regcred --docker-server={config.docker_registry_server} --docker-username={config.docker_registry_username} --docker-password={config.docker_registry_password.get_secret_value()} --docker-email={config.docker_registry_email}",  # noqa: E501
                ],
                # [
                #     "runuser",
                #     "-l",
                #     username,
                #     "-c",
                #     f"sudo arkade install --kubeconfig /home/{username}/kubeconfig docker-registry",  # noqa: E501
                # ],
                # [
                #     "runuser",
                #     "-l",
                #     username,
                #     "-c",
                # f"sudo arkade install --kubeconfig /home/{username}/kubeconfig docker-registry --password password --set app.kubernetes.io/managed-by=Helm --set ingress.annotations.cert-manager.io/cluster-issuer=letsencrypt-staging --set ingress.annotations.kubernetes.io/ingress.class=traefik-internal --set ingress.className=traefik-internal --set ingress.enabled=true --set ingress.hosts[0]=registry.{config.variables.get('primary_domain_name')} --set meta.helm.sh/release-name=docker-registry --set meta.helm.sh/release-namespace=default --set persistence.enabled=true --username admin --set ingress.tls="  # noqa: E501
                # ],
                # [
                #     "runuser",
                #     "-l",
                #     username,
                #     "-c",
                #     f"sudo arkade install --kubeconfig /home/{username}/kubeconfig docker-registry --password password --set app.kubernetes.io/managed-by=Helm --set ingress.annotations.cert-manager.io/cluster-issuer=letsencrypt-staging --set ingress.annotations.kubernetes.io/ingress.class=traefik-internal --set ingress.className=traefik-internal --set meta.helm.sh/release-name=docker-registry --set meta.helm.sh/release-namespace=default --set persistence.enabled=true --username admin"  # noqa: E501
                # ],
                # [
                #     "runuser",
                #     "-l",
                #     username,
                #     "-c",
                #     f"sudo arkade install --kubeconfig /home/{username}/kubeconfig docker-registry --password password --set app.kubernetes.io/managed-by=Helm --set ingress.annotations.cert-manager.io/cluster-issuer=letsencrypt-staging --set ingress.annotations.kubernetes.io/ingress.class=caddy --set ingress.className=caddy --set meta.helm.sh/release-name=docker-registry --set meta.helm.sh/release-namespace=default --set persistence.enabled=true --username admin"  # noqa: E501
                # ],
                # [
                #     "runuser",
                #     "-l",
                #     username,
                #     "-c",
                #     f"sudo arkade install --kubeconfig /home/{username}/kubeconfig chart --repo-name twuni/docker-registry --repo-url https://helm.twun.io --set ingress.annotations.cert-manager.io/cluster-issuer=letsencrypt-staging --set ingress.annotations.kubernetes.io/ingress.class=traefik-internal --set ingress.className=traefik-internal --set ingress.enabled=true --set ingress.hosts[0]=registry.{config.variables.get('primary_domain_name')} --set persistence.enabled=true --values-file - docker-registry",  # noqa: E501
                # ],
                # [
                #     "runuser",
                #     "-l",
                #     username,
                #     "-c",
                #     f"sudo arkade install --kubeconfig /home/{username}/kubeconfig docker-registry-ingress --ingress-class traefik-internal --domain registry.{config.variables.get('primary_domain_name')} --email agent@{config.variables.get('primary_domain_name')} --staging",  # noqa: E501
                # ],
                # [
                #     "runuser",
                #     "-l",
                #     username,
                #     "-c",
                #     f"sudo arkade install --kubeconfig /home/{username}/kubeconfig docker-registry-ingress --ingress-class caddy --domain registry.{config.variables.get('primary_domain_name')} --email m@mjschock.com --staging",  # noqa: E501
                # ],
            ],
            users=[
                "default",
                {
                    "groups": "sudo",
                    "name": config.cloud_instance_user,
                    "shell": "/bin/bash",
                    "ssh_authorized_keys": [
                        # config.variables.get("ssh_public_key").strip(),
                        config.ssh_public_key.strip(),
                    ],
                    "sudo": "ALL=(ALL) NOPASSWD:ALL",
                },
            ],
            #             write_files=[
            #                 {
            #                     "path": "/etc/rancher/k3s/registries.yaml",
            #                     "content": f"""mirrors:
            #   docker.io:
            #     endpoint:
            #       - "https://registry.{config.primary_domain_name}:5000"
            # configs:
            #   "registry.{config.primary_domain_name}:5000":
            #     auth:
            #         password: password
            #         username: user
            #     tls:
            #         ca_file: /home/{config.cloud_instance_user}/.local/share/mkcert/rootCA.pem  # noqa: E501
            #         cert_file: /home/{config.cloud_instance_user}/registry.{config.primary_domain_name}.pem  # noqa: E501
            #         key_file: /home/{config.cloud_instance_user}/registry.{config.primary_domain_name}-key.pem  # noqa: E501
            # """
            #                 },
            #             ],
        )

        user_data = CloudInitDoc()
        user_data.add(cloud_cfg)

        if config.cloud_instance_provider == CloudInstanceProvider.MULTIPASS:
            cloud_init_config_resource = File(
                id="cloud_init_config_resource",
                content=user_data.render(),
                filename="cloud-config.yaml",
                provider=cloud_init_config_provider,
                scope=scope,
            )

        else:
            null_provider = NullTerraformProvider(
                id="null_provider",
                scope=scope,
            )
            cloud_init_config_resource = Resource(
                id="cloud_init_config_resource",
                provider=null_provider,
                scope=scope,
                triggers={
                    "content": user_data.render(),
                },
            )

        if config.cloud_instance_provider == CloudInstanceProvider.MULTIPASS:
            cloud_init_config_data_source = DataLocalFile(
                id="cloud_init_config_data_source",
                filename=cloud_init_config_resource.filename,
                scope=scope,
                provider=cloud_init_config_resource.provider,
            )

        else:
            data_cloud_init_config_part = DataCloudinitConfigPart(
                content=cloud_init_config_resource.triggers_input["content"],
                content_type="text/cloud-config",
                filename="cloud-config.yaml",
                merge_type=None,
            )

            cloud_init_config_data_source = DataCloudinitConfig(
                scope=scope,
                id="cloud_init_config_data_source",
                base64_encode=False,
                boundary=None,
                gzip=False,
                part=[
                    data_cloud_init_config_part,
                ],
                connection=None,
                count=None,
                depends_on=None,
                for_each=None,
                lifecycle=None,
                provider=cloud_init_config_provider,
                provisioners=None,
            )

        cloud_init_config_outputs = {}

        if config.cloud_instance_provider == CloudInstanceProvider.MULTIPASS:
            cloud_init_config_outputs["cloudinit_file"] = TerraformOutput(
                scope=scope,
                id="cloud_init_config_outputs_cloudinit_file",
                value=cloud_init_config_data_source.filename,
            )

        else:
            cloud_init_config_outputs["user_data"] = TerraformOutput(
                scope=scope,
                id="cloud_init_config_outputs_user_data",
                value=cloud_init_config_data_source.rendered,
            )

        self.data_source: TerraformDataSource[
            DataLocalFile | DataCloudinitConfig
        ] = cloud_init_config_data_source
