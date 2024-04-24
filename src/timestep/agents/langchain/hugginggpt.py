from dataclasses import dataclass, field
from typing import List

from langchain.agents import AgentExecutor, Tool
from langchain.agents.react.agent import create_react_agent
from langchain.chains.llm import LLMChain
from langchain.memory import ChatMessageHistory
from langchain.schema import BaseChatMessageHistory
from langchain.tools.base import BaseTool
from langchain_community.tools.human.tool import HumanInputRun
from langchain_community.vectorstores.inmemory import InMemoryVectorStore
from langchain_core.embeddings.fake import DeterministicFakeEmbedding
from langchain_core.language_models import BaseChatModel
from langchain_core.language_models.fake_chat_models import FakeChatModel
from langchain_core.vectorstores import VectorStore, VectorStoreRetriever
from langchain_experimental.autonomous_agents import HuggingGPT
from langchain_experimental.autonomous_agents.baby_agi.task_creation import (
    TaskCreationChain,
)
from langchain_experimental.autonomous_agents.baby_agi.task_execution import (
    TaskExecutionChain,
)
from langchain_experimental.autonomous_agents.baby_agi.task_prioritization import (
    TaskPrioritizationChain,
)
from langchain_openai import ChatOpenAI, OpenAI

from timestep.agents.agent import Agent


class LangChainHuggingGPTAgent(Agent):
    @dataclass
    class Config:
        # ai_name: str = "LangChainAutoGPTAgent"
        # ai_role: str = "Assistant"
        # chain: LLMChain = None
        # chat_history_memory: BaseChatMessageHistory = field(default_factory=ChatMessageHistory)
        # human_in_the_loop: bool = True
        # feedback_tool: Optional[HumanInputRun] = None
        llm: BaseChatModel = field(default_factory=FakeChatModel)
        # max_iterations: int = 1
        # memory: VectorStoreRetriever = field(default_factory=_get_default_memory)
        # output_parser: BaseAutoGPTOutputParser = field(default_factory=AutoGPTOutputParser)
        # prefix: str = field(default_factory=_get_default_prefix)
        # suffix: str = field(default_factory=_get_default_suffix)
        # task_execution_chain: TaskExecutionChain = None
        tools: List[BaseTool] = field(default_factory=list)
        # vector_store: VectorStore = field(default_factory=_get_default_vector_store)
        # verbose: bool = True

        # def __post_init__(self):
        #     if self.chain is None:
        #         self.chain = LLMChain(
        #             llm=self.llm,
        #             prompt=AutoGPTPrompt(
        #                 ai_name=self.ai_name,
        #                 ai_role=self.ai_role,
        #                 input_variables=["memory", "messages", "goals", "user_input"],
        #                 token_counter=self.llm.get_num_tokens,
        #                 tools=self.tools,
        #             ),
        #             verbose=self.verbose,
        #         )

        #     if self.human_in_the_loop:
        #         self.feedback_tool = HumanInputRun()

        #     else:
        #         self.feedback_tool = None

        # agent = create_react_agent(
        #     llm=self.llm,
        #     prompt=prompt,
        #     tools=self.tools,
        # )

        # self.task_execution_chain = AgentExecutor.from_agent_and_tools(
        #     agent=ZeroShotAgent(
        #         allowed_tools=[tool.name for tool in self.tools],
        #         llm_chain=LLMChain(
        #             llm=self.llm,
        #             prompt=ZeroShotAgent.create_prompt(
        #                 input_variables=["objective", "task", "context", "agent_scratchpad"],
        #                 prefix=self.prefix,
        #                 suffix=self.suffix,
        #                 tools=self.tools,
        #             ),
        #             verbose=self.verbose,
        #         ),
        #     ),
        #     tools=self.tools,
        #     verbose=self.verbose,
        # )

        # if self.task_execution_chain is None:
        #     # execution_chain: Chain = TaskExecutionChain.from_llm(llm, verbose=verbose)
        #     self.task_execution_chain = TaskExecutionChain.from_llm(self.llm, verbose=self.verbose)

        # else:
        # execution_chain = self.task_execution_chain

    def __init__(
        self,
        # *,
        config: Config = Config(),
    ):
        super().__init__()

        # ai_name = config.ai_name
        # chain = config.chain
        # chat_history_memory = config.chat_history_memory
        # feedback_tool = config.feedback_tool
        # memory = config.memory
        # output_parser = config.output_parser
        # tools = config.tools

        # self.agent = AutoGPT(
        #     ai_name=ai_name,
        #     chain=chain,
        #     chat_history_memory=chat_history_memory,
        #     feedback_tool=feedback_tool,
        #     memory=memory,
        #     output_parser=output_parser,
        #     tools=tools,
        # )

        # self.agent = BabyAGI.from_llm(
        #     llm=config.llm,
        #     max_iterations=config.max_iterations,
        #     task_execution_chain=config.task_execution_chain,
        #     vectorstore=config.vector_store,
        #     verbose=config.verbose,
        # )

        # self.agent = BabyAGI(
        #     llm=config.llm,
        #     max_iterations=config.max_iterations,
        #     task_execution_chain=config.task_execution_chain,
        #     vectorstore=config.vector_store,
        #     verbose=config.verbose,
        # )

        # llm = config.llm
        # execution_chain = config.task_execution_chain
        # max_iterations = config.max_iterations
        # vectorstore = config.vector_store
        # verbose = config.verbose

        # task_creation_chain = TaskCreationChain.from_llm(llm, verbose=verbose)
        # task_prioritization_chain = TaskPrioritizationChain.from_llm(
        #     llm, verbose=verbose
        # )

        # # if task_execution_chain is None:
        # #     execution_chain: Chain = TaskExecutionChain.from_llm(llm, verbose=verbose)

        # # else:
        # #     execution_chain = task_execution_chain

        # self.agent = BabyAGI(
        #     task_creation_chain=task_creation_chain,
        #     task_prioritization_chain=task_prioritization_chain,
        #     execution_chain=execution_chain,
        #     max_iterations=max_iterations,
        #     vectorstore=vectorstore,
        #     # **kwargs,
        # )

        self.agent = HuggingGPT(
            llm=config.llm,
            # max_iterations=config.max_iterations,
            tools=config.tools,
        )

    # def step(self):
    # return self.agent.run(goals=[""])
