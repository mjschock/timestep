# import os

# from agent import Agent
# from agent_protocol import (
#     TaskDB,
# )

# from agent_protocol.db import InMemoryTaskDB, TaskDB
# from agent_protocol.server import app
from fastapi import FastAPI

# from hypercorn.asyncio import serve
from ray import serve

app = FastAPI()


@serve.deployment
@serve.ingress(app)
class AgentDeployment:
    def __init__(self) -> None:
        pass

        # db: TaskDB = InMemoryTaskDB() # TODO: use PostgreSQL database
        # workspace: str = os.getenv("AGENT_WORKSPACE", "workspace") # TODO: use MinIO bucket

        # self.agent = Agent(
        #     db=db,
        #     workspace=workspace,
        # )

    @app.get("/livez")
    async def is_live(self) -> str:
        return "ok"

    @app.get("/readyz")
    async def is_ready(self) -> str:
        return "ok"


deployment = AgentDeployment.bind()
