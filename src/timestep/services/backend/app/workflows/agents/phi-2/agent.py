import logging
import os
from typing import List

from agent_protocol import Artifact, Step, StepHandler, TaskDB, TaskHandler
from agent_protocol import Task as AgentProtocolTask
from agent_protocol.db import InMemoryTaskDB
from llama_index.agent import (
    AgentRunner,
    MultimodalReActAgentWorker,
)
from llama_index.agent.types import (
    Task as AgentRunnerTask,
)
from llama_index.callbacks import CallbackManager
from llama_index.chat_engine.types import (
    AGENT_CHAT_RESPONSE_TYPE,
)
from llama_index.multi_modal_llms import MultiModalLLM, OpenAIMultiModal
from tools import add_tool, divide_tool, multiply_tool, write_to_file_tool
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    set_seed,
)
from utils import StreamingCallbackHandler

logger = logging.getLogger(__name__)


class Agent:
    db: InMemoryTaskDB = InMemoryTaskDB()
    workspace: str = os.getenv("AGENT_WORKSPACE", "workspace")

    def __init__(
            self,
            db: TaskDB,
            workspace: str
    ) -> None:
        self.db = db
        self.models = {}
        self.tokenizers = {}
        self.workspace = workspace

        self.reset()

    async def create_task(self, input: str, additional_input: str) -> AgentProtocolTask:
        """
        Creates a task for the agent.
        """
        # image_document = ImageDocument(image_path="data/dev_day.png")

        agent_runner_task: AgentRunnerTask = self.agent_runner.create_task(
            input,
            # extra_state={"image_docs": [image_document]},
            # extra_state={},
            extra_state={"image_docs": []}
        )

        agent_runner_task_id = agent_runner_task.task_id
        # additional_input["agent_runner_task_id"] = agent_runner_task_id
        task: AgentProtocolTask = await self.db.create_task(input, additional_input)

        async def task_handler(task: AgentProtocolTask) -> None:
            agent_runner_task_step_id = self.agent_runner.get_upcoming_steps(
                task_id=agent_runner_task_id
            )[0].step_id

            # await Agent.db.create_step(task_id=task.task_id, name="plan", ...)
            await self.db.create_step(
                task.task_id,
                name="plan",
                input=task.input,
                is_last=False,
                additional_properties={
                    "agent_runner_task_id": agent_runner_task_id,
                    "agent_runner_task_step_id": agent_runner_task_step_id
                },
                # artifacts=[],
                artifacts=task.artifacts,
            )

        await task_handler(task)

        return task

    async def execute(self, step: Step) -> Step:
        # Use tools, websearch, etc.
        agent_runner_task_id = step.additional_properties["agent_runner_task_id"]
        agent_runner_task_step_id = step.additional_properties["agent_runner_task_step_id"]
        agent_runner_task: AgentRunnerTask = self.agent_runner.get_task(task_id=agent_runner_task_id)

        def execute_step(agent_runner: AgentRunner, agent_runner_task: AgentRunnerTask):
            step_output = agent_runner.run_step(agent_runner_task.task_id)

            if step_output.is_last:
                response = agent_runner.finalize_response(agent_runner_task.task_id)
                print(f"> Agent finished: {str(response)}")
                return response

            else:
                return None

        def execute_steps(agent_runner: AgentRunner, agent_runner_task: AgentRunnerTask):
            response = execute_step(agent_runner, agent_runner_task)

            while response is None:
                response = execute_step(agent_runner, agent_runner_task)

            return response

        response: AGENT_CHAT_RESPONSE_TYPE | None = execute_step(self.agent_runner, agent_runner_task)

        step.output = str(response)

        return step

    def get_artifact_folder(self, task_id: str, artifact: Artifact) -> str:
        """
        Get the artifact folder for the specified task and artifact.
        """
        # workspace_path = Agent.get_workspace(task_id)
        workspace_path = self.get_workspace(task_id)
        relative_path = artifact.relative_path or ""
        # return os.path.join(workspace_path, relative_path)
        # return f"{workspace_path}/{relative_path}"
        return f"{workspace_path}" if relative_path == "" else f"{workspace_path}/{relative_path}"

    def get_artifact_path(self, task_id: str, artifact: Artifact) -> str:
        """
        Get the artifact path for the specified task and artifact.
        """
        # return os.path.join(
        #     # Agent.get_artifact_folder(task_id, artifact), artifact.file_name
        #     self.get_artifact_folder(task_id, artifact), artifact.file_name
        # )
        return f"{self.get_artifact_folder(task_id, artifact)}/{artifact.file_name}"

    async def get_tasks(self) -> List[AgentProtocolTask]:
        """
        List all tasks that have been created for the agent.
        """
        return await self.db.list_tasks()

    def get_workspace(self, task_id: str) -> str:
        """
        Get the workspace path for the specified task.
        """
        # return os.path.join(os.getcwd(), Agent.workspace, task_id)
        # return os.path.join(os.getcwd(), self.workspace, task_id)
        # bucket_name = "default"
        # return f"s3://{bucket_name}/{self.workspace}/{task_id}"
        return f"{self.workspace}/{task_id}"

    # async def plan(self, step: Step) -> Step:
    #     task = await Agent.db.get_task(step.task_id)
    #     steps = generete_steps(task.input)

    #     last_step = steps[-1]
    #     for step in steps[:-1]:
    #         await Agent.db.create_step(task_id=task.task_id, name=step, ...)

    #     await Agent.db.create_step(task_id=task.task_id, name=last_step, is_last=True)
    #     step.output = steps
    #     return step

    def reset(self, seed: int = 42):
        """
        Reset the agent's state.
        """
        set_seed(seed)

        checkpoint = "microsoft/phi-2"
        tokenizer = AutoTokenizer.from_pretrained(checkpoint, trust_remote_code=True)
        self.tokenizers[checkpoint] = tokenizer

        model = AutoModelForCausalLM.from_pretrained(
            checkpoint,
            device_map="auto",
            # pad_token_id=tokenizer.eos_token_id,
            trust_remote_code=True,
        )
        self.models[checkpoint] = model

        self.tools = [add_tool, divide_tool, multiply_tool, write_to_file_tool]

        handler = StreamingCallbackHandler()
        callback_manager = CallbackManager([handler])

        multi_modal_llm = MultiModalLLM(
            model=model,
            max_new_tokens=1000,
        )

        multi_modal_react_agent_worker: MultimodalReActAgentWorker = (
            MultimodalReActAgentWorker.from_tools(
                self.tools,
                multi_modal_llm=multi_modal_llm,
                verbose=True,
            )
        )

        self.agent_runner = AgentRunner(
            agent_worker=multi_modal_react_agent_worker,
            callback_manager=callback_manager,
            # init_task_state_kwargs=init_task_state_kwargs,
        )

        logger.info("Built agent.")

    async def step(self, step: Step) -> Step:
        """
        Step the agent.
        """
        logger.info(f"Stepping agent for task {step.task_id}.")
        print(f"Stepping agent for task {step.task_id}.")

        # if step.name == "plan":
        #     await self.plan(step)

        # elif step.name == "train":
        #     await self.train(step)

        # else:
        #     await self.execute(step)

        step = await self.execute(step)

        return step

    async def train(self, step: Step) -> Step:
        """
        Train the agent.
        """
        return step
