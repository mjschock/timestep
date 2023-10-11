# from pettingzoo.butterfly import knights_archers_zombies_v10

# env = knights_archers_zombies_v10.env(render_mode="human")
# env.reset(seed=42)

# def policy(observation, agent):
#     action = env.action_space(agent).sample()

#     return action

# for agent in env.agent_iter():
#     observation, reward, termination, truncation, info = env.last()

#     print(termination)

#     action = policy(observation, agent)
#     env.step(action)

# import random
# from torch.distributions.categorical import Categorical
# gym.pprint_registry()
from collections import deque
from typing import Any, List, TypeVar

import gymnasium as gym
import ivy
import jax
import numpy as np
from gymnasium.spaces import Discrete

# PRINT_STREAM = True
# class User(BaseModel):
#     id: uuid.UUID
#     name: str
#     signup_ts: datetime | None
# class State(BaseModel):
#     user: User | None = None
# def stream_handler(message: Message):
#     if PRINT_STREAM:
#         print("=== Begin message ===")
#         print(f"message.role: {message.role}")
#         print(f"message.content: {message.content}")
#         print(f"message.name: {message.name}")
#         print(f"message.timestamp: {message.timestamp}")
#         print(f"message.data: {message.data}")
#         print(f"message.llm_response: {message.llm_response}")
#         # print(f"message.data['streaming_delta']: {message.data['streaming_delta']}")
#         print("=== End message ===\n")
# @tool
# def roll_dice(n_dice: int = 1) -> list[int]:
#     return [random.randint(1, 6) for _ in range(n_dice)]
# @tool
# def generate_uuid() -> uuid.UUID:
#     return uuid.uuid4()
# app = AIApplication(
#     state=State(),
#     stream_handler=stream_handler,
#     tools=[generate_uuid],
# )
# model: ChatLLM = None
# input_text = "What's my name?"
# response = run_sync(app.run(input_text=input_text, model=model))
# print(f"response.content: {response.content}")
# print(f"app.history: {app.history}")
# print(f"app.plan: {app.plan}")
# print(f"app.state: {app.state}")
# response = app("My name is Marvin")
# print(response.content)
# print(app.state)
# assert app.state.user is not None, "app.state.user is None"
# response = app("What's my name?")
# print(response.content)
# print(app.state)
# assert app.state.user is not None, "app.state.user is None"
# import time
# import gymnasium
# from miniwob.action import ActionTypes
# env = gymnasium.make('miniwob/click-test-2-v1', render_mode='human')
# # Wrap the code in try-finally to ensure proper cleanup.
# try:
#   # Start a new episode.
#   obs, info = env.reset()
#   assert obs["utterance"] == "Click button ONE."
#   assert obs["fields"] == (("target", "ONE"),)
#   time.sleep(2)       # Only here to let you look at the environment.
#   # Find the HTML element with text "ONE".
#   for element in obs["dom_elements"]:
#     if element["text"] == "ONE":
#       break
#   # Click on the element.
#   action = env.unwrapped.create_action(ActionTypes.CLICK_ELEMENT, ref=element["ref"])
#   obs, reward, terminated, truncated, info = env.step(action)
#   # Check if the action was correct.
#   print(reward)      # Should be around 0.8 since 2 seconds has passed.
#   assert terminated is True
#   time.sleep(2)
# finally:
#   env.close()
# from marvin import AIApplication
# from marvin.engine.executors import OpenAIFunctionsExecutor
# from marvin.prompts import library as prompt_library
# from marvin.prompts.base import Prompt
# from marvin.tools import Tool, tool
from pettingzoo.test import (
    api_test,
    max_cycles_test,
    parallel_api_test,
    parallel_seed_test,
    performance_benchmark,
    render_test,
    seed_test,
    test_save_obs,
)
from pettingzoo.utils.conversions import aec_to_parallel
from pettingzoo.utils.env import AECEnv, AgentID, ParallelEnv

# from marvin.utilities.history import History, HistoryFilter
# from marvin.utilities.messages import Message, Role
# from marvin.utilities.types import LoggerMixin, MarvinBaseModel
from pydantic import BaseModel

# from src.timestep.platform.agents.ppo.ppo_agent import Agent as PPOAgent
# from src.timestep.platform.agents.dqn.dqn_agent import Agent as DQNAgent
from src.timestep.platform.agents.ddpg.ddpg_agent import Agent as DDPGAgent

# import torch
# from pettingzoo.utils.all_modules import all_environments
from src.timestep.platform.all_modules import all_environments

jax.config.update("jax_enable_x64", True)
ivy.set_inplace_mode("strict")
ivy.set_backend("jax", dynamic=False)


# class Agent(AIApplication):
class Agent:
    id: AgentID
    # env: AECEnv

    prev_observation: Any = None
    prev_action: Any = None

    score: float = 0.0
    # eps: float = 0.

    # name: str = None
    # description: str = None
    # state: BaseModel = Field(default_factory=FreeformState)
    # plan: AppPlan = Field(default_factory=AppPlan)
    # tools: list[Union[Tool, Callable]] = []
    # history: History = Field(default_factory=History)
    # additional_prompts: list[Prompt] = Field(
    #     [],
    #     description=(
    #         "Additional prompts that will be added to the prompt stack for rendering."
    #     ),
    # )
    # stream_handler: Callable[[Message], None] = None
    # state_enabled: bool = True
    # plan_enabled: bool = True

    # def __init__(self, id: AgentID, env):
    #     self.id = id

    # self.observation_space = env.observation_space(self.id) # TODO: what about varying size?  # noqa: E501
    # self.action_space = env.action_space(self.id)

    # def __init__(
    #         self,
    #         id: AgentID,
    #         name: str = None,
    #         description: str = None,
    #         state: BaseModel = None,
    #         plan: AppPlan = None,
    #         tools: list[Union[Tool, Callable]] = [],
    #         history: History = None,
    #         additional_prompts: list[Prompt] = None,
    #         stream_handler: Callable[[Message], None] = None,
    #         state_enabled: bool = True,
    #         plan_enabled: bool = True,
    #     ):
    #     super().__init__(
    #         name=name,
    #         description=description,
    #         state=state,
    #         plan=plan,
    #         tools=tools,
    #         history=history,
    #         additional_prompts=additional_prompts,
    #         stream_handler=stream_handler,
    #         state_enabled=state_enabled,
    #         plan_enabled=plan_enabled
    #     )
    #     self.id = id

    def __init__(self, id, state_size, action_size, **kwargs):
        # super().__init__(*args, **kwargs)

        # self.state.episodes = []

        self.id = id

        # self.agent = DQNAgent(
        #     state_size=state_size,
        #     action_size=action_size,
        #     seed=42,
        # )

        self.agent = DDPGAgent(
            state_size=state_size,
            action_size=action_size,
            random_seed=42,
        )

        # self.eps = 0.

    def reset(self, seed: int | None = None, options: dict | None = None) -> None:
        self.score = 0.0

    def step(self, env, agent_id, observation, reward, termination, truncation, info):
        if termination or truncation:
            action = None

        else:
            if "action_mask" in info:
                info["action_mask"]

            elif isinstance(observation, dict) and "action_mask" in observation:
                observation["action_mask"]

            else:
                pass

            # action = env.action_space(agent_id).sample(mask)

            #             marvin.settings.llm_model = 'openai/gpt-3.5-turbo'
            #             model: ChatLLM = None

            #             # if len(self.state.episodes) > 0:
            #             # episode_return = self.state.episodes[]
            #             episode_return = reward

            #             input_text = f"""
            # Observation: {observation}
            # Reward: {reward}
            # Termination: {termination}
            # Truncation: {truncation}
            # Return: {episode_return}
            #             """
            #             response = run_sync(self.run(input_text=input_text, model=model))  # noqa: E501
            #             print(f"response.content: {response.content}")

            #             action_parser = RegexParser(
            #                 regex=r"Action: (.*)", output_keys=["action"], default_output_key="action"  # noqa: E501
            #             )

            #             action = int(action_parser.parse(response.content)["action"])

            self.score += reward

            # if isinstance()

            if self.prev_observation is not None and self.prev_action is not None:
                self.agent.step(
                    state=self.prev_observation,
                    action=self.prev_action,
                    reward=reward,
                    next_state=observation,
                    done=termination or truncation,
                )

            # action = self.agent.act(observation, self.eps)

            # ivy.set_backend("numpy")
            action = self.agent.act(observation)
            action = action.to_native()
            action = action.tolist()
            action = np.asarray(action)

            # action = env.action_space(agent_id).sample()

            # if isinstance(env.action_space(agent_id), Discrete):
            #     action = np.argmax(action)

            # Epsilon-greedy action selection
            # if random.random() > eps:
            #     return np.argmax(action_values.cpu().data.numpy())
            # else:
            #     return random.choice(np.arange(self.action_size))

        self.prev_action = action
        self.prev_observation = observation

        return action


for env_name, env_module in all_environments.items():
    print(f"=== Env: {env_name} ===")

    assert "env" in env_module.__all__
    assert "raw_env" in env_module.__all__
    # assert "ManualPolicy" in env_module.__all__

    env: AECEnv = env_module.env()

    # print('=== GoalEnv check ===')
    # print('type: ', type(env))
    # print('type unwrapped: ', type(env.unwrapped))

    api_test(env, num_cycles=100, verbose_progress=False)

    env_fn = env_module.env
    seed_test(env_fn, num_cycles=10)

    if env.metadata.get("is_parallelizable", True):
        assert "parallel_env" in env_module.__all__

        parallel_env: ParallelEnv = aec_to_parallel(env)
        parallel_api_test(parallel_env, num_cycles=100)

        parallel_env_fn = env_module.parallel_env
        parallel_seed_test(parallel_env_fn)

        max_cycles_test(env_module)

    render_test(env_fn)
    performance_benchmark(env)
    test_save_obs(env)

    # ### BEGIN TESTING
    # import random
    # import time

    # print("BEGIN TESTING")

    # cycles = 0
    # turn = 0
    # env.reset()
    # start = time.time()
    # end = 0

    # while True:
    #     cycles += 1
    #     for agent in env.agent_iter(
    #         env.num_agents
    #     ):  # step through every agent once with observe=True
    #         obs, reward, termination, truncation, info = env.last()

    #         if termination or truncation:
    #             action = None

    #         elif isinstance(obs, dict) and "action_mask" in obs:
    #             action = random.choice(np.flatnonzero(obs["action_mask"]).tolist())

    #         else:
    #             action = env.action_space(agent).sample()

    #         env.step(action)
    #         turn += 1

    #         if all(env.terminations.values()) or all(env.truncations.values()):
    #             env.reset()

    #     if time.time() - start > 5:
    #         end = time.time()
    #         break

    # # length = end - start

    # # turns_per_time = turn / length
    # # cycles_per_time = cycles / length
    # # print(str(turns_per_time) + " turns per second")
    # # print(str(cycles_per_time) + " cycles per second")
    # print("END TESTING")

    ### END TESTING

    print("Starting agent-environment loop")
    # env: AECEnv = env_module.env(render_mode="human") # ~2 turns/sec
    env: AECEnv = env_module.env()  # ~28k turns/sec
    # env = DataCollectorV0(env, record_infos=True, max_buffer_steps=100000)
    env.reset(seed=42)

    agents_db = {}

    ObsType = TypeVar("ObsType")
    ActType = TypeVar("ActType")

    class Episode(BaseModel):
        observations: List[ObsType] = []
        actions: List[ActType] = []
        rewards: List[float] = []
        terminations: List[bool] = []
        truncations: List[bool] = []

    class State(BaseModel):
        # episodes: List[EpisodeData] = []
        episodes: List[Episode] = []
        # class Config:
        #     arbitrary_types_allowed = True

    for agent_id in env.possible_agents:
        action_space: gym.Space = env.action_space(agent_id)
        print(f"action_space: {action_space}")
        observation_space: gym.Space = env.observation_space(agent_id)
        print(f"observation_space: {observation_space}")

        if isinstance(action_space, Discrete):
            action_size = action_space.n
        else:
            action_size = action_space.shape[0]

        if isinstance(observation_space, Discrete):
            state_size = observation_space.n
        else:
            state_size = observation_space.shape[0]

        print("action_size: ", action_size)
        print("state_size: ", state_size)

        agents_db[agent_id] = Agent(
            id=agent_id,
            action_size=action_size,
            state_size=state_size,
            #             name=agent_id,
            #             description=f"""
            # Your goal is to maximize your return, i.e. the sum of the rewards you receive.  # noqa: E501
            # I will give you an observation, reward, termination flag, truncation flag, and the return so far, formatted as:  # noqa: E501
            # Observation: <observation>
            # Reward: <reward>
            # Termination: <termination>
            # Truncation: <truncation>
            # Return: <sum_of_rewards>
            # You will respond with an action, formatted as:
            # Action: <action>
            # where you replace <action> with your actual action.
            # Do nothing else but return the action.
            # """,
            #             state=State(),
            #             # plan=,
            #             # tools=[],
            #             # history=[],
            #             # additional_prompts=,
            #             stream_handler=None,
            #             state_enabled=True,
            #             plan_enabled=True,
        )
        agents_db[agent_id].reset(seed=42)

        assert (
            agents_db[agent_id].id == agent_id
        ), f"agents_db[{agent_id}].id != {agent_id}"  # noqa: E501
        # print(f"=== Agent: {agents_db[agent_id].id} ===")
        # print(f"app.history: {agents_db[agent_id].history}")
        # print(f"app.plan: {agents_db[agent_id].plan}")
        # print(f"app.state: {agents_db[agent_id].state}")

    # eps_start=1.0
    # eps_end=0.01
    # eps_decay=0.995
    scores = {
        agent_id: [] for agent_id in agents_db.keys()
    }  # list containing scores from each episode  # noqa: E501
    scores_window = {
        agent_id: deque(maxlen=100) for agent_id in agents_db.keys()
    }  # last 100 scores  # noqa: E501
    # eps = eps_start                    # initialize epsilon
    n_episodes = 1

    ### BEGIN TESTING
    import random
    import time

    print("BEGIN TESTING")

    cycles = 0
    turn = 0
    env.reset(seed=42)
    start = time.time()
    end = 0

    while True:
        cycles += 1
        for agent in env.agent_iter(
            env.num_agents
        ):  # step through every agent once with observe=True
            obs, reward, termination, truncation, info = env.last()

            if termination or truncation:
                action = None

            elif isinstance(obs, dict) and "action_mask" in obs:
                action = random.choice(np.flatnonzero(obs["action_mask"]).tolist())

            else:
                action = env.action_space(agent).sample()

            # print('action: ', action)
            env.step(action)
            turn += 1

            if all(env.terminations.values()) or all(env.truncations.values()):
                env.reset(seed=42)

        if time.time() - start > 5:
            end = time.time()
            break

    length = end - start

    turns_per_time = turn / length
    cycles_per_time = cycles / length
    print(str(turns_per_time) + " turns per second")
    print(str(cycles_per_time) + " cycles per second")
    print("END TESTING")

    for i_episode in range(1, n_episodes + 1):
        env.reset(seed=42)
        agents_db[agent_id].reset(seed=42)
        # agents_db[agent_id].eps = eps

        i_iter = 0
        cycles = 0
        turn = 0
        start = time.time()

        while True:
            cycles += 1
            for agent_id in env.agent_iter(max_iter=env.num_agents):
                observation, reward, termination, truncation, info = env.last()
                # print('reward: ', reward)

                if isinstance(env.observation_space(agent_id), Discrete):
                    # one-hot encode the observation
                    observation_one_hot = np.zeros(
                        (1, env.observation_space(agent_id).n)
                    )  # noqa: E501
                    observation_one_hot[0][observation] = 1
                    observation = observation_one_hot

                # print('observation: ', observation, 'type(observation): ', type(observation))  # noqa: E501
                # action = agents_db[agent_id].step(env, agent_id, observation, reward, termination, truncation, info)  # noqa: E501

                # if isinstance(env.action_space(agent_id), Discrete) and action is not None:  # noqa: E501
                #     action = np.argmax(action)

                # print('action: ', action, 'type(action): ', type(action))
                # print('action: ', action)
                action = env.action_space(agent_id).sample()
                env.step(action)
                turn += 1

                # print('\rEpisode {}\tIteration: {:.2f}'.format(i_episode, i_iter), end="")  # noqa: E501
                i_iter += 1

                if all(env.terminations.values()) or all(env.truncations.values()):
                    env.reset(seed=42)

            if time.time() - start > 5:
                end = time.time()
                break

        for agent_id in agents_db.keys():
            scores_window[agent_id].append(
                agents_db[agent_id].score
            )  # save most recent score  # noqa: E501
            scores[agent_id].append(
                agents_db[agent_id].score
            )  # save most recent score  # noqa: E501
            # eps = max(eps_end, eps_decay*eps) # decrease epsilon
            print(
                "\rEpisode {}\tAverage Score: {:.2f}".format(
                    i_episode, np.mean(scores_window[agent_id])
                ),
                end="",
            )  # noqa: E501

            if i_episode % 10 == 0:
                print(
                    "\rEpisode {}\tAverage Score: {:.2f}".format(
                        i_episode, np.mean(scores_window[agent_id])
                    )
                )  # noqa: E501

            if np.mean(scores_window[agent_id]) >= 200.0:
                print(
                    "\nEnvironment solved in {:d} episodes!\tAverage Score: {:.2f}".format(  # noqa: E501
                        i_episode - 100, np.mean(scores_window[agent_id])
                    )
                )  # noqa: E501
                # torch.save(agents_db[agent_id].agent.qnetwork_local.state_dict(), 'checkpoint.pth')  # noqa: E501
                # torch.save(agents_db[agent_id].agent.actor_local.state_dict(), 'checkpoint_actor.pth')  # noqa: E501
                # torch.save(agents_db[agent_id].agent.critic_local.state_dict(), 'checkpoint.critic.pth')  # noqa: E501
                break

    env.close()
    print("\nFinished agent-environment loop\n")
