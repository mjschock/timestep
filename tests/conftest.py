import asyncio
import os
from typing import Dict, Union
import httpx
import openai
import pytest
import pytest_asyncio
from asgi_lifespan import LifespanManager

from timestep.server import fastapi_app
from timestep.config import Settings

settings = Settings()

@pytest_asyncio.fixture(
    autouse=True,
    scope="session",
)
async def app(tmp_path_factory, worker_id):
    async with LifespanManager(app=fastapi_app, startup_timeout=300) as manager:
        print("App is ready")
        yield manager.app
        print('App is closing')

@pytest_asyncio.fixture(
    scope="function"
)
async def current_loop():
    return asyncio.get_running_loop()

@pytest_asyncio.fixture(
    autouse=True,
    scope="function"
)
async def client(app, current_loop, monkeypatch):
    assert current_loop is asyncio.get_running_loop()

    base_url = settings.openai_base_url.replace("/api/openai/v1", "") # TODO: create a new setting for the base_url
    assert base_url == "http://localhost:8000", f"Unexpected base_url: {base_url}"

    monkeypatch.setenv("OPENAI_API_KEY", settings.openai_api_key.get_secret_value())
    monkeypatch.setenv("OPENAI_BASE_URL", settings.openai_base_url.replace(base_url, "http://openai.local"))
    assert os.getenv("OPENAI_BASE_URL") == "http://openai.local/api/openai/v1", f"Unexpected OPENAI_BASE_URL: {os.getenv('OPENAI_BASE_URL')}"

    # monkeypatch.setattr(
    #     httpx.HTTPTransport,
    #     "handle_request",
    #     mocked_handle_request,
    # )

    async with httpx.AsyncClient(base_url=base_url, transport=httpx.ASGITransport(app=app)) as client, openai.AsyncOpenAI(
        api_key=settings.openai_api_key.get_secret_value(),
        base_url=os.getenv("OPENAI_BASE_URL"),
    ) as openai_client:
        print("Clients are ready")
        # yield client
        # yield client, openai_client
        clients: Dict[str, Union[httpx.AsyncClient, openai.AsyncOpenAI]] = {
            # "httpx": client,
            "async_httpx": client,
            "async_openai": openai_client,
        }

        yield clients["async_httpx"] # TODO: return both clients
        print('Clients are closing')

@pytest.fixture
def non_mocked_hosts() -> list:
    return ["localhost"]
