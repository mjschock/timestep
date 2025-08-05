import os
from collections.abc import Callable
from typing import Any

import httpx
import yaml
from fastapi import FastAPI, HTTPException, Request, Response, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse, StreamingResponse

from backend._shared.logging_config import logger
from backend.apis.audio_api import audio_router
from backend.apis.batches_api import batches_router
from backend.apis.chat_api import chat_router
from backend.apis.containers_api import containers_router
from backend.apis.embeddings_api import embeddings_router
from backend.apis.evals_api import evals_router
from backend.apis.files_api import files_router
from backend.apis.fine_tuning_api import fine_tuning_router
from backend.apis.images_api import images_router
from backend.apis.models_api import models_router
from backend.apis.moderations_api import moderations_router
from backend.apis.organization_api import organization_router
from backend.apis.realtime_api import realtime_router
from backend.apis.responses_api import responses_router
from backend.apis.uploads_api import uploads_router
from backend.apis.vector_stores_api import vector_stores_router

app: FastAPI = FastAPI()

# Load provider configuration
config_path = os.path.join(
    os.path.dirname(os.path.dirname(__file__)), "..", "config.yaml"
)
with open(config_path) as f:
    config = yaml.safe_load(f)

app.include_router(audio_router, prefix="/v1")
app.include_router(batches_router, prefix="/v1")
app.include_router(chat_router, prefix="/v1")
app.include_router(containers_router, prefix="/v1")
app.include_router(embeddings_router, prefix="/v1")
app.include_router(evals_router, prefix="/v1")
app.include_router(files_router, prefix="/v1")
app.include_router(fine_tuning_router, prefix="/v1")
app.include_router(images_router, prefix="/v1")
app.include_router(models_router, prefix="/v1")
app.include_router(moderations_router, prefix="/v1")
app.include_router(organization_router, prefix="/v1")
app.include_router(realtime_router, prefix="/v1")
app.include_router(responses_router, prefix="/v1")

app.include_router(uploads_router, prefix="/v1")
app.include_router(vector_stores_router, prefix="/v1")


# Provider routing - NEW
@app.api_route(
    "/api/{provider}/v1/{path:path}", methods=["DELETE", "GET", "PATCH", "POST", "PUT"]
)
async def provider_proxy(provider: str, path: str, request: Request):
    """Route requests to different providers"""

    provider_config = config.get("providers", {}).get(provider)
    if not provider_config:
        raise HTTPException(status_code=404, detail=f"Provider '{provider}' not found")

    method = request.method
    headers = dict(request.headers)

    try:
        body = await request.json() if method in ["PATCH", "POST", "PUT"] else None
    except Exception:
        body = None

    is_streaming = body and body.get("stream", False) if body else False

    if provider_config["type"] == "local":
        return await route_to_local(path, method, request, body)
    elif provider_config["type"] == "proxy":
        if is_streaming:
            return await stream_from_provider(
                provider_config, path, method, headers, body
            )
        else:
            return await proxy_to_provider(provider_config, path, method, headers, body)
    else:
        raise HTTPException(
            status_code=400, detail=f"Unknown provider type: {provider_config['type']}"
        )


async def proxy_to_provider(
    provider_config: dict, path: str, method: str, headers: dict, body: Any
):
    """Proxy request to external provider"""

    base_url = provider_config["base_url"]
    api_key = provider_config["api_key"]

    if "anthropic" in base_url:
        proxy_headers = {
            "anthropic-version": "2023-06-01",
            "Content-Type": "application/json",
            "x-api-key": api_key,
        }
    else:
        proxy_headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }

    async with httpx.AsyncClient(timeout=60.0) as client:
        url = f"{base_url}/{path}"

        response = await client.request(
            method=method, url=url, headers=proxy_headers, json=body
        )

        if response.status_code != 200:
            error_content = (
                response.json() if response.content else {"error": "Unknown error"}
            )
            raise HTTPException(status_code=response.status_code, detail=error_content)

        return JSONResponse(content=response.json())


async def route_to_local(path: str, method: str, request: Request, body: Any):
    """Route to your existing local APIs"""

    local_url = f"http://localhost:8000/v1/{path}"

    async with httpx.AsyncClient() as client:
        response = await client.request(
            method=method,
            url=local_url,
            headers=dict(request.headers),
            json=body,
            params=dict(request.query_params),
        )

        if response.headers.get("content-type", "").startswith("application/json"):
            return JSONResponse(
                content=response.json(),
                status_code=response.status_code,
                headers=dict(response.headers),
            )
        else:
            return Response(
                content=response.content,
                status_code=response.status_code,
                headers=dict(response.headers),
            )


async def stream_from_provider(
    provider_config: dict, path: str, method: str, headers: dict, body: Any
):
    """Handle streaming requests"""

    base_url = provider_config["base_url"]
    api_key = provider_config["api_key"]

    if "anthropic" in base_url:
        proxy_headers = {
            "Accept": "text/event-stream",
            "anthropic-version": "2023-06-01",
            "Content-Type": "application/json",
            "x-api-key": api_key,
        }
    else:
        proxy_headers = {
            "Accept": "text/event-stream",
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }

    async def stream_generator():
        async with httpx.AsyncClient(timeout=60.0) as client:
            url = f"{base_url}/{path}"

            async with client.stream(
                "POST", url, headers=proxy_headers, json=body
            ) as response:
                if response.status_code != 200:
                    error_content = await response.aread()
                    raise HTTPException(
                        status_code=response.status_code, detail=error_content.decode()
                    )

                async for chunk in response.aiter_text():
                    if chunk.strip():
                        yield chunk

    return StreamingResponse(
        stream_generator(),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "Connection": "keep-alive"},
    )


@app.get("/health")
async def health_check():
    return {
        "providers": list(config.get("providers", {}).keys()),
        "status": "healthy",
        "version": "2.0.0",
    }


@app.middleware("http")
async def log_requests(
    request: Request, call_next: Callable[[Request], Any]
) -> Response:
    logger.info(f"Incoming request: {request.method} {request.url}")
    try:
        response: Response = await call_next(request)
        return response
    except Exception as exc:
        logger.error(f"Unhandled error: {exc}", exc_info=True)
        raise


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    logger.error(f"Global exception: {exc}", exc_info=True)
    return JSONResponse(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        content={"detail": "Not implemented", "error": str(exc)},
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
    request: Request, exc: RequestValidationError
) -> JSONResponse:
    logger.error(f"Validation error: {exc}")

    def clean_error(err: dict[str, Any]) -> dict[str, Any]:
        if "ctx" in err:
            ctx = err["ctx"]
            err["ctx"] = {k: str(v) for k, v in ctx.items()}
        return err

    errors = [clean_error(e) for e in exc.errors()]
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"detail": errors},
    )
