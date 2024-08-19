import os

import typer
from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings

app_dir = typer.get_app_dir(__package__)

os.makedirs(f"{app_dir}/data", exist_ok=True)
os.makedirs(f"{app_dir}/models", exist_ok=True)
os.makedirs(f"{app_dir}/secrets", exist_ok=True)


class Settings(BaseSettings):
    app_dir: str = Field(default=app_dir)
    bearerinfo_func: str = Field(default="timestep.api.decode_token")
    default_hf_repo_id: str = Field(
        default="Mozilla/TinyLlama-1.1B-Chat-v1.0-llamafile"
        # default="squeeze-ai-lab/TinyAgent-1.1B-GGUF",
        # default="RichardErkhov/upstage_-_TinySolar-248m-4k-py-gguf",
        # default="mjschock/SmolLM-135M-Q4_K_M-GGUF",
        # default="mjschock/TinySolar-248m-4k-code-instruct-Q4_K_M-GGUF",
        # default="mjschock/TinySolar-248m-4k-py-Q4_K_M-GGUF",
        # default="mjschock/TinyLlama-1.1B-Chat-v1.0-Q4_K_M-GGUF",
        # default="mjschock/TinyLlama-1.1B-Chat-v1.0-Tinygrad"
        # default="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    )
    # default_hf_repo_id: str = Field(default="jartine/TinyLlama-1.1B-Chat-v1.0-GGUF")
    # default_hf_repo_id: str = Field(default="jartine/rocket-3B-llamafile")
    # default_hf_repo_id: str = Field(default="jartine/phi-2-llamafile")
    # default_llamafile_filename: str = Field(
    #     default="TinyLlama-1.1B-Chat-v1.0.F16.llamafile"
    # )
    # default_llamafile_filename: str = Field(default="TinyLlama-1.1B-Chat-v1.0.Q5_K_M.llamafile")
    # default_llamafile_filename: str = Field(default="rocket-3b.Q5_K_M.llamafile")
    # default_llamafile_filename: str = Field(default="phi-2.Q5_K_M.llamafile")
    default_llamafile_host: str = Field(default="0.0.0.0")
    default_llamafile_port: int = Field(default=8080)
    default_model_filename: str = Field(
        default="TinyLlama-1.1B-Chat-v1.0.F16.llamafile"
        # default="TinyAgent-1.1B-Q4_K_M.gguf",
        # default="TinyAgent-1.1B-F16.gguf",
        # default="TinySolar-248m-4k-py.Q8_0.gguf",
        # default="smollm-135m-q4_k_m.gguf", # TODO: what's a imatrix.data file and should it be used?
        # default="tinysolar-248m-4k-code-instruct-q4_k_m.gguf",
        # default="tinysolar-248m-4k-py-q4_k_m.gguf",
        # default="tinyllama-1.1b-chat-v1.0-q4_k_m.gguf",
        # default="Models-1.1B-F16.gguf",
        # default="model.safetensors",
    )
    default_multimodal_model_projector_filename: str | None = Field(
        default=None,
    )
    openai_api_key: SecretStr = Field(default="openai_api_key")
    openai_base_url: str = Field(default="http://localhost:8000/api/openai/v1")
    openai_org_id: str = Field(default="organization_id")
    openai_project_id: str = Field(default="project_id")
    poetry_repositories_testpypi_url: str = Field(
        default="https://test.pypi.org/legacy/"
    )
    poetry_virtualenvs_in_project: bool = Field(default=True)
    poetry_virtualenvs_prefer_active_python: bool = Field(default=True)
    prefect_api_url: str = Field(default="http://127.0.0.1:4200/api")
    prefect_logging_level: str = Field(default="INFO")
    prefect_logging_log_prints: bool = Field(default=True)
    pyenv_version: str = Field(default="3.10.14")

    # poetry_pypi_token_testpypi: SecretStr = Field(default=None)
    # poetry_virtualenvs_create: bool = Field()
    # poetry_virtualenvs_in_project: bool = Field()
    # prefect_api_key: Optional[SecretStr] = Field(default=None)
    # prefect_api_url: str = Field(
    #     default="http://prefect-server.default.svc.cluster.local:4200/api"
    # )
    # pyenv_version: str = Field()
    verbose: bool = Field(default=True)
    # version: str = Field()

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        # secrets_dir = "./secrets"  # TODO: Change to f"{app_dir}/secrets" when ready
        secrets_dir = f"{app_dir}/secrets"


settings = Settings()

if "OPENAI_API_KEY" not in os.environ:
    os.environ["OPENAI_API_KEY"] = settings.openai_api_key.get_secret_value()

if "OPENAI_BASE_URL" not in os.environ:
    os.environ["OPENAI_BASE_URL"] = settings.openai_base_url

if "PREFECT_API_URL" not in os.environ:
    os.environ["PREFECT_API_URL"] = settings.prefect_api_url
