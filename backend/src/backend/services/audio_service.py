# mypy: ignore-errors
import tempfile

from fastapi import HTTPException, Request, UploadFile
from fastapi.responses import Response

from backend.logging_config import logger
from backend.services.models_service import get_models_service
from backend.services.speech_to_image_service import get_speech_to_image_service


class AudioService:
    async def create_speech(self, request: Request) -> Response:
        """Generates audio from the input text."""
        try:
            logger.info("Received request for speech synthesis")
            # Parse request body
            try:
                body = await request.json()
            except Exception:
                body = {}
            model = body.get("model", "microsoft/speecht5_tts")
            body.get(
                "voice", "alloy"
            )  # For compatibility, but we'll use model's default
            input_text = body.get("input", "")
            response_format = body.get("response_format", "mp3")

            if not input_text:
                raise HTTPException(status_code=400, detail="Missing 'input' field.")

            # Get TTS pipeline from models service
            tts_pipeline = get_models_service().get_tts_pipeline(model)

            # Generate speech
            audio = tts_pipeline(input_text)

            # Convert to bytes
            if hasattr(audio, "numpy"):
                audio_array = audio.numpy()
            elif isinstance(audio, dict) and "audio" in audio:
                audio_array = audio["audio"]
            else:
                audio_array = audio

            # Convert to bytes (assuming 16-bit PCM)
            import numpy as np

            if isinstance(audio_array, np.ndarray):
                # Ensure it's the right format
                if audio_array.dtype != np.int16:
                    audio_array = (audio_array * 32767).astype(np.int16)
                audio_bytes = audio_array.tobytes()
            else:
                audio_bytes = audio_array

            # Return audio response
            return Response(
                content=audio_bytes,
                media_type=f"audio/{response_format}",
                headers={"Content-Disposition": "attachment; filename=speech.mp3"},
            )

        except Exception as e:
            logger.error(f"Speech generation failed: {e}", exc_info=True)
            raise HTTPException(
                status_code=500, detail=f"Speech generation failed: {str(e)}"
            ) from e

    async def create_transcription_with_upload(
        self,
        audio_file: UploadFile,
        model: str = "openai/whisper-tiny",
        response_format: str = "text",
        language: str = "en",
        prompt: str = "",
        temperature: float = 0.0,
    ) -> dict[str, str] | str:
        """Transcribes audio into the input language using UploadFile."""
        try:
            logger.info("Received request for audio transcription")

            # Check if this is a VLM-based model
            if model.startswith("vlm:"):
                # Extract VLM parameters from model string
                # Format: vlm:image_type:vlm_model_name
                parts = model.split(":")
                if len(parts) >= 2:
                    image_type = parts[1] if len(parts) > 1 else "spectrogram"
                    vlm_model = parts[2] if len(parts) > 2 else "HuggingFaceTB/SmolVLM2-256M-Video-Instruct"
                    
                    logger.info(f"Using VLM-based transcription with {image_type} visualization")
                    
                    # Use VLM-based transcription
                    speech_to_image_service = get_speech_to_image_service()
                    vlm_prompt = prompt if prompt else f"Please transcribe the speech shown in this audio {image_type} image. Extract all spoken words and convert them to text."
                    
                    text = await speech_to_image_service.transcribe_with_vlm(
                        audio_file, image_type, vlm_model, vlm_prompt
                    )
                    
                    if response_format == "json":
                        return {"text": text}
                    else:
                        return text
                else:
                    raise HTTPException(
                        status_code=400, 
                        detail="Invalid VLM model format. Use: vlm:image_type:vlm_model_name"
                    )
            else:
                # Traditional STT approach
                # Save to temp file
                with tempfile.NamedTemporaryFile(delete=True, suffix=".wav") as tmp:
                    content = await audio_file.read()
                    tmp.write(content)
                    tmp.flush()

                    # Get STT pipeline from models service
                    stt_pipeline = get_models_service().get_stt_pipeline(model)

                    # Run transcription with minimal parameters
                    result = stt_pipeline(tmp.name)

                    text = (
                        result["text"]
                        if isinstance(result, dict) and "text" in result
                        else str(result)
                    )

                    if response_format == "json":
                        return {"text": text}
                    else:
                        return text

        except Exception as e:
            logger.error(f"Transcription failed: {e}", exc_info=True)
            raise HTTPException(
                status_code=500, detail=f"Transcription failed: {str(e)}"
            ) from e

    async def create_translation_with_upload(
        self,
        audio_file: UploadFile,
        model: str = "openai/whisper-tiny",
        response_format: str = "text",
        prompt: str = "",
        temperature: float = 0.0,
    ) -> dict[str, str] | str:
        """Translates audio into English using UploadFile."""
        try:
            logger.info("Received request for audio translation")

            # Check if this is a VLM-based model
            if model.startswith("vlm:"):
                # Extract VLM parameters from model string
                # Format: vlm:image_type:vlm_model_name
                parts = model.split(":")
                if len(parts) >= 2:
                    image_type = parts[1] if len(parts) > 1 else "spectrogram"
                    vlm_model = parts[2] if len(parts) > 2 else "HuggingFaceTB/SmolVLM2-256M-Video-Instruct"
                    
                    logger.info(f"Using VLM-based translation with {image_type} visualization")
                    
                    # Use VLM-based translation (same as transcription but with translation prompt)
                    speech_to_image_service = get_speech_to_image_service()
                    vlm_prompt = prompt if prompt else f"Please translate the speech shown in this audio {image_type} image to English. Extract all spoken words and convert them to English text."
                    
                    text = await speech_to_image_service.transcribe_with_vlm(
                        audio_file, image_type, vlm_model, vlm_prompt
                    )
                    
                    if response_format == "json":
                        return {"text": text}
                    else:
                        return text
                else:
                    raise HTTPException(
                        status_code=400, 
                        detail="Invalid VLM model format. Use: vlm:image_type:vlm_model_name"
                    )
            else:
                # Traditional STT approach
                # Save to temp file
                with tempfile.NamedTemporaryFile(delete=True, suffix=".wav") as tmp:
                    content = await audio_file.read()
                    tmp.write(content)
                    tmp.flush()

                    # Get STT pipeline from models service
                    stt_pipeline = get_models_service().get_stt_pipeline(model)

                    # Run translation (same as transcription but with English output)
                    result = stt_pipeline(tmp.name)

                    text = (
                        result["text"]
                        if isinstance(result, dict) and "text" in result
                        else str(result)
                    )

                    if response_format == "json":
                        return {"text": text}
                    else:
                        return text

        except Exception as e:
            logger.error(f"Translation failed: {e}", exc_info=True)
            raise HTTPException(
                status_code=500, detail=f"Translation failed: {str(e)}"
            ) from e

    async def create_transcription(self, request: Request) -> dict[str, str] | str:
        """Transcribes audio into the input language."""
        try:
            logger.info("Received request for audio transcription")
            # Parse multipart form
            form = await request.form()
            audio_file_raw = form.get("file")
            if not isinstance(audio_file_raw, UploadFile):
                raise HTTPException(status_code=400, detail="Missing audio file.")
            audio_file: UploadFile = audio_file_raw
            model = form.get("model", "openai/whisper-tiny")
            response_format = form.get("response_format", "text")
            form.get("language", "en")
            form.get("prompt")
            form.get("temperature")

            # Save to temp file
            with tempfile.NamedTemporaryFile(delete=True, suffix=".wav") as tmp:
                content = await audio_file.read()
                tmp.write(content)
                tmp.flush()

                # Get STT pipeline from models service
                stt_pipeline = get_models_service().get_stt_pipeline(model)

                # Run transcription with minimal parameters
                result = stt_pipeline(tmp.name)

                text = (
                    result["text"]
                    if isinstance(result, dict) and "text" in result
                    else str(result)
                )

            if response_format == "json":
                return {"text": text}
            return text

        except Exception as e:
            logger.error(f"Transcription failed: {e}", exc_info=True)
            raise HTTPException(
                status_code=500, detail=f"Transcription failed: {str(e)}"
            ) from e

    async def create_translation(self, request: Request) -> dict[str, str] | str:
        """Translates audio into English."""
        try:
            # Parse multipart form
            form = await request.form()
            audio_file_raw = form.get("file")
            if not isinstance(audio_file_raw, UploadFile):
                raise HTTPException(status_code=400, detail="Missing audio file.")
            audio_file: UploadFile = audio_file_raw
            model = form.get("model", "openai/whisper-tiny")
            response_format = form.get("response_format", "text")
            form.get("prompt")
            form.get("temperature")

            # Save to temp file
            with tempfile.NamedTemporaryFile(delete=True, suffix=".wav") as tmp:
                content = await audio_file.read()
                tmp.write(content)
                tmp.flush()

                # Get STT pipeline from models service
                stt_pipeline = get_models_service().get_stt_pipeline(model)

                # Run translation (Whisper can translate to English)
                result = stt_pipeline(tmp.name)

                text = (
                    result["text"]
                    if isinstance(result, dict) and "text" in result
                    else str(result)
                )

            if response_format == "json":
                return {"text": text}
            return text

        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Translation failed: {str(e)}"
            ) from e
