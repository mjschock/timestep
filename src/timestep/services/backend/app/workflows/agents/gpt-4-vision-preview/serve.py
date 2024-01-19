import asyncio
import os
import tempfile
from typing import Annotated, Any, Callable, Coroutine, List, Optional
from uuid import uuid4

import aiofiles
from agent import Agent
from agent_protocol import (
    TaskDB,
    TaskRequestBody,
)
from agent_protocol.db import InMemoryTaskDB, NotFoundException, Step, Task, TaskDB
from agent_protocol.models import (
    Artifact,
    Pagination,
    Status,
    StepRequestBody,
    Task,
    TaskListResponse,
    TaskRequestBody,
    TaskStepsListResponse,
)
from agent_protocol.server import app
from fastapi import APIRouter, FastAPI, File, Form, HTTPException, UploadFile
from fastapi.responses import FileResponse
from hypercorn.asyncio import serve
from hypercorn.config import Config
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

    @app.get("/ap/v1/agent/tasks", response_model=TaskListResponse, tags=["agent"])
    # async def list_agent_tasks_ids(self, page_size: int = 10, current_page: int = 1) -> List[str]: # TODO: address discrepancy between TaskListResponse and List[str] (tasks vs task_ids)
    async def list_agent_tasks(self, page_size: int = 10, current_page: int = 1) -> TaskListResponse:
        """
        List all tasks that have been created for the agent.
        """
        # tasks = await Agent.db.list_tasks()
        tasks = await self.agent.get_tasks() # TODO: db.Task vs models.Task
        start_index = (current_page - 1) * page_size
        end_index = start_index + page_size
        return TaskListResponse(
            tasks=tasks[start_index:end_index],
            pagination=Pagination(
                total_items=len(tasks),
                # total_pages=len(tasks) // page_size,
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
        # return await Agent.db.get_task(task_id)
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
        # task = await Agent.db.get_task(task_id)
        task = await self.agent.db.get_task(task_id)
        start_index = (current_page - 1) * page_size
        end_index = start_index + page_size
        return TaskStepsListResponse(
            steps=task.steps[start_index:end_index],
            pagination=Pagination(
                total_items=len(task.steps),
                # total_pages=len(task.steps) // page_size,
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
        # if not _step_handler:
            # raise Exception("Step handler not defined")

        # task = await Agent.db.get_task(task_id)
        try:
            task = await self.agent.db.get_task(task_id)
            step = next(filter(lambda x: x.status == Status.created, task.steps), None)

            if not step:
                # raise Exception("No steps to execute")
                raise HTTPException(
                    detail="No steps to execute",
                    status_code=200,
                )

            step.status = Status.running

            step.input = body.input if body else None
            step.additional_input = body.additional_input if body else None

            # step = await _step_handler(step)
            step = await self.agent.step(step)

            step.status = Status.completed
            return step

        except NotFoundException as e:
            print(f"{e.item_name} with {e.item_id} not found.")
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
        # return await Agent.db.get_step(task_id, step_id)
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
        # task = await Agent.db.get_task(task_id)
        task = await self.agent.db.get_task(task_id)
        return task.artifacts

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
        # await Agent.db.get_task(task_id)
        await self.agent.db.get_task(task_id)
        # artifact = await Agent.db.create_artifact(
        #     task_id=task_id,
        #     agent_created=False,
        #     file_name=file_name,
        #     relative_path=relative_path,
        # )
        artifact = await self.agent.db.create_artifact(
            task_id=task_id,
            agent_created=False,
            file_name=file_name,
            relative_path=relative_path,
        )

        # path = Agent.get_artifact_folder(task_id, artifact)
        # path = self.agent.get_artifact_folder(task_id, artifact)
        # if not os.path.exists(path):
        #     os.makedirs(path)

        # async with aiofiles.open(os.path.join(path, file_name), "wb") as f:
        #     while content := await file.read(1024 * 1024):  # async read chunk ~1MiB
        #         await f.write(content)

        minio_endpoint = os.getenv("MINIO_ENDPOINT")
        minio_client = Minio(
            minio_endpoint,
            access_key=os.getenv("MINIO_ROOT_USER"),
            secret_key=os.getenv("MINIO_ROOT_PASSWORD"),
            secure=False,
        )

        # The destination bucket and filename on the MinIO server
        bucket_name = "default"
        # destination_file = "my-test-file.txt"

        # Make the bucket if it doesn't exist.
        found = minio_client.bucket_exists(bucket_name)

        if not found:
            minio_client.make_bucket(bucket_name)
            print("Created bucket", bucket_name)

        else:
            print("Bucket", bucket_name, "already exists")

        # TODO: use nhost storage to store files

        folder_path = self.agent.get_artifact_folder(task_id, artifact)
        # assert self.agent.get_artifact_path(task_id, artifact) == f"{path}/{artifact.file_name}", f"{self.agent.get_artifact_path(task_id, artifact)} != {f'{path}/{artifact.file_name}'}"
        artifact_path = self.agent.get_artifact_path(task_id, artifact)
        # assert artifact_path == f"{folder_path}/{artifact.file_name}", f"{artifact_path} != {f'{folder_path}/{artifact.file_name}'}"

        # print('path', path)
        print('folder_path', folder_path)
        print('artifact_path', artifact_path)
        print('relative_path', relative_path)
        print('artifact.file_name', artifact.file_name)
        print('file_name', file_name)
        # if not minio_client.stat_object(bucket_name, path):
            # minio_client.fput_object(bucket_name, path, file.file)
        minio_client.put_object(
            bucket_name=bucket_name,
            # object_name=f"{path}/{file_name}",
            object_name=artifact_path,
            data=file.file,
            length=file.size,
            content_type="application/octet-stream",
            # content_type=file.media_type,
        )

        # data = io.BytesIO(source_contents.encode())
        # minio_client.put_object(
        #     bucket_name=bucket_name,
        #     object_name=destination_file,
        #     # file_path=source_file,
        #     # =taio.BytesIO(source_contents.encode()),
        #     data=data,
        #     length=len(source_contents),
        #     content_type="application/octet-stream",
        # )

        return artifact

    @app.get(
        "/ap/v1/agent/tasks/{task_id}/artifacts/{artifact_id}",
        tags=["agent"],
    )
    async def download_agent_task_artifacts(self, task_id: str, artifact_id: str) -> FileResponse:
        """
        Download the specified artifact.
        """
        # artifact = await Agent.db.get_artifact(task_id, artifact_id)
        artifact = await self.agent.db.get_artifact(task_id, artifact_id)
        # path = Agent.get_artifact_path(task_id, artifact)
        artifact_path = self.agent.get_artifact_path(task_id, artifact)

        minio_endpoint = os.getenv("MINIO_ENDPOINT")
        minio_client = Minio(
            minio_endpoint,
            access_key=os.getenv("MINIO_ROOT_USER"),
            secret_key=os.getenv("MINIO_ROOT_PASSWORD"),
            secure=False,
        )

        # The destination bucket and filename on the MinIO server
        bucket_name = "default"

        with tempfile.NamedTemporaryFile(delete=False) as fp:
            tmp_file_path: str = fp.name
            print('tmp_file_path', tmp_file_path)

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

        # return FileResponse( # TODO: stream directly from MinIO instead of downloading to local filesystem
        #     path=path, media_type="application/octet-stream", filename=artifact.file_name
        # )


deployment = AgentDeployment.bind()
