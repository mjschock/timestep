from fastapi.testclient import TestClient
import pytest
from timestep.server import fastapi_app

@pytest.fixture(
    autouse=True,
    # scope="session",
    scope="function"
)
def client(monkeypatch):
    _client = TestClient(fastapi_app)

    monkeypatch.setenv("OPENAI_API_KEY", "openai_api_key")
    monkeypatch.setenv("OPENAI_BASE_URL", f"{_client.base_url}/api/openai/v1")

    yield _client

    _client.close()
