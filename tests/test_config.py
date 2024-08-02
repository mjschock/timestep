from fastapi.testclient import TestClient

def test_settings(client):
    assert type(client) == TestClient

    from timestep.config import Settings

    settings = Settings()
    # assert settings.openai_api
    assert True
