from fastapi import APIRouter, Depends, File, Form, Request, Response, UploadFile

from backend.services.audio_service import AudioService
from backend.services.speech_to_image_service import get_speech_to_image_service, SpeechToImageService

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


@audio_router.post("/audio/transcriptions/vlm")
async def create_vlm_transcription(
    file: UploadFile = AUDIO_FILE_DEPENDENCY,
    image_type: str = Form("spectrogram"),
    vlm_model: str = Form("HuggingFaceTB/SmolVLM2-256M-Video-Instruct"),
    prompt: str = Form("Please transcribe the speech shown in this audio spectrogram image. Extract all spoken words and convert them to text."),
    service: SpeechToImageService = Depends(get_speech_to_image_service),  # noqa: B008
) -> str:
    """Transcribes audio using VLM by converting speech to image representation."""
    return await service.transcribe_with_vlm(
        file, image_type, vlm_model, prompt
    )


@audio_router.post("/audio/transcriptions/compare")
async def compare_transcription_methods(
    file: UploadFile = AUDIO_FILE_DEPENDENCY,
    vlm_prompt: str = Form("Please transcribe the speech shown in this audio spectrogram image. Extract all spoken words and convert them to text."),
    service: SpeechToImageService = Depends(get_speech_to_image_service),  # noqa: B008
) -> dict[str, str]:
    """Compares traditional STT with VLM-based transcription methods."""
    return await service.compare_transcription_methods(file, vlm_prompt)
