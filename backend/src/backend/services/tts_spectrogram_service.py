"""
Text-to-Speech service using spectrogram generation and vocoder synthesis.
This provides better audio quality and more control over the synthesis process.
"""

import torch
import numpy as np
import librosa
import soundfile as sf
from typing import Optional, Tuple, Any, Dict
from transformers import (
    SpeechT5HifiGan,
    SpeechT5Processor,
    SpeechT5ForTextToSpeech,
    AutoTokenizer,
    AutoModelForSeq2SeqLM
)
from fastapi import HTTPException
import logging

logger = logging.getLogger(__name__)


class SpectrogramTTSService:
    """
    Text-to-Speech service using spectrogram generation and vocoder synthesis.
    
    This approach:
    1. Converts text to spectrogram using a text-to-spectrogram model
    2. Converts spectrogram to audio using a vocoder
    3. Provides better control over audio quality and characteristics
    """
    
    def __init__(self):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.processor = None
        self.text_to_spectrogram_model = None
        self.vocoder = None
        self.sample_rate = 22050
        self.hop_length = 256
        self.win_length = 1024
        self.n_fft = 1024
        self.n_mels = 80
        
    def load_models(self, model_name: str = "microsoft/speecht5_tts"):
        """
        Load the text-to-spectrogram model and vocoder.
        
        Args:
            model_name: The name of the model to load
        """
        try:
            logger.info(f"Loading TTS models for {model_name}")
            
            # Load processor and model
            self.processor = SpeechT5Processor.from_pretrained(model_name)
            self.text_to_spectrogram_model = SpeechT5ForTextToSpeech.from_pretrained(model_name)
            
            # Load vocoder (HiFi-GAN)
            vocoder_name = "microsoft/speecht5_hifigan"
            self.vocoder = SpeechT5HifiGan.from_pretrained(vocoder_name)
            
            # Move models to device
            self.text_to_spectrogram_model.to(self.device)
            self.vocoder.to(self.device)
            
            logger.info("TTS models loaded successfully")
            
        except Exception as e:
            logger.error(f"Failed to load TTS models: {e}")
            raise HTTPException(
                status_code=500, 
                detail=f"Failed to load TTS models: {str(e)}"
            )
    
    def text_to_spectrogram(self, text: str, **kwargs) -> np.ndarray:
        """
        Convert text to mel spectrogram.
        
        Args:
            text: Input text to convert
            **kwargs: Additional parameters for spectrogram generation
            
        Returns:
            mel_spectrogram: Mel spectrogram as numpy array
        """
        try:
            # Process text
            inputs = self.processor(text=text, return_tensors="pt")
            inputs = {k: v.to(self.device) for k, v in inputs.items()}
            
            # Generate speech features (spectrogram)
            with torch.no_grad():
                speech = self.text_to_spectrogram_model.generate_speech(
                    inputs["input_ids"], 
                    speaker_embeddings=torch.zeros(1, 512).to(self.device),
                    vocoder=None  # We'll use our own vocoder
                )
            
            # Convert to mel spectrogram with enhanced processing
            mel_spectrogram = self._audio_to_mel_spectrogram(speech.cpu().numpy(), **kwargs)
            
            return mel_spectrogram
            
        except Exception as e:
            logger.error(f"Failed to generate spectrogram: {e}")
            raise HTTPException(
                status_code=500,
                detail=f"Failed to generate spectrogram: {str(e)}"
            )
    
    def spectrogram_to_audio(self, mel_spectrogram: np.ndarray, **kwargs) -> np.ndarray:
        """
        Convert mel spectrogram to audio using vocoder.
        
        Args:
            mel_spectrogram: Mel spectrogram as numpy array
            **kwargs: Additional parameters for vocoder synthesis
            
        Returns:
            audio: Audio waveform as numpy array
        """
        try:
            # Preprocess spectrogram
            mel_spectrogram = self._preprocess_spectrogram(mel_spectrogram, **kwargs)
            
            # Convert to tensor
            mel_tensor = torch.from_numpy(mel_spectrogram).unsqueeze(0).to(self.device)
            
            # Generate audio using vocoder
            with torch.no_grad():
                audio = self.vocoder(mel_tensor)
            
            # Post-process audio
            audio = self._postprocess_audio(audio.cpu().numpy().squeeze(), **kwargs)
            
            return audio
            
        except Exception as e:
            logger.error(f"Failed to convert spectrogram to audio: {e}")
            raise HTTPException(
                status_code=500,
                detail=f"Failed to convert spectrogram to audio: {str(e)}"
            )
    
    def _audio_to_mel_spectrogram(self, audio: np.ndarray, **kwargs) -> np.ndarray:
        """
        Convert audio to mel spectrogram with enhanced processing.
        
        Args:
            audio: Audio waveform
            **kwargs: Additional parameters for spectrogram generation
            
        Returns:
            mel_spectrogram: Mel spectrogram
        """
        # Ensure audio is mono
        if len(audio.shape) > 1:
            audio = np.mean(audio, axis=1)
        
        # Apply pre-emphasis filter for better high-frequency representation
        pre_emphasis = kwargs.get('pre_emphasis', 0.97)
        if pre_emphasis > 0:
            audio = np.append(audio[0], audio[1:] - pre_emphasis * audio[:-1])
        
        # Generate mel spectrogram with configurable parameters
        n_mels = kwargs.get('n_mels', self.n_mels)
        n_fft = kwargs.get('n_fft', self.n_fft)
        hop_length = kwargs.get('hop_length', self.hop_length)
        win_length = kwargs.get('win_length', self.win_length)
        
        mel_spectrogram = librosa.feature.melspectrogram(
            y=audio,
            sr=self.sample_rate,
            n_fft=n_fft,
            hop_length=hop_length,
            win_length=win_length,
            n_mels=n_mels,
            fmin=kwargs.get('fmin', 0),
            fmax=kwargs.get('fmax', self.sample_rate // 2)
        )
        
        # Convert to log scale with configurable reference
        ref = kwargs.get('ref', np.max)
        mel_spectrogram = librosa.power_to_db(mel_spectrogram, ref=ref)
        
        # Apply normalization if requested
        if kwargs.get('normalize', True):
            mel_spectrogram = self._normalize_spectrogram(mel_spectrogram)
        
        return mel_spectrogram
    
    def _preprocess_spectrogram(self, mel_spectrogram: np.ndarray, **kwargs) -> np.ndarray:
        """
        Preprocess spectrogram before vocoder synthesis.
        
        Args:
            mel_spectrogram: Input mel spectrogram
            **kwargs: Preprocessing parameters
            
        Returns:
            Processed spectrogram
        """
        # Apply smoothing if requested
        if kwargs.get('smooth', False):
            from scipy.ndimage import gaussian_filter
            mel_spectrogram = gaussian_filter(mel_spectrogram, sigma=0.5)
        
        # Apply frequency masking for data augmentation
        if kwargs.get('freq_mask', False):
            freq_mask_param = kwargs.get('freq_mask_param', 10)
            mel_spectrogram = self._apply_frequency_masking(mel_spectrogram, freq_mask_param)
        
        # Apply time masking for data augmentation
        if kwargs.get('time_mask', False):
            time_mask_param = kwargs.get('time_mask_param', 10)
            mel_spectrogram = self._apply_time_masking(mel_spectrogram, time_mask_param)
        
        return mel_spectrogram
    
    def _postprocess_audio(self, audio: np.ndarray, **kwargs) -> np.ndarray:
        """
        Post-process audio after vocoder synthesis.
        
        Args:
            audio: Raw audio from vocoder
            **kwargs: Post-processing parameters
            
        Returns:
            Processed audio
        """
        # Normalize audio
        if kwargs.get('normalize_audio', True):
            audio = librosa.util.normalize(audio)
        
        # Apply fade in/out to prevent clicks
        if kwargs.get('fade_duration', 0) > 0:
            fade_samples = int(kwargs.get('fade_duration', 0.01) * self.sample_rate)
            audio = self._apply_fade(audio, fade_samples)
        
        # Apply high-pass filter to remove DC offset
        if kwargs.get('high_pass_filter', True):
            from scipy.signal import butter, filtfilt
            nyquist = self.sample_rate // 2
            cutoff = kwargs.get('high_pass_cutoff', 80)  # Hz
            b, a = butter(4, cutoff / nyquist, btype='high')
            audio = filtfilt(b, a, audio)
        
        return audio
    
    def _normalize_spectrogram(self, mel_spectrogram: np.ndarray) -> np.ndarray:
        """
        Normalize mel spectrogram.
        
        Args:
            mel_spectrogram: Input spectrogram
            
        Returns:
            Normalized spectrogram
        """
        # Min-max normalization
        mel_min = mel_spectrogram.min()
        mel_max = mel_spectrogram.max()
        if mel_max > mel_min:
            mel_spectrogram = (mel_spectrogram - mel_min) / (mel_max - mel_min)
        
        return mel_spectrogram
    
    def _apply_frequency_masking(self, mel_spectrogram: np.ndarray, mask_param: int) -> np.ndarray:
        """
        Apply frequency masking for data augmentation.
        
        Args:
            mel_spectrogram: Input spectrogram
            mask_param: Masking parameter
            
        Returns:
            Masked spectrogram
        """
        freq_size = mel_spectrogram.shape[0]
        freq_mask_size = min(mask_param, freq_size)
        freq_start = np.random.randint(0, freq_size - freq_mask_size + 1)
        mel_spectrogram[freq_start:freq_start + freq_mask_size, :] = 0
        return mel_spectrogram
    
    def _apply_time_masking(self, mel_spectrogram: np.ndarray, mask_param: int) -> np.ndarray:
        """
        Apply time masking for data augmentation.
        
        Args:
            mel_spectrogram: Input spectrogram
            mask_param: Masking parameter
            
        Returns:
            Masked spectrogram
        """
        time_size = mel_spectrogram.shape[1]
        time_mask_size = min(mask_param, time_size)
        time_start = np.random.randint(0, time_size - time_mask_size + 1)
        mel_spectrogram[:, time_start:time_start + time_mask_size] = 0
        return mel_spectrogram
    
    def _apply_fade(self, audio: np.ndarray, fade_samples: int) -> np.ndarray:
        """
        Apply fade in/out to audio.
        
        Args:
            audio: Input audio
            fade_samples: Number of samples for fade
            
        Returns:
            Audio with fade applied
        """
        if fade_samples > 0:
            # Fade in
            fade_in = np.linspace(0, 1, min(fade_samples, len(audio)))
            audio[:len(fade_in)] *= fade_in
            
            # Fade out
            fade_out = np.linspace(1, 0, min(fade_samples, len(audio)))
            audio[-len(fade_out):] *= fade_out
        
        return audio
    
    def synthesize_speech(self, text: str, **kwargs) -> np.ndarray:
        """
        Complete text-to-speech synthesis pipeline with enhanced control.
        
        Args:
            text: Input text to synthesize
            **kwargs: Additional parameters for synthesis
            
        Returns:
            audio: Synthesized audio waveform
        """
        try:
            # Step 1: Text to spectrogram with enhanced processing
            mel_spectrogram = self.text_to_spectrogram(text, **kwargs)
            
            # Step 2: Spectrogram to audio with enhanced processing
            audio = self.spectrogram_to_audio(mel_spectrogram, **kwargs)
            
            return audio
            
        except Exception as e:
            logger.error(f"Speech synthesis failed: {e}")
            raise HTTPException(
                status_code=500,
                detail=f"Speech synthesis failed: {str(e)}"
            )
    
    def get_audio_parameters(self) -> dict:
        """
        Get audio processing parameters.
        
        Returns:
            Dictionary containing audio parameters
        """
        return {
            "sample_rate": self.sample_rate,
            "hop_length": self.hop_length,
            "win_length": self.win_length,
            "n_fft": self.n_fft,
            "n_mels": self.n_mels
        }
    
    def get_synthesis_options(self) -> Dict[str, Any]:
        """
        Get available synthesis options and their default values.
        
        Returns:
            Dictionary of synthesis options
        """
        return {
            "pre_emphasis": 0.97,
            "n_mels": 80,
            "n_fft": 1024,
            "hop_length": 256,
            "win_length": 1024,
            "fmin": 0,
            "fmax": 11025,
            "normalize": True,
            "smooth": False,
            "freq_mask": False,
            "freq_mask_param": 10,
            "time_mask": False,
            "time_mask_param": 10,
            "normalize_audio": True,
            "fade_duration": 0.01,
            "high_pass_filter": True,
            "high_pass_cutoff": 80
        }


# Global instance
_tts_service = None


def get_spectrogram_tts_service() -> SpectrogramTTSService:
    """
    Get the global TTS service instance.
    
    Returns:
        SpectrogramTTSService instance
    """
    global _tts_service
    if _tts_service is None:
        _tts_service = SpectrogramTTSService()
    return _tts_service