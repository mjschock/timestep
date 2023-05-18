from langchain.chat_models import ChatOpenAI

from timestep.agents.petting_zoo_agent.agent import PettingZooAgent

def rock_paper_scissors(openai_api_key):
    from pettingzoo.classic import rps_v2

    env = rps_v2.env(max_cycles=3, render_mode="human")
    agents = {
        name: PettingZooAgent(name=name, model=ChatOpenAI(openai_api_key=openai_api_key, temperature=1), env=env)
        for name in env.possible_agents
    }

    return env, agents
