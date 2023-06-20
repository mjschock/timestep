import os
from cdktf import App
from dotenv import dotenv_values
from prefect import flow, get_run_logger
from prefect.task_runners import SequentialTaskRunner
from timestep.conf import AppConfig

from timestep.infra.stacks.base.stack import (
    BaseTerraformStack,
    # BaseTerraformStackConfig,
)

@flow(
    task_runner=SequentialTaskRunner(),
)
def main(config: AppConfig) -> None:
    logger = get_run_logger()

    if not os.path.exists(config.CDKTF_OUTDIR):
        os.makedirs(os.path.dirname(config.CDKTF_OUTDIR), exist_ok=True)

    app = App()

    # base_tf_stack_config = BaseTerraformStackConfig(**config)
    base_tf_stack = BaseTerraformStack(
        # scope=app, id=f"{config.DOMAIN}-base-stack", config=base_tf_stack_config
        scope=app, id=f"{config.DOMAIN}-base-stack", config=config
    )

    # k8s_tf_stack_config = KubernetesTerraformStackConfig(**config)
    # k8s_tf_stack = KubernetesTerraformStack(
    #     scope=app, id=f"{app_name}-{env}-k8s-stack", config=k8s_tf_stack_config
    # )

    # platform_tf_stack_config = PlatformTerraformStackConfig(**config)
    # platform_tf_stack = PlatformTerraformStack(
    #     scope=app,
    #     id=f"{app_name}-{env}-platform-stack",
    #     config=platform_tf_stack_config,
    # )

    app.synth()


if __name__ == "__main__":
    config: dict[str, str] = dotenv_values(verbose=True)

    main(config=config)
