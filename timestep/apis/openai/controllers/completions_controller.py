import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from timestep.apis.openai.models.create_completion_request import CreateCompletionRequest  # noqa: E501
from timestep.apis.openai.models.create_completion_response import CreateCompletionResponse  # noqa: E501
from timestep.apis.openai import util


def create_completion(create_completion_request):  # noqa: E501
    """Creates a completion for the provided prompt and parameters.

     # noqa: E501

    :param create_completion_request: 
    :type create_completion_request: dict | bytes

    :rtype: Union[CreateCompletionResponse, Tuple[CreateCompletionResponse, int], Tuple[CreateCompletionResponse, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        create_completion_request = CreateCompletionRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
