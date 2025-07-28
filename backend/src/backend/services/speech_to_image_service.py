# mypy: ignore-errors
import io
import tempfile
from typing import Any

import numpy as np
import torch
from fastapi import HTTPException, UploadFile
from PIL import Image
import librosa
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend

from backend.logging_config import logger
from backend.services.models_service import get_models_service


class SpeechToImageService:
    """Service for converting speech to image representations and using VLM for transcription."""
    
    def __init__(self):
        self.models_service = get_models_service()
    
    async def _audio_to_spectrogram_image(self, audio_file: UploadFile) -> Image.Image:
        """
        Convert audio file to a spectrogram image.
        
        Args:
            audio_file: The uploaded audio file
            
        Returns:
            PIL Image of the spectrogram
        """
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
        """
        Convert audio file to a waveform image.
        
        Args:
            audio_file: The uploaded audio file
            
        Returns:
            PIL Image of the waveform
        """
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
        """
        Convert audio file to MFCC (Mel-frequency cepstral coefficients) image.
        
        Args:
            audio_file: The uploaded audio file
            
        Returns:
            PIL Image of the MFCC
        """
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
    
    async def transcribe_with_vlm(
        self,
        audio_file: UploadFile,
        image_type: str = "spectrogram",
        vlm_model: str = "HuggingFaceTB/SmolVLM2-256M-Video-Instruct",
        prompt: str = "Please transcribe the speech shown in this audio spectrogram image. Extract all spoken words and convert them to text."
    ) -> str:
        """
        Transcribe audio by converting it to an image representation and using a VLM.
        
        Args:
            audio_file: The uploaded audio file
            image_type: Type of audio visualization ("spectrogram", "waveform", "mfcc")
            vlm_model: The VLM model to use for transcription
            prompt: Prompt to give the VLM for transcription
            
        Returns:
            Transcribed text
        """
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
    
    async def compare_transcription_methods(
        self,
        audio_file: UploadFile,
        vlm_prompt: str = "Please transcribe the speech shown in this audio spectrogram image. Extract all spoken words and convert them to text."
    ) -> dict[str, Any]:
        """
        Compare traditional STT with VLM-based transcription.
        
        Args:
            audio_file: The uploaded audio file
            vlm_prompt: Prompt for VLM transcription
            
        Returns:
            Dictionary with both transcription results
        """
        try:
            logger.info("Comparing STT vs VLM transcription methods")
            
            # Traditional STT
            audio_service = get_models_service().get_stt_pipeline("openai/whisper-tiny")
            
            # Save to temp file for STT
            with tempfile.NamedTemporaryFile(delete=True, suffix=".wav") as tmp:
                content = await audio_file.read()
                tmp.write(content)
                tmp.flush()
                
                # Run traditional STT
                stt_result = audio_service(tmp.name)
                stt_text = stt_result["text"] if isinstance(stt_result, dict) else str(stt_result)
            
            # Reset file pointer for VLM
            await audio_file.seek(0)
            
            # VLM-based transcription
            vlm_text = await self.transcribe_with_vlm(
                audio_file, 
                image_type="spectrogram",
                prompt=vlm_prompt
            )
            
            return {
                "traditional_stt": stt_text,
                "vlm_transcription": vlm_text,
                "methods_compared": ["whisper", "vlm_spectrogram"]
            }
            
        except Exception as e:
            logger.error(f"Comparison failed: {e}", exc_info=True)
            raise HTTPException(
                status_code=500, 
                detail=f"Transcription comparison failed: {str(e)}"
            )


def get_speech_to_image_service() -> SpeechToImageService:
    """Get singleton instance of SpeechToImageService."""
    if not hasattr(get_speech_to_image_service, '_instance'):
        get_speech_to_image_service._instance = SpeechToImageService()
    return get_speech_to_image_service._instance