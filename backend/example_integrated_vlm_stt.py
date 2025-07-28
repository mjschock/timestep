#!/usr/bin/env python3
"""
Example script demonstrating the integrated VLM-based STT as the primary STT method.
This shows how the VLM approach has replaced the traditional STT pathway.
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
    """Demonstrate the integrated VLM-based STT as the primary approach."""
    print("🎤 Integrated VLM-based STT as Primary Method")
    print("=" * 60)
    
    # Create test audio
    audio_file_path = await create_test_audio_with_speech()
    print(f"✅ Created test audio file: {audio_file_path}")
    
    try:
        # Initialize the audio service
        audio_service = AudioService()
        
        # Create mock upload file
        mock_audio_file = MockUploadFile(audio_file_path)
        
        print("\n🔄 Testing the new integrated VLM-based STT approach...")
        
        # Test default VLM-based transcription (spectrogram)
        print("\n📝 Default VLM-based STT (Spectrogram):")
        try:
            default_result = await audio_service.create_transcription_with_upload(
                mock_audio_file,
                model="vlm:spectrogram:HuggingFaceTB/SmolVLM2-256M-Video-Instruct",
                response_format="text"
            )
            print(f"   Result: {default_result}")
        except Exception as e:
            print(f"   Error: {e}")
        
        # Reset file pointer
        await mock_audio_file.seek(0)
        
        # Test VLM-based STT with waveform
        print("\n📊 VLM-based STT (Waveform):")
        try:
            waveform_result = await audio_service.create_transcription_with_upload(
                mock_audio_file,
                model="vlm:waveform:HuggingFaceTB/SmolVLM2-256M-Video-Instruct",
                response_format="text"
            )
            print(f"   Result: {waveform_result}")
        except Exception as e:
            print(f"   Error: {e}")
        
        # Reset file pointer
        await mock_audio_file.seek(0)
        
        # Test VLM-based STT with MFCC
        print("\n🎵 VLM-based STT (MFCC):")
        try:
            mfcc_result = await audio_service.create_transcription_with_upload(
                mock_audio_file,
                model="vlm:mfcc:HuggingFaceTB/SmolVLM2-256M-Video-Instruct",
                response_format="text"
            )
            print(f"   Result: {mfcc_result}")
        except Exception as e:
            print(f"   Error: {e}")
        
        # Reset file pointer
        await mock_audio_file.seek(0)
        
        # Test VLM-based translation
        print("\n🌐 VLM-based Translation:")
        try:
            translation_result = await audio_service.create_translation_with_upload(
                mock_audio_file,
                model="vlm:spectrogram:HuggingFaceTB/SmolVLM2-256M-Video-Instruct",
                response_format="text"
            )
            print(f"   Result: {translation_result}")
        except Exception as e:
            print(f"   Error: {e}")
        
        # Reset file pointer
        await mock_audio_file.seek(0)
        
        # Test legacy fallback to traditional STT
        print("\n🔙 Legacy Traditional STT (Fallback):")
        try:
            legacy_result = await audio_service.create_transcription_with_upload(
                mock_audio_file,
                model="openai/whisper-tiny",  # Legacy model
                response_format="text"
            )
            print(f"   Result: {legacy_result}")
        except Exception as e:
            print(f"   Error: {e}")
    
    finally:
        # Clean up
        Path(audio_file_path).unlink(missing_ok=True)
        print(f"\n🧹 Cleaned up test file: {audio_file_path}")


def explain_integration():
    """Explain how the VLM-based STT is now the primary approach."""
    print("\n" + "=" * 60)
    print("🔗 VLM-BASED STT AS PRIMARY METHOD")
    print("=" * 60)
    
    print("""
This implementation has replaced the traditional STT pathway with VLM-based transcription as the primary method.

🎯 KEY CHANGES:

1. **Primary Method**: VLM-based transcription is now the default
2. **Integrated Approach**: All VLM functionality is built into AudioService
3. **Legacy Support**: Traditional STT still available as fallback
4. **Same API**: No changes needed to existing API endpoints

📋 DEFAULT BEHAVIOR:

• Default model: vlm:spectrogram:HuggingFaceTB/SmolVLM2-256M-Video-Instruct
• All transcription/translation requests use VLM by default
• Traditional STT available by explicitly specifying legacy models

🔄 API USAGE:

Default (VLM-based):
   POST /audio/transcriptions
   POST /audio/translations

Legacy (Traditional STT):
   POST /audio/transcriptions?model=openai/whisper-tiny
   POST /audio/translations?model=openai/whisper-tiny

✅ BENEFITS:

• VLM-based transcription is now the primary approach
• No separate service needed - everything integrated
• Backward compatibility maintained
• Multiple visualization types available
• Same error handling and response formats

🔧 IMPLEMENTATION DETAILS:

• AudioService now includes VLM functionality directly
• Default models changed to VLM-based
• Legacy STT models still supported
• All API endpoints work unchanged
• Integrated audio-to-image conversion
""")


if __name__ == "__main__":
    print("🚀 Starting Integrated VLM-based STT Demo")
    
    # Explain the integration
    explain_integration()
    
    # Run the demonstration
    asyncio.run(demonstrate_integrated_vlm_stt())
    
    print("\n✅ Demo completed!")