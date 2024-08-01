import os
from contextlib import asynccontextmanager
from pathlib import Path

import uvicorn
from connexion import AsyncApp, ConnexionMiddleware
from connexion.options import SwaggerUIOptions
from fastapi import FastAPI, Request
from prefect import flow

from timestep.api.openai.v1.controllers.completions_controller import create_completion
from timestep.utils import download_with_progress_bar, start_shell_script

# from timestep.worker import agent_flow

default_llamafile_filename = "TinyLlama-1.1B-Chat-v1.0.F16.llamafile"
default_llamafile_url = f"https://huggingface.co/Mozilla/TinyLlama-1.1B-Chat-v1.0-llamafile/resolve/main/{default_llamafile_filename}?download=true"

host = "0.0.0.0"  # TODO: move to config
llamafile_path = f"./models/{default_llamafile_filename}"  # TODO: namespace under llamafile, include port, etc.
port = 8080

connexion_app = AsyncApp(import_name=__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # agent_flow = flow.from_source(
    #     source=str(Path(__file__).parent),
    #     entrypoint="worker.py:agent_flow",
    # ).deploy(
    #     name="agent-flow-deployment",
    #     # parameters=dict(name="Marvin"),
    #     # work_pool_name="local",
    #     work_pool_name="default",
    # )

    agent_flow = await flow.from_source(
        source=str(Path(__file__).parent),
        entrypoint="worker.py:agent_flow",
    )

    await agent_flow.deploy(
        name="agent-flow-deployment",
        # parameters=dict(name="Marvin"),
        # work_pool_name="local",
        work_pool_name="default",
    )

    if os.path.basename(
        llamafile_path
    ) == default_llamafile_filename and not os.path.exists(llamafile_path):
        os.makedirs(os.path.dirname(llamafile_path), exist_ok=True)
        download_with_progress_bar(default_llamafile_url, llamafile_path)

    assert os.path.exists(llamafile_path)

    process = start_shell_script(
        llamafile_path,
        "--host",
        host,
        "--nobrowser",
        "--path",
        "/zip/llama.cpp/server/public",
        "--port",
        f"{port}",
    )

    print(f"Started llamafile with PID: {process.pid}.")

    yield

    print(f"Terminating llamafile with PID: {process.pid}.")
    process.terminate()


fastapi_app = FastAPI(
    lifespan=lifespan,
)

# from timestep.api.openai.v1.controllers.completions_controller import create_completion

# from timestep.services import model_service

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
    resolver_error=501,
)

fastapi_app.mount("/api", ConnexionMiddleware(app=connexion_app, import_name=__name__))


@fastapi_app.post("/v1/engines/{engine}/completions")
async def create_code_completion(engine: str, request: Request):
    if engine == "copilot-codex":
        body = await request.json()
        body["model"] = "LLaMA_CPP"

        return await create_completion(body, token_info={}, user=None)

    else:
        raise NotImplementedError("Not implemented")

    # @fastapi_app.get("/v2/models/{model_id}")
    # async def create_code_completion(model_id: str, request: Request):
    #     # model_info = models_service.retrieve_model(model_id, token_info, user)
    #     model_info = model_service.retrieve_model(model_id)

    #     print("model_info: ", model_info)

    #     return model_info

    # cwd = os.getcwd()
    # print(f"cwd: {cwd}")

    # uvicorn.run(
    #     # f"{__name__}:fastapi_app",
    #     app=fastapi_app,
    #     host="0.0.0.0",
    #     log_level="info",
    #     loop="asyncio",
    #     port=8000,
    #     reload=True,
    #     reload_dirs=[
    #         f"{os.getcwd()}",
    #     ],
    #     workers=1,
    # )

    # return fastapi_app


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
            f"{os.getcwd()}",
        ],
        workers=1,
    )


if __name__ == "__main__":
    main()
