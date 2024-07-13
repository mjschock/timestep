import os

from connexion import AsyncApp
import uvicorn

from timestep.api import generate_token

user_id = -1
token = generate_token(user_id)

with open("OPENAI_API_KEY", "w") as f:
    f.write(token)

connexion_app = AsyncApp(__name__)

connexion_app.add_api(
    "apis/openai/openapi/openapi.yaml",
    base_path="/api/openai/v1",
    pythonic_params=True,
    resolver_error=501,
)

connexion_app.add_api(
    "apis/v1/openapi/openapi.yaml",
    base_path="/v1", # TODO: move this?
    pythonic_params=True,
    resolver_error=501,
)

app = connexion_app

cwd = os.getcwd()
print('cwd: ', cwd)

def main():
    uvicorn.run(
        "timestep.serve:app",
        host="0.0.0.0",
        log_level="info",
        port=8000,
        # reload=True,
        # reload_dirs=[
        #     f"{cwd}/apis",
        # ],
    )


if __name__ == "__main__":
    main()
