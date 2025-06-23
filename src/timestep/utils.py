"""
Utility functions for video and conversation processing.
"""

import json
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import PIL
import requests
import yt_dlp
from decord import VideoReader
from transformers import AutoProcessor
from transformers.image_utils import load_image


def load_video(video_path) -> List[PIL.Image.Image]:
    frames: List[PIL.Image.Image] = []

    # Create cache directory if it doesn't exist
    cache_dir = Path("cache")
    cache_dir.mkdir(exist_ok=True)

    # Download video if it's a URL
    if video_path.startswith(("http://", "https://")):
        if "youtube.com" in video_path or "youtu.be" in video_path:
            # Handle YouTube URLs
            try:
                # Extract video ID for caching
                with yt_dlp.YoutubeDL() as ydl:
                    info = ydl.extract_info(video_path, download=False)
                    video_id = info["id"]

                # Check if video exists in cache
                cached_path = cache_dir / f"{video_id}.mp4"
                if cached_path.exists():
                    print(f"Using cached video: {cached_path}")
                    vr = VideoReader(str(cached_path))
                    for frame in vr:
                        # Convert frame to PIL Image and resize
                        pil_frame = PIL.Image.fromarray(frame.asnumpy())
                        resized_frame = resize_image(pil_frame)
                        frames.append(resized_frame)
                    print(f"Successfully read {len(frames)} frames from cached video")
                    # Sample frames to match model requirements
                    frames = sample_video_frames(frames)
                    print(f"Sampled down to {len(frames)} frames")
                    return frames

                # If not in cache, download it
                print(f"Downloading video from: {video_path}")
                ydl_opts = {
                    "format": "18",  # Use format 18 (360p MP4) which is consistently available
                    "outtmpl": str(cached_path),
                    "quiet": False,
                    "no_warnings": False,
                    "nocheckcertificate": True,
                    "geo_bypass": True,
                }

                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([video_path])

                    # Verify file after download
                    if cached_path.exists():
                        size = cached_path.stat().st_size
                        if size == 0:
                            raise RuntimeError("Downloaded file is empty")

                        print(f"Attempting to read video file of size: {size} bytes")
                        vr = VideoReader(str(cached_path))
                        for frame in vr:
                            # Convert frame to PIL Image and resize
                            pil_frame = PIL.Image.fromarray(frame.asnumpy())
                            resized_frame = resize_image(pil_frame)
                            frames.append(resized_frame)
                        print(f"Successfully read {len(frames)} frames from video")
                        # Sample frames to match model requirements
                        frames = sample_video_frames(frames)
                        print(f"Sampled down to {len(frames)} frames")

            except Exception as e:
                raise RuntimeError(f"Failed to download YouTube video: {str(e)}")

        else:
            # Handle other URLs
            # Generate a hash of the URL for the cache filename
            import hashlib

            url_hash = hashlib.md5(video_path.encode()).hexdigest()
            cached_path = cache_dir / f"{url_hash}.mp4"

            if cached_path.exists():
                print(f"Using cached video: {cached_path}")
                vr = VideoReader(str(cached_path))
                for frame in vr:
                    # Convert frame to PIL Image and resize
                    pil_frame = PIL.Image.fromarray(frame.asnumpy())
                    resized_frame = resize_image(pil_frame)
                    frames.append(resized_frame)
                print(f"Successfully read {len(frames)} frames from cached video")
                # Sample frames to match model requirements
                frames = sample_video_frames(frames)
                print(f"Sampled down to {len(frames)} frames")
                return frames

            # If not in cache, download it
            response = requests.get(video_path, stream=True)
            response.raise_for_status()

            # Download directly to cache file
            with open(cached_path, "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)

            try:
                # Verify the file exists and has content
                if not cached_path.exists():
                    raise RuntimeError("Downloaded video file does not exist")

                size = cached_path.stat().st_size
                if size == 0:
                    raise RuntimeError(
                        f"Downloaded video file is empty (size: {size} bytes)"
                    )

                print(f"Attempting to read video file of size: {size} bytes")
                vr = VideoReader(str(cached_path))
                for frame in vr:
                    # Convert frame to PIL Image and resize
                    pil_frame = PIL.Image.fromarray(frame.asnumpy())
                    resized_frame = resize_image(pil_frame)
                    frames.append(resized_frame)
                print(f"Successfully read {len(frames)} frames from video")
                # Sample frames to match model requirements
                frames = sample_video_frames(frames)
                print(f"Sampled down to {len(frames)} frames")

            except Exception as e:
                # Clean up failed download
                try:
                    cached_path.unlink()
                except Exception:
                    pass
                raise RuntimeError(f"Error processing video file: {str(e)}")
    else:
        # If it's a local file path, read directly
        try:
            vr = VideoReader(video_path)
            for frame in vr:
                # Convert frame to PIL Image and resize
                pil_frame = PIL.Image.fromarray(frame.asnumpy())
                resized_frame = resize_image(pil_frame)
                frames.append(resized_frame)
            # Sample frames to match model requirements
            frames = sample_video_frames(frames)
            print(f"Sampled down to {len(frames)} frames")
        except Exception as e:
            raise RuntimeError(f"Error reading local video file: {str(e)}")

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
    text = processor.bos_token
    videos = None

    def format_message_role_prefix(message, message_idx):
        message_role_prefix = "" if message_idx == 0 else "\n"
        message_role_prefix += f"{message['role'].capitalize()}:"

        if (
            not isinstance(message["content"], list)
            or message["content"][0]["type"] == "text"
        ):
            message_role_prefix += " "

        return message_role_prefix

    # Process all messages in a single loop
    for message_idx, message in enumerate(conversation):
        try:
            message["content"] = json.loads(message["content"])

        except (json.decoder.JSONDecodeError, TypeError):
            pass

        text += format_message_role_prefix(message, message_idx)

        if type(message["content"]) == list:
            for content in message["content"]:
                if content["type"] == "text":
                    text += content["text"]

                elif content["type"] == "image":
                    image_url = content["url"]
                    image = load_image(image_url)
                    # Resize image to target dimensions
                    image = resize_image(image)
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

    text += f"{processor.eos_token}\nAssistant:"  # TODO: abstract this

    return images, text, videos


def resize_image(
    image: PIL.Image.Image, target_size: Tuple[int, int] = (224, 224)
) -> PIL.Image.Image:
    """
    Resize an image to fit within target dimensions while preserving aspect ratio.
    The image will be centered on a black background if aspect ratio doesn't match.

    Args:
        image: PIL Image to resize
        target_size: Target dimensions (width, height)

    Returns:
        Resized PIL Image
    """
    # Create a new black image of target size
    resized = PIL.Image.new("RGB", target_size, (0, 0, 0))

    # Calculate scaling factor to fit within target dimensions
    width_ratio = target_size[0] / image.width
    height_ratio = target_size[1] / image.height
    scale = min(width_ratio, height_ratio)

    # Calculate new dimensions
    new_width = int(image.width * scale)
    new_height = int(image.height * scale)

    # Resize image
    resized_image = image.resize((new_width, new_height), PIL.Image.Resampling.LANCZOS)

    # Calculate position to paste resized image (centered)
    paste_x = (target_size[0] - new_width) // 2
    paste_y = (target_size[1] - new_height) // 2

    # Paste resized image onto black background
    resized.paste(resized_image, (paste_x, paste_y))

    return resized


def sample_video_frames(
    frames: List[PIL.Image.Image], max_frames: int = 64
) -> List[PIL.Image.Image]:
    """
    Sample frames from a video to get a maximum number of frames.
    Uses uniform sampling to select frames.

    Args:
        frames: List of video frames
        max_frames: Maximum number of frames to return

    Returns:
        List of sampled frames
    """
    if len(frames) <= max_frames:
        return frames

    # Calculate sampling interval
    interval = len(frames) / max_frames

    # Sample frames uniformly
    sampled_frames = []
    for i in range(max_frames):
        idx = int(i * interval)
        sampled_frames.append(frames[idx])

    return sampled_frames
