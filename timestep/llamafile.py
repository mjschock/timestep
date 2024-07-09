import os

import typer

from timestep.utils import download_with_progress_bar, start_shell_script, stop_shell_script

typer_app = typer.Typer()

default_llamafile_filename = "TinyLlama-1.1B-Chat-v1.0.F16.llamafile"
default_llamafile_url = f"https://huggingface.co/Mozilla/TinyLlama-1.1B-Chat-v1.0-llamafile/resolve/main/{default_llamafile_filename}?download=true"


@typer_app.command()
def load(
    llamafile_path=f"./models/{default_llamafile_filename}",
    host='0.0.0.0',
    public_path='/zip/llama.cpp/server/public',
    port=8080,
):
    """
    Load a model
    """
    typer.echo(f"Loading model...")

    if os.path.basename(llamafile_path) == default_llamafile_filename and not os.path.exists(llamafile_path):
        os.makedirs(os.path.dirname(llamafile_path))
        download_with_progress_bar(default_llamafile_url, llamafile_path)

    assert os.path.exists(llamafile_path)

    process = start_shell_script(
        llamafile_path,
        '--host', host,
        '--path', public_path,
        '--port', f'{port}',
    )

    typer.echo(f"... loaded model with PID: {process.pid}.")


@typer_app.command()
def unload(pid: int):
    """
    Unload a model by PID
    """
    typer.echo("Unloading model...")

    stop_shell_script(pid)

    typer.echo(f"... unloaded model with PID: {pid}.")


if __name__ == "__main__":
    typer_app()
