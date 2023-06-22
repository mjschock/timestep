import os
from cdktf import App
from dotenv import dotenv_values
from prefect import flow, get_run_logger
from prefect.task_runners import SequentialTaskRunner
from timestep.conf import AppConfig

from timestep.infra.stacks.base.stack import (
    BaseTerraformStack,
)

@flow(
    task_runner=SequentialTaskRunner(),
)
def main(config: AppConfig) -> None:
    logger = get_run_logger()

    if not os.path.exists(config.CDKTF_OUTDIR):
        os.makedirs(os.path.dirname(config.CDKTF_OUTDIR), exist_ok=True)

    app = App()

    tf_stack = BaseTerraformStack(
        scope=app, id=f"{config.DOMAIN}-tf-stack", config=config
    )

    app.synth()


if __name__ == "__main__":
    config: dict[str, str] = dotenv_values(verbose=True)

    main(config=config)
