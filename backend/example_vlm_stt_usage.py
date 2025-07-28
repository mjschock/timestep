#!/usr/bin/env python3
"""
Example script demonstrating VLM-based STT as a replacement for traditional STT.
This shows how to use the integrated approach where VLM models are used
through the existing STT API endpoints.
"""

import asyncio
import tempfile
from pathlib import Path

import numpy as np
import soundfile as sf
from fastapi import UploadFile

from src.backend.services.audio_service import AudioService


async def create_test_audio_with_speech():
    """Create a test audio file that simulates speech."""
    # Generate a more complex audio that could represent speech
    sample_rate = 22050
    duration = 5.0  # 5 seconds
    
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    
    # Create a complex signal that could represent speech
    # This is a simplified simulation - real speech would be much more complex
    base_freq = 200  # Base frequency for "speech"
    
    # Simulate different speech components
    speech_signal = (
        0.3 * np.sin(2 * np.pi * base_freq * t) +  # Fundamental frequency
        0.2 * np.sin(2 * np.pi * base_freq * 2 * t) +  # Second harmonic
        0.1 * np.sin(2 * np.pi * base_freq * 3 * t) +  # Third harmonic
        0.05 * np.random.randn(len(t))  # Add some noise
    )
    
    # Add some variation over time to simulate speech patterns
    envelope = 0.5 + 0.3 * np.sin(2 * np.pi * 0.5 * t)  # Amplitude modulation
    speech_signal *= envelope
    
    # Create a temporary file
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
        sf.write(tmp.name, speech_signal, sample_rate)
        return tmp.name


class MockUploadFile:
    """Mock UploadFile for testing."""
    def __init__(self, file_path):
        self.file_path = file_path
        self._content = None
    
    async def read(self):
        if self._content is None:
            with open(self.file_path, 'rb') as f:
                self._content = f.read()
        return self._content
    
    async def seek(self, position):
        pass


async def demonstrate_integrated_vlm_stt():
    """Demonstrate the integrated VLM-based STT approach."""
    print("🎤 Integrated VLM-based STT Demonstration")
    print("=" * 60)
    
    # Create test audio
    audio_file_path = await create_test_audio_with_speech()
    print(f"✅ Created test audio file: {audio_file_path}")
    
    try:
        # Initialize the audio service
        audio_service = AudioService()
        
        # Create mock upload file
        mock_audio_file = MockUploadFile(audio_file_path)
        
        print("\n🔄 Testing different STT approaches...")
        
        # Test traditional STT
        print("\n📝 Traditional STT (Whisper):")
        try:
            traditional_result = await audio_service.create_transcription_with_upload(
                mock_audio_file,
                model="openai/whisper-tiny",
                response_format="text"
            )
            print(f"   Result: {traditional_result}")
        except Exception as e:
            print(f"   Error: {e}")
        
        # Reset file pointer
        await mock_audio_file.seek(0)
        
        # Test VLM-based STT with spectrogram
        print("\n🖼️  VLM-based STT (Spectrogram):")
        try:
            vlm_spectrogram_result = await audio_service.create_transcription_with_upload(
                mock_audio_file,
                model="vlm:spectrogram:HuggingFaceTB/SmolVLM2-256M-Video-Instruct",
                response_format="text"
            )
            print(f"   Result: {vlm_spectrogram_result}")
        except Exception as e:
            print(f"   Error: {e}")
        
        # Reset file pointer
        await mock_audio_file.seek(0)
        
        # Test VLM-based STT with waveform
        print("\n📊 VLM-based STT (Waveform):")
        try:
            vlm_waveform_result = await audio_service.create_transcription_with_upload(
                mock_audio_file,
                model="vlm:waveform:HuggingFaceTB/SmolVLM2-256M-Video-Instruct",
                response_format="text"
            )
            print(f"   Result: {vlm_waveform_result}")
        except Exception as e:
            print(f"   Error: {e}")
        
        # Reset file pointer
        await mock_audio_file.seek(0)
        
        # Test VLM-based STT with MFCC
        print("\n🎵 VLM-based STT (MFCC):")
        try:
            vlm_mfcc_result = await audio_service.create_transcription_with_upload(
                mock_audio_file,
                model="vlm:mfcc:HuggingFaceTB/SmolVLM2-256M-Video-Instruct",
                response_format="text"
            )
            print(f"   Result: {vlm_mfcc_result}")
        except Exception as e:
            print(f"   Error: {e}")
        
        # Reset file pointer
        await mock_audio_file.seek(0)
        
        # Test translation with VLM
        print("\n🌐 VLM-based Translation:")
        try:
            vlm_translation_result = await audio_service.create_translation_with_upload(
                mock_audio_file,
                model="vlm:spectrogram:HuggingFaceTB/SmolVLM2-256M-Video-Instruct",
                response_format="text"
            )
            print(f"   Result: {vlm_translation_result}")
        except Exception as e:
            print(f"   Error: {e}")
    
    finally:
        # Clean up
        Path(audio_file_path).unlink(missing_ok=True)
        print(f"\n🧹 Cleaned up test file: {audio_file_path}")


def explain_integration():
    """Explain how the VLM-based STT is integrated."""
    print("\n" + "=" * 60)
    print("🔗 INTEGRATED VLM-BASED STT APPROACH")
    print("=" * 60)
    
    print("""
This implementation integrates VLM-based STT as a drop-in replacement for traditional STT models.

🎯 HOW IT WORKS:

1. **Model Detection**: The audio service checks if the model name starts with "vlm:"
2. **Parameter Parsing**: Extracts image type and VLM model from the model string
3. **Processing**: Uses the speech-to-image service for VLM-based transcription
4. **Seamless Integration**: Same API endpoints, same response format

📋 MODEL FORMAT:
   vlm:image_type:vlm_model_name

Examples:
   • vlm:spectrogram:HuggingFaceTB/SmolVLM2-256M-Video-Instruct
   • vlm:waveform:HuggingFaceTB/SmolVLM2-256M-Video-Instruct  
   • vlm:mfcc:HuggingFaceTB/SmolVLM2-256M-Video-Instruct

🔄 API USAGE:
   Same endpoints as traditional STT:
   • POST /audio/transcriptions
   • POST /audio/translations

   Just change the model parameter to use VLM-based approach.

✅ BENEFITS:
   • Drop-in replacement for existing STT
   • No changes needed to existing API clients
   • Can easily switch between traditional and VLM approaches
   • Supports multiple visualization types
   • Same error handling and response formats

🔧 IMPLEMENTATION DETAILS:
   • Audio service detects VLM models by "vlm:" prefix
   • Speech-to-image service handles the actual processing
   • Models service includes VLM models in supported list
   • All existing API endpoints work unchanged
""")


if __name__ == "__main__":
    print("🚀 Starting Integrated VLM-based STT Demo")
    
    # Explain the integration
    explain_integration()
    
    # Run the demonstration
    asyncio.run(demonstrate_integrated_vlm_stt())
    
    print("\n✅ Demo completed!")