import connexion

from timestep.api.openai.v1.models.create_embedding_request import (  # noqa: E501
    CreateEmbeddingRequest,
)


def create_embedding(create_embedding_request):  # noqa: E501
    """Creates an embedding vector representing the input text.

     # noqa: E501

    :param create_embedding_request:
    :type create_embedding_request: dict | bytes

    :rtype: Union[CreateEmbeddingResponse, Tuple[CreateEmbeddingResponse, int], Tuple[CreateEmbeddingResponse, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        create_embedding_request = CreateEmbeddingRequest.from_dict(
            connexion.request.get_json()
        )  # noqa: E501
    raise NotImplementedError
