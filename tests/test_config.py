from timestep.config import Settings

def test_settings():
    settings = Settings()

    assert settings.openai_api_key == "openai_api_key"
