import asyncio
import os
import httpx
import pytest
import pytest_asyncio
from asgi_lifespan import LifespanManager

# from timestep.database import create_db_and_tables
from timestep.server import fastapi_app
from timestep.config import Settings

settings = Settings()

@pytest_asyncio.fixture(
    scope="session",
)
async def app(tmp_path_factory, worker_id):
    async with LifespanManager(app=fastapi_app, startup_timeout=30) as manager:
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

    base_url = settings.openai_base_url.replace("/api/openai/v1", "")
    monkeypatch.setenv("OPENAI_API_KEY", settings.openai_api_key.get_secret_value())
    monkeypatch.setenv("OPENAI_BASE_URL", settings.openai_base_url.replace(base_url, "http://openai.local"))
    assert os.getenv("OPENAI_BASE_URL") == "http://openai.local/api/openai/v1", f"Unexpected OPENAI_BASE_URL: {os.getenv('OPENAI_BASE_URL')}"

    # monkeypatch.setattr(
    #     httpx.HTTPTransport,
    #     "handle_request",
    #     mocked_handle_request,
    # )

    async with httpx.AsyncClient(base_url=base_url, transport=httpx.ASGITransport(app=app)) as client:
        print("Client is ready")
        yield client
        print('Client is closing')

@pytest.fixture
def non_mocked_hosts() -> list:
    return ["localhost"]
