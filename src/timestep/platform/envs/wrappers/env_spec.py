from __future__ import annotations

from typing import Any

from pettingzoo.utils.env import AECEnv
from pettingzoo.utils.wrappers.base import BaseWrapper


class EnvSpecWrapper(BaseWrapper):
    def __init__(self, env: AECEnv):
        super().__init__(env)

    def __getattr__(self, value: str) -> Any:
        if value == "spec":
            return self.env.unwrapped.spec

        return super().__getattr__(value)
