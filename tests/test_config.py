from timestep.config import Settings

def test_settings():
    settings = Settings()

    assert settings.openai_api_key.get_secret_value() == "**********"
