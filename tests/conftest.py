import asyncio
import os
import httpx
import pytest_asyncio
from asgi_lifespan import LifespanManager

from timestep.server import fastapi_app
from timestep.config import Settings

settings = Settings()

@pytest_asyncio.fixture()
async def current_loop():
    return asyncio.get_running_loop()

@pytest_asyncio.fixture
async def app():
    async with LifespanManager(app=fastapi_app) as manager:
        print("App is ready")
        yield manager.app
        print('App is closing')

@pytest_asyncio.fixture(
    autouse=True,
    # scope="function"
)
async def client(app, monkeypatch):
    base_url = settings.openai_base_url.replace("/api/openai/v1", "") # TODO: create a new setting for the base_url
    assert base_url == "http://localhost:8000", f"Unexpected base_url: {base_url}"

    monkeypatch.setenv("OPENAI_API_KEY", settings.openai_api_key)
    # monkeypatch.setenv("OPENAI_API_KEY", "test-test-test-test")
    monkeypatch.setenv("OPENAI_BASE_URL", settings.openai_base_url)
    # monkeypatch.setenv("OPENAI_BASE_URL", "test-test-test-test")

    # sync_client = httpx.Client(app=app, base_url=base_url)
    def sync_client(*args, **kwargs):
        print('Sync client is not supported')
        print('args:', args)
        print('kwargs:', kwargs)
        raise NotImplementedError("Sync client is not supported")

    # monkeypatch.setattr(httpx, "Client", sync_client)
    monkeypatch.setattr("httpx.Client", sync_client)

    async with httpx.AsyncClient(app=app, base_url=base_url) as client:
        print("Client is ready")
        yield client
        print('Client is closing')

# @pytest.fixture(
#     autouse=True,
#     # scope="session",
#     scope="function"
# )
# async def client(current_loop, monkeypatch):
#     assert current_loop is asyncio.get_running_loop()

#     # _client = TestClient(
#     #     app=fastapi_app,
#     #     base_url="http://testserver",
#     # )

#     # monkeypatch.setenv("OPENAI_API_KEY", "openai_api_key")
#     # monkeypatch.setenv("OPENAI_BASE_URL", f"{_client.base_url}/api/openai/v1")

#     # # await _client.lifespan()

#     # async with _client.lifespan():
#     #     yield _client

#     # _client.close()

#     async with LifespanManager(
#         app=fastapi_app,
#     ) as manager:
#         # async with AsyncClient(
#         #     app=fastapi_app,
#         #     base_url="http://testserver",
#         # ) as _client:
#         #     yield _client

#         _client = TestClient(
#             # app=fastapi_app,
#             app=manager.app,
#             base_url="http://testserver",
#         )

#         yield _client

#         _client.close()
