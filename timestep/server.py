import json
import os
import signal
import subprocess
import urllib.request
from contextlib import asynccontextmanager
from enum import Enum
from pathlib import Path

import uvicorn
from connexion import AsyncApp, ConnexionMiddleware
from connexion.options import SwaggerUIOptions
from fastapi import FastAPI, Request
from prefect import flow
from tqdm import tqdm

from timestep.api.openai.v1.controllers.completions_controller import create_completion
from timestep.config import Settings

settings = Settings()

connexion_app = AsyncApp(import_name=__name__)
default_hf_repo_id = settings.default_hf_repo_id
default_llamafile_filename = settings.default_llamafile_filename
default_llamafile_host = settings.default_llamafile_host
default_llamafile_port = settings.default_llamafile_port
default_llamafile_url = f"https://huggingface.co/{default_hf_repo_id}/resolve/main/{default_llamafile_filename}?download=true"
local_llamafile_path = (
    f"{settings.app_dir}/models/{default_hf_repo_id}/{default_llamafile_filename}"
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    agent_flow = await flow.from_source(
        source=str(Path(__file__).parent),
        entrypoint="worker.py:agent_flow",
    )

    try:
        await agent_flow.deploy(
            name="agent-flow-deployment",
            # parameters=dict(name="Marvin"),
            # work_pool_name="local",
            work_pool_name="default",
        )

    except Exception as e:
        print(
            f"{e} - Recommendation: `prefect server start` and `prefect worker start --pool default`"
        )

    if os.path.basename(
        local_llamafile_path
    ) == default_llamafile_filename and not os.path.exists(local_llamafile_path):
        os.makedirs(os.path.dirname(local_llamafile_path), exist_ok=True)
        download_with_progress_bar(default_llamafile_url, local_llamafile_path)

    assert os.path.exists(local_llamafile_path)

    # if local_llamafile_path is not executable, make it executable
    if not os.access(local_llamafile_path, os.X_OK):
        os.chmod(local_llamafile_path, 0o755)

    process = start_shell_script(
        local_llamafile_path,
        "--host",
        f"{default_llamafile_host}",
        "--nobrowser",
        "--path",
        "/zip/llama.cpp/server/public",
        "--port",
        f"{default_llamafile_port}",
        "--temp",
        "0.0",
    )

    yield

    print(f"Terminating llamafile with PID: {process.pid}")
    process.terminate()


fastapi_app = FastAPI(
    lifespan=lifespan,
    # servers= # TODO: add server for testing?
)

connexion_app.add_api(
    "api/ap/v1/openapi/openapi.yaml",
    pythonic_params=True,
    resolver_error=501,
    swagger_ui_options=SwaggerUIOptions(serve_spec=False),
)

connexion_app.add_api(
    "api/openai/v1/openapi/openapi.yaml",
    base_path="/openai/v1",
    pythonic_params=True,
    resolver_error=500,
)

fastapi_app.mount("/api", ConnexionMiddleware(app=connexion_app, import_name=__name__))


class Engine(str, Enum):
    copilot_codex = "copilot-codex"


@fastapi_app.get("/v1/engines")
async def list_engines():
    # return [engine.value for engine in Engine]
    return {
        "data": [
            {
                "id": Engine.copilot_codex,
                "name": "Copilot Codex",
                "description": "OpenAI's Codex model, formerly known as GitHub Copilot",
            }
        ]
    }


@fastapi_app.post("/v1/engines/{engine}/completions")
async def create_code_completion(engine: Engine, request: Request):
    print(
        f"=== {__name__}.create_code_completion(engine: Engine, request: Request) ==="
    )
    print(f"engine: {engine}")
    print(f"request: {request}")

    if engine == Engine.copilot_codex:
        try:
            body = await request.json()

        except json.decoder.JSONDecodeError as e:
            print(f"Error: {e}")
            body = {
                "model": "LLaMA_CPP",
                "prompt": "int main() {",
            }

        # body["model"] = "LLaMA_CPP"

        return await create_completion(body, token_info={}, user=None)

    else:
        raise NotImplementedError("Not implemented")

    # @fastapi_app.get("/v2/models/{model_id}")
    # async def create_code_completion(model_id: str, request: Request):
    #     # model_info = models_service.retrieve_model(model_id, token_info, user)
    #     model_info = model_service.retrieve_model(model_id)

    #     print("model_info: ", model_info)

    #     return model_info


def download_with_progress_bar(
    url, filename
):  # TODO: just use from huggingface_hub import hf_hub_download and hf_hub_upload
    # Extract the basename of the file
    base_filename = os.path.basename(filename)

    # Define the reporthook function
    def reporthook(block_num, block_size, total_size):
        if pbar.total is None:
            pbar.total = total_size

        pbar.update(block_size)

    # Create a tqdm progress bar instance with a custom bar_format
    pbar = tqdm(
        unit="B",
        unit_scale=True,
        miniters=1,
        desc=base_filename,
        bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [{percentage:.0f}%]",
    )

    # Use urlretrieve to download the file with the reporthook
    urllib.request.urlretrieve(url, filename, reporthook)

    # Close the progress bar
    pbar.close()


def start_shell_script(file_path, *args):
    try:
        # Construct the command with the script and the additional arguments
        command = ["sh", file_path] + list(args)

        # Open the script and redirect its stdout and stderr to log files for debugging
        with open("script_output.log", "w") as out, open(
            "script_error.log", "w"
        ) as err:
            process = subprocess.Popen(
                command,
                stdout=out,
                stderr=err,
                preexec_fn=os.setpgrp,  # Start the process in a new process group
            )

        print(f"Started the file: {file_path} with PID: {process.pid}")

        return process

    except FileNotFoundError:
        print(f"File not found: {file_path}")

    except Exception as e:
        print(f"An error occurred: {e}")


def main(*args, **kwargs):
    print(f"=== {__name__}.main(*args, **kwargs) ===")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")

    cwd = os.getcwd()
    print(f"cwd: {cwd}")

    uvicorn.run(
        f"{__name__}:fastapi_app",
        host="0.0.0.0",
        log_level="info",
        loop="asyncio",
        port=8000,
        reload=True,
        reload_dirs=[
            f"{os.getcwd()}/timestep",
        ],
        workers=1,
    )


if __name__ == "__main__":
    main()
