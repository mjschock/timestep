from langchain.chat_models import ChatOpenAI

from timestep.agents.action_mask_agent.agent import ActionMaskAgent

def tic_tac_toe(openai_api_key):
    from pettingzoo.classic import tictactoe_v3

    env = tictactoe_v3.env(render_mode="human")
    agents = {
        name: ActionMaskAgent(name=name, model=ChatOpenAI(openai_api_key=openai_api_key, temperature=0.2), env=env)
        for name in env.possible_agents
    }

    return env, agents
