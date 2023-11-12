import uuid  # noqa: F401

from pettingzoo.utils.all_modules import all_environments as zoo_envs  # noqa: F401

envs_by_id = {
    "default": {
        "env_id": "default",
        "agent_ids": ["default"],
    },
}


# for env_name in zoo_envs.keys():
#     envs_by_id[f"{str(uuid.uuid4())}"] = {
#         "name": env_name,
#         "namespace": "zoo",
#         "agents": [
#             {
#                 "name": "foo",
#                 "models": ["bar"],
#             },
#         ],
#     }
