from __future__ import annotations

import base64
import gc
import os
from io import BytesIO
from pathlib import Path

import torch
from pdf2image import convert_from_path
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError,
)
from PIL import Image


def base64_encode_image(image: Image.Image) -> str:
    buff = BytesIO()
    image.save(buff, format="JPEG")
    return base64.b64encode(buff.getvalue()).decode("utf-8")


def clear_gpu_memory(model: torch.nn.Module = None) -> None:
    if model is not None:
        del model

    torch.cuda.empty_cache()
    gc.collect()


def compress_pdf(pdf_path: str, output_path: str) -> None:
    images: list[Image.Image] = convert_pdf_to_images(pdf_path)
    save_images_to_pdf(images, output_path)


def convert_pdf_to_images(pdf_path: str) -> list[Image.Image]:
    try:
        images_from_path: list[Image.Image] = convert_from_path(pdf_path)

    except PDFInfoNotInstalledError:
        pass

    except PDFPageCountError:
        pass

    except PDFSyntaxError:
        pass

    except Exception:
        pass

    return images_from_path


def decode_base64_image(base64_image: str) -> Image.Image:
    return Image.open(BytesIO(base64.b64decode(base64_image)))


def get_parent_folder_where_folder_name_is(folder_name: str) -> str | None:
    # current_path = os.getcwd()
    current_path = str(Path.cwd())

    while current_path != "/":
        if folder_name in os.listdir(current_path):
            return current_path

        # current_path = os.path.dirname(current_path)
        current_path = str(Path(current_path).parent)

    return None


def get_data_path(
    subfolder: str = "01_raw", top_level_folder: str = "notebooks"
) -> Path:
    parent_folder: str | None = get_parent_folder_where_folder_name_is(top_level_folder)

    if parent_folder is None:
        msg = f"Could not find folder {top_level_folder} in the path."
        raise FileNotFoundError(msg)

    return Path(parent_folder) / f"data/{subfolder}"


def get_data_paths() -> dict[str, Path]:
    return {
        "01_raw": get_data_path("01_raw"),
        "02_intermediate": get_data_path("02_intermediate"),
        "03_primary": get_data_path("03_primary"),
        "04_feature": get_data_path("04_feature"),
        "05_model_input": get_data_path("05_model_input"),
        "06_models": get_data_path("06_models"),
        "07_model_output": get_data_path("07_model_output"),
        "08_reporting": get_data_path("08_reporting"),
        "09_workspaces": get_data_path("09_workspaces"),
    }


def save_images(
    images: list[Image.Image], save_path: str, extension: str = "jpg"
) -> None:
    # os.makedirs(save_path, exist_ok=True)
    Path(save_path).mkdir(exist_ok=True, parents=True)
    num_images = len(images)

    for i, image in enumerate(images):
        # save images with name padded with zeros to match the number of images
        image.save(
            # os.path.join(save_path, f"{str(i).zfill(len(str(num_images)))}.{extension}")
            Path(save_path) / f"{str(i).zfill(len(str(num_images)))}.{extension}"
        )


def save_images_to_pdf(images: list[Image.Image], output_path: str) -> None:
    images[0].save(
        output_path, "PDF", resolution=100.0, save_all=True, append_images=images[1:]
    )
