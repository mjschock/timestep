from langchain.chat_models import ChatOpenAI
from prefect import flow

from action_masking_agent import ActionMaskAgent  # isort: skip


@flow(name="Main", log_prints=True)
def main(agents, env):
    env.reset()

    for name, agent in agents.items():
        agent.reset()

    for agent_name in env.agent_iter():
        observation, reward, termination, truncation, info = env.last()
        obs_message = agents[agent_name].observe(
            observation, reward, termination, truncation, info
        )
        print(obs_message)
        if termination or truncation:
            action = None
        else:
            action = agents[agent_name].act()
        print(f"Action: {action}")
        env.step(action)

    env.close()


@flow(name="No Limit Texas Hold'em", log_prints=True)
def texas_holdem_no_limit():
    from pettingzoo.classic import texas_holdem_no_limit_v6

    env = texas_holdem_no_limit_v6.env(num_players=4, render_mode="human")
    agents = {
        name: ActionMaskAgent(name=name, model=ChatOpenAI(temperature=0.2), env=env)
        for name in env.possible_agents
    }
    main(agents, env)
