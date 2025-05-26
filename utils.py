"""
Utility functions for video and conversation processing.
"""

import tempfile
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import PIL
import requests
from decord import VideoReader
from transformers import AutoProcessor
from transformers.image_utils import load_image


def load_video(video_path) -> List[PIL.Image.Image]:
    frames: List[PIL.Image.Image] = []

    # Download video if it's a URL
    if video_path.startswith(("http://", "https://")):
        response = requests.get(video_path, stream=True)
        response.raise_for_status()

        # Create a temporary file to store the video
        with tempfile.NamedTemporaryFile(suffix=".mp4", delete=False) as temp_file:
            for chunk in response.iter_content(chunk_size=8192):
                temp_file.write(chunk)
            temp_path = temp_file.name

        try:
            vr = VideoReader(temp_path)
            for frame in vr:
                frames.append(PIL.Image.fromarray(frame.asnumpy()))
        finally:
            # Clean up the temporary file
            Path(temp_path).unlink()
    else:
        # If it's a local file path, read directly
        vr = VideoReader(video_path)
        for frame in vr:
            frames.append(PIL.Image.fromarray(frame.asnumpy()))

    return frames


def process_conversation(
    conversation: List[Dict],
    processor: AutoProcessor,
) -> Tuple[Optional[List[PIL.Image.Image]], str, Optional[List[List[PIL.Image.Image]]]]:
    """
    Process a conversation to extract images, text, and videos.

    Args:
        conversation: List of message dictionaries containing the conversation

    Returns:
        Tuple containing:
        - List of PIL Images (or None if no images)
        - Formatted text string with image tokens
        - List of video frames (or None if no videos)
    """
    images = None
    text = ""
    videos = None

    def name_me_better(message):
        if (
            type(message["content"]) == list
            and message["content"][0]["type"] == "image"
        ):
            return f"{message['role'].capitalize()}:"

        else:
            return f"{message['role'].capitalize()}: "

    # Process all messages in a single loop
    for message in conversation:
        text += f"{processor.bos_token}{name_me_better(message)}"

        if type(message["content"]) == list:
            for content in message["content"]:
                if content["type"] == "text":
                    text += content["text"]

                elif content["type"] == "image":
                    image_url = content["url"]
                    image = load_image(image_url)
                    images = [image] if images is None else images + [image]
                    text += processor.image_token

                elif content["type"] == "video":
                    video_path = content["path"]
                    video = load_video(video_path)
                    videos = [video] if videos is None else videos + [video]
                    # Add image token for each frame in the video
                    text += processor.image_token * len(video)

        elif type(message["content"]) == str:
            text += message["content"]

    text += f"{processor.eos_token}\nAssistant:"

    return images, text, videos
