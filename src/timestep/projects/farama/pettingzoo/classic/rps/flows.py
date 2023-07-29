from langchain.chat_models import ChatOpenAI
from pettingzoo_agent import PettingZooAgent
from prefect import flow


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


@flow(name="Rock Paper Scissors", log_prints=True)
def rock_paper_scissors():
    from pettingzoo.classic import rps_v2

    env = rps_v2.env(max_cycles=3, render_mode="human")
    agents = {
        name: PettingZooAgent(name=name, model=ChatOpenAI(temperature=1), env=env)
        for name in env.possible_agents
    }
    main(agents, env)
