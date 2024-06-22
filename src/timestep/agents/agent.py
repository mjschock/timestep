# class Agent(mesa.Agent):
# TODO: Take inspiration from https://pettingzoo.farama.org/tutorials/langchain/langchain/#gymnasium-agent
from __future__ import annotations

from pettingzoo.utils.env import ActionType


class Agent:
    """
    An agent.
    """

    # def __init__(self, unique_id, model):
    #     """
    #     Customize the agent
    #     """
    #     self.unique_id = unique_id
    #     super().__init__(unique_id, model)

    def act(  # type: ignore[no-untyped-def]
        self, observation, reward, termination, truncation, info
    ) -> ActionType:
        """
        Observe, orient, decide, etc. and return an action.
        """

        raise NotImplementedError

    # TODO: rename to `step` and either package up the observation, reward, termination, truncation, and info into a single object that could have different fields or add @overload to the method signature for the env.step method
