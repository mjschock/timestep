"""
Tests for the spectrogram-based TTS system.
"""

import pytest
import numpy as np
from unittest.mock import Mock, patch

from backend.services.tts_spectrogram_service import SpectrogramTTSService


class TestSpectrogramTTSService:
    """Test cases for the SpectrogramTTSService."""
    
    @pytest.fixture
    def tts_service(self):
        """Create a TTS service instance for testing."""
        return SpectrogramTTSService()
    
    def test_service_initialization(self, tts_service):
        """Test that the service initializes correctly."""
        assert tts_service.device in ["cuda", "cpu"]
        assert tts_service.sample_rate == 22050
        assert tts_service.n_mels == 80
        assert tts_service.n_fft == 1024
        assert tts_service.hop_length == 256
        assert tts_service.win_length == 1024
    
    def test_get_audio_parameters(self, tts_service):
        """Test getting audio parameters."""
        params = tts_service.get_audio_parameters()
        assert "sample_rate" in params
        assert "n_mels" in params
        assert "n_fft" in params
        assert "hop_length" in params
        assert "win_length" in params
    
    def test_get_synthesis_options(self, tts_service):
        """Test getting synthesis options."""
        options = tts_service.get_synthesis_options()
        assert "pre_emphasis" in options
        assert "n_mels" in options
        assert "normalize" in options
        assert "smooth" in options
        assert "normalize_audio" in options
    
    def test_normalize_spectrogram(self, tts_service):
        """Test spectrogram normalization."""
        # Create a test spectrogram
        test_spec = np.random.rand(80, 100)
        
        # Normalize it
        normalized = tts_service._normalize_spectrogram(test_spec)
        
        # Check that values are in [0, 1] range
        assert normalized.min() >= 0
        assert normalized.max() <= 1
    
    def test_apply_frequency_masking(self, tts_service):
        """Test frequency masking."""
        # Create a test spectrogram
        test_spec = np.ones((80, 100))
        
        # Apply frequency masking
        masked = tts_service._apply_frequency_masking(test_spec, 10)
        
        # Check that some values are masked (set to 0)
        assert np.any(masked == 0)
    
    def test_apply_time_masking(self, tts_service):
        """Test time masking."""
        # Create a test spectrogram
        test_spec = np.ones((80, 100))
        
        # Apply time masking
        masked = tts_service._apply_time_masking(test_spec, 10)
        
        # Check that some values are masked (set to 0)
        assert np.any(masked == 0)
    
    def test_apply_fade(self, tts_service):
        """Test fade application."""
        # Create test audio
        test_audio = np.ones(1000)
        
        # Apply fade
        faded = tts_service._apply_fade(test_audio, 100)
        
        # Check that fade is applied
        assert faded[0] < 1.0  # Fade in
        assert faded[-1] < 1.0  # Fade out
    
    @patch('backend.services.tts_spectrogram_service.SpeechT5Processor')
    @patch('backend.services.tts_spectrogram_service.SpeechT5ForTextToSpeech')
    @patch('backend.services.tts_spectrogram_service.SpeechT5HifiGan')
    def test_load_models(self, mock_hifigan, mock_model, mock_processor, tts_service):
        """Test model loading."""
        # Mock the models
        mock_processor.from_pretrained.return_value = Mock()
        mock_model.from_pretrained.return_value = Mock()
        mock_hifigan.from_pretrained.return_value = Mock()
        
        # Load models
        tts_service.load_models("microsoft/speecht5_tts")
        
        # Check that models were loaded
        assert tts_service.processor is not None
        assert tts_service.text_to_spectrogram_model is not None
        assert tts_service.vocoder is not None
    
    def test_audio_to_mel_spectrogram(self, tts_service):
        """Test audio to mel spectrogram conversion."""
        # Create test audio
        test_audio = np.random.randn(22050)  # 1 second of audio
        
        # Convert to spectrogram
        spec = tts_service._audio_to_mel_spectrogram(test_audio)
        
        # Check output shape and properties
        assert spec.shape[0] == tts_service.n_mels
        assert spec.ndim == 2
    
    def test_audio_to_mel_spectrogram_with_pre_emphasis(self, tts_service):
        """Test audio to mel spectrogram with pre-emphasis."""
        # Create test audio
        test_audio = np.random.randn(22050)
        
        # Convert with pre-emphasis
        spec = tts_service._audio_to_mel_spectrogram(test_audio, pre_emphasis=0.97)
        
        # Check output
        assert spec.shape[0] == tts_service.n_mels
        assert spec.ndim == 2
    
    def test_preprocess_spectrogram(self, tts_service):
        """Test spectrogram preprocessing."""
        # Create test spectrogram
        test_spec = np.random.rand(80, 100)
        
        # Preprocess without any options
        processed = tts_service._preprocess_spectrogram(test_spec)
        
        # Should return the same spectrogram
        np.testing.assert_array_equal(processed, test_spec)
        
        # Preprocess with smoothing
        processed = tts_service._preprocess_spectrogram(test_spec, smooth=True)
        
        # Should be different due to smoothing
        assert not np.array_equal(processed, test_spec)
    
    def test_postprocess_audio(self, tts_service):
        """Test audio post-processing."""
        # Create test audio
        test_audio = np.random.randn(22050)
        
        # Post-process without options
        processed = tts_service._postprocess_audio(test_audio)
        
        # Should be normalized
        assert np.abs(processed).max() <= 1.0
        
        # Post-process with fade
        processed = tts_service._postprocess_audio(test_audio, fade_duration=0.01)
        
        # Should have fade applied
        assert processed[0] < processed[len(processed)//2]
        assert processed[-1] < processed[len(processed)//2]


class TestSpectrogramTTSIntegration:
    """Integration tests for the spectrogram TTS system."""
    
    @pytest.mark.slow
    def test_end_to_end_synthesis(self):
        """Test end-to-end speech synthesis (requires models)."""
        # This test would require actual models to be loaded
        # It's marked as slow and would typically be run separately
        pass
    
    def test_synthesis_parameters(self):
        """Test that synthesis parameters are properly handled."""
        service = SpectrogramTTSService()
        
        # Test with different parameter combinations
        options = service.get_synthesis_options()
        
        # Check that all options have reasonable default values
        assert options["pre_emphasis"] > 0
        assert options["n_mels"] > 0
        assert options["n_fft"] > 0
        assert options["hop_length"] > 0
        assert options["win_length"] > 0
        assert options["fade_duration"] >= 0
        assert options["high_pass_cutoff"] > 0