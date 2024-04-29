from __future__ import annotations

import pytest

from timestep.agents.agent import Agent
from timestep.agents.langchain.autogpt import LangChainAutoGPTAgent

# def _input_func() -> str:
#     return "q"

# def _prompt_func(query: str) -> None:
#     print("\n")
#     print(query)

# class HumanInputRun(BaseTool):
#     """Tool that asks user for input."""

#     name: str = "human"
#     description: str = (
#         "You can ask a human for guidance when you think you "
#         "got stuck or you are not sure what to do next. "
#         "The input should be a question for the human."
#     )
#     # prompt_func: Callable[[str], None] = Field(default_factory=lambda: _print_func)
#     # input_func: Callable = Field(default_factory=lambda: input)
#     input_func: Callable = Field(default_factory=lambda: _input_func)
#     prompt_func: Callable[[str], None] = Field(default_factory=lambda: _prompt_func)

#     def _run(
#         self,
#         query: str,
#         run_manager: Optional[CallbackManagerForToolRun] = None,
#     ) -> str:
#         """Use the Human input tool."""
#         self.prompt_func(query)
#         return self.input_func()

# class HumanInputRunQuitter(HumanInputRun):


def test_langchain_autogpt_agent():
    config = LangChainAutoGPTAgent.Config(
        # human_in_the_loop=True,
        # feedback_tool=FeedbackTool(),
        # verbose=True,
    )

    agent = LangChainAutoGPTAgent(config=config)

    assert isinstance(agent, Agent)

    with pytest.raises(TypeError):
        # agent.step()
        agent.agent.run()
