from datetime import date, datetime  # noqa: F401
from typing import Dict, List  # noqa: F401

from timestep.api.openai.v1 import util
from timestep.api.openai.v1.models.base_model import Model


class Embedding(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, index=None, embedding=None, object=None):  # noqa: E501
        """Embedding - a model defined in OpenAPI

        :param index: The index of this Embedding.  # noqa: E501
        :type index: int
        :param embedding: The embedding of this Embedding.  # noqa: E501
        :type embedding: List[float]
        :param object: The object of this Embedding.  # noqa: E501
        :type object: str
        """
        self.openapi_types = {
            'index': int,
            'embedding': List[float],
            'object': str
        }

        self.attribute_map = {
            'index': 'index',
            'embedding': 'embedding',
            'object': 'object'
        }

        self._index = index
        self._embedding = embedding
        self._object = object

    @classmethod
    def from_dict(cls, dikt) -> 'Embedding':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Embedding of this Embedding.  # noqa: E501
        :rtype: Embedding
        """
        return util.deserialize_model(dikt, cls)

    @property
    def index(self) -> int:
        """Gets the index of this Embedding.

        The index of the embedding in the list of embeddings.  # noqa: E501

        :return: The index of this Embedding.
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index: int):
        """Sets the index of this Embedding.

        The index of the embedding in the list of embeddings.  # noqa: E501

        :param index: The index of this Embedding.
        :type index: int
        """
        if index is None:
            raise ValueError("Invalid value for `index`, must not be `None`")  # noqa: E501

        self._index = index

    @property
    def embedding(self) -> List[float]:
        """Gets the embedding of this Embedding.

        The embedding vector, which is a list of floats. The length of vector depends on the model as listed in the [embedding guide](/docs/guides/embeddings).   # noqa: E501

        :return: The embedding of this Embedding.
        :rtype: List[float]
        """
        return self._embedding

    @embedding.setter
    def embedding(self, embedding: List[float]):
        """Sets the embedding of this Embedding.

        The embedding vector, which is a list of floats. The length of vector depends on the model as listed in the [embedding guide](/docs/guides/embeddings).   # noqa: E501

        :param embedding: The embedding of this Embedding.
        :type embedding: List[float]
        """
        if embedding is None:
            raise ValueError("Invalid value for `embedding`, must not be `None`")  # noqa: E501

        self._embedding = embedding

    @property
    def object(self) -> str:
        """Gets the object of this Embedding.

        The object type, which is always \"embedding\".  # noqa: E501

        :return: The object of this Embedding.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object: str):
        """Sets the object of this Embedding.

        The object type, which is always \"embedding\".  # noqa: E501

        :param object: The object of this Embedding.
        :type object: str
        """
        allowed_values = ["embedding"]  # noqa: E501
        if object not in allowed_values:
            raise ValueError(
                "Invalid value for `object` ({0}), must be one of {1}"
                .format(object, allowed_values)
            )

        self._object = object
