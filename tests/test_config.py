import pytest

from timestep.config import settings


def test_settings_instantiation():

    assert settings is not None


def test_settings_openai_api_key_exists():

    assert hasattr(settings, "openai_api_key")


# def test_settings_openai_api_key_value():
#
#     # Assuming the secret value is set to "**********" for testing purposes
#     assert settings.openai_api_key.get_secret_value() == "**********"
