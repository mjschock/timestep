import os
from pathlib import Path
from typing import Any, Callable

import connexion
from connexion import AsyncApp, ConnexionMiddleware
from connexion.exceptions import OAuthProblem
from connexion.resolver import RelativeResolver, Resolver
from connexion.utils import get_function_from_name
from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
from flask import Flask, request
from markupsafe import escape

from timestep.api import generate_token

token = generate_token(47)
print('token: ', token)

connexion_app = AsyncApp(__name__)
# connexion_app = AsyncApp(import_name="timestep")
# connexion_app = connexion.App(__name__)
# connexion_app = connexion.FlaskApp(__name__)

connexion_app.add_api(
    "apis/openai/openapi/openapi.yaml",
    base_path="/api/openai/v1",
    pythonic_params=True,
    # resolver=RelativeResolver('timestep.api'),
    resolver_error=501,
)

connexion_app.add_api(
    "apis/v1/openapi/openapi.yaml",
    base_path="/v1", # TODO: move this?
    pythonic_params=True,
    # resolver=RelativeResolver('timestep.api'),
    resolver_error=501,
)

# flask_app = Flask(__name__)
# # flask_app = connexion_app._middleware_app.app
# # flask_app = connexion_app.app

# @flask_app.route("/")
# def flask_main():
#     name = request.args.get("name", "World")
#     return f"Hello, {escape(name)} from Flask!"


# fastapi_app = FastAPI()


# @fastapi_app.get("/v2")
# def read_main():
#     return {"message": "Hello World"}


# app.mount("/api/openai/v1", WSGIMiddleware(flask_app))
# app.mount("/api/openai/v1", flask_app)
# fastapi_app.mount("/v1", WSGIMiddleware(flask_app))
# fastapi_app.mount("/api/openai", connexion_app)
# fastapi_app.mount("/", connexion_app)

# connexion_app.add_middleware(ConnexionMiddleware(fastapi_app.add_middleware
# fastapi_app.add_middleware(ConnexionMiddleware(connexion_app))

app = connexion_app
# app = fastapi_app
