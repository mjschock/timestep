from typing import Union

from prefect import flow
from connexion import AsyncApp, ConnexionMiddleware
from connexion.options import SwaggerUIOptions
from fastapi import FastAPI, Request
import typer
import uvicorn
from timestep.agent import hello_world
from timestep.api.openai.v1.controllers.completions_controller import create_completion

connexion_app = AsyncApp(__name__)
fastapi_app = FastAPI()
typer_app = typer.Typer()

def main():
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

    fastapi_app.mount("/api", ConnexionMiddleware(connexion_app))

    # @app.post("/v1/engines/{engine}/completions")
    @fastapi_app.post("/v1/engines/engine/completions")
    async def create_code_completion(request: Request):
        body = await request.json()
        body["model"] = "LLaMA_CPP"

        return await create_completion(body, token_info={}, user=None)

    uvicorn.run(
        "timestep.__main__:fastapi_app",
        host="0.0.0.0",
        log_level="info",
        port=8000,
        # reload=True,
        # reload_dirs=[
        #     f"{cwd}/apis",
        # ],
    )

@typer_app.callback()
def callback():
    """
    Timestep AI CLI
    """

@typer_app.command()
def up():
    """
    Up
    """
    typer.echo("Timestep up...")

    main()

if __name__ == "__main__":
    main()
