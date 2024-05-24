import argparse
import logging
from contextlib import asynccontextmanager

import uvicorn
from app.api.accounts import accounts_router
from app.api.agents import agents_router
from app.api.artifacts import artifacts_router
from app.api.chat import chat_router
from app.api.tasks import tasks_router
from app.services import accounts as accounts_service
from app.services import agents as agents_service
from app.services import artifacts as artifacts_service
from app.services import chat as chat_service
from app.services import tasks as tasks_service
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    await accounts_service.on_startup()
    await agents_service.on_startup()
    await artifacts_service.on_startup()
    await chat_service.on_startup()
    await tasks_service.on_startup()
    yield
    await tasks_service.on_shutdown()
    await chat_service.on_shutdown()
    await artifacts_service.on_shutdown()
    await agents_service.on_shutdown()
    await accounts_service.on_shutdown()


app = FastAPI(
    lifespan=lifespan,
)


def enable_cors(app):
    logger = logging.getLogger("uvicorn")
    logger.warning("Running in development mode - allowing CORS for all origins")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


app.include_router(accounts_router, prefix="/api/accounts")
app.include_router(agents_router, prefix="/api/agents")
app.include_router(artifacts_router, prefix="/api/artifacts")
app.include_router(chat_router, prefix="/api/chat")
app.include_router(tasks_router, prefix="/api/tasks")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--reload", action="store_true", default=False)
    args = parser.parse_args()

    if args.reload:
        enable_cors(app)  # TODO: does this need to be added before the router?

    uvicorn.run(
        "main:app",
        port=8000,
        reload=args.reload,
        host="0.0.0.0",
        proxy_headers=True,
    )
