import uuid

from pettingzoo.utils.all_modules import all_environments as zoo_envs

envs_by_id = {}


for env_name in zoo_envs.keys():
    envs_by_id[f"{str(uuid.uuid4())}"] = {
        "name": env_name,
        "namespace": "zoo",
        "agents": [
            {
                "name": "foo",
                "models": ["bar"],
            },
        ],
    }
