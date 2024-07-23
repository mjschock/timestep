import uvicorn
from connexion import AsyncApp, ConnexionMiddleware
from connexion.options import SwaggerUIOptions
from fastapi import FastAPI, Request

connexion_app = AsyncApp(import_name=__name__)
fastapi_app = FastAPI()


def main():
    from timestep.api.openai.v1.controllers.completions_controller import (
        create_completion,
    )
    from timestep.services import models_service

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

    fastapi_app.mount(
        "/api", ConnexionMiddleware(app=connexion_app, import_name=__name__)
    )

    @fastapi_app.post("/v1/engines/{engine}/completions")
    async def create_code_completion(engine: str, request: Request):
        if engine == "copilot-codex":
            body = await request.json()
            body["model"] = "LLaMA_CPP"

            return await create_completion(body, token_info={}, user=None)

        else:
            raise NotImplementedError("Not implemented")

    @fastapi_app.get("/v2/models/{model_id}")
    async def create_code_completion(model_id: str, request: Request):
        # model_info = models_service.retrieve_model(model_id, token_info, user)
        model_info = models_service.retrieve_model(model_id)

        print("model_info: ", model_info)

        return model_info

    uvicorn.run(
        f"{__name__}:fastapi_app",
        host="0.0.0.0",
        log_level="info",
        loop="asyncio",
        port=8000,
        # reload=True,
        # reload_dirs=[
        #     f"{cwd}/api",
        # ],
        workers=1,
    )


if __name__ == "__main__":
    main()
