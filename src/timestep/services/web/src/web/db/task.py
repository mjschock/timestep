import uuid
from typing import Any, Dict, List, Optional

from agent_protocol import Artifact, Status, Step, Task, TaskDB
from agent_protocol.db import NotFoundException
from web.db.env import envs_by_id


class TimestepAITaskDB(TaskDB):
    _tasks: Dict[str, Task] = {
        f"{env[0]}": Task(
            task_id=f"{env[0]}",
            input=None,
            steps=[],
            artifacts=[],
            additional_input=None,
        )
        for env in envs_by_id.items()
    }

    async def create_task(
        self,
        input: Optional[str],
        additional_input: Any = None,
        artifacts: Optional[List[Artifact]] = None,
        steps: Optional[List[Step]] = None,
    ) -> Task:
        # if not steps:
        #     steps = []
        # if not artifacts:
        #     artifacts = []
        # task_id = str(uuid.uuid4())
        # task = Task(
        #     task_id=task_id,
        #     input=input,
        #     steps=steps,
        #     artifacts=artifacts,
        #     additional_input=additional_input,
        # )
        # self._tasks[task_id] = task
        # return task

        raise NotImplementedError

    async def create_step(
        self,
        task_id: str,
        name: Optional[str] = None,
        input: Optional[str] = None,
        is_last=False,
        additional_properties: Optional[Dict[str, Any]] = None,
        artifacts: List[Artifact] = [],
    ) -> Step:
        step_id = str(uuid.uuid4())
        step = Step(
            task_id=task_id,
            step_id=step_id,
            name=name,
            input=input,
            status=Status.created,
            is_last=is_last,
            additional_properties=additional_properties,
            artifacts=artifacts,
        )
        task = await self.get_task(task_id)
        task.steps.append(step)
        return step

    async def get_task(self, task_id: str) -> Task:
        task = self._tasks.get(task_id, None)
        if not task:
            raise NotFoundException("Task", task_id)
        return task

    async def get_step(self, task_id: str, step_id: str) -> Step:
        task = await self.get_task(task_id)
        step = next(filter(lambda s: s.task_id == task_id, task.steps), None)
        if not step:
            raise NotFoundException("Step", step_id)
        return step

    async def get_artifact(self, task_id: str, artifact_id: str) -> Artifact:
        task = await self.get_task(task_id)
        artifact = next(
            filter(lambda a: a.artifact_id == artifact_id, task.artifacts), None
        )
        if not artifact:
            raise NotFoundException("Artifact", artifact_id)
        return artifact

    async def create_artifact(
        self,
        task_id: str,
        file_name: str,
        agent_created: bool = True,
        relative_path: Optional[str] = None,
        step_id: Optional[str] = None,
    ) -> Artifact:
        artifact_id = str(uuid.uuid4())
        artifact = Artifact(
            artifact_id=artifact_id,
            agent_created=agent_created,
            file_name=file_name,
            relative_path=relative_path,
        )
        task = await self.get_task(task_id)
        task.artifacts.append(artifact)

        if step_id:
            step = await self.get_step(task_id, step_id)
            step.artifacts.append(artifact)

        return artifact

    async def list_tasks(self) -> List[Task]:
        return [task for task in self._tasks.values()]

    async def list_steps(
        self, task_id: str, status: Optional[Status] = None
    ) -> List[Step]:
        task = await self.get_task(task_id)
        steps = task.steps
        if status:
            steps = list(filter(lambda s: s.status == status, steps))
        return steps
