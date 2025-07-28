from fastapi import APIRouter, Depends, File, Form, Request, Response, UploadFile

from backend.services.audio_service import AudioService

audio_router = APIRouter()

# Module-level constants for dependencies to avoid ruff B008
AUDIO_FILE_DEPENDENCY = File(...)
AUDIO_FORM_DEPENDENCY = Form(...)


@audio_router.post("/audio/speech")
async def create_speech(
    request: Request,
    service: AudioService = Depends(AudioService),  # noqa: B008
) -> Response:
    """Generates audio from the input text."""
    return await service.create_speech(request)


@audio_router.post("/audio/transcriptions")
async def create_transcription(
    file: UploadFile = AUDIO_FILE_DEPENDENCY,
    model: str = Form("openai/whisper-tiny"),
    response_format: str = Form("text"),
    language: str = Form("en"),
    prompt: str = Form(""),
    temperature: float = Form(0.0),
    service: AudioService = Depends(AudioService),  # noqa: B008
) -> dict[str, str] | str:
    """Transcribes audio into the input language."""
    return await service.create_transcription_with_upload(
        file, model, response_format, language, prompt, temperature
    )


@audio_router.post("/audio/translations")
async def create_translation(
    file: UploadFile = AUDIO_FILE_DEPENDENCY,
    model: str = Form("openai/whisper-tiny"),
    response_format: str = Form("text"),
    prompt: str = Form(""),
    temperature: float = Form(0.0),
    service: AudioService = Depends(AudioService),  # noqa: B008
) -> dict[str, str] | str:
    """Translates audio into English."""
    return await service.create_translation_with_upload(
        file, model, response_format, prompt, temperature
    )
