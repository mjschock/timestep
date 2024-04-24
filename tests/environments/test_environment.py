import pytest

from timestep.agents.agent import Agent
from timestep.environments import environment as mod
from timestep.environments.environment import env as env_fn, Environment, parallel_env as parallel_env_fn
from pettingzoo.utils.conversions import aec_to_parallel
from pettingzoo.utils.env import AECEnv

def test_pettingzoo_compatibility():
    with pytest.deprecated_call():
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

    aec_env = Environment()

    assert isinstance(aec_env, AECEnv)
    assert isinstance(aec_env, Agent)
    assert isinstance(aec_env, Environment)

    assert hasattr(aec_env, "env") is False
    assert hasattr(aec_env, "unwrapped")

    assert isinstance(aec_env.unwrapped, AECEnv)
    assert isinstance(aec_env.unwrapped, Agent)
    assert isinstance(aec_env.unwrapped, Environment)
    assert isinstance(aec_env.unwrapped.unwrapped, AECEnv)
    assert isinstance(aec_env.unwrapped.unwrapped, Agent)
    assert isinstance(aec_env.unwrapped.unwrapped, Environment)

    api_test(env=aec_env, num_cycles=1, verbose_progress=True)

    par_env = aec_to_parallel(aec_env=aec_env)

    parallel_api_test(par_env=par_env, num_cycles=1)

    seed_test(env_constructor=Environment, num_cycles=1)
    parallel_seed_test(parallel_env_fn=parallel_env_fn, num_cycles=1)

    max_cycles_test(mod=mod)

    custom_tests = {
        "svg": lambda render_result: isinstance(render_result, str)
    }

    render_test(env_fn=env_fn, custom_tests=custom_tests)

    performance_benchmark(env=aec_env)

    test_save_obs(env=aec_env)
