from timestep.agents.petting_zoo_agent.agent import PettingZooAgent
from timestep.envs.no_limit_texas_holdem.env import texas_holdem_no_limit
from timestep.envs.rock_paper_scissors.env import rock_paper_scissors
from timestep.envs.tic_tac_toe.env import tic_tac_toe
import typer

from constructs import Construct
from cdktf import App, TerraformOutput, TerraformProvider, TerraformStack

from lib.imports.multipass.provider import MultipassProvider as MultipassTerraformProvider
from lib.imports.multipass.instance import Instance as MultipassTerraformResource
from lib.imports.multipass.data_multipass_instance import DataMultipassInstance as MultipassTerraformDataSource


class MainTerraformStack(TerraformStack):
    def __init__(self, scope: Construct, id: str, target: str):
        super().__init__(scope, id)

        provider = MultipassTerraformProvider(
            id=f"{id}-{target}-provider",
            scope=self,
        )
        assert isinstance(provider, TerraformProvider)

        import os
        cwd = os.getcwd()
        print(f"cwd: {cwd}")

        cloudinit_file = f"{cwd}/src/timestep/envs/env/cloud.yaml"

        resource = MultipassTerraformResource(
            cloudinit_file=cloudinit_file,
            cpus=2,
            disk="40G",
            id=f"{id}-{target}-resource",
            image="22.04", # "ros2-humble",
            # image="ros2-humble",
            # memory="4G",
            name=f"{id}",
            provider=provider,
            scope=self,
        )
        assert isinstance(resource, MultipassTerraformResource)

        data_source = MultipassTerraformDataSource(
            id=f"{id}-{target}-data_source",
            name=resource.name,
            provider=provider,
            scope=self,
        )
        assert isinstance(data_source, MultipassTerraformDataSource)

        output = TerraformOutput(
            id=f"{target}-ipv4",
            value=data_source.ipv4,
            scope=self,
        )
        # print(f"output: {output}")

def main(app_name: str="timestep", env: str="localhost", openai_api_key: str=""):
    print(f"Running {app_name} in {env} mode")

    app = App()

    MainTerraformStack(scope=app, id=app_name, target=env)

    app.synth()

    env_iter = {
        "rock_paper_scissors": rock_paper_scissors,
        "tic_tac_toe": tic_tac_toe,
        "texas_holdem_no_limit": texas_holdem_no_limit,
    }

    for env_name, env_func in env_iter.items():
        print(f"Running {env_name} environment")
        env, agents = env_func(openai_api_key=openai_api_key)

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


app = typer.Typer()

@app.callback()
def callback():
    """
    Timestep AI
    """

@app.command()
def loop():
    """
    Run the main loop
    """
    typer.echo("Running the loop")

    MARVIN_OPENAI_API_KEY='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'

    main(openai_api_key=MARVIN_OPENAI_API_KEY)


if __name__ == "__main__":
    app()
