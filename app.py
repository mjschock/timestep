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
# import uuid
# from datetime import datetime

# from marvin import AIApplication
# from marvin.engine.executors import OpenAIFunctionsExecutor
# from marvin.engine.language_models import ChatLLM, chat_llm
# from marvin.prompts import library as prompt_library
# from marvin.prompts.base import Prompt
# from marvin.tools import Tool, tool
# from marvin.utilities.async_utils import run_sync
# from marvin.utilities.history import History, HistoryFilter
# from marvin.utilities.messages import Message, Role
# from marvin.utilities.types import LoggerMixin, MarvinBaseModel
# from pydantic import BaseModel, Field, PrivateAttr, validator

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

import gymnasium as gym
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

# from pettingzoo.utils.all_modules import all_environments
from src.timestep.platform.all_modules import all_environments

gym.pprint_registry()


class Agent():
    id: AgentID

    def __init__(self, id: AgentID):
        self.id = id

    def reset(self, seed: int | None = None, options: dict | None = None) -> None:
        pass

    def step(self, env, agent_id, observation, termination, truncation, info):
        if termination or truncation:
            action = None

        else:
            if "action_mask" in info:
                mask = info["action_mask"]

            elif isinstance(observation, dict) and "action_mask" in observation:
                mask = observation["action_mask"]

            else:
                mask = None

            action = env.action_space(agent_id).sample(mask)

        return action


for env_name, env_module in all_environments.items():
    print(f"=== Env: {env_name} ===")

    assert "env" in env_module.__all__
    assert "raw_env" in env_module.__all__
    # assert "ManualPolicy" in env_module.__all__

    env: AECEnv = env_module.env()
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

    print("Starting agent-environment loop")
    env: AECEnv = env_module.env(render_mode="human")
    env.reset(seed=42)

    for agent_id in env.possible_agents:
        agent = Agent(id=agent_id)

        print(f"=== Agent: {agent.id} ===")

        agent.reset(seed=42)

    for agent_id in env.agent_iter():
        observation, reward, termination, truncation, info = env.last()

        action = agent.step(env, agent_id, observation, termination, truncation, info)

        env.step(action)

    env.close()
    print("Finished agent-environment loop\n")
