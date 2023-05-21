default: up

agents:
	poetry new --name=timestep.agents.action_mask_agent --src src/timestep/agents/action_mask_agent || true
	poetry add -e src/timestep/agents/action_mask_agent
	poetry new --name=timestep.agents.gymnasium_agent --src src/timestep/agents/gymnasium_agent || true
	poetry add -e src/timestep/agents/gymnasium_agent
	poetry new --name=timestep.agents.petting_zoo_agent --src src/timestep/agents/petting_zoo_agent || true
	poetry add -e src/timestep/agents/petting_zoo_agent

envs:
	poetry new --name=timestep.envs.no_limit_texas_holdem --src src/timestep/envs/no_limit_texas_holdem || true
	poetry add -e src/timestep/envs/no_limit_texas_holdem
	poetry new --name=timestep.envs.rock_paper_scissors --src src/timestep/envs/rock_paper_scissors || true
	poetry add -e src/timestep/envs/rock_paper_scissors
	poetry new --name=timestep.envs.tic_tac_toe --src src/timestep/envs/tic_tac_toe || true
	poetry add -e src/timestep/envs/tic_tac_toe

up:
	tilt up
