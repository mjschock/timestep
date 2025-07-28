from collections.abc import Callable
from typing import Any

from fastapi import FastAPI, Request, Response, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

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
from backend.apis.tts_api import router as tts_router
from backend.logging_config import logger

app: FastAPI = FastAPI()

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
app.include_router(tts_router, prefix="/v1")


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
