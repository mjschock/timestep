from typing import Dict, Tuple, Union

import connexion

from timestep.api.openai.v1 import util
from timestep.api.openai.v1.models.create_moderation_request import \
    CreateModerationRequest  # noqa: E501
from timestep.api.openai.v1.models.create_moderation_response import \
    CreateModerationResponse  # noqa: E501


def create_moderation(create_moderation_request):  # noqa: E501
    """Classifies if text is potentially harmful.

     # noqa: E501

    :param create_moderation_request: 
    :type create_moderation_request: dict | bytes

    :rtype: Union[CreateModerationResponse, Tuple[CreateModerationResponse, int], Tuple[CreateModerationResponse, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        create_moderation_request = CreateModerationRequest.from_dict(connexion.request.get_json())  # noqa: E501
    raise NotImplementedError
