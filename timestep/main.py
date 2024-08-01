import inspect
import os

import typer
from sqlmodel import SQLModel, create_engine

from timestep.server import main as timestep_serve
from timestep.worker import main as timestep_train

# TODO: move these to the config/env
app_dir = typer.get_app_dir(__package__)
default_llamafile_filename = "TinyLlama-1.1B-Chat-v1.0.F16.llamafile"
default_llamafile_url = f"https://huggingface.co/Mozilla/TinyLlama-1.1B-Chat-v1.0-llamafile/resolve/main/{default_llamafile_filename}?download=true"

os.makedirs(f"{app_dir}/data", exist_ok=True)
os.makedirs(f"{app_dir}/models", exist_ok=True)
os.makedirs(f"{app_dir}/work", exist_ok=True)

engine = create_engine(f"sqlite:///{app_dir}/database.db")
SQLModel.metadata.create_all(
    bind=engine,
    checkfirst=True,
    tables=None,
)


def get_help_message():
    is_readme_context = inspect.getmodule(inspect.stack()[1][0]) is None

    return """
Timestep AI CLI - free, local-first, open-source AI
""" + (
        """
**Setup**:

### Development

```console
$ python3 -m pip install --upgrade pip
$ python3 -m pip install --user pipx
$ python3 -m pipx ensurepath
$ pipx install poetry==1.8.3
$ cp .env.example .env
$ direnv allow # See https://direnv.net/#getting-started to install direnv on your platform
$ make
```

### Library

```console
$ python3 -m pip install --upgrade pip
$ python3 -m pip install --user pipx
$ python3 -m pipx ensurepath
$ pipx install timestep
```

**Pre-requisites**:

```console
$ prefect server start
$ prefect worker start --pool "default"
```
"""
        if is_readme_context
        else ""
    )


typer_app = typer.Typer(
    help=get_help_message(),
    no_args_is_help=True,
)

# typer_app.add_typer(llamafile_typer_app, name="up")


@typer_app.callback()
def main():
    f"""
    Timestep AI CLI
    """


@typer_app.command()
def evals():
    """
    Run evaluations.
    """
    typer.echo("Running evaluations...")

    raise NotImplementedError


@typer_app.command()
def serve(
    # host="0.0.0.0",
    # llamafile_path=f"./models/{default_llamafile_filename}", # TODO: namespace under llamafile, include port, etc.
    # port=8080,
):
    """
    Run serving.
    """
    typer.echo("Running serving...")

    timestep_serve(
        # host=host,
        # llamafile_path=llamafile_path,
        # port=port,
    )


@typer_app.command()
def train():
    """
    Run training.
    """
    typer.echo("Running training...")

    timestep_train()


if __name__ == "__main__":
    typer_app()
