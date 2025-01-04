import json
from contextlib import asynccontextmanager
from enum import Enum

import uvicorn
from connexion import AsyncApp, ConnexionMiddleware
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from openai import AsyncOpenAI
from routes import router

# from timestep.config import settings

# app_dir = settings.app_dir
connexion_app = AsyncApp(import_name=__name__)
# default_hf_repo_id = settings.default_hf_repo_id

# client = AsyncOpenAI(
#     api_key="sk-no-key-required",
#     # base_url="http://localhost:8080/v1",
#     base_url="http://localhost:8000/v1",
# )


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        print("=== Lifespan startup ===")

        # await flet_fastapi.app_manager.start()
        yield
        # await flet_fastapi.app_manager.shutdown()

    finally:
        print("=== Lifespan cleanup ===")
        print("Shutting down...")


fastapi_app = FastAPI(
    lifespan=lifespan,
    # servers= # TODO: add server for testing?
)

# connexion_app.add_api(
#     "api/openai/v1/openapi/openapi.yaml",
#     base_path="/openai/v1",
#     pythonic_params=True,
#     resolver_error=500,
# )

fastapi_app.mount("/api", ConnexionMiddleware(app=connexion_app, import_name=__name__))

# app = FastAPI(title="Flet FastAPI Backend")

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# app.include_router(router, prefix="/api")


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

        # return await create_completion(body, token_info={}, user=None)
        raise NotImplementedError("Not implemented")

    else:
        raise NotImplementedError("Not implemented")


def main(*args, **kwargs):
    print(f"=== {__name__}.main(*args, **kwargs) ===")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")

    # cwd = os.getcwd()
    # print(f"cwd: {cwd}")

    # uvicorn.run(
    #     f"{__name__}:fastapi_app",
    #     # host="0.0.0.0",
    #     host=kwargs.get("host", "0.0.0.0"),
    #     log_level="info",
    #     loop="asyncio",
    #     # port=8000,
    #     # port=kwargs.get("port", 8000),
    #     port=kwargs.get("port", 8080),
    #     # reload=True,
    #     reload=kwargs.get("dev", False),
    #     reload_dirs=[
    #         # f"{os.getcwd()}/timestep",
    #         f"{os.getcwd()}/src/timestep",
    #     ],
    #     workers=1,
    # )

    # uvicorn.run(app, host="0.0.0.0", port=8080)
    uvicorn.run(
        fastapi_app,
        host="0.0.0.0",
        port=8080,
    )


if __name__ == "__main__":
    main()
