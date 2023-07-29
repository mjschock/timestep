from langchain.chat_models import ChatOpenAI
from pettingzoo_agent import PettingZooAgent
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


@flow(name="Rock Paper Scissors", log_prints=True)
def rock_paper_scissors():
    from pettingzoo.classic import rps_v2

    env = rps_v2.env(max_cycles=3, render_mode="human")
    agents = {
        name: PettingZooAgent(name=name, model=ChatOpenAI(temperature=1), env=env)
        for name in env.possible_agents
    }
    main(agents, env)


@flow(name="Tic-Tac-Toe", log_prints=True)
def tic_tac_toe():
    from pettingzoo.classic import tictactoe_v3

    env = tictactoe_v3.env(render_mode="human")
    agents = {
        name: ActionMaskAgent(name=name, model=ChatOpenAI(temperature=0.2), env=env)
        for name in env.possible_agents
    }
    main(agents, env)


@flow(name="No Limit Texas Hold'em", log_prints=True)
def texas_holdem_no_limit():
    from pettingzoo.classic import texas_holdem_no_limit_v6

    env = texas_holdem_no_limit_v6.env(num_players=4, render_mode="human")
    agents = {
        name: ActionMaskAgent(name=name, model=ChatOpenAI(temperature=0.2), env=env)
        for name in env.possible_agents
    }
    main(agents, env)


@flow(name="Repo Info", log_prints=True)
def repo_info(repo_owner: str = "PrefectHQ", repo_name: str = "prefect"):
    rock_paper_scissors()
    tic_tac_toe()
    texas_holdem_no_limit()


# @task(retries=2)
# def get_repo_info(repo_owner: str, repo_name: str):
#     """ Get info about a repo - will retry twice after failing """
#     url = f"https://api.github.com/repos/{repo_owner}/{repo_name}"
#     api_response = httpx.get(url)
#     api_response.raise_for_status()
#     repo_info = api_response.json()
#     return repo_info

# @task
# def get_contributors(repo_info: dict):
#     contributors_url = repo_info["contributors_url"]
#     response = httpx.get(contributors_url)
#     response.raise_for_status()
#     contributors = response.json()
#     return contributors

# @flow(name="Repo Info", log_prints=True)
# def repo_info(
#     repo_owner: str = "PrefectHQ", repo_name: str = "prefect"
# ):
#     # call our `get_repo_info` task
#     repo_info = get_repo_info(repo_owner, repo_name)
#     print(f"Stars 🌠 : {repo_info['stargazers_count']}")

#     # call our `get_contributors` task,
#     # passing in the upstream result
#     contributors = get_contributors(repo_info)
#     print(
#         f"Number of contributors 👷: {len(contributors)}"
#     )

# @flow()
# def main():
#     """ This is the main flow """
#     logger = get_run_logger()
#     logger.info("Starting main flow")

# if __name__ == "__main__":
#     # Call a flow function for a local flow run!
#     # repo_info()
#     main()
