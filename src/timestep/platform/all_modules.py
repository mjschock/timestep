# from gymnasium_robotics.envs.multiagent_mujoco import (
#     pusher_v2,
# )

# all_prefixes = ["atari", "classic", "butterfly", "mpe", "sisl"]
# manual_environments = {
#     "butterfly/knights_archers_zombies",
#     "butterfly/pistonball",
#     "butterfly/cooperative_pong",
#     "sisl/pursuit",
# }
from timestep.platform.envs.gymnasium.toy_text import (
    frozen_lake_v1,
)

# gym_envs = gymnasium.envs.registry

# gymnasium_env_latest_versions = {}

# for gymnasium_env_id, gymnasium_env_spec in gym_envs.items():
#     # print(f"gymnasium_env_id: {gymnasium_env_id}")
#     # print('gymnasium_env_spec: ', gymnasium_env_spec)

#     assert isinstance(gymnasium_env_spec, gymnasium.envs.registration.EnvSpec)
#     assert gymnasium_env_spec.id == gymnasium_env_id, f"{gymnasium_env_spec.id} != {gymnasium_env_id}"  # noqa: E501

#     if gymnasium_env_spec.name not in gymnasium_env_latest_versions:
#         gymnasium_env_latest_versions[gymnasium_env_spec.name] = gymnasium_env_spec.version  # noqa: E501
#     elif gymnasium_env_spec.version > gymnasium_env_latest_versions[gymnasium_env_spec.name]:  # noqa: E501
#         gymnasium_env_latest_versions[gymnasium_env_spec.name] = gymnasium_env_spec.version  # noqa: E501

#     entry_point = gymnasium_env_spec.entry_point
#     print(f"entry_point: {entry_point}")

#     version = gymnasium_env_spec.version

#     if entry_point.startswith("gymnasium.envs"):
#         env_path = entry_point.replace("gymnasium.envs", "gymnasium").replace(".", "/").replace(f"_v{version}", "").split(":")[0]  # noqa: E501
#         env_name = env_path.split("/")[-1]
#         env_folder = env_path.replace(f"/{env_name}", "")

#         os.makedirs(f"src/timestep/platform/envs/gym/{env_folder}", exist_ok=True)

#         with open(f"src/timestep/platform/envs/gym/{env_folder}/{env_name}_v{version}.py", 'w') as file:  # noqa: E501
#             file.write(f"""from functools import partial

# from timestep.platform.envs.gymnasium.env import (
#     RawEnv,
#     env_creator,
# )

# env = partial(
#     env_creator,
#     id="{gymnasium_env_id}",
#     name="{env_name}_v{version}",
# )

# raw_env = RawEnv(
#     id="{gymnasium_env_id}",
#     name="{env_name}_v{version}",
# )

# __all__ = ["env", "raw_env"]

# """)
# elif entry_point.startswith("gymnasium_robotics.envs"):
#     os.makedirs(f"src/timestep/platform/envs/{entry_point}", exist_ok=True)


# break

# print(f"gymnasium_env_latest_versions: {gymnasium_env_latest_versions}")

all_environments = {
    # "atari/adventure_v5": adventure_v5, # TODO: ALE/Adventure-ram-v5
    # "box2d/bipedal_walker_v3": bipedal_walker_v3, # TODO: pass hardcore=True as well?
    # "box2d/car_racing_v2": car_racing_v2, # TODO: pass domain_randomize=True as well?
    # "box2d/lunar_lander_v2": lunar_lander_v2,
    # "classic_control/acrobot_v1": acrobot_v1,
    # "classic_control/cart_pole_v1": cart_pole_v1,
    # "classic_control/mountain_car_continuous_v0": mountain_car_continuous_v0,
    # "classic_control/mountain_car_v0": mountain_car_v0,
    # "classic_control/pendulum_v1": pendulum_v1,
    # "mujoco/ant_v4": ant_v4,
    # "mujoco/half_cheetah_v4": half_cheetah_v4,
    # "mujoco/hopper_v4": hopper_v4,
    # "mujoco/humanoid_standup_v4": humanoid_standup_v4,
    # "mujoco/humanoid_v4": humanoid_v4,
    # "mujoco/inverted_double_pendulum_v4": inverted_double_pendulum_v4,
    # "mujoco/inverted_pendulum_v4": inverted_pendulum_v4,
    # "mujoco/pusher_v4": pusher_v4,
    # "mujoco/reacher_v4": reacher_v4,
    # "mujoco/swimmer_v4": swimmer_v4,
    # "mujoco/walker2d_v4": walker2d_v4,
    # "toy_text/blackjack_v1": blackjack_v1,
    # "toy_text/cliff_walking_v0": cliff_walking_v0,
    "toy_text/frozen_lake_v1": frozen_lake_v1,
    # "toy_text/taxi_v3": taxi_v3,
    # "gymnasium_robotics/fetch/fetch_pick_and_place_v2": fetch_pick_and_place_v2,
    # "atari/basketball_pong_v3": basketball_pong_v3,
    # "atari/boxing_v2": boxing_v2,
    # "atari/combat_tank_v2": combat_tank_v2,
    # "atari/combat_plane_v2": combat_plane_v2,
    # "atari/double_dunk_v3": double_dunk_v3,
    # "atari/entombed_competitive_v3": entombed_competitive_v3,
    # "atari/entombed_cooperative_v3": entombed_cooperative_v3,
    # "atari/flag_capture_v2": flag_capture_v2,
    # "atari/foozpong_v3": foozpong_v3,
    # "atari/joust_v3": joust_v3,
    # "atari/ice_hockey_v2": ice_hockey_v2,
    # "atari/maze_craze_v3": maze_craze_v3,
    # "atari/mario_bros_v3": mario_bros_v3,
    # "atari/othello_v3": othello_v3,
    # "atari/pong_v3": pong_v3,
    # "atari/quadrapong_v4": quadrapong_v4,
    # "atari/space_invaders_v2": space_invaders_v2,
    # "atari/space_war_v2": space_war_v2,
    # "atari/surround_v2": surround_v2,
    # "atari/tennis_v3": tennis_v3,
    # "atari/video_checkers_v4": video_checkers_v4,
    # "atari/volleyball_pong_v3": volleyball_pong_v3,
    # "atari/wizard_of_wor_v3": wizard_of_wor_v3,
    # "atari/warlords_v3": warlords_v3,
    # # "classic/chess_v6": chess_v6,
    # "classic/chess_v5": chess_v5,
    # "classic/rps_v2": rps_v2,
    # "classic/connect_four_v3": connect_four_v3,
    # "classic/tictactoe_v3": tictactoe_v3,
    # "classic/leduc_holdem_v4": leduc_holdem_v4,
    # "classic/texas_holdem_v4": texas_holdem_v4,
    # "classic/texas_holdem_no_limit_v6": texas_holdem_no_limit_v6,
    # "classic/gin_rummy_v4": gin_rummy_v4,
    # "classic/go_v5": go_v5,
    # # "classic/hanabi_v5": hanabi_v5,
    # "classic/hanabi_v4": hanabi_v4,
    # "butterfly/knights_archers_zombies_v10": knights_archers_zombies_v10,
    # "butterfly/pistonball_v6": pistonball_v6,
    # "butterfly/cooperative_pong_v5": cooperative_pong_v5,
    # "mpe/simple_adversary_v3": simple_adversary_v3,
    # "mpe/simple_crypto_v3": simple_crypto_v3,
    # "mpe/simple_push_v3": simple_push_v3,
    # "mpe/simple_reference_v3": simple_reference_v3,
    # "mpe/simple_speaker_listener_v4": simple_speaker_listener_v4,
    # "mpe/simple_spread_v3": simple_spread_v3,
    # "mpe/simple_tag_v3": simple_tag_v3,
    # "mpe/simple_world_comm_v3": simple_world_comm_v3,
    # "mpe/simple_v3": simple_v3,
    # "sisl/multiwalker_v9": multiwalker_v9,
    # "sisl/waterworld_v4": waterworld_v4,
    # "sisl/pursuit_v4": pursuit_v4,
}
