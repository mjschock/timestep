"""
Enhanced TTS API with spectrogram-based synthesis and configurable parameters.
"""

from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import Response
from pydantic import BaseModel
from typing import Optional, Dict, Any
import numpy as np

from backend.services.tts_spectrogram_service import get_spectrogram_tts_service
from backend.logging_config import logger

router = APIRouter()


class TTSRequest(BaseModel):
    """Request model for enhanced TTS synthesis."""
    text: str
    model: str = "microsoft/speecht5_tts"
    response_format: str = "mp3"
    
    # Spectrogram generation parameters
    pre_emphasis: Optional[float] = 0.97
    n_mels: Optional[int] = 80
    n_fft: Optional[int] = 1024
    hop_length: Optional[int] = 256
    win_length: Optional[int] = 1024
    fmin: Optional[int] = 0
    fmax: Optional[int] = 11025
    normalize: Optional[bool] = True
    
    # Preprocessing parameters
    smooth: Optional[bool] = False
    freq_mask: Optional[bool] = False
    freq_mask_param: Optional[int] = 10
    time_mask: Optional[bool] = False
    time_mask_param: Optional[int] = 10
    
    # Post-processing parameters
    normalize_audio: Optional[bool] = True
    fade_duration: Optional[float] = 0.01
    high_pass_filter: Optional[bool] = True
    high_pass_cutoff: Optional[int] = 80


class TTSOptionsResponse(BaseModel):
    """Response model for available TTS options."""
    options: Dict[str, Any]
    description: str


@router.post("/tts/synthesize")
async def synthesize_speech(request: TTSRequest) -> Response:
    """
    Synthesize speech using enhanced spectrogram-based TTS.
    
    This endpoint provides fine-grained control over the synthesis process,
    including spectrogram generation parameters, preprocessing options,
    and post-processing audio enhancements.
    """
    try:
        logger.info(f"Received enhanced TTS request for text: {request.text[:50]}...")
        
        # Get TTS service
        tts_service = get_spectrogram_tts_service()
        
        # Load models if not already loaded
        if tts_service.text_to_spectrogram_model is None:
            tts_service.load_models(request.model)
        
        # Prepare synthesis parameters
        synthesis_params = {
            "pre_emphasis": request.pre_emphasis,
            "n_mels": request.n_mels,
            "n_fft": request.n_fft,
            "hop_length": request.hop_length,
            "win_length": request.win_length,
            "fmin": request.fmin,
            "fmax": request.fmax,
            "normalize": request.normalize,
            "smooth": request.smooth,
            "freq_mask": request.freq_mask,
            "freq_mask_param": request.freq_mask_param,
            "time_mask": request.time_mask,
            "time_mask_param": request.time_mask_param,
            "normalize_audio": request.normalize_audio,
            "fade_duration": request.fade_duration,
            "high_pass_filter": request.high_pass_filter,
            "high_pass_cutoff": request.high_pass_cutoff
        }
        
        # Remove None values
        synthesis_params = {k: v for k, v in synthesis_params.items() if v is not None}
        
        # Synthesize speech
        audio = tts_service.synthesize_speech(request.text, **synthesis_params)
        
        # Convert to bytes
        if isinstance(audio, np.ndarray):
            # Normalize audio to [-1, 1] range if needed
            if audio.max() > 1.0 or audio.min() < -1.0:
                audio = np.clip(audio, -1.0, 1.0)
            
            # Convert to 16-bit PCM
            if audio.dtype != np.int16:
                audio = (audio * 32767).astype(np.int16)
            audio_bytes = audio.tobytes()
        else:
            audio_bytes = audio
        
        # Return audio response
        return Response(
            content=audio_bytes,
            media_type=f"audio/{request.response_format}",
            headers={"Content-Disposition": "attachment; filename=speech.mp3"},
        )
        
    except Exception as e:
        logger.error(f"Enhanced TTS synthesis failed: {e}", exc_info=True)
        raise HTTPException(
            status_code=500, detail=f"Enhanced TTS synthesis failed: {str(e)}"
        ) from e


@router.get("/tts/options")
async def get_tts_options() -> TTSOptionsResponse:
    """
    Get available TTS synthesis options and their default values.
    
    This endpoint provides information about all available parameters
    for customizing the spectrogram-based TTS synthesis process.
    """
    try:
        tts_service = get_spectrogram_tts_service()
        options = tts_service.get_synthesis_options()
        
        description = """
        Enhanced TTS synthesis with spectrogram generation and vocoder synthesis.
        
        Available parameters:
        - Spectrogram Generation: Control mel spectrogram creation (n_mels, n_fft, etc.)
        - Preprocessing: Apply smoothing, frequency/time masking for data augmentation
        - Post-processing: Audio normalization, fade effects, and filtering
        """
        
        return TTSOptionsResponse(
            options=options,
            description=description.strip()
        )
        
    except Exception as e:
        logger.error(f"Failed to get TTS options: {e}", exc_info=True)
        raise HTTPException(
            status_code=500, detail=f"Failed to get TTS options: {str(e)}"
        ) from e


@router.get("/tts/parameters")
async def get_audio_parameters() -> Dict[str, Any]:
    """
    Get current audio processing parameters.
    
    Returns the current audio processing parameters used by the TTS service.
    """
    try:
        tts_service = get_spectrogram_tts_service()
        return tts_service.get_audio_parameters()
        
    except Exception as e:
        logger.error(f"Failed to get audio parameters: {e}", exc_info=True)
        raise HTTPException(
            status_code=500, detail=f"Failed to get audio parameters: {str(e)}"
        ) from e


@router.post("/tts/spectrogram")
async def generate_spectrogram(request: TTSRequest) -> Dict[str, Any]:
    """
    Generate mel spectrogram from text without converting to audio.
    
    This endpoint is useful for analyzing the spectrogram generation process
    or for custom vocoder synthesis.
    """
    try:
        logger.info(f"Received spectrogram generation request for text: {request.text[:50]}...")
        
        # Get TTS service
        tts_service = get_spectrogram_tts_service()
        
        # Load models if not already loaded
        if tts_service.text_to_spectrogram_model is None:
            tts_service.load_models(request.model)
        
        # Prepare synthesis parameters
        synthesis_params = {
            "pre_emphasis": request.pre_emphasis,
            "n_mels": request.n_mels,
            "n_fft": request.n_fft,
            "hop_length": request.hop_length,
            "win_length": request.win_length,
            "fmin": request.fmin,
            "fmax": request.fmax,
            "normalize": request.normalize
        }
        
        # Remove None values
        synthesis_params = {k: v for k, v in synthesis_params.items() if v is not None}
        
        # Generate spectrogram
        mel_spectrogram = tts_service.text_to_spectrogram(request.text, **synthesis_params)
        
        return {
            "spectrogram_shape": mel_spectrogram.shape,
            "spectrogram_min": float(mel_spectrogram.min()),
            "spectrogram_max": float(mel_spectrogram.max()),
            "spectrogram_mean": float(mel_spectrogram.mean()),
            "parameters": synthesis_params
        }
        
    except Exception as e:
        logger.error(f"Spectrogram generation failed: {e}", exc_info=True)
        raise HTTPException(
            status_code=500, detail=f"Spectrogram generation failed: {str(e)}"
        ) from e