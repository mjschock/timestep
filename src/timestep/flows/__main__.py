import asyncio
from PIL import Image
import numpy as np
from prefect import State, flow
from prefect.client.schemas import StateType

from timestep.environments.environment import ActionType, AgentID, Environment, ObsType


@flow(log_prints=True)
async def main_flow(max_cycles=3, render_mode="rgb_array"):
    print("=== BEGIN MAIN FLOW ===")

    aec_env = Environment(
        max_cycles=max_cycles,
        render_mode=render_mode,
    )

    # Observe
    rgb_array: np.ndarray = aec_env.render()
    assert isinstance(rgb_array, np.ndarray), f"rgb_array must be a numpy array, got {type(rgb_array)}."

    if render_mode == "human":
        Image.fromarray(rgb_array).show()

    observations, infos = aec_env.reset()
    # print("Observations:", observations)
    # print("Infos:", infos)

    agent_ids: AgentID = aec_env.agents

    for agent_id in aec_env.agent_iter():
        print("Timestep:", aec_env.timestep)
        print("Agent ID:", agent_id)

        observation, reward, termination, truncation, info = aec_env.last()
        # print("Observation:", observation)
        # print("Reward:", reward)
        # print("Termination:", termination)
        # print("Truncation:", truncation)
        # print("Info:", info)

        # action: ActionType = aec_env.action_spaces[agent_id].sample()
        # action: ActionType = agent.step(observation, reward, termination, truncation, info)
        # print("Action:", action)

        if agent_id == "env_0":
            action = None

        aec_env.step(action)

    print("=== END MAIN FLOW ===")

async def main(*args, **kwargs):
    state: State = await main_flow(*args, **kwargs, return_state=True)
    print("state:", state)
    assert state.is_final()
    assert state.is_completed()

if __name__ == "__main__":
    asyncio.run(main())
