from __future__ import annotations

from dataclasses import dataclass, field

from langchain.chains.llm import LLMChain
from langchain.memory import ChatMessageHistory
from langchain.schema import BaseChatMessageHistory
from langchain.tools.base import BaseTool
from langchain_community.tools.human.tool import HumanInputRun
from langchain_community.vectorstores.inmemory import InMemoryVectorStore
from langchain_core.embeddings.fake import DeterministicFakeEmbedding
from langchain_core.language_models import BaseChatModel
from langchain_core.language_models.fake_chat_models import FakeChatModel
from langchain_core.vectorstores import VectorStoreRetriever
from langchain_experimental.autonomous_agents import AutoGPT
from langchain_experimental.autonomous_agents.autogpt.output_parser import (
    AutoGPTOutputParser,
    BaseAutoGPTOutputParser,
)
from langchain_experimental.autonomous_agents.autogpt.prompt import AutoGPTPrompt
from pettingzoo.utils.env import ActionType

from timestep.agents.agent import Agent


def _get_default_memory():  # type: ignore[no-untyped-def]
    return InMemoryVectorStore(
        embedding=DeterministicFakeEmbedding(size=512)
    ).as_retriever()


class LangChainAutoGPTAgent(Agent):
    @dataclass
    class Config:
        ai_name: str = "LangChainAutoGPTAgent"
        ai_role: str = "Assistant"
        chain: LLMChain = None
        chat_history_memory: BaseChatMessageHistory = field(
            default_factory=ChatMessageHistory
        )
        human_in_the_loop: bool = True
        feedback_tool: HumanInputRun | None = None
        llm: BaseChatModel = field(default_factory=FakeChatModel)
        memory: VectorStoreRetriever = field(default_factory=_get_default_memory)
        output_parser: BaseAutoGPTOutputParser = field(
            default_factory=AutoGPTOutputParser
        )
        tools: list[BaseTool] = field(default_factory=list)
        verbose: bool = True

        def __post_init__(self) -> None:
            if self.chain is None:
                self.chain = LLMChain(
                    llm=self.llm,
                    prompt=AutoGPTPrompt(
                        ai_name=self.ai_name,
                        ai_role=self.ai_role,
                        input_variables=["memory", "messages", "goals", "user_input"],
                        token_counter=self.llm.get_num_tokens,
                        tools=self.tools,
                    ),
                    verbose=self.verbose,
                )

            if self.human_in_the_loop:
                self.feedback_tool = HumanInputRun()

            else:
                self.feedback_tool = None

    def __init__(
        self,
        *,
        config: Config = Config(),  # noqa: B008
    ):
        super().__init__()

        ai_name = config.ai_name
        chain = config.chain
        chat_history_memory = config.chat_history_memory
        feedback_tool = config.feedback_tool
        memory = config.memory
        output_parser = config.output_parser
        tools = config.tools

        self.agent = AutoGPT(
            ai_name=ai_name,
            chain=chain,
            chat_history_memory=chat_history_memory,
            feedback_tool=feedback_tool,
            memory=memory,
            output_parser=output_parser,
            tools=tools,
        )

    def step(  # type: ignore[no-untyped-def]
        self,
        observation,  # noqa: ARG002
        reward,  # noqa: ARG002
        termination,  # noqa: ARG002
        truncation,  # noqa: ARG002
        info,  # noqa: ARG002
        *args,  # noqa: ARG002
        **kwargs,  # noqa: ARG002
    ) -> ActionType:
        # action = super().step(observation, reward, termination, truncation, info)

        # observation = self.sense(observation, reward, termination, truncation, info)
        # orientation = self.orient(observation, reward, termination, truncation, info)
        # action = self.decide(orientation)
        # action = self.act(observation, reward, termination, truncation, info)

        # def observe(
        #     observation, reward, termination, truncation, info, *args, **kwargs
        # ):
        #     return observation

        # def orient(observation, reward, termination, truncation, info, *args, **kwargs):
        #     orientation = {
        #         "goals": [""],
        #     }

        #     return orientation

        # def decide(
        #     orientation,
        #     observation,
        #     reward,
        #     termination,
        #     truncation,
        #     info,
        #     *args,
        #     **kwargs,
        # ):
        #     decision = self.agent.run(**orientation)

        #     return decision

        # def act(
        #     decision,
        #     observation,
        #     reward,
        #     termination,
        #     truncation,
        #     info,
        #     *args,
        #     **kwargs,
        # ):
        #     return decision

        # observation = observe(
        #     observation, reward, termination, truncation, info, *args, **kwargs
        # )
        # orientation = orient(
        #     observation, reward, termination, truncation, info, *args, **kwargs
        # )
        # decision = decide(
        #     orientation,
        #     observation,
        #     reward,
        #     termination,
        #     truncation,
        #     info,
        #     *args,
        #     **kwargs,
        # )
        # action = act(
        #     decision,
        #     observation,
        #     reward,
        #     termination,
        #     truncation,
        #     info,
        #     *args,
        #     **kwargs,
        # )

        return self.agent.run(
            goals=[""],
        )
