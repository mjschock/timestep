import atexit
import json
import os
import signal
import subprocess
import time
import urllib.request
from contextlib import asynccontextmanager
from enum import Enum
from pathlib import Path

import uvicorn
from connexion import AsyncApp, ConnexionMiddleware
from connexion.options import SwaggerUIOptions
from fastapi import FastAPI, Request
from filelock import SoftFileLock, Timeout
from huggingface_hub import hf_hub_download
from prefect import flow
from prefect.server.api.server import SubprocessASGIServer
from prefect.settings import (
    PREFECT_DEFAULT_WORK_POOL_NAME,
    PREFECT_SERVER_EPHEMERAL_STARTUP_TIMEOUT_SECONDS,
)
from prefect.utilities.processutils import get_sys_executable
from prefect.workers.process import ProcessWorker
from tqdm import tqdm

from timestep.api.openai.v1.controllers.completions_controller import create_completion
from timestep.config import settings
from timestep.database import create_db_and_tables

app_dir = settings.app_dir
connexion_app = AsyncApp(import_name=__name__)
default_hf_repo_id = settings.default_hf_repo_id
# default_llamafile_filename = settings.default_llamafile_filename
default_llamafile_host = settings.default_llamafile_host
default_llamafile_port = settings.default_llamafile_port
# default_llamafile_url = f"https://huggingface.co/{default_hf_repo_id}/resolve/main/{default_llamafile_filename}?download=true"
default_model_filename = settings.default_model_filename
default_multimodal_model_projector_filename = (
    settings.default_multimodal_model_projector_filename
)
# local_llamafile_path = (
#     f"{app_dir}/models/{default_hf_repo_id}/{default_llamafile_filename}"
# )
local_model_path = f"{app_dir}/models/{default_hf_repo_id}/{default_model_filename}"
local_multimodal_model_projector_path = f"{app_dir}/models/{default_hf_repo_id}/{default_multimodal_model_projector_filename}"


@asynccontextmanager
async def lifespan(app: FastAPI):
    lock_file = Path(f"{app_dir}/data/data.json")
    subprocess_manager = SubprocessManager()

    try:
        soft_lock = SoftFileLock(
            f"{str(lock_file)}.lock",
            is_singleton=True,
            thread_local=False,
            timeout=120,
        )

        worker_count = int(os.getenv("PYTEST_XDIST_WORKER_COUNT", 1))
        worker_name = os.getenv("PYTEST_XDIST_WORKER", "master")
        worker_pid = os.getpid()

        with soft_lock.acquire():
            create_db_and_tables()

            if lock_file.is_file():
                data = json.loads(lock_file.read_text())

                data["timestep"][worker_name] = {
                    "pid": worker_pid,
                    "status": "running",
                }

                lock_file.write_text(json.dumps(data))

            else:
                # create_db_and_tables()

                llamafile_pid = start_llamafile(subprocess_manager)

                prefect_server_pid = subprocess_manager.start(
                    args=[
                        "sh",
                        "-c",
                        f"PREFECT_API_URL={settings.prefect_api_url} prefect server start",
                    ],
                    name="prefect.server",
                )

                # prefect_server = SubprocessASGIServer(port=4200)
                # prefect_server.start(timeout=30)
                # prefect_server_pid = prefect_server.server_process.pid

                # print(
                #     f"Waiting {PREFECT_SERVER_EPHEMERAL_STARTUP_TIMEOUT_SECONDS.value()} seconds for Prefect server to start..."
                # )
                # time.sleep(PREFECT_SERVER_EPHEMERAL_STARTUP_TIMEOUT_SECONDS.value())
                print(
                    f"Sleeping for {PREFECT_SERVER_EPHEMERAL_STARTUP_TIMEOUT_SECONDS.value()} seconds..."
                )
                time.sleep(PREFECT_SERVER_EPHEMERAL_STARTUP_TIMEOUT_SECONDS.value())

                prefect_worker_pid = subprocess_manager.start(
                    args=[
                        "sh",
                        "-c",
                        f"PREFECT_API_URL={settings.prefect_api_url} prefect worker start --pool 'default' --type 'process'",
                    ],
                    name="prefect.worker.default",
                )

                print(f"Sleeping for 15 seconds...")
                time.sleep(15)

                data = {
                    "llamafiles": {
                        "default": {
                            "pid": llamafile_pid,
                            "status": "running",
                        }
                    },
                    "prefect": {
                        "server": {
                            "pid": prefect_server_pid,
                            "status": "running",
                        },
                        "workers": {
                            "default": {
                                "pid": prefect_worker_pid,
                                "status": "running",
                            }
                        },
                    },
                    "timestep": {
                        worker_name: {
                            "pid": worker_pid,
                            "status": "running",
                        }
                    },
                }

                lock_file.write_text(json.dumps(data))

        # TODO: Filelock doesnt support async, try https://py-filelock.readthedocs.io/en/latest/_modules/filelock/asyncio.html
        try:
            agent_flow = await flow.from_source(
                source=str(Path(__file__).parent),
                entrypoint="worker.py:agent_flow",
            )

            await agent_flow.deploy(
                name="agent-flow-deployment",
                work_pool_name="default",
            )

        except Exception as e:
            print(e)

        yield

        print(f"Exiting {worker_name} worker process with PID: {worker_pid}")

    except Exception as e:
        print(f"An error occurred: {e}; attempting to clean up...")

    finally:
        try:
            with soft_lock.acquire():
                data = json.loads(lock_file.read_text())

                print(f"Stopping {worker_name} worker process with PID: {worker_pid}")
                try:
                    data["timestep"][worker_name]["status"] = "stopped"

                except Exception as e:
                    print(e)

                stopped_workers = [
                    worker
                    for worker in data["timestep"].values()
                    if worker["status"] == "stopped"
                ]

                if len(stopped_workers) >= worker_count:
                    print("stopped_workers: ", stopped_workers)
                    print("worker_count: ", worker_count)

                    for prefect_worker_id, prefect_worker in data["prefect"][
                        "workers"
                    ].items():
                        if prefect_worker["status"] != "stopped":
                            print(
                                f"Stopping Prefect worker {prefect_worker_id} process with PID: {prefect_worker['pid']}"
                            )
                            subprocess_manager.stop(prefect_worker["pid"])

                        else:
                            print(
                                f"Prefect worker {prefect_worker_id} process with PID: {prefect_worker['pid']} already stopped"
                            )

                    if data["prefect"]["server"]["status"] != "stopped":
                        print(
                            f"Stopping Prefect server process with PID: {data['prefect']['server']['pid']}"
                        )
                        subprocess_manager.stop(data["prefect"]["server"]["pid"])

                    else:
                        print(
                            f"Prefect server process with PID: {data['prefect']['server']['pid']} already stopped"
                        )

                    for llamafile_id, llamafile in data["llamafiles"].items():
                        if llamafile["status"] != "stopped":
                            print(
                                f"Stopping llamafile {llamafile_id} process with PID: {llamafile['pid']}"
                            )
                            subprocess_manager.stop(llamafile["pid"])

                        else:
                            print(
                                f"llamafile {llamafile_id} process with PID: {llamafile['pid']} already stopped"
                            )

                    lock_file.unlink()

                else:
                    lock_file.write_text(json.dumps(data))

        except FileNotFoundError as e:
            print(f"An error occurred: {e}")

        except Exception as e:
            print(f"An error occurred in the finally block: {e}")
            raise RuntimeWarning(f"An error occurred in the finally block: {e}")


def start_llamafile(subprocess_manager):
    # if os.path.basename(
    #                 local_llamafile_path
    #             ) == default_llamafile_filename and not os.path.exists(
    #                 local_llamafile_path
    #             ):
    # os.makedirs(os.path.dirname(local_llamafile_path), exist_ok=True)
    # os.makedirs(f"{app_dir}/models/{default_hf_repo_id}", exist_ok=True)
    os.makedirs(os.path.dirname(local_model_path), exist_ok=True)
    # download_with_progress_bar(
    #                 default_llamafile_url, local_llamafile_path
    #             )
    hf_hub_download(
        # cache_dir=f"{app_dir}/models",
        # filename=default_llamafile_filename,
        filename=settings.default_model_filename,
        # local_dir=os.path.dirname(local_llamafile_path),
        local_dir=f"{app_dir}/models/{default_hf_repo_id}",
        # local_files_only=True,
        repo_id=default_hf_repo_id,
        repo_type="model",
    )

    # assert os.path.exists(local_llamafile_path)
    # assert os.path.exists(f"{app_dir}/models/{default_hf_repo_id}/{default_model_filename}")
    assert os.path.exists(local_model_path)

    if default_multimodal_model_projector_filename:
        os.makedirs(
            os.path.dirname(local_multimodal_model_projector_path), exist_ok=True
        )
        hf_hub_download(
            filename=default_multimodal_model_projector_filename,
            local_dir=f"{app_dir}/models/{default_hf_repo_id}",
            # local_files_only=True,
            repo_id=default_hf_repo_id,
            repo_type="model",
        )

        assert os.path.exists(local_multimodal_model_projector_path)

    args = ["sh"]

    if default_model_filename.endswith(".gguf"):
        args += [
            "bin/llamafile",
            "--model",
            local_model_path,
        ]

        if default_multimodal_model_projector_filename:
            args += [
                "--mmproj",
                f"{local_multimodal_model_projector_path}",
            ]

    elif default_model_filename.endswith(".llamafile"):
        # if local_model_path is not executable, make it executable
        if not os.access(local_model_path, os.X_OK):
            os.chmod(local_model_path, 0o755)

        args += [
            local_model_path,
        ]

    else:
        raise NotImplementedError(
            f"Unsupported model file type: {default_model_filename}"
        )

    args += [
        "--host",
        f"{default_llamafile_host}",
        # "--model‐draft", # TODO: Draft model for speculative decoding
        "--nobrowser",
        "--path",
        "/zip/llama.cpp/server/public",
        "--port",
        f"{default_llamafile_port}",
        "--server",
        "--temp",
        "0.0",
    ]

    # TODO: add support for LoRA adapters

    llamafile_pid = subprocess_manager.start(
        args=args,
        name="llamafiles.default",
    )

    return llamafile_pid


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


class SubprocessManager:
    def start(self, args, name):
        try:
            stdout_log_path = f"stdout.{name}.log"
            stderr_log_path = f"stderr.{name}.log"

            with open(stderr_log_path, "w") as stderr, open(
                stdout_log_path, "w"
            ) as stdout:
                self.process = subprocess.Popen(
                    args,
                    preexec_fn=os.setpgrp,  # Start the process in a new process group
                    stderr=stderr,
                    stdout=stdout,
                )

            print(f"Started {name} process with PID: {self.process.pid}")

            return self.process.pid

        except Exception as e:
            print(f"An error occurred: {e}")

    def stop(self, pid=None):
        if pid:
            try:
                os.killpg(os.getpgid(pid), signal.SIGTERM)

            except ProcessLookupError as e:
                print(f"An error occurred: {e}")

        else:
            print("No process to terminate")


def main(*args, **kwargs):
    print(f"=== {__name__}.main(*args, **kwargs) ===")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")

    cwd = os.getcwd()
    print(f"cwd: {cwd}")

    uvicorn.run(
        f"{__name__}:fastapi_app",
        # host="0.0.0.0",
        host=kwargs.get("host", "0.0.0.0"),
        log_level="info",
        loop="asyncio",
        # port=8000,
        port=kwargs.get("port", 8000),
        # reload=True,
        reload=kwargs.get("dev", False),
        reload_dirs=[
            f"{os.getcwd()}/timestep",
        ],
        workers=1,
    )


if __name__ == "__main__":
    main()
