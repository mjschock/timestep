import asyncio
from fastapi.testclient import TestClient
import pytest
import pytest_asyncio
from asgi_lifespan import LifespanManager
from httpx import AsyncClient

from timestep.server import fastapi_app

@pytest_asyncio.fixture()
async def current_loop():
    return asyncio.get_running_loop()

@pytest.fixture(
    autouse=True,
    # scope="session",
    scope="function"
)
async def client(current_loop, monkeypatch):
    # _client = TestClient(
    #     app=fastapi_app,
    #     base_url="http://testserver",
    # )

    # monkeypatch.setenv("OPENAI_API_KEY", "openai_api_key")
    # monkeypatch.setenv("OPENAI_BASE_URL", f"{_client.base_url}/api/openai/v1")

    # # await _client.lifespan()

    # async with _client.lifespan():
    #     yield _client

    # _client.close()

    async with LifespanManager(
        app=fastapi_app,
    ) as manager:
        # async with AsyncClient(
        #     app=fastapi_app,
        #     base_url="http://testserver",
        # ) as _client:
        #     yield _client

        _client = TestClient(
            # app=fastapi_app,
            app=manager.app,
            base_url="http://testserver",
        )

        yield _client

        _client.close()
