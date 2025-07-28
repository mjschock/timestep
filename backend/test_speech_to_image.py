#!/usr/bin/env python3
"""
Test script for speech-to-image transcription using VLM.
This demonstrates converting speech to spectrogram images and using VLM for transcription.
"""

import asyncio
import io
import tempfile
from pathlib import Path

import numpy as np
import soundfile as sf
from PIL import Image

from src.backend.services.speech_to_image_service import get_speech_to_image_service


async def create_test_audio():
    """Create a simple test audio file with spoken content."""
    # Generate a simple sine wave as a placeholder
    # In practice, you'd use real speech audio
    sample_rate = 22050
    duration = 3.0  # 3 seconds
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    
    # Create a simple tone (this is just for demonstration)
    # Real implementation would use actual speech
    frequency = 440  # A4 note
    audio = 0.3 * np.sin(2 * np.pi * frequency * t)
    
    # Add some variation to make it more interesting
    audio += 0.1 * np.sin(2 * np.pi * 880 * t)  # Higher frequency
    
    # Create a temporary file
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
        sf.write(tmp.name, audio, sample_rate)
        return tmp.name


async def test_speech_to_image_transcription():
    """Test the speech-to-image transcription approach."""
    print("🎤 Testing Speech-to-Image Transcription with VLM")
    print("=" * 60)
    
    # Create test audio
    audio_file_path = await create_test_audio()
    print(f"✅ Created test audio file: {audio_file_path}")
    
    try:
        # Initialize the service
        service = get_speech_to_image_service()
        
        # Create a mock UploadFile from the audio file
        class MockUploadFile:
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
        
        mock_audio_file = MockUploadFile(audio_file_path)
        
        print("\n🔄 Testing different audio visualizations...")
        
        # Test different image types
        image_types = ["spectrogram", "waveform", "mfcc"]
        
        for image_type in image_types:
            print(f"\n📊 Testing {image_type} visualization...")
            
            # Reset file pointer
            await mock_audio_file.seek(0)
            
            try:
                # Test the transcription
                result = await service.transcribe_with_vlm(
                    mock_audio_file,
                    image_type=image_type,
                    prompt=f"Please transcribe the speech shown in this audio {image_type} image. Extract all spoken words and convert them to text."
                )
                
                print(f"✅ {image_type.capitalize()} transcription result:")
                print(f"   {result}")
                
            except Exception as e:
                print(f"❌ {image_type.capitalize()} transcription failed: {e}")
        
        print("\n🔄 Testing comparison with traditional STT...")
        
        # Reset file pointer
        await mock_audio_file.seek(0)
        
        try:
            comparison = await service.compare_transcription_methods(
                mock_audio_file,
                vlm_prompt="Please transcribe the speech shown in this audio spectrogram image. Extract all spoken words and convert them to text."
            )
            
            print("✅ Comparison results:")
            print(f"   Traditional STT: {comparison['traditional_stt']}")
            print(f"   VLM Transcription: {comparison['vlm_transcription']}")
            print(f"   Methods compared: {comparison['methods_compared']}")
            
        except Exception as e:
            print(f"❌ Comparison failed: {e}")
    
    finally:
        # Clean up
        Path(audio_file_path).unlink(missing_ok=True)
        print(f"\n🧹 Cleaned up test file: {audio_file_path}")


def demonstrate_concept():
    """Demonstrate the concept and potential benefits."""
    print("\n" + "=" * 60)
    print("🎯 SPEECH-TO-IMAGE TRANSCRIPTION CONCEPT")
    print("=" * 60)
    
    print("""
This approach converts speech to image representations and uses Vision Language Models (VLM) 
for transcription instead of traditional Speech-to-Text models.

🔍 HOW IT WORKS:
1. Audio file → Spectrogram/Waveform/MFCC image
2. Image → VLM processing with transcription prompt
3. VLM output → Transcribed text

🎯 POTENTIAL BENEFITS:
• Visual context: VLM can "see" audio patterns, noise, and characteristics
• Robustness: May handle different accents, background noise, or audio quality better
• Interpretability: Visual representation makes the process more transparent
• Flexibility: Can use different image types (spectrogram, waveform, MFCC)
• Leverage: Uses powerful vision-language models for audio processing

🔬 DIFFERENT AUDIO VISUALIZATIONS:
• Spectrogram: Shows frequency content over time (most common)
• Waveform: Shows amplitude over time (simpler)
• MFCC: Shows mel-frequency cepstral coefficients (speech-specific features)

⚠️  LIMITATIONS:
• May be slower than direct STT
• Requires more computational resources
• VLM models may not be optimized for audio transcription
• Quality depends on the VLM model's understanding of audio visualizations

🚀 USE CASES:
• Research and experimentation
• Audio quality analysis
• Educational demonstrations
• Alternative transcription methods
""")


if __name__ == "__main__":
    print("🚀 Starting Speech-to-Image Transcription Test")
    
    # Demonstrate the concept
    demonstrate_concept()
    
    # Run the test
    asyncio.run(test_speech_to_image_transcription())
    
    print("\n✅ Test completed!")