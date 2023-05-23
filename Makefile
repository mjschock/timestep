default: up

# agents:
# 	pipx run poetry new --name=timestep.agents.action_mask_agent --src src/timestep/agents/action_mask_agent || true
# 	pipx run poetry add -e src/timestep/agents/action_mask_agent
	pipx run poetry new --name=timestep.agents.agent --src src/timestep/agents/agent || true # TODO turn this into a cruft skaffold
	pipx run poetry add -e src/timestep/agents/agent
	cd src/timestep/agents/agent && pipx run poetry run prefect project init && git init
	# pipx run poetry new --name=timestep.agents.gymnasium_agent --src src/timestep/agents/gymnasium_agent || true
	# pipx run poetry add -e src/timestep/agents/gymnasium_agent
	# pipx run poetry new --name=timestep.agents.petting_zoo_agent --src src/timestep/agents/petting_zoo_agent || true
	# pipx run poetry add -e src/timestep/agents/petting_zoo_agent

envs:
	pipx run poetry new --name=timestep.envs.env --src src/timestep/envs/env || true
	pipx run poetry add -e src/timestep/envs/env
	pipx run poetry new --name=timestep.envs.no_limit_texas_holdem --src src/timestep/envs/no_limit_texas_holdem || true
	pipx run poetry add -e src/timestep/envs/no_limit_texas_holdem
	pipx run poetry new --name=timestep.envs.rock_paper_scissors --src src/timestep/envs/rock_paper_scissors || true
	pipx run poetry add -e src/timestep/envs/rock_paper_scissors
	pipx run poetry new --name=timestep.envs.tic_tac_toe --src src/timestep/envs/tic_tac_toe || true
	pipx run poetry add -e src/timestep/envs/tic_tac_toe
	pipx run poetry new --name=timestep.envs.turtle_sim --src src/timestep/envs/turtle_sim || true
	pipx run poetry add -e src/timestep/envs/turtle_sim

up:
	tilt up
