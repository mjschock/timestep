import pytest
from timestep.config import Settings

def test_settings_instantiation():
    settings = Settings()
    assert settings is not None

def test_settings_openai_api_key_exists():
    settings = Settings()
    assert hasattr(settings, 'openai_api_key')

# def test_settings_openai_api_key_value():
#     settings = Settings()
#     # Assuming the secret value is set to "**********" for testing purposes
#     assert settings.openai_api_key.get_secret_value() == "**********"
