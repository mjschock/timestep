# VLM-Based Speech-to-Text (Primary STT Method)

This project has replaced the traditional STT pathway with an innovative VLM-based approach that converts audio to image representations and uses Vision Language Models (VLM) for transcription.

## 🎯 Concept Overview

Instead of directly processing audio with STT models like Whisper, this approach:

1. **Converts audio to visual representations** (spectrograms, waveforms, MFCC)
2. **Uses VLM models** to "read" the audio images
3. **Extracts text** from the VLM's understanding of the audio visualization

## 🔬 How It Works

### Audio Visualization Types

#### 1. Spectrogram
- **What**: Shows frequency content over time
- **Best for**: Most speech transcription tasks
- **Visual**: Color-coded frequency intensity over time

#### 2. Waveform
- **What**: Shows amplitude over time
- **Best for**: Simple audio analysis
- **Visual**: Wave-like pattern showing audio intensity

#### 3. MFCC (Mel-frequency Cepstral Coefficients)
- **What**: Speech-specific frequency features
- **Best for**: Speech recognition and analysis
- **Visual**: Compact representation of speech characteristics

### Processing Pipeline

```
Audio File → Audio Visualization → VLM Processing → Transcribed Text
     ↓              ↓                    ↓              ↓
   Input        Spectrogram         VLM Model      Output Text
```

## 🚀 API Endpoints

### Primary VLM-Based Transcription
The VLM-based approach is now the primary STT method.

#### Standard Transcription Endpoint
```http
POST /audio/transcriptions
```

**Default Parameters:**
- `file`: Audio file (multipart/form-data)
- `model`: `vlm:spectrogram:HuggingFaceTB/SmolVLM2-256M-Video-Instruct` (default)
- `response_format`: "text" or "json"
- `language`: Language code
- `prompt`: Custom prompt for VLM
- `temperature`: Temperature for generation

#### Available VLM Models:
- `vlm:spectrogram:HuggingFaceTB/SmolVLM2-256M-Video-Instruct` (default)
- `vlm:waveform:HuggingFaceTB/SmolVLM2-256M-Video-Instruct`
- `vlm:mfcc:HuggingFaceTB/SmolVLM2-256M-Video-Instruct`

#### Translation Endpoint
```http
POST /audio/translations
```

**Default Parameters:**
- `file`: Audio file (multipart/form-data)
- `model`: `vlm:spectrogram:HuggingFaceTB/SmolVLM2-256M-Video-Instruct` (default)
- `response_format`: "text" or "json"
- `prompt`: Custom prompt for VLM translation
- `temperature`: Temperature for generation

### Legacy Traditional STT (Fallback)
To use traditional STT models, explicitly specify the model:
```http
POST /audio/transcriptions?model=openai/whisper-tiny
POST /audio/translations?model=openai/whisper-tiny
```

## 🎯 Potential Benefits

### 1. Visual Context Understanding
- VLM can "see" audio patterns, noise, and characteristics
- May handle different accents or speech patterns better
- Visual representation provides additional context

### 2. Robustness
- Could be more robust to background noise
- May handle audio quality variations better
- Visual processing might be more interpretable

### 3. Flexibility
- Multiple visualization types (spectrogram, waveform, MFCC)
- Different VLM models can be used
- Customizable prompts for different use cases

### 4. Research Value
- Novel approach to audio processing
- Educational for understanding audio-visual relationships
- Potential for new research directions

## ⚠️ Limitations

### 1. Performance
- Slower than direct STT processing
- Requires more computational resources
- Additional processing steps (audio → image → VLM)

### 2. Model Limitations
- VLM models not specifically trained for audio transcription
- Quality depends on VLM's understanding of audio visualizations
- May not handle all audio types equally well

### 3. Accuracy
- Experimental approach with unproven accuracy
- May not match traditional STT performance
- Depends heavily on VLM model capabilities

## 🛠️ Technical Implementation

### Dependencies Added
```toml
librosa>=0.10.1    # Audio processing
matplotlib>=3.7.0   # Image generation
```

### Key Components

#### Integrated AudioService
- **Primary Method**: VLM-based transcription is now the default
- **Audio Visualization**: Built-in spectrogram, waveform, and MFCC conversion
- **VLM Processing**: Direct integration with vision-language models
- **Legacy Support**: Traditional STT available as fallback

#### Audio Visualization Methods
- `_audio_to_spectrogram_image()`: Converts audio to spectrogram
- `_audio_to_waveform_image()`: Converts audio to waveform
- `_audio_to_mfcc_image()`: Converts audio to MFCC
- `_transcribe_with_vlm()`: Main VLM transcription method

#### Models Service Integration
- VLM models are now the primary supported STT models
- Default pipeline uses VLM-based approach
- Legacy STT models still supported for fallback
- Seamless model switching based on model string format

#### API Integration
- Same endpoints, enhanced functionality
- Default models changed to VLM-based
- Backward compatibility maintained
- Async processing for better performance

## 🧪 Testing

### Run the Primary VLM Demo
```bash
cd backend
python example_integrated_vlm_stt.py
```

### Test Different Approaches
The demo script demonstrates:
- Default VLM-based STT (spectrogram)
- VLM-based STT with waveform
- VLM-based STT with MFCC
- VLM-based translation
- Legacy traditional STT (fallback)

## 🔬 Use Cases

### 1. Research and Experimentation
- Novel approach to audio processing
- Understanding audio-visual relationships
- Testing VLM capabilities on audio data

### 2. Educational Demonstrations
- Visual representation of audio
- Understanding how audio can be "seen"
- Teaching audio processing concepts

### 3. Audio Quality Analysis
- Visual inspection of audio characteristics
- Identifying audio patterns and features
- Quality assessment through visualization

### 4. Alternative Transcription Methods
- When traditional STT fails
- For specific audio types or conditions
- As a backup or verification method

## 🚀 Future Enhancements

### 1. Model Optimization
- Train VLM models specifically for audio transcription
- Fine-tune on audio visualization datasets
- Optimize prompts for better transcription accuracy

### 2. Advanced Visualizations
- Multi-scale spectrograms
- Advanced audio feature representations
- Custom visualization techniques

### 3. Hybrid Approaches
- Combine traditional STT with VLM results
- Ensemble methods for better accuracy
- Adaptive method selection based on audio characteristics

### 4. Real-time Processing
- Optimize for real-time audio transcription
- Streaming audio visualization
- Low-latency VLM processing

## 📊 Performance Considerations

### Memory Usage
- Audio visualization requires additional memory
- VLM models are typically larger than STT models
- Image processing adds computational overhead

### Processing Time
- Audio → Image conversion: ~100-500ms
- VLM processing: ~1-5 seconds (depending on model)
- Total time: 2-10x slower than traditional STT

### Accuracy Trade-offs
- Experimental approach with unproven accuracy
- May work better for certain audio types
- Requires careful evaluation and comparison

## 🔍 Monitoring and Debugging

### Logging
- Audio processing steps are logged
- VLM processing details are captured
- Error handling with detailed messages

### Visualization Debugging
- Generated images can be saved for inspection
- Different visualization types can be compared
- Quality assessment through visual inspection

## 📚 References

- [Librosa Documentation](https://librosa.org/)
- [Matplotlib Documentation](https://matplotlib.org/)
- [Vision Language Models](https://huggingface.co/models?pipeline_tag=image-to-text)
- [Audio Visualization Techniques](https://en.wikipedia.org/wiki/Spectrogram)

## 🤝 Contributing

This is an experimental approach. Contributions are welcome for:
- Improving visualization techniques
- Optimizing VLM prompts
- Adding new audio visualization types
- Performance optimizations
- Accuracy improvements

## ⚖️ License

This implementation follows the same license as the main project.