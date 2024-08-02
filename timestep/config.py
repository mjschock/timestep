# from typing import Optional

from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    bearerinfo_func: str = Field(default="timestep.api.decode_token")
    openai_api_key: SecretStr = Field(default="openai_api_key")
    openai_base_url: str = Field(default="http://localhost:8000/api/openai/v1")
    openai_org_id: str = Field(default="organization_id")
    openai_project_id: str = Field(default="project_id")
    poetry_repositories_testpypi_url: str = Field(
        default="https://test.pypi.org/legacy/"
    )
    poetry_virtualenvs_in_project: bool = Field(default=True)
    poetry_virtualenvs_prefer_active_python: bool = Field(default=True)
    prefect_api_url: str = Field(default="http://localhost:4200/api")
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
    # version: str = Field()

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        secrets_dir = "./secrets"
