import inspect

import typer

from timestep.config import settings
from timestep.server import main as timestep_serve


def get_help_message():
    is_readme_context = inspect.getmodule(inspect.stack()[1][0]) is None

    return """
Timestep AI CLI - free, local-first, open-source AI
""" + (
        """
**Development Setup**:

```console
$ python3 -m pip install --upgrade pip
$ python3 -m pip install --user pipx
$ python3 -m pipx ensurepath
$ pipx install poetry==1.8.3
$ cp .env.example .env
$ direnv allow # See https://direnv.net/#getting-started
$ make
$ timestep up --dev
```

**Library Setup**:

```console
$ python3 -m pip install --upgrade pip
$ python3 -m pip install --user pipx
$ python3 -m pipx ensurepath
$ pipx install timestep
$ timestep up
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
    """


@typer_app.command()
def up(
    dev: bool = False,
    host: str = "0.0.0.0",
    # llamafile_path=f"./models/{default_llamafile_filename}", # TODO: namespace under llamafile, include port, etc.
    port: int = 8000,
):
    """
    Start up the Timestep AI platform.
    """

    typer.echo(f"Starting up the Timestep AI platform at http://{host}:{port}...")

    timestep_serve(
        dev=dev,
        host=host,
        # llamafile_path=llamafile_path,
        port=port,
    )


if __name__ == "__main__":
    typer_app()
