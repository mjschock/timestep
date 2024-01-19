import logging
import os
from typing import List

from agent_protocol import StepHandler, TaskDB, TaskHandler
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
from llama_index.multi_modal_llms import MultiModalLLM, OpenAIMultiModal
from tools import add_tool, divide_tool, multiply_tool
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    set_seed,
)
from utils import StreamingCallbackHandler

# logger = logging.getLogger("uvicorn")
logger = logging.getLogger(__name__)


class Agent:
    db: InMemoryTaskDB = InMemoryTaskDB()
    workspace: str = os.getenv("AGENT_WORKSPACE", "workspace")

    def __init__(
            self,
            db: TaskDB,
            # step_handler: StepHandler,
            # task_handler: TaskHandler,
            workspace: str
    ) -> None:
        self.db = db
        self.models = {}
        # self.step_handler = step_handler
        # self.task_handler = task_handler
        self.tokenizers = {}
        self.workspace = workspace

        # checkpoint = "gpt2"
        # tokenizer = AutoTokenizer.from_pretrained(checkpoint)
        # model = AutoModelForCausalLM.from_pretrained(
        #     checkpoint,
        #     device_map="auto",
        #     pad_token_id=tokenizer.eos_token_id,
        # )

        # self.model = model
        # self.tokenizer = tokenizer

        # self.agent = LocalAgent(
        #     self.model,
        #     self.tokenizer,
        #     additional_tools=None,
        #     chat_prompt_template=None,
        #     run_prompt_template=None,
        # )

    def chat(self, conversation):
        self.reset()

        try:
            # https://huggingface.co/docs/transformers/main/en/main_classes/tokenizer#transformers.PreTrainedTokenizerFast.apply_chat_template
            token_ids: List[int] = self.tokenizers["gpt2"].apply_chat_template(
                conversation,
                add_generation_prompt=True,
                return_tensors="pt",
                tokenize=True,
            )

            # return self.tokenizers["gpt2"].decode(token_ids[0])

            # https://huggingface.co/docs/transformers/main_classes/model.html#transformers.PreTrainedModel.generate
            outputs = self.models["gpt2"].generate(
                token_ids,
                do_sample=True,
                top_k=50,
                top_p=0.95,
                temperature=0.9,
                max_length=200,
                min_length=50,
                num_return_sequences=1,
            )

            return self.tokenizers["gpt2"].decode(outputs[0])
            # return self.tokenizers["gtp2"].batch_decode(outputs, skip_special_tokens=True)[0]

        except Exception as e:
            return str(e)

        # return self.agent.chat(messages)
        return "Hello worlds!"

    async def create_task(self, input: str, additional_input: str) -> AgentProtocolTask:
        """
        Creates a task for the agent.
        """
        # image_document = ImageDocument(image_path="data/dev_day.png")

        agent_runner_task: AgentRunnerTask = self.agent_runner.create_task(
            input,
            # extra_state={"image_docs": [image_document]},
            extra_state={},
        )

        agent_runner_task_id = agent_runner_task.task_id
        additional_input["agent_runner_task_id"] = agent_runner_task_id
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
                    "agent_runner_task_id": agent_runner_task.task_id,
                    "agent_runner_task_step_id": agent_runner_task_step_id
                },
                # artifacts=[],
                artifacts=task.artifacts,
            )

        await task_handler(task)

        return task

    async def get_tasks(self) -> List[AgentProtocolTask]:
        """
        List all tasks that have been created for the agent.
        """
        return await self.db.list_tasks()

    def reset(self, seed: int = 42):
        """
        Reset the agent's state.
        """
        set_seed(seed)

        checkpoint = "gpt2" # "distilgpt2"
        tokenizer = AutoTokenizer.from_pretrained(checkpoint)
        self.tokenizers[checkpoint] = tokenizer

        model = AutoModelForCausalLM.from_pretrained(
            checkpoint,
            device_map="auto",
            pad_token_id=tokenizer.eos_token_id,
        )
        self.models[checkpoint] = model

        self.tools = [add_tool, divide_tool, multiply_tool]

        handler = StreamingCallbackHandler()
        callback_manager = CallbackManager([handler])

        multi_modal_llm: MultiModalLLM = OpenAIMultiModal(
            model="gpt-4-vision-preview",
            max_new_tokens=1000
        )
        # TODO: multi_modal_llm = MultiModalLLM()

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

    # @staticmethod
    # def setup_agent(task_handler: TaskHandler, step_handler: StepHandler):
    #     """
    #     Set the agent's task and step handlers.
    #     """
    #     global _task_handler
    #     _task_handler = task_handler

    #     global _step_handler
    #     _step_handler = step_handler

    #     return Agent

    # @staticmethod
    # def get_workspace(task_id: str) -> str:
    #     """
    #     Get the workspace path for the specified task.
    #     """
    #     return os.path.join(os.getcwd(), Agent.workspace, task_id)

    # @staticmethod
    # def get_artifact_folder(task_id: str, artifact: Artifact) -> str:
    #     """
    #     Get the artifact path for the specified task and artifact.
    #     """
    #     workspace_path = Agent.get_workspace(task_id)
    #     relative_path = artifact.relative_path or ""
    #     return os.path.join(workspace_path, relative_path)

    # @staticmethod
    # def get_artifact_path(task_id: str, artifact: Artifact) -> str:
    #     """
    #     Get the artifact path for the specified task and artifact.
    #     """
    #     return os.path.join(
    #         Agent.get_artifact_folder(task_id, artifact), artifact.file_name
    #     )
