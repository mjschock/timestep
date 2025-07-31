import os
import tempfile

import pytest
from PIL import Image

IMAGE_MODEL = (
    "stable-diffusion-v1-5/stable-diffusion-v1-5"  # Use Stable Diffusion model
)


@pytest.mark.asyncio
@pytest.mark.xfail(reason="Image models not configured in backend")
async def test_image_generation(async_client):
    response = await async_client.images.generate(
        model=IMAGE_MODEL,
        prompt="A simple test image of a blue square",
        size="256x256",
        n=1,
    )
    assert hasattr(response, "data")
    assert len(response.data) == 1
    image = response.data[0]
    assert hasattr(image, "url") or hasattr(image, "b64_json")


@pytest.mark.asyncio
@pytest.mark.xfail(reason="Image models not configured in backend")
async def test_image_variation(async_client, sample_image):
    with open(sample_image, "rb") as image_file:
        response = await async_client.images.create_variation(
            image=image_file, n=1, size="256x256"
        )
    assert hasattr(response, "data")
    assert len(response.data) == 1


@pytest.mark.asyncio
@pytest.mark.xfail(reason="Image models not configured in backend")
async def test_image_edit(async_client, sample_image):
    mask = Image.new("RGBA", (256, 256), (0, 0, 0, 0))
    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as mask_file:
        mask.save(mask_file.name, format="PNG")
        try:
            with (
                open(sample_image, "rb") as image_file,
                open(mask_file.name, "rb") as mask_f,
            ):
                response = await async_client.images.edit(
                    image=image_file,
                    mask=mask_f,
                    prompt="Add a red circle in the center",
                    n=1,
                    size="256x256",
                )
            assert hasattr(response, "data")
        finally:
            os.unlink(mask_file.name)
