import os
import tempfile
from typing import Annotated, List, Optional
from uuid import uuid4

from agent import Agent
from agent_protocol import (
    TaskRequestBody,
)
from agent_protocol.db import InMemoryTaskDB, NotFoundException, Step, Task, TaskDB
from agent_protocol.models import (
    Artifact,
    Pagination,
    Status,
    StepRequestBody,
    TaskListResponse,
    TaskStepsListResponse,
)
from fastapi import FastAPI, File, Form, HTTPException, UploadFile
from fastapi.responses import FileResponse
from minio import Minio
from ray import serve
from starlette.background import BackgroundTask

app = FastAPI()


@serve.deployment
@serve.ingress(app)
class AgentDeployment:
    def __init__(self) -> None:
        db: TaskDB = InMemoryTaskDB() # TODO: use PostgreSQL database
        workspace: str = os.getenv("AGENT_WORKSPACE", "workspace") # TODO: use MinIO bucket

        self.agent = Agent(
            db=db,
            workspace=workspace,
        )

    @app.get("/livez")
    async def is_live(self) -> str:
        return "ok"

    @app.get("/readyz")
    async def is_ready(self) -> str:
        return "ok"

    @app.post("/ap/v1/agent/tasks", response_model=Task, tags=["agent"])
    async def create_agent_task(self, body: TaskRequestBody | None = None) -> Task:
        """
        Creates a task for the agent.
        """
        return await self.agent.create_task(
            input=body.input if body else None,
            additional_input=body.additional_input if body else None,
        )

    @app.get("/ap/v1/agent/tasks", response_model=TaskListResponse, tags=["agent"])
    async def list_agent_tasks(
        self,
        page_size: int = 10,
        current_page: int = 1
    ) -> TaskListResponse:
        """
        List all tasks that have been created for the agent.
        """
        tasks = await self.agent.get_tasks()
        start_index = (current_page - 1) * page_size
        end_index = start_index + page_size

        return TaskListResponse(
            tasks=tasks[start_index:end_index],
            pagination=Pagination(
                total_items=len(tasks),
                total_pages=len(tasks) // page_size + 1,
                current_page=current_page,
                page_size=page_size,
            ),
        )

    @app.get("/ap/v1/agent/tasks/{task_id}", response_model=Task, tags=["agent"])
    async def get_agent_task(self, task_id: str) -> Task:
        """
        Get details about a specified agent task.
        """
        return await self.agent.db.get_task(task_id)

    @app.get(
        "/ap/v1/agent/tasks/{task_id}/steps",
        response_model=TaskStepsListResponse,
        tags=["agent"],
    )
    async def list_agent_task_steps(
        self, task_id: str, page_size: int = 10, current_page: int = 1
    ) -> List[str]:
        """
        List all steps for the specified task.
        """
        task = await self.agent.db.get_task(task_id)
        start_index = (current_page - 1) * page_size
        end_index = start_index + page_size

        return TaskStepsListResponse(
            steps=task.steps[start_index:end_index],
            pagination=Pagination(
                total_items=len(task.steps),
                total_pages=len(task.steps) // page_size + 1,
                current_page=current_page,
                page_size=page_size,
            ),
        )

    @app.post(
        "/ap/v1/agent/tasks/{task_id}/steps",
        response_model=Step,
        tags=["agent"],
    )
    async def execute_agent_task_step(
        self,
        task_id: str,
        body: StepRequestBody | None = None,
    ) -> Step:
        """
        Execute a step in the specified agent task.
        """
        try:
            task = await self.agent.db.get_task(task_id)
            step = next(filter(lambda x: x.status == Status.created, task.steps), None)

            if not step:
                raise HTTPException(
                    detail="No steps to execute",
                    status_code=200,
                )

            step.status = Status.running
            step.input = body.input if body else None
            step.additional_input = body.additional_input if body else None
            step = await self.agent.step(step)
            step.status = Status.completed

            return step

        except NotFoundException as e:
            raise HTTPException(
                detail=f"{e.item_name} with {e.item_id} not found.",
                status_code=400,
            )

    @app.get(
        "/ap/v1/agent/tasks/{task_id}/steps/{step_id}",
        response_model=Step,
        tags=["agent"],
    )
    async def get_agent_task_step(self, task_id: str, step_id: str) -> Step:
        """
        Get details about a specified task step.
        """
        return await self.agent.db.get_step(task_id, step_id)

    @app.get(
        "/ap/v1/agent/tasks/{task_id}/artifacts",
        response_model=List[Artifact],
        tags=["agent"],
    )
    async def list_agent_task_artifacts(self, task_id: str) -> List[Artifact]:
        """
        List all artifacts for the specified task.
        """
        return await self.agent.db.get_task(task_id)

    @app.post(
        "/ap/v1/agent/tasks/{task_id}/artifacts",
        response_model=Artifact,
        tags=["agent"],
    )
    async def upload_agent_task_artifacts(
        self,
        task_id: str,
        file: Annotated[UploadFile, File()],
        relative_path: Annotated[Optional[str], Form()] = None,
    ) -> Artifact:
        """
        Upload an artifact for the specified task.
        """
        file_name = file.filename or str(uuid4())
        artifact = await self.agent.db.create_artifact(
            task_id=task_id,
            agent_created=False,
            file_name=file_name,
            relative_path=relative_path,
        )

        minio_endpoint = os.getenv("MINIO_ENDPOINT")
        minio_client = Minio(
            minio_endpoint,
            access_key=os.getenv("MINIO_ROOT_USER"),
            secret_key=os.getenv("MINIO_ROOT_PASSWORD"),
            secure=False,
        )

        bucket_name = "default"
        found = minio_client.bucket_exists(bucket_name)

        if not found:
            minio_client.make_bucket(bucket_name)
            print("Created bucket", bucket_name)

        else:
            print("Bucket", bucket_name, "already exists")

        # TODO: use nhost storage to store files

        artifact_path = self.agent.get_artifact_path(task_id, artifact)

        minio_client.put_object(
            bucket_name=bucket_name,
            object_name=artifact_path,
            data=file.file,
            length=file.size,
            content_type="application/octet-stream",
        )

        return artifact

    @app.get(
        "/ap/v1/agent/tasks/{task_id}/artifacts/{artifact_id}",
        tags=["agent"],
    )
    async def download_agent_task_artifacts(
        self,
        task_id: str,
        artifact_id: str
    ) -> FileResponse:
        """
        Download the specified artifact.
        """
        artifact = await self.agent.db.get_artifact(task_id, artifact_id)
        artifact_path = self.agent.get_artifact_path(task_id, artifact)

        minio_endpoint = os.getenv("MINIO_ENDPOINT")
        minio_client = Minio(
            minio_endpoint,
            access_key=os.getenv("MINIO_ROOT_USER"),
            secret_key=os.getenv("MINIO_ROOT_PASSWORD"),
            secure=False,
        )

        bucket_name = "default"

        with tempfile.NamedTemporaryFile(delete=False) as fp:
            tmp_file_path: str = fp.name

            minio_client.fget_object(
                bucket_name=bucket_name,
                object_name=artifact_path,
                file_path=tmp_file_path
            )

            def cleanup(tmp_file_path: str) -> None:
                os.remove(tmp_file_path)

            return FileResponse(
                path=tmp_file_path,
                media_type="application/octet-stream",
                filename=artifact.file_name,
                background=BackgroundTask(cleanup, tmp_file_path),
            )


deployment = AgentDeployment.bind()
