from cdktf import App

from timestep.config import Settings

# from timestep.config import (
# AppConfig,
# SecureShellCredentials,
# )
from timestep.infra.stacks.main.stack import MainStack


# def main(config: Settings) -> None:
def main() -> None:
    config = Settings()

    app: App = App(
        context={
            "allowSepCharsInLogicalIds": "true",
            "excludeStackIdFromLogicalIds": "true",
        },
        # outdir=DIST_PATH,
        outdir=config.cdktf_outdir,
        skip_validation=False,
        stack_traces=True,
    )

    assert app.node.get_context("allowSepCharsInLogicalIds") == "true"
    assert app.node.get_context("excludeStackIdFromLogicalIds") == "true"

    # cpus = TerraformVariable(
    #     scope=app,
    #     id="cpus",
    #     type=VariableType.NUMBER,
    #     default=CPUS,
    # )

    # disk_size_gb = TerraformVariable(
    #     scope=app,
    #     id="disk_size_gb",
    #     type=VariableType.NUMBER,
    #     default=DISK_SIZE_GB,
    # )

    # memory_size_gb = TerraformVariable(
    #     scope=app,
    #     id="memory_size_gb",
    #     type=VariableType.NUMBER,
    #     default=MEMORY_SIZE_GB,
    # )

    # do_droplet_image = TerraformVariable(
    #     scope=app,
    #     id="do_droplet_image",
    #     type=VariableType.STRING,
    #     default=DO_DROPLET_IMAGE,
    # )

    # do_droplet_region = TerraformVariable(
    #     scope=app,
    #     id="do_droplet_region",
    #     type=VariableType.STRING,
    #     default=DO_DROPLET_REGION,
    # )

    # do_droplet_size = TerraformVariable(
    #     scope=app,
    #     id="do_droplet_size",
    #     type=VariableType.STRING,
    #     default=DO_DROPLET_SIZE,
    # )

    # multipass_instance_cpus = TerraformVariable(
    #     scope=app,
    #     id="multipass_instance_cpus",
    #     type=VariableType.NUMBER,
    #     default=MULTIPASS_INSTANCE_CPUS,
    # )

    # multipass_instance_disk = TerraformVariable(
    #     scope=app,
    #     id="multipass_instance_disk",
    #     type=VariableType.STRING,
    #     default=MULTIPASS_INSTANCE_DISK,
    # )

    # multipass_instance_image = TerraformVariable(
    #     scope=app,
    #     id="multipass_instance_image",
    #     type=VariableType.STRING,
    #     default=MULTIPASS_INSTANCE_IMAGE,
    # )

    # multipass_instance_memory = TerraformVariable(
    #     scope=app,
    #     id="multipass_instance_memory",
    #     type=VariableType.NUMBER,
    #     default=MULTIPASS_INSTANCE_MEMORY,
    # )

    # primary_domain_name = config.get("PRIMARY_DOMAIN_NAME")
    # kubeconfig = f"{DIST_PATH}/stacks/{primary_domain_name}/kube-config.yaml"
    # app_config_block = AppConfig(
    # config = AppConfig(

    # postgres_password = TerraformVariable(
    #     scope=app,
    #     id="postgres_password",
    #     type=VariableType.STRING,
    #     default=config.get("POSTGRESQL_PASSWORD", None),
    #     sensitive=True,
    # )

    # primary_domain_name = TerraformVariable(
    #     scope=app,
    #     id="primary_domain_name",
    #     type=VariableType.STRING,
    #     default=config.get("PRIMARY_DOMAIN_NAME", None),
    #     nullable=False,
    # )

    # main_config = TerraformVariable(
    #     scope=app,
    #     id="main_config",
    #     type=VariableType.MAP,
    #     default={
    #         "public": Var

    #     secrets={
    #         "do_token": config.get("DO_TOKEN", None),
    #         "namecheap_api_key": config.get("NAMECHEAP_API_KEY", None),
    #         "namecheap_api_user": config.get("NAMECHEAP_API_USER", None),
    #         "namecheap_user_name": config.get("NAMECHEAP_USER_NAME", None),
    #         "postgresql_password": config.get("POSTGRESQL_PASSWORD", None),
    #         # "ssh_private_key": ssh_credentials_block.private_key,
    #         "ssh_private_key": config.get("SSH_PRIVATE_KEY", None),
    #         # "tf_api_token": config.get("TF_API_TOKEN", None),
    #     },
    #     variables={
    #         "cdktf_outdir": config.get("CDKTF_OUTPUT", DIST_PATH),
    #         "cloud_instance_name": config.get("CLOUD_INSTANCE_NAME", None),
    #         "cloud_instance_provider": config.get("CLOUD_INSTANCE_PROVIDER", None),
    #         "do_droplet_image": config.get("DO_DROPLET_IMAGE", DO_DROPLET_IMAGE),
    #         "do_droplet_region": config.get("DO_DROPLET_REGION", DO_DROPLET_REGION),
    #         "do_droplet_size": config.get("DO_DROPLET_SIZE", DO_DROPLET_SIZE),
    #         "domain_name_registrar_provider": config.get(
    #             "DOMAIN_NAME_REGISTRAR_PROVIDER", None
    #         ),
    #         # "kubeconfig": kubeconfig,
    #         "kubecontext": config.get("KUBECONTEXT", None),
    #         "multipass_instance_cpus": config.get(
    #             "MULTIPASS_INSTANCE_CPUS", MULTIPASS_INSTANCE_CPUS
    #         ),
    #         "multipass_instance_disk": config.get(
    #             "MULTIPASS_INSTANCE_DISK", MULTIPASS_INSTANCE_DISK
    #         ),
    #         "multipass_instance_image": config.get(
    #             "MULTIPASS_INSTANCE_IMAGE", MULTIPASS_INSTANCE_IMAGE
    #         ),
    #         "multipass_instance_memory": config.get(
    #             "MULTIPASS_INSTANCE_MEMORY", MULTIPASS_INSTANCE_MEMORY
    #         ),
    #         # "namecheap_client_ip": config.get("NAMECHEAP_CLIENT_IP", None),
    #         "primary_domain_name": config.get("PRIMARY_DOMAIN_NAME", None),
    #         # "ssh_public_key": ssh_credentials_block.public_key,
    #         "ssh_public_key": config.get("SSH_PUBLIC_KEY", None),
    #         # "tf_hostname": config.get("TF_HOSTNAME", None),
    #         # "tf_organization": config.get("TF_ORGANIZATION", None),
    #         # "tf_workspace": config.get("TF_WORKSPACE", None),
    #     },
    # )

    # public_variables = TerraformVariable(
    #     scope=app,
    #     id="public_variables",
    #     # type=VariableType.MAP,
    #     type=VariableType.object({
    #         "primary_domain_name": VariableType.STRING,
    #     }),
    #     nullable=False,
    #     default={
    #         "primary_domain_name": primary_domain_name,
    #     },
    # )

    MainStack(
        # config=public_variables,
        config=config,
        id=config.primary_domain_name,
        scope=app,
        # id=config.primary_domain_name,
        # id=primary_domain_name.string_value,
        # id=primary_domain_name,
        # id=config.get("PRIMARY_DOMAIN_NAME", None),
    )

    app.synth()


if __name__ == "__main__":
    # external_data: dict[str, str] = {
    #     **dotenv_values(verbose=True),
    #     **os.environ,  # override loaded values with environment variables
    # }

    # try:
    #     ssh_credentials_block = SecureShellCredentials.load("ssh-credentials")

    # except ValueError:
    #     ssh_credentials_block = SecureShellCredentials(
    #         public_key=config.get("SSH_PUBLIC_KEY", None),
    #         private_key=config.get("SSH_PRIVATE_KEY", None),
    #     )

    #     ssh_credentials_block.save(
    #         name="ssh-credentials",
    #         overwrite=False,
    #     )

    # main_config = Settings(**external_data)

    # main(config=main_config)
    main()
