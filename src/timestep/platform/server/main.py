import argparse
import logging
from contextlib import asynccontextmanager

import uvicorn
from app.api.agents import agents_router
from app.services import agents as agents_service
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    # ml_models["answer_to_everything"] = fake_answer_to_everything_ml_model
    await agents_service.on_startup()
    yield
    # Clean up the ML models and release the resources
    # ml_models.clear()
    await agents_service.on_shutdown()

app = FastAPI(
    lifespan=lifespan,
)

# environment = os.getenv("ENVIRONMENT", "dev")  # Default to 'development' if not set

# if environment == "dev":
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

app.include_router(agents_router, prefix="/api/agents")
# app.include_router(chat_router, prefix="/api/chat")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--reload", action="store_true", default=False)
    args = parser.parse_args()

    if args.reload:
        enable_cors(app) # TODO: does this need to be added before the router?

    uvicorn.run(
        "main:app",
        port=8000,
        reload=args.reload,
        host="0.0.0.0",
        proxy_headers=True,
    )
