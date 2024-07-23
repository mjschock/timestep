from datetime import date, datetime  # noqa: F401
from typing import Dict, List  # noqa: F401

from timestep.api.openai.v1 import util
from timestep.api.openai.v1.models.auto_chunking_strategy_request_param import \
    AutoChunkingStrategyRequestParam  # noqa: E501
from timestep.api.openai.v1.models.base_model import Model
from timestep.api.openai.v1.models.static_chunking_strategy import \
    StaticChunkingStrategy  # noqa: E501
from timestep.api.openai.v1.models.static_chunking_strategy_request_param import \
    StaticChunkingStrategyRequestParam  # noqa: E501


class ChunkingStrategyRequestParam(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, type=None, static=None):  # noqa: E501
        """ChunkingStrategyRequestParam - a model defined in OpenAPI

        :param type: The type of this ChunkingStrategyRequestParam.  # noqa: E501
        :type type: str
        :param static: The static of this ChunkingStrategyRequestParam.  # noqa: E501
        :type static: StaticChunkingStrategy
        """
        self.openapi_types = {
            'type': str,
            'static': StaticChunkingStrategy
        }

        self.attribute_map = {
            'type': 'type',
            'static': 'static'
        }

        self._type = type
        self._static = static

    @classmethod
    def from_dict(cls, dikt) -> 'ChunkingStrategyRequestParam':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ChunkingStrategyRequestParam of this ChunkingStrategyRequestParam.  # noqa: E501
        :rtype: ChunkingStrategyRequestParam
        """
        return util.deserialize_model(dikt, cls)

    @property
    def type(self) -> str:
        """Gets the type of this ChunkingStrategyRequestParam.

        Always `auto`.  # noqa: E501

        :return: The type of this ChunkingStrategyRequestParam.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this ChunkingStrategyRequestParam.

        Always `auto`.  # noqa: E501

        :param type: The type of this ChunkingStrategyRequestParam.
        :type type: str
        """
        allowed_values = ["auto", "static"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def static(self) -> StaticChunkingStrategy:
        """Gets the static of this ChunkingStrategyRequestParam.


        :return: The static of this ChunkingStrategyRequestParam.
        :rtype: StaticChunkingStrategy
        """
        return self._static

    @static.setter
    def static(self, static: StaticChunkingStrategy):
        """Sets the static of this ChunkingStrategyRequestParam.


        :param static: The static of this ChunkingStrategyRequestParam.
        :type static: StaticChunkingStrategy
        """
        if static is None:
            raise ValueError("Invalid value for `static`, must not be `None`")  # noqa: E501

        self._static = static
