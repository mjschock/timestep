import inspect
import os

import typer

from timestep.server import main as timestep_serve
from timestep.worker import main as timestep_train

app_dir = typer.get_app_dir(__package__)
os.makedirs(app_dir, exist_ok=True)


def get_help_message():
    is_readme_context = inspect.getmodule(inspect.stack()[1][0]) is None

    return """
Timestep AI CLI - free, local-first, open-source AI
""" + (
        """
**Setup**:

```console
$ prefect server start
$ prefect worker start --pool "default"
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
