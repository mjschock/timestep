import base64
import gc
from io import BytesIO
from PIL import Image
import os
from typing import List

from pdf2image import convert_from_path
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)
import torch

def base64_encode_image(image):
    buff = BytesIO()
    image.save(buff, format="JPEG")
    base64_image = base64.b64encode(buff.getvalue()).decode("utf-8")

    return base64_image


def clear_gpu_memory(model=None):
    if model is not None:
        del model

    torch.cuda.empty_cache()
    gc.collect()


def compress_pdf(pdf_path: str, output_path: str) -> None:
    images: List[Image.Image] = convert_pdf_to_images(pdf_path)
    save_images_to_pdf(images, output_path)


def convert_pdf_to_images(pdf_path: str) -> List[Image.Image]:
    try:
        images_from_path: List[Image.Image] = convert_from_path(pdf_path)

    except PDFInfoNotInstalledError:
        print('PDFInfoNotInstalledError')

    except PDFPageCountError:
        print('PDFPageCountError')

    except PDFSyntaxError:
        print('PDFSyntaxError')

    except Exception as e:
        print(e)

    return images_from_path


def decode_base64_image(base64_image):
    image = Image.open(BytesIO(base64.b64decode(base64_image)))

    return image


def get_parent_folder_where_folder_name_is(folder_name):
    current_path = os.getcwd()

    while current_path != "/":
        if folder_name in os.listdir(current_path):
            return current_path

        current_path = os.path.dirname(current_path)

    return None


def get_data_path(subfolder="01_raw"):
    return os.path.join(
        get_parent_folder_where_folder_name_is("notebooks"), f"data/{subfolder}"
    )


def get_data_paths():
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


def save_images(images: List[Image.Image], save_path: str, extension: str = 'jpg') -> None:
    os.makedirs(save_path, exist_ok=True)
    num_images = len(images)

    for i, image in enumerate(images):
        # save images with name padded with zeros to match the number of images
        image.save(os.path.join(save_path, f'{str(i).zfill(len(str(num_images)))}.{extension}'))

def save_images_to_pdf(images: List[Image.Image], output_path: str) -> None:
    images[0].save(output_path, 'PDF', resolution=100.0, save_all=True, append_images=images[1:])
