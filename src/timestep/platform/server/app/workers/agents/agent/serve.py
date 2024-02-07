import json
import os
from typing import Annotated, List, Optional

from fastapi import FastAPI, File, Form, Response, UploadFile, status
from fastapi.responses import StreamingResponse
from forge.db import ForgeDatabase
from forge.sdk import (
    AgentDB,
    Artifact,
    LocalWorkspace,
    Step,
    StepRequestBody,
    Task,
    TaskListResponse,
    TaskRequestBody,
    TaskStepsListResponse,
    Workspace,
)
from forge.sdk.errors import NotFoundError
from ray import serve

from agent import ForgeAgent

app = FastAPI()


@serve.deployment
@serve.ingress(app)
class AgentDeployment:
    def __init__(self) -> None:
        database_string = os.getenv("DATABASE_STRING", "sqlite:///agent.db")
        database: AgentDB = ForgeDatabase(
            database_string=database_string,
            debug_enabled=False,
        )
        workspace: Workspace = LocalWorkspace(
            base_path=os.getenv("AGENT_WORKSPACE", "workspace"),
        )

        self.agent = ForgeAgent(
            database=database,
            workspace=workspace,
        )

    @app.get("/livez")
    async def is_live(self) -> str:
        return "ok"

    @app.get("/readyz")
    async def is_ready(self) -> str:
        return "ok"

    @app.post("/ap/v1/agent/tasks", response_model=Task, tags=["agent"])
    async def create_agent_task(self, task_request: TaskRequestBody | None = None) -> Task:
        """
        Creates a new task using the provided TaskRequestBody and returns a Task.

        Args:
            request (Request): FastAPI request object.
            task (TaskRequestBody): The task request containing input and additional input data.

        Returns:
            Task: A new task with task_id, input, additional_input, and empty lists for artifacts and steps.

        Example:
            Request (TaskRequestBody defined in schema.py):
                {
                    "input": "Write the words you receive to the file 'output.txt'.",
                    "additional_input": "python/code"
                }

            Response (Task defined in schema.py):
                {
                    "task_id": "50da533e-3904-4401-8a07-c49adf88b5eb",
                    "input": "Write the word 'Washington' to a .txt file",
                    "additional_input": "python/code",
                    "artifacts": [],
                }
        """
        try:
            task_request = await self.agent.create_task(
                task_request=task_request,
            )

            return Response(
                content=task_request.json(),
                status_code=status.HTTP_200_OK,
                media_type="application/json",
            )

        except Exception:
            return Response(
                content=json.dumps({"error": "Internal server error"}),
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                media_type="application/json",
            )

    @app.get("/ap/v1/agent/tasks", response_model=TaskListResponse, tags=["agent"])
    async def list_agent_tasks_ids(
        self, page_size: int = 10, current_page: int = 1
    ) -> List[str]:
        """
        List all tasks that have been created for the agent.
        """
        return await self.agent.list_tasks(
            page=current_page,
            pageSize=page_size,
        )

    @app.get("/ap/v1/agent/tasks/{task_id}", response_model=Task, tags=["agent"])
    async def get_agent_task(self, task_id: str) -> Task:
        """
        Get details about a specified agent task.
        """
        return await self.agent.get_task(
            task_id=task_id,
        )

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
        return await self.agent.list_steps(
            task_id=task_id,
            page=current_page,
            pageSize=page_size,
        )

    @app.post(
        "/ap/v1/agent/tasks/{task_id}/steps",
        response_model=Step,
        tags=["agent"],
    )
    async def execute_agent_task_step(
        self, task_id: str, step: Optional[StepRequestBody] = None
    ) -> Step:
        """
        Executes the next step for a specified task based on the current task status and returns the
        executed step with additional feedback fields.

        Depending on the current state of the task, the following scenarios are supported:

        1. No steps exist for the task.
        2. There is at least one step already for the task, and the task does not have a completed step marked as `last_step`.
        3. There is a completed step marked as `last_step` already on the task.

        In each of these scenarios, a step object will be returned with two additional fields: `output` and `additional_output`.
        - `output`: Provides the primary response or feedback to the user.
        - `additional_output`: Supplementary information or data. Its specific content is not strictly defined and can vary based on the step or agent's implementation.

        Args:
            request (Request): FastAPI request object.
            task_id (str): The ID of the task.
            step (StepRequestBody): The details for executing the step.

        Returns:
            Step: Details of the executed step with additional feedback.

        Example:
            Request:
                POST /agent/tasks/50da533e-3904-4401-8a07-c49adf88b5eb/steps
                {
                    "input": "Step input details...",
                    ...
                }

            Response:
                {
                    "task_id": "50da533e-3904-4401-8a07-c49adf88b5eb",
                    "step_id": "step1_id",
                    "output": "Primary feedback...",
                    "additional_output": "Supplementary details...",
                    ...
                }
        """
        try:
            # An empty step request represents a yes to continue command
            if not step:
                step = StepRequestBody(input="y")

            step = await self.agent.execute_step(
                task_id=task_id,
                step_request=step,
            )

            return Response(
                content=step.json(),
                status_code=status.HTTP_200_OK,
                media_type="application/json",
            )

        except NotFoundError:
            return Response(
                content=json.dumps({"error": f"Task not found {task_id}"}),
                status_code=status.HTTP_404_NOT_FOUND,
                media_type="application/json",
            )

        except Exception:
            return Response(
                content=json.dumps({"error": "Internal server error"}),
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                media_type="application/json",
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
        return await self.agent.get_step(
            task_id=task_id,
            step_id=step_id,
        )

    @app.get(
        "/ap/v1/agent/tasks/{task_id}/artifacts",
        response_model=List[Artifact],
        tags=["agent"],
    )
    async def list_agent_task_artifacts(self, task_id: str) -> List[Artifact]:
        """
        List all artifacts for the specified task.
        """
        return await self.agent.list_artifacts(
            task_id=task_id,
            page=1,
            pageSize=10,
        )

    @app.post(
        "/ap/v1/agent/tasks/{task_id}/artifacts",
        response_model=Artifact,
        tags=["agent"],
    )
    async def upload_agent_task_artifacts(
        self,
        task_id: str,
        file: Annotated[UploadFile, File()],
        relative_path: Annotated[Optional[str], Form()] = "",
    ) -> Artifact:
        """
        This endpoint is used to upload an artifact associated with a specific task. The artifact is provided as a file.

        Args:
            request (Request): The FastAPI request object.
            task_id (str): The unique identifier of the task for which the artifact is being uploaded.
            file (UploadFile): The file being uploaded as an artifact.
            relative_path (str): The relative path for the file. This is a query parameter.

        Returns:
            Artifact: An object containing metadata of the uploaded artifact, including its unique identifier.

        Example:
            Request:
                POST /agent/tasks/50da533e-3904-4401-8a07-c49adf88b5eb/artifacts?relative_path=my_folder/my_other_folder
                File: <uploaded_file>

            Response:
                {
                    "artifact_id": "b225e278-8b4c-4f99-a696-8facf19f0e56",
                    "created_at": "2023-01-01T00:00:00Z",
                    "modified_at": "2023-01-01T00:00:00Z",
                    "agent_created": false,
                    "relative_path": "/my_folder/my_other_folder/",
                    "file_name": "main.py"
                }
        """
        if file is None:
            return Response(
                content=json.dumps({"error": "File must be specified"}),
                status_code=404,
                media_type="application/json",
            )

        try:
            artifact = await self.agent.create_artifact(
                task_id=task_id,
                file=file,
                relative_path=relative_path,
            )

            return Response(
                content=artifact.json(),
                status_code=status.HTTP_200_OK,
                media_type="application/json",
            )

        except Exception:
            return Response(
                content=json.dumps({"error": "Internal server error"}),
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                media_type="application/json",
            )

    @app.get(
        "/ap/v1/agent/tasks/{task_id}/artifacts/{artifact_id}",
        tags=["agent"],
    )
    async def download_agent_task_artifacts(
        self, task_id: str, artifact_id: str
    ) -> StreamingResponse:
        """
        Download the specified artifact.
        """
        return await self.agent.get_artifact(
            task_id=task_id,
            artifact_id=artifact_id,
        )


deployment = AgentDeployment.bind()
