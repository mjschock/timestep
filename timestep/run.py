import os
from pathlib import Path
from typing import Any, Callable

from connexion import AsyncApp
from connexion.exceptions import OAuthProblem
from connexion.resolver import RelativeResolver, Resolver
from connexion.utils import get_function_from_name

from timestep.api import generate_token

token = generate_token(47)
print('token: ', token)

app = AsyncApp(__name__)

app.add_api(
    "apis/openai/openapi/openapi.yaml",
    base_path="/api/openai/v1",
    pythonic_params=True,
    # resolver=RelativeResolver('timestep.api'),
    resolver_error=501,
)
