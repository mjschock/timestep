import inspect
import os
from pathlib import Path

import typer

from prefect import deploy, flow
from timestep.server import main as timestep_serve
from timestep.worker import agent_flow, main as timestep_train

app_dir = typer.get_app_dir(__package__)
os.makedirs(f"{app_dir}/data", exist_ok=True)
os.makedirs(f"{app_dir}/work", exist_ok=True)

def get_help_message():
    is_readme_context = inspect.getmodule(inspect.stack()[1][0]) is None

    return """
Timestep AI CLI - free, local-first, open-source AI
""" + (
        """
**Setup**:

```console
$ prefect server start
$ prefect worker start --pool "default" --work-queue "default"
$ timestep serve
```
"""
        if is_readme_context
        else ""
    )


typer_app = typer.Typer(
    help=get_help_message(),
    no_args_is_help=True,
)


@typer_app.callback()
def main():
    f"""
    Timestep AI CLI

    **Prefect setup**:

    ```console
    $ timestep [OPTIONS] COMMAND [ARGS]...
    ```
    """


@typer_app.command()
def evals():
    """
    Run evaluations.
    """
    typer.echo("Running evaluations...")

    raise NotImplementedError


@typer_app.command()
def serve():
    """
    Run serving.
    """
    typer.echo("Running serving...")

    # deploy(
    #     agent_flow.to_deployment(
    #         # entrypoint_type=
    #         name="agent-flow-deployment",
    #     ),
    #     # image=None,
    #     build=False,
    #     push=False,
    #     work_pool_name="default",
    # )
    # agent_flow.deploy(
    #     name="agent-flow-deployment",
    #     work_pool_name="default",
    # )
    # flow.from_source(
    #     # source="https://github.com/org/repo.git",
    #     entrypoint="timestep/worker.py:agent_flow",
    # ).to_deployment(
    #     name="agent-flow-deployment",
    # )

    agent_flow.from_source(
        source=str(Path(__file__).parent),
        entrypoint="worker.py:agent_flow",
    ).deploy(
        name="agent-flow-deployment",
        # parameters=dict(name="Marvin"),
        # work_pool_name="local",
        work_pool_name="default",
    )

    timestep_serve()


@typer_app.command()
def train():
    """
    Run training.
    """
    typer.echo("Running training...")

    timestep_train()


if __name__ == "__main__":
    typer_app()
