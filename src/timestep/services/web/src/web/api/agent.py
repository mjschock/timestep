from typing import List

from agent_protocol import Agent, Step, Task, router  # noqa: F401
from web.db.task import TimestepAITaskDB

Agent.db = TimestepAITaskDB()


async def task_handler(task: Task) -> None:
    # await Agent.db.create_step(task_id=task.task_id, name="plan", ...)
    await Agent.db.create_step(task_id=task.task_id, name="plan")


def generete_steps(input: str) -> List[str]:
    raise NotImplementedError


async def plan(step: Step) -> Step:
    task = await Agent.db.get_task(step.task_id)
    steps = generete_steps(task.input)

    last_step = steps[-1]
    for step in steps[:-1]:
        #    await Agent.db.create_step(task_id=task.task_id, name=step, ...)
        await Agent.db.create_step(task_id=task.task_id, name=step)

    await Agent.db.create_step(task_id=task.task_id, name=last_step, is_last=True)
    step.output = steps
    return step


async def execute(step: Step) -> Step:
    # Use tools, websearch, etc.
    raise NotImplementedError


async def step_handler(step: Step) -> Step:
    if step.name == "plan":
        await plan(step)
    else:
        await execute(step)

    return step


Agent.setup_agent(task_handler, step_handler)
