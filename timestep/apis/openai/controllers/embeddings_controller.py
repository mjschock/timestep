import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from timestep.apis.openai.models.create_embedding_request import CreateEmbeddingRequest  # noqa: E501
from timestep.apis.openai.models.create_embedding_response import CreateEmbeddingResponse  # noqa: E501
from timestep.apis.openai import util


def create_embedding(create_embedding_request):  # noqa: E501
    """Creates an embedding vector representing the input text.

     # noqa: E501

    :param create_embedding_request: 
    :type create_embedding_request: dict | bytes

    :rtype: Union[CreateEmbeddingResponse, Tuple[CreateEmbeddingResponse, int], Tuple[CreateEmbeddingResponse, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        create_embedding_request = CreateEmbeddingRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
