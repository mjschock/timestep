import base64
import time
from io import BytesIO
from typing import List

import connexion
import PIL.Image
from openai.types.image import Image
from openai.types.images_response import ImagesResponse


def create_image(body: dict, token_info: dict, user: str):
    """Creates an image given a prompt.

     # noqa: E501

    :param create_image_request:
    :type create_image_request: dict | bytes

    :rtype: Union[ImagesResponse, Tuple[ImagesResponse, int], Tuple[ImagesResponse, int, Dict[str, str]]
    """
    # if connexion.request.is_json:
    #     create_image_request = CreateImageRequest.from_dict(connexion.request.get_json())  # noqa: E501
    # raise NotImplementedErrora

    # print('args: ', args)
    # kwargs:  {'body': {'prompt': 'a white siamese cat', 'model': 'dall-e-3', 'n': 1, 'quality': 'standard', 'size': '1024x1024'}, 'user': 'user_id', 'token_info': {'uid': 'user_id'}}
    # print('kwargs: ', kwargs)

    assert body.get("user") == user

    width, height = map(int, body.get("size", "512x512").split("x"))

    output: List[PIL.Image.Image] = stable_diffusion.txt_to_img(
        body.get("prompt"),
        height=height,
        # sample_steps=5, # default is 20
        width=width,
    )

    image: PIL.Image.Image = output[0]

    # buffered = BytesIO()
    # image.save(buffered, format="PNG")
    # image.save(buffered, format="JSON")
    # b64_json = str(base64.b64encode(buffered.getvalue()))

    # s: ReadableBuffer
    # base64.urlsafe_b64encode(s)
    b64_json: str = base64.b64encode(image._repr_png_()).decode("utf-8")

    images: List[Image] = [
        Image(
            b64_json=b64_json,
            revised_prompt=body.get("prompt"),
            url=None,
        )
    ]

    return ImagesResponse(
        created=int(time.time()),
        data=images,
    ).model_dump(mode="json")


def create_image_edit(
    image,
    prompt,
    mask=None,
    model=None,
    n=None,
    size=None,
    response_format=None,
    user=None,
):  # noqa: E501
    """Creates an edited or extended image given an original image and a prompt.

     # noqa: E501

    :param image: The image to edit. Must be a valid PNG file, less than 4MB, and square. If mask is not provided, image must have transparency, which will be used as the mask.
    :type image: str
    :param prompt: A text description of the desired image(s). The maximum length is 1000 characters.
    :type prompt: str
    :param mask: An additional image whose fully transparent areas (e.g. where alpha is zero) indicate where &#x60;image&#x60; should be edited. Must be a valid PNG file, less than 4MB, and have the same dimensions as &#x60;image&#x60;.
    :type mask: str
    :param model:
    :type model: dict | bytes
    :param n: The number of images to generate. Must be between 1 and 10.
    :type n: int
    :param size: The size of the generated images. Must be one of &#x60;256x256&#x60;, &#x60;512x512&#x60;, or &#x60;1024x1024&#x60;.
    :type size: str
    :param response_format: The format in which the generated images are returned. Must be one of &#x60;url&#x60; or &#x60;b64_json&#x60;. URLs are only valid for 60 minutes after the image has been generated.
    :type response_format: str
    :param user: A unique identifier representing your end-user, which can help OpenAI to monitor and detect abuse. [Learn more](/docs/guides/safety-best-practices/end-user-ids).
    :type user: str

    :rtype: Union[ImagesResponse, Tuple[ImagesResponse, int], Tuple[ImagesResponse, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        model = CreateImageEditRequestModel.from_dict(
            connexion.request.get_json()
        )  # noqa: E501
    raise NotImplementedError


def create_image_variation(
    image, model=None, n=None, response_format=None, size=None, user=None
):  # noqa: E501
    """Creates a variation of a given image.

     # noqa: E501

    :param image: The image to use as the basis for the variation(s). Must be a valid PNG file, less than 4MB, and square.
    :type image: str
    :param model:
    :type model: dict | bytes
    :param n: The number of images to generate. Must be between 1 and 10. For &#x60;dall-e-3&#x60;, only &#x60;n&#x3D;1&#x60; is supported.
    :type n: int
    :param response_format: The format in which the generated images are returned. Must be one of &#x60;url&#x60; or &#x60;b64_json&#x60;. URLs are only valid for 60 minutes after the image has been generated.
    :type response_format: str
    :param size: The size of the generated images. Must be one of &#x60;256x256&#x60;, &#x60;512x512&#x60;, or &#x60;1024x1024&#x60;.
    :type size: str
    :param user: A unique identifier representing your end-user, which can help OpenAI to monitor and detect abuse. [Learn more](/docs/guides/safety-best-practices/end-user-ids).
    :type user: str

    :rtype: Union[ImagesResponse, Tuple[ImagesResponse, int], Tuple[ImagesResponse, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        model = CreateImageEditRequestModel.from_dict(
            connexion.request.get_json()
        )  # noqa: E501
    raise NotImplementedError
