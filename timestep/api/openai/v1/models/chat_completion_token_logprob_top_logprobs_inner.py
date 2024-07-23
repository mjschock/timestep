from datetime import date, datetime  # noqa: F401
from typing import Dict, List  # noqa: F401

from timestep.api.openai.v1 import util
from timestep.api.openai.v1.models.base_model import Model


class ChatCompletionTokenLogprobTopLogprobsInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, token=None, logprob=None, bytes=None):  # noqa: E501
        """ChatCompletionTokenLogprobTopLogprobsInner - a model defined in OpenAPI

        :param token: The token of this ChatCompletionTokenLogprobTopLogprobsInner.  # noqa: E501
        :type token: str
        :param logprob: The logprob of this ChatCompletionTokenLogprobTopLogprobsInner.  # noqa: E501
        :type logprob: float
        :param bytes: The bytes of this ChatCompletionTokenLogprobTopLogprobsInner.  # noqa: E501
        :type bytes: List[int]
        """
        self.openapi_types = {
            'token': str,
            'logprob': float,
            'bytes': List[int]
        }

        self.attribute_map = {
            'token': 'token',
            'logprob': 'logprob',
            'bytes': 'bytes'
        }

        self._token = token
        self._logprob = logprob
        self._bytes = bytes

    @classmethod
    def from_dict(cls, dikt) -> 'ChatCompletionTokenLogprobTopLogprobsInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ChatCompletionTokenLogprob_top_logprobs_inner of this ChatCompletionTokenLogprobTopLogprobsInner.  # noqa: E501
        :rtype: ChatCompletionTokenLogprobTopLogprobsInner
        """
        return util.deserialize_model(dikt, cls)

    @property
    def token(self) -> str:
        """Gets the token of this ChatCompletionTokenLogprobTopLogprobsInner.

        The token.  # noqa: E501

        :return: The token of this ChatCompletionTokenLogprobTopLogprobsInner.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token: str):
        """Sets the token of this ChatCompletionTokenLogprobTopLogprobsInner.

        The token.  # noqa: E501

        :param token: The token of this ChatCompletionTokenLogprobTopLogprobsInner.
        :type token: str
        """
        if token is None:
            raise ValueError("Invalid value for `token`, must not be `None`")  # noqa: E501

        self._token = token

    @property
    def logprob(self) -> float:
        """Gets the logprob of this ChatCompletionTokenLogprobTopLogprobsInner.

        The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.  # noqa: E501

        :return: The logprob of this ChatCompletionTokenLogprobTopLogprobsInner.
        :rtype: float
        """
        return self._logprob

    @logprob.setter
    def logprob(self, logprob: float):
        """Sets the logprob of this ChatCompletionTokenLogprobTopLogprobsInner.

        The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.  # noqa: E501

        :param logprob: The logprob of this ChatCompletionTokenLogprobTopLogprobsInner.
        :type logprob: float
        """
        if logprob is None:
            raise ValueError("Invalid value for `logprob`, must not be `None`")  # noqa: E501

        self._logprob = logprob

    @property
    def bytes(self) -> List[int]:
        """Gets the bytes of this ChatCompletionTokenLogprobTopLogprobsInner.

        A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.  # noqa: E501

        :return: The bytes of this ChatCompletionTokenLogprobTopLogprobsInner.
        :rtype: List[int]
        """
        return self._bytes

    @bytes.setter
    def bytes(self, bytes: List[int]):
        """Sets the bytes of this ChatCompletionTokenLogprobTopLogprobsInner.

        A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.  # noqa: E501

        :param bytes: The bytes of this ChatCompletionTokenLogprobTopLogprobsInner.
        :type bytes: List[int]
        """
        if bytes is None:
            raise ValueError("Invalid value for `bytes`, must not be `None`")  # noqa: E501

        self._bytes = bytes
