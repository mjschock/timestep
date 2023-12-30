import logging

from fastapi import FastAPI

from .routers import agents, threads

app = FastAPI()

logger = logging.getLogger(__name__)


@app.on_event("startup")
async def startup_event():
    logger.info("Starting up")


@app.get("/ready")
async def get_ready():
    # TODO: https://kubernetes.io/docs/reference/using-api/health-checks/
    # Change to /livez and /readyz
    return {
        "ready": "okay",
    }


app.include_router(agents.router)
# app.include_router(documents.router)
app.include_router(threads.router)
