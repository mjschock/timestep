from typing import Dict, Tuple, Union

import connexion

from timestep.api.openai.v1 import util
from timestep.api.openai.v1.models.create_image_edit_request_model import \
    CreateImageEditRequestModel  # noqa: E501
from timestep.api.openai.v1.models.create_image_request import \
    CreateImageRequest  # noqa: E501
from timestep.api.openai.v1.models.images_response import \
    ImagesResponse  # noqa: E501


def create_image(create_image_request):  # noqa: E501
    """Creates an image given a prompt.

     # noqa: E501

    :param create_image_request: 
    :type create_image_request: dict | bytes

    :rtype: Union[ImagesResponse, Tuple[ImagesResponse, int], Tuple[ImagesResponse, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        create_image_request = CreateImageRequest.from_dict(connexion.request.get_json())  # noqa: E501
    raise NotImplementedError


def create_image_edit(image, prompt, mask=None, model=None, n=None, size=None, response_format=None, user=None):  # noqa: E501
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
        model = CreateImageEditRequestModel.from_dict(connexion.request.get_json())  # noqa: E501
    raise NotImplementedError


def create_image_variation(image, model=None, n=None, response_format=None, size=None, user=None):  # noqa: E501
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
        model = CreateImageEditRequestModel.from_dict(connexion.request.get_json())  # noqa: E501
    raise NotImplementedError
