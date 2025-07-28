import pytest


@pytest.mark.asyncio
async def test_audio_transcription(async_client, sample_audio):
    """Test audio transcription endpoint."""
    with open(sample_audio, "rb") as audio_file:
        response = await async_client.audio.transcriptions.create(
            model="openai/whisper-tiny", file=audio_file, response_format="text"
        )
    assert isinstance(response, str)


@pytest.mark.asyncio
async def test_audio_translation(async_client, sample_audio):
    """Test audio translation endpoint."""
    with open(sample_audio, "rb") as audio_file:
        response = await async_client.audio.translations.create(
            model="openai/whisper-tiny",
            file=audio_file,
            response_format="text",
        )
    assert isinstance(response, str)


@pytest.mark.asyncio
async def test_text_to_speech(async_client):
    """Test text-to-speech endpoint."""
    response = await async_client.audio.speech.create(
        model="microsoft/speecht5_tts",
        voice="alloy",
        input="Hello, this is a test of text to speech.",
    )
    assert hasattr(response, "content") or hasattr(response, "read")
