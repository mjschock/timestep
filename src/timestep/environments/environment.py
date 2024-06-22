from __future__ import annotations

from typing import Any

import gymnasium.spaces
import numpy as np
from pettingzoo.utils.conversions import parallel_wrapper_fn
from pettingzoo.utils.env import ActionType, AECEnv, AgentID, ObsType

from timestep.agents.agent import Agent


class Environment(
    # BaseWrapper,
    AECEnv,  # type: ignore[misc]
    Agent,  # https://pettingzoo.farama.org/content/basic_usage/#environment-as-an-agent
    # Model,
):
    """
    An environment.
    """

    # Cumulative rewards for each agent
    _cumulative_rewards: dict[AgentID, float]

    # Action space for each agent
    action_spaces: dict[AgentID, gymnasium.spaces.Space]

    agent_selection: AgentID  # The agent currently being stepped
    agents: list[AgentID]  # Agents active at any given time

    infos: dict[
        AgentID, dict[str, Any]
    ]  # Additional information from the last step for each agent

    observation_spaces: dict[
        AgentID, gymnasium.spaces.Space
    ]  # Observation space for each agent

    metadata: dict[str, Any]  # Metadata for the environment

    # All agents that may appear in the environment
    possible_agents: list[AgentID]

    rewards: dict[AgentID, float]  # Reward from the last step for each agent

    # Whether each agent has just reached a terminal state
    terminations: dict[AgentID, bool]
    truncations: dict[AgentID, bool]

    def __init__(
        self,
        max_cycles: int | None = None,
        render_mode: str | None = None,
        *args: list[Any],  # noqa: ARG002
        **kwargs: dict[str, Any],  # noqa: ARG002
    ):
        env_name = "env_0"  # f"{env_name}" or "env"?
        self.metadata = {
            "is_parallelizable": True,
            "name": f"{env_name}",
            "render_modes": ["ansi", "human", "rgb_array", "svg"],
        }

        self.reset()

        self.max_cycles = max_cycles
        # self.max_cycles = kwargs.get("max_cycles", None)
        self.render_mode = render_mode
        # self.render_mode = kwargs.get("render_mode", "human")

    def close(self) -> None:
        """Closes any resources that should be released.

        Closes the rendering window, subprocesses, network connections,
        or any other resources that should be released.
        """

    def action_space(self, agent: AgentID) -> gymnasium.spaces.Space:
        """Takes in agent and returns the action space for that agent.

        MUST return the same value for the same agent name

        Default implementation is to return the action_spaces dict
        """
        return self.action_spaces[agent]

    def observation_space(self, agent: AgentID) -> gymnasium.spaces.Space:
        """Takes in agent and returns the observation space for that agent.

        MUST return the same value for the same agent name

        Default implementation is to return the observation_spaces dict
        """
        return self.observation_spaces[agent]

    def observe(self, agent: AgentID) -> ObsType | None:
        """Returns the observation an agent currently can make.

        `last()` calls this function.
        """
        observation = self.observation_space(agent).sample()

        # if isinstance(observation, str):
        #     # observation = np.array([observation])
        #     # convert string to list of characters
        #     observation = list(observation)
        #     # convert list of characters to numbers
        #     observation = [ord(character) for character in observation]
        #     observation = np.array(observation)

        assert isinstance(
            observation, np.ndarray
        ), f"Observation must be a numpy array, got {type(observation)}."

        return observation

    def render(self) -> None | np.ndarray | str | list[Any]:
        """Renders the environment as specified by self.render_mode.

        Render mode can be `human` to display a window.
        Other render modes in the default environments are `'rgb_array'`
        which returns a numpy array and is supported by all environments outside of classic,
        and `'ansi'` which returns the strings printed (specific to classic environments).
        """
        if self.render_mode == "ansi":
            return ""

        elif self.render_mode == "human":  # noqa: RET505
            return None

        elif self.render_mode == "rgb_array":
            return self.observe(self.agent_selection)

        elif self.render_mode == "svg":
            return ""

        else:
            msg = f"Invalid render mode: {self.render_mode}"
            raise ValueError(msg)

    def reset(
        self,
        seed: int = 42,
        options: dict[str, Any] | None = None,  # noqa: ARG002
    ) -> tuple[dict[AgentID, ObsType], dict[AgentID, dict[str, Any]]]:
        """
        Reset the environment to its initial state.
        """
        # self.agents = self.possible_agents[:]
        # self.rewards = {agent: 0 for agent in self.agents}
        # self._cumulative_rewards = {agent: 0 for agent in self.agents}
        # self.terminations = {agent: False for agent in self.agents}
        # self.truncations = {agent: False for agent in self.agents}
        # self.infos = {agent: {} for agent in self.agents}
        # self.state = {agent: NONE for agent in self.agents}
        # self.observations = {agent: NONE for agent in self.agents}
        # self.num_moves = 0
        # """
        # Our agent_selector utility allows easy cyclic stepping through the agents list.
        # """
        # self._agent_selector = agent_selector(self.agents)
        # self.agent_selection = self._agent_selector.next()

        env_name = str(self)
        assert env_name == "env_0", f"{env_name} != env_0"
        # box_shape = (2048, 2048, 3)
        box_shape = (256, 256, 3)

        self._cumulative_rewards = {f"{env_name}": 0}
        self.action_spaces = {
            f"{env_name}": gymnasium.spaces.Box(
                low=0.0, high=255.0, shape=box_shape, dtype=np.uint8, seed=seed
            )
        }
        self.agent_selection = f"{env_name}"
        self.agents = [f"{env_name}"]
        self.infos = {f"{env_name}": {}}
        # metadata = {"render_modes": ["human"], "name": "rps_v2"}
        # self.metadata = { "is_parallelizable": True, "name": f"{env_name}", "render.modes": ["human", "rgb_array"] }
        self.num_moves = 0
        # self.observation_spaces = { f"{env_name}": gymnasium.spaces.Text(min_length=2, max_length=2) }
        self.observation_spaces = {
            f"{env_name}": gymnasium.spaces.Box(
                low=0.0, high=255.0, shape=box_shape, dtype=np.uint8, seed=seed
            )
        }
        self.possible_agents = [f"{env_name}"]
        self.rewards = {f"{env_name}": 0}
        self.terminations = {f"{env_name}": False}
        self.timestep = 0
        self.truncations = {f"{env_name}": False}

        observations = {agent_id: self.observe(agent_id) for agent_id in self.agents}

        return observations, self.infos

    def step(self, action: ActionType) -> None:
        """Accepts and executes the action of the current agent_selection in the environment.

        Automatically switches control to the next agent.
        """
        if (
            self.terminations[self.agent_selection]
            or self.truncations[self.agent_selection]
        ):
            return self._was_dead_step(action)  # type: ignore[no-any-return]

        # agent = self.agent_selection

        self.num_moves += 1  # TODO: self.timestep += 1?

        # print(f"num_moves: {self.num_moves}")

        if self.max_cycles is not None:
            self.truncations = {
                agent_id: self.num_moves >= self.max_cycles for agent_id in self.agents
            }

        else:
            self.truncations = {agent_id: False for agent_id in self.agents}

        # self.num_moves += 1

        # if any(self.terminations.values()) or all(self.truncations.values()):
        #     self.agents = []

        # self.num_moves += 1

        # self._cumulative_rewards[self.agent_selection] = 0
        # self.agent_selection = self._agent_selector.next()
        # self._accumulate_rewards()

        if self.agent_selection == "env_0":
            # assert action == None, f"action must be None for env_0, got {action}."
            self.timestep += 1

        return None

    # def step(
    #     self, actions: dict[AgentID, ActionType]
    # ) -> tuple[
    #     dict[AgentID, ObsType],
    #     dict[AgentID, float],
    #     dict[AgentID, bool],
    #     dict[AgentID, bool],
    #     dict[AgentID, dict],
    # ]:
    #     """Receives a dictionary of actions keyed by the agent name.

    #     Returns the observation dictionary, reward dictionary, terminated dictionary, truncated dictionary
    #     and info dictionary, where each dictionary is keyed by the agent.
    #     """
    #     raise NotImplementedError

    # def step(self, action: ActionType | dict[AgentID, ActionType]) -> None | tuple[
    #     dict[AgentID, ObsType],
    #     dict[AgentID, float],
    #     dict[AgentID, bool],
    #     dict[AgentID, bool],
    #     dict[AgentID, dict],
    # ]:
    #     """Accepts and executes the action of the current agent_selection in the environment.

    #     Automatically switches control to the next agent.
    #     """
    #     self.infos = self.infos

    #     self.num_moves += 1

    #     observations = {
    #         agent_id: self.observe(agent_id) for agent_id in self.agents
    #     }

    #     self.rewards = self.rewards
    #     self.terminations = self.terminations

    #     if self.max_cycles is not None:
    #         self.truncations = {
    #             agent_id: self.num_moves >= self.max_cycles for agent_id in self.agents
    #         }

    #     else:
    #         self.truncations = {
    #             agent_id: False for agent_id in self.agents
    #         }

    #     if isinstance(action, dict) == False:
    #         return None

    #     return observations, self.rewards, self.terminations, self.truncations, self.infos # TODO: return self.get_last() instead?


def env(*args: list[Any], **kwargs: dict[str, Any]) -> Environment:
    return Environment(*args, **kwargs)  # type: ignore[arg-type]


parallel_env = parallel_wrapper_fn(env)
