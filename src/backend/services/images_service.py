# mypy: ignore-errors
import base64
import io
import tempfile

import torch
from fastapi import HTTPException, Request, UploadFile
from PIL import Image

from backend.services.models_service import get_models_service


class ImagesService:
    async def create_image(self, request: Request):
        """Creates an image given a prompt."""
        try:
            # Parse request body
            try:
                body = await request.json()
            except Exception:
                body = {}

            model = body.get("model", "stable-diffusion-v1-5/stable-diffusion-v1-5")
            prompt = body.get("prompt", "")
            n = body.get("n", 1)
            size = body.get("size", "1024x1024")
            body.get("quality", "standard")
            response_format = body.get("response_format", "url")
            body.get("style", "vivid")
            body.get("user")

            if not prompt:
                raise HTTPException(status_code=400, detail="Missing 'prompt' field.")

            # Validate parameters
            if n < 1 or n > 10:
                raise HTTPException(
                    status_code=400, detail="'n' must be between 1 and 10."
                )

            if size not in [
                "256x256",
                "512x512",
                "1024x1024",
                "1792x1024",
                "1024x1792",
            ]:
                raise HTTPException(
                    status_code=400,
                    detail="Invalid size. Must be one of: 256x256, 512x512, 1024x1024, 1792x1024, 1024x1792.",
                )

            if response_format not in ["url", "b64_json"]:
                raise HTTPException(
                    status_code=400,
                    detail="response_format must be 'url' or 'b64_json'.",
                )

            # Parse size
            width, height = map(int, size.split("x"))

            # Get image generation pipeline
            pipeline = get_models_service().get_image_pipeline(model)

            # Generate images
            images = []
            for _ in range(n):
                # Generate image
                result = pipeline(
                    prompt=prompt,
                    width=width,
                    height=height,
                    num_inference_steps=20,  # Keep it fast for testing
                    guidance_scale=7.5,
                )

                image = result.images[0]

                # Convert to bytes
                img_byte_arr = io.BytesIO()
                image.save(img_byte_arr, format="PNG")
                img_byte_arr = img_byte_arr.getvalue()

                if response_format == "b64_json":
                    # Return base64 encoded image
                    b64_image = base64.b64encode(img_byte_arr).decode("utf-8")
                    images.append({"b64_json": b64_image, "revised_prompt": prompt})
                else:
                    # For URL format, we'll return a data URL
                    b64_image = base64.b64encode(img_byte_arr).decode("utf-8")
                    data_url = f"data:image/png;base64,{b64_image}"
                    images.append({"url": data_url, "revised_prompt": prompt})

            return {
                "created": int(torch.tensor(0).item()),  # Placeholder timestamp
                "data": images,
            }

        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Image generation failed: {str(e)}"
            ) from e

    async def create_image_variation(self, request: Request):
        """Creates a variation of a given image."""
        try:
            # Parse multipart form
            form = await request.form()
            image_file: UploadFile = form.get("image")
            model = form.get("model", "stable-diffusion-v1-5/stable-diffusion-v1-5")
            n = int(form.get("n", 1))
            response_format = form.get("response_format", "url")
            size = form.get("size", "1024x1024")
            form.get("user")

            if not image_file:
                raise HTTPException(status_code=400, detail="Missing image file.")

            # Validate parameters
            if n < 1 or n > 10:
                raise HTTPException(
                    status_code=400, detail="'n' must be between 1 and 10."
                )

            if size not in [
                "256x256",
                "512x512",
                "1024x1024",
                "1792x1024",
                "1024x1792",
            ]:
                raise HTTPException(status_code=400, detail="Invalid size.")

            if response_format not in ["url", "b64_json"]:
                raise HTTPException(
                    status_code=400,
                    detail="response_format must be 'url' or 'b64_json'.",
                )

            # Parse size
            width, height = map(int, size.split("x"))

            # Save image to temp file
            with tempfile.NamedTemporaryFile(delete=True, suffix=".png") as tmp:
                content = await image_file.read()
                tmp.write(content)
                tmp.flush()

                # Load and preprocess image
                init_image = Image.open(tmp.name).convert("RGB")
                init_image = init_image.resize((width, height))

                # Get image variation pipeline
                pipeline = get_models_service().get_image_pipeline(model)

                # Generate variations
                images = []
                for _ in range(n):
                    # Generate variation
                    result = pipeline(
                        prompt="",  # Empty prompt for variations
                        image=init_image,
                        width=width,
                        height=height,
                        num_inference_steps=20,
                        guidance_scale=7.5,
                    )

                    image = result.images[0]

                    # Convert to bytes
                    img_byte_arr = io.BytesIO()
                    image.save(img_byte_arr, format="PNG")
                    img_byte_arr = img_byte_arr.getvalue()

                    if response_format == "b64_json":
                        b64_image = base64.b64encode(img_byte_arr).decode("utf-8")
                        images.append({"b64_json": b64_image})
                    else:
                        b64_image = base64.b64encode(img_byte_arr).decode("utf-8")
                        data_url = f"data:image/png;base64,{b64_image}"
                        images.append({"url": data_url})

            return {"created": int(torch.tensor(0).item()), "data": images}

        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Image variation failed: {str(e)}"
            ) from e

    async def create_image_edit(self, request: Request):
        """Creates an edited or extended image given a source image and a prompt."""
        body = await self._get_request_body(request)
        image = self._extract_image(body)
        prompt = self._extract_prompt(body)
        try:
            edited_image = self._edit_image(image, prompt)
            return {"image": edited_image}
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Image editing failed: {str(e)}"
            ) from e

    async def _get_request_body(self, request: Request) -> dict:
        try:
            return await request.json()
        except Exception:
            return {}

    def _extract_image(self, body: dict):
        # Dummy implementation for demonstration
        return body.get("image")

    def _extract_prompt(self, body: dict) -> str:
        prompt = body.get("prompt")
        if not prompt:
            raise HTTPException(status_code=400, detail="'prompt' is required")
        return prompt

    def _edit_image(self, image, prompt: str):
        # Dummy implementation for demonstration
        return image
