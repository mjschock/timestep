from cdktf import App
from omegaconf import DictConfig
import hydra

from timestep.infra.stacks.base.stack import BaseTerraformStack, BaseTerraformStackConfig
from timestep.infra.stacks.kubernetes.stack import KubernetesTerraformStack, KubernetesTerraformStackConfig
# from timestep.infra.stacks.platform.stack import PlatformTerraformStack, PlatformTerraformStackConfig


@hydra.main(config_name="config", config_path="conf", version_base=None)
def main(config: DictConfig) -> None:
    print(f"config: {config}")

    app_name = config.target.app_name
    env = config.target.env
    id = f"{app_name}-{env}"

    app = App()

    base_tf_stack_config = BaseTerraformStackConfig(**config)
    base_tf_stack = BaseTerraformStack(scope=app, id=f"{app_name}-{env}-base-stack", config=base_tf_stack_config)

    print(f"base_tf_stack.outputs: {base_tf_stack.outputs}")

    # # TODO: Run prefect shell script to load kubeconfig from cloud instance
    k8s_tf_stack_config = KubernetesTerraformStackConfig(**config)
    k8s_tf_stack = KubernetesTerraformStack(scope=app, id=f"{app_name}-{env}-k8s-stack", config=k8s_tf_stack_config)

    # platform_tf_stack_config = PlatformTerraformStackConfig(k8s_tf_stack=k8s_tf_stack)
    # platform_tf_stack = PlatformTerraformStack(scope=app, id=f"{app_name}-{env}-platform-stack", config=platform_tf_stack_config)

    app.synth()


if __name__ == "__main__":
    main()
