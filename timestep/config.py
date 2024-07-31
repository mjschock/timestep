from typing import Optional

from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # openai_api_key: SecretStr = Field(default=None)
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
