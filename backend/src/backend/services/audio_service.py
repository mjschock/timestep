# mypy: ignore-errors
import io
import tempfile
from typing import Any

import numpy as np
import torch
from fastapi import HTTPException, Request, UploadFile
from fastapi.responses import Response
from PIL import Image
import librosa
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend

from backend.logging_config import logger
from backend.services.models_service import get_models_service


class AudioService:
    def __init__(self):
        self.models_service = get_models_service()
    
    async def _audio_to_spectrogram_image(self, audio_file: UploadFile) -> Image.Image:
        """Convert audio file to a spectrogram image."""
        try:
            # Read audio file
            content = await audio_file.read()
            
            # Load audio using librosa
            audio_data, sr = librosa.load(io.BytesIO(content), sr=None)
            
            # Generate mel-spectrogram
            mel_spec = librosa.feature.melspectrogram(
                y=audio_data, 
                sr=sr,
                n_mels=128,
                fmax=8000
            )
            
            # Convert to log scale
            mel_spec_db = librosa.power_to_db(mel_spec, ref=np.max)
            
            # Create figure and plot
            fig, ax = plt.subplots(figsize=(10, 4))
            img = librosa.display.specshow(
                mel_spec_db, 
                sr=sr, 
                x_axis='time', 
                y_axis='mel',
                ax=ax
            )
            
            # Add colorbar
            fig.colorbar(img, ax=ax, format='%+2.0f dB')
            ax.set_title('Mel-Spectrogram')
            
            # Convert plot to PIL Image
            buf = io.BytesIO()
            fig.savefig(buf, format='png', dpi=150, bbox_inches='tight')
            buf.seek(0)
            plt.close(fig)
            
            return Image.open(buf)
            
        except Exception as e:
            logger.error(f"Failed to convert audio to spectrogram: {e}")
            raise HTTPException(
                status_code=500, 
                detail=f"Failed to convert audio to spectrogram: {str(e)}"
            )
    
    async def _audio_to_waveform_image(self, audio_file: UploadFile) -> Image.Image:
        """Convert audio file to a waveform image."""
        try:
            # Read audio file
            content = await audio_file.read()
            
            # Load audio using librosa
            audio_data, sr = librosa.load(io.BytesIO(content), sr=None)
            
            # Create figure and plot waveform
            fig, ax = plt.subplots(figsize=(12, 3))
            librosa.display.waveshow(audio_data, sr=sr, ax=ax)
            ax.set_title('Audio Waveform')
            ax.set_xlabel('Time (s)')
            ax.set_ylabel('Amplitude')
            
            # Convert plot to PIL Image
            buf = io.BytesIO()
            fig.savefig(buf, format='png', dpi=150, bbox_inches='tight')
            buf.seek(0)
            plt.close(fig)
            
            return Image.open(buf)
            
        except Exception as e:
            logger.error(f"Failed to convert audio to waveform: {e}")
            raise HTTPException(
                status_code=500, 
                detail=f"Failed to convert audio to waveform: {str(e)}"
            )
    
    async def _audio_to_mfcc_image(self, audio_file: UploadFile) -> Image.Image:
        """Convert audio file to MFCC (Mel-frequency cepstral coefficients) image."""
        try:
            # Read audio file
            content = await audio_file.read()
            
            # Load audio using librosa
            audio_data, sr = librosa.load(io.BytesIO(content), sr=None)
            
            # Extract MFCC features
            mfcc = librosa.feature.mfcc(y=audio_data, sr=sr, n_mfcc=13)
            
            # Create figure and plot
            fig, ax = plt.subplots(figsize=(10, 4))
            img = librosa.display.specshow(
                mfcc, 
                sr=sr, 
                x_axis='time',
                ax=ax
            )
            
            # Add colorbar
            fig.colorbar(img, ax=ax)
            ax.set_title('MFCC Features')
            
            # Convert plot to PIL Image
            buf = io.BytesIO()
            fig.savefig(buf, format='png', dpi=150, bbox_inches='tight')
            buf.seek(0)
            plt.close(fig)
            
            return Image.open(buf)
            
        except Exception as e:
            logger.error(f"Failed to convert audio to MFCC: {e}")
            raise HTTPException(
                status_code=500, 
                detail=f"Failed to convert audio to MFCC: {str(e)}"
            )
    
    async def _transcribe_with_vlm(
        self,
        audio_file: UploadFile,
        image_type: str = "spectrogram",
        vlm_model: str = "HuggingFaceTB/SmolVLM2-256M-Video-Instruct",
        prompt: str = "Please transcribe the speech shown in this audio spectrogram image. Extract all spoken words and convert them to text."
    ) -> str:
        """Transcribe audio by converting it to an image representation and using a VLM."""
        try:
            logger.info(f"Starting VLM-based transcription with {image_type} visualization")
            
            # Convert audio to image based on type
            if image_type == "spectrogram":
                audio_image = await self._audio_to_spectrogram_image(audio_file)
            elif image_type == "waveform":
                audio_image = await self._audio_to_waveform_image(audio_file)
            elif image_type == "mfcc":
                audio_image = await self._audio_to_mfcc_image(audio_file)
            else:
                raise HTTPException(
                    status_code=400, 
                    detail=f"Unsupported image type: {image_type}. Supported types: spectrogram, waveform, mfcc"
                )
            
            # Get VLM model and processor
            model, processor = self.models_service.get_model_instance(vlm_model)
            
            # Prepare the image and prompt for the VLM
            if hasattr(processor, 'image_processor'):
                # Use image processor if available
                image_inputs = processor.image_processor(audio_image, return_tensors="pt")
            else:
                # Fallback: convert image to tensor
                import torchvision.transforms as transforms
                transform = transforms.Compose([
                    transforms.Resize((224, 224)),
                    transforms.ToTensor(),
                    transforms.Normalize(mean=[0.485, 0.456, 0.406], 
                                      std=[0.229, 0.224, 0.225])
                ])
                image_inputs = {"pixel_values": transform(audio_image).unsqueeze(0)}
            
            # Prepare text inputs
            text_inputs = processor.tokenizer(
                prompt,
                return_tensors="pt",
                padding=True,
                truncation=True
            )
            
            # Generate transcription
            with torch.no_grad():
                outputs = model.generate(
                    **text_inputs,
                    **image_inputs,
                    max_length=512,
                    num_beams=4,
                    early_stopping=True,
                    do_sample=False
                )
            
            # Decode the output
            transcription = processor.tokenizer.decode(outputs[0], skip_special_tokens=True)
            
            # Clean up the transcription (remove the prompt if it appears in output)
            if prompt.lower() in transcription.lower():
                transcription = transcription.replace(prompt, "").strip()
            
            logger.info(f"VLM transcription completed: {transcription[:100]}...")
            return transcription
            
        except Exception as e:
            logger.error(f"VLM-based transcription failed: {e}", exc_info=True)
            raise HTTPException(
                status_code=500, 
                detail=f"VLM-based transcription failed: {str(e)}"
            )

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
        model: str = "vlm:spectrogram:HuggingFaceTB/SmolVLM2-256M-Video-Instruct",
        response_format: str = "text",
        language: str = "en",
        prompt: str = "",
        temperature: float = 0.0,
    ) -> dict[str, str] | str:
        """Transcribes audio into the input language using VLM-based approach."""
        try:
            logger.info("Received request for audio transcription")

            # Parse model string to determine approach
            if model.startswith("vlm:"):
                # VLM-based approach (primary method)
                parts = model.split(":")
                if len(parts) >= 2:
                    image_type = parts[1] if len(parts) > 1 else "spectrogram"
                    vlm_model = parts[2] if len(parts) > 2 else "HuggingFaceTB/SmolVLM2-256M-Video-Instruct"
                    
                    logger.info(f"Using VLM-based transcription with {image_type} visualization")
                    
                    # Use VLM-based transcription
                    vlm_prompt = prompt if prompt else f"Please transcribe the speech shown in this audio {image_type} image. Extract all spoken words and convert them to text."
                    
                    text = await self._transcribe_with_vlm(
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
                # Fallback to traditional STT approach (legacy support)
                logger.info(f"Using traditional STT approach with model: {model}")
                
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
        model: str = "vlm:spectrogram:HuggingFaceTB/SmolVLM2-256M-Video-Instruct",
        response_format: str = "text",
        prompt: str = "",
        temperature: float = 0.0,
    ) -> dict[str, str] | str:
        """Translates audio into English using VLM-based approach."""
        try:
            logger.info("Received request for audio translation")

            # Parse model string to determine approach
            if model.startswith("vlm:"):
                # VLM-based approach (primary method)
                parts = model.split(":")
                if len(parts) >= 2:
                    image_type = parts[1] if len(parts) > 1 else "spectrogram"
                    vlm_model = parts[2] if len(parts) > 2 else "HuggingFaceTB/SmolVLM2-256M-Video-Instruct"
                    
                    logger.info(f"Using VLM-based translation with {image_type} visualization")
                    
                    # Use VLM-based translation (same as transcription but with translation prompt)
                    vlm_prompt = prompt if prompt else f"Please translate the speech shown in this audio {image_type} image to English. Extract all spoken words and convert them to English text."
                    
                    text = await self._transcribe_with_vlm(
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
                # Fallback to traditional STT approach (legacy support)
                logger.info(f"Using traditional STT approach with model: {model}")
                
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
