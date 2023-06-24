import os
from cdktf import App, TerraformStack, TerraformOutput, RemoteBackend, LocalBackend
from constructs import Construct
from dotenv import dotenv_values, load_dotenv
from prefect import flow, get_run_logger
from prefect.futures import PrefectFuture
from prefect.task_runners import SequentialTaskRunner
from timestep.conf import MainConfig
from timestep.infra.stacks.base.stack import BaseStack

@flow(
    # task_runner=SequentialTaskRunner(),
)
def main(config: MainConfig) -> None:
    logger = get_run_logger()
    logger.info(f"config: {config}")

    # if not os.path.exists(config.CDKTF_OUTDIR):
    #     logger.info(f"Creating {config.CDKTF_OUTDIR}")
    #     os.makedirs(os.path.dirname(config.CDKTF_OUTDIR), exist_ok=True)

    app: App = App()

    stack: TerraformStack = BaseStack(app, config.STACK_ID, config=config)
    backend: LocalBackend = LocalBackend(
        scope=stack,
        path=f"terraform.{config.STACK_ID}.tfstate",
        workspace_dir=None,
    )

    app.synth()

    # outputs_future: PrefectFuture[dict[str, TerraformOutput]] = stack.get_outputs()
    # outputs: dict[str, TerraformOutput] = outputs_future.result()
    # logger.info(f"outputs: {outputs}")

    tf = stack.to_terraform()
    logger.info(f"tf: {tf}")


if __name__ == "__main__":
    # config: dict[str, str] = dotenv_values(verbose=True)
    config: dict[str, str] = load_dotenv(override=False)
    print(f"config: {config}")

    main(config=config)
