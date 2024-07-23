from typing import Dict, Tuple, Union

import connexion

from timestep.api.openai.v1 import util
from timestep.api.openai.v1.models.create_embedding_request import \
    CreateEmbeddingRequest  # noqa: E501
from timestep.api.openai.v1.models.create_embedding_response import \
    CreateEmbeddingResponse  # noqa: E501


def create_embedding(create_embedding_request):  # noqa: E501
    """Creates an embedding vector representing the input text.

     # noqa: E501

    :param create_embedding_request: 
    :type create_embedding_request: dict | bytes

    :rtype: Union[CreateEmbeddingResponse, Tuple[CreateEmbeddingResponse, int], Tuple[CreateEmbeddingResponse, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        create_embedding_request = CreateEmbeddingRequest.from_dict(connexion.request.get_json())  # noqa: E501
    raise NotImplementedError
