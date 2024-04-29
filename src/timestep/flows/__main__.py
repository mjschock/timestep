from __future__ import annotations

import asyncio
from typing import Any

import numpy as np
from PIL import Image
from prefect import State, flow

from timestep.environments.environment import Environment


@flow(log_prints=True)  # type: ignore[misc]
async def sub_flow() -> State:
    return None


@flow(log_prints=True)  # type: ignore[misc]
async def main_flow(
    max_cycles: int = 3,
    render_mode: str = "rgb_array",
    # ) -> Coroutine[Any, Any, State]:
) -> State:
    aec_env = Environment(
        max_cycles=max_cycles,
        render_mode=render_mode,
    )

    # Observe
    rgb_array: np.ndarray = aec_env.render()
    assert isinstance(
        rgb_array, np.ndarray
    ), f"rgb_array must be a numpy array, got {type(rgb_array)}."

    if render_mode == "human":
        Image.fromarray(rgb_array).show()

    observations, infos = aec_env.reset()
    # print("Observations:", observations)
    # print("Infos:", infos)

    for agent_id in aec_env.agent_iter():
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

    # future = await sub_flow.submit()
    return await sub_flow()
    # result = await future.result()

    # return result + 1


async def main(*args: list[Any], **kwargs: dict[str, Any]) -> None:
    state: State = await main_flow(*args, **kwargs, return_state=True)
    assert state.is_final()
    assert state.is_completed()


if __name__ == "__main__":
    asyncio.run(main())
