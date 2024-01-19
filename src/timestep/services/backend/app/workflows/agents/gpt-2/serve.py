import os
from typing import List

from agent import Agent
from agent_protocol import (
    Artifact,
    Step,
    StepHandler,
    Task,
    TaskDB,
    TaskHandler,
    TaskRequestBody,
)
from agent_protocol.db import InMemoryTaskDB
from fastapi import FastAPI
from ray import serve

app = FastAPI()


@serve.deployment
@serve.ingress(app)
class AgentDeployment:
    def __init__(self) -> None:
        db: TaskDB = InMemoryTaskDB() # TODO: use PostgreSQL database
        # step_handler: StepHandler = None
        # task_handler: TaskHandler = None
        workspace: str = os.getenv("AGENT_WORKSPACE", "workspace") # TODO: use MinIO bucket

        self.agent = Agent(
            db=db,
            # step_handler=step_handler,
            # task_handler=task_handler,
            workspace=workspace,
        )

    @app.get("/livez")
    async def is_live(self) -> str:
        return "ok"

    @app.get("/readyz")
    async def is_ready(self) -> str:
        return "ok"

    @app.get("/v1/chat/completions")
    async def chat_completions(self) -> str:
        messages = [
            {
                "role": "system",
                "content": "You are a friendly chatbot who always responds in the style of a pirate",
            },
            {"role": "user", "content": "How many helicopters can a human eat in one sitting?"},
        ]

        # tokenized_chat = self.agent.tokenizer.apply_chat_template(
        #     messages,
        #     add_generation_prompt=True,
        #     return_tensors="pt",
        #     tokenize=True
        # )

        # return self.agent.tokenizer.decode(tokenized_chat[0])

        # return "ok"

        return self.agent.chat(messages)

    @app.post("/ap/v1/agent/tasks", response_model=Task, tags=["agent"])
    async def create_agent_task(self, body: TaskRequestBody | None = None) -> Task:
        """
        Creates a task for the agent.
        """
        # artifacts: List[Artifact] = []
        # steps: List[Step] = []

        # task = Task(
        #     input=body.input if body else None,
        #     additional_input=body.additional_input if body else None,
        #     task_id="50da533e-3904-4401-8a07-c49adf88b5eb",
        #     artifacts=artifacts,
        #     steps=steps,
        # )

        task = await self.agent.create_task(
            input=body.input if body else None,
            additional_input=body.additional_input if body else None,
        )

        # await self.agent.task_handler(task)

        return task

        # if not _task_handler:
        #     raise Exception("Task handler not defined")

        # task = await Agent.db.create_task(
        #     input=body.input if body else None,
        #     additional_input=body.additional_input if body else None,
        # )
        # await _task_handler(task)

        # return task

    @app.get("/ap/v1/agent/tasks", response_model=List[Task], tags=["agent"]) # TODO: add current_page and page_size "path" attributes
    async def list_agent_tasks(self) -> List[Task]:
        """
        List all tasks that have been created for the agent.
        """
        return await self.agent.get_tasks()

deployment = AgentDeployment.bind()
