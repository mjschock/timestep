from datetime import date, datetime  # noqa: F401
from typing import Dict, List  # noqa: F401

from timestep.api.openai.v1 import util
from timestep.api.openai.v1.models.base_model import Model
from timestep.api.openai.v1.models.completion_usage import \
    CompletionUsage  # noqa: E501
from timestep.api.openai.v1.models.create_chat_completion_response_choices_inner import \
    CreateChatCompletionResponseChoicesInner  # noqa: E501


class CreateChatCompletionResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, choices=None, created=None, model=None, service_tier=None, system_fingerprint=None, object=None, usage=None):  # noqa: E501
        """CreateChatCompletionResponse - a model defined in OpenAPI

        :param id: The id of this CreateChatCompletionResponse.  # noqa: E501
        :type id: str
        :param choices: The choices of this CreateChatCompletionResponse.  # noqa: E501
        :type choices: List[CreateChatCompletionResponseChoicesInner]
        :param created: The created of this CreateChatCompletionResponse.  # noqa: E501
        :type created: int
        :param model: The model of this CreateChatCompletionResponse.  # noqa: E501
        :type model: str
        :param service_tier: The service_tier of this CreateChatCompletionResponse.  # noqa: E501
        :type service_tier: str
        :param system_fingerprint: The system_fingerprint of this CreateChatCompletionResponse.  # noqa: E501
        :type system_fingerprint: str
        :param object: The object of this CreateChatCompletionResponse.  # noqa: E501
        :type object: str
        :param usage: The usage of this CreateChatCompletionResponse.  # noqa: E501
        :type usage: CompletionUsage
        """
        self.openapi_types = {
            'id': str,
            'choices': List[CreateChatCompletionResponseChoicesInner],
            'created': int,
            'model': str,
            'service_tier': str,
            'system_fingerprint': str,
            'object': str,
            'usage': CompletionUsage
        }

        self.attribute_map = {
            'id': 'id',
            'choices': 'choices',
            'created': 'created',
            'model': 'model',
            'service_tier': 'service_tier',
            'system_fingerprint': 'system_fingerprint',
            'object': 'object',
            'usage': 'usage'
        }

        self._id = id
        self._choices = choices
        self._created = created
        self._model = model
        self._service_tier = service_tier
        self._system_fingerprint = system_fingerprint
        self._object = object
        self._usage = usage

    @classmethod
    def from_dict(cls, dikt) -> 'CreateChatCompletionResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CreateChatCompletionResponse of this CreateChatCompletionResponse.  # noqa: E501
        :rtype: CreateChatCompletionResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this CreateChatCompletionResponse.

        A unique identifier for the chat completion.  # noqa: E501

        :return: The id of this CreateChatCompletionResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this CreateChatCompletionResponse.

        A unique identifier for the chat completion.  # noqa: E501

        :param id: The id of this CreateChatCompletionResponse.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def choices(self) -> List[CreateChatCompletionResponseChoicesInner]:
        """Gets the choices of this CreateChatCompletionResponse.

        A list of chat completion choices. Can be more than one if `n` is greater than 1.  # noqa: E501

        :return: The choices of this CreateChatCompletionResponse.
        :rtype: List[CreateChatCompletionResponseChoicesInner]
        """
        return self._choices

    @choices.setter
    def choices(self, choices: List[CreateChatCompletionResponseChoicesInner]):
        """Sets the choices of this CreateChatCompletionResponse.

        A list of chat completion choices. Can be more than one if `n` is greater than 1.  # noqa: E501

        :param choices: The choices of this CreateChatCompletionResponse.
        :type choices: List[CreateChatCompletionResponseChoicesInner]
        """
        if choices is None:
            raise ValueError("Invalid value for `choices`, must not be `None`")  # noqa: E501

        self._choices = choices

    @property
    def created(self) -> int:
        """Gets the created of this CreateChatCompletionResponse.

        The Unix timestamp (in seconds) of when the chat completion was created.  # noqa: E501

        :return: The created of this CreateChatCompletionResponse.
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created: int):
        """Sets the created of this CreateChatCompletionResponse.

        The Unix timestamp (in seconds) of when the chat completion was created.  # noqa: E501

        :param created: The created of this CreateChatCompletionResponse.
        :type created: int
        """
        if created is None:
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def model(self) -> str:
        """Gets the model of this CreateChatCompletionResponse.

        The model used for the chat completion.  # noqa: E501

        :return: The model of this CreateChatCompletionResponse.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model: str):
        """Sets the model of this CreateChatCompletionResponse.

        The model used for the chat completion.  # noqa: E501

        :param model: The model of this CreateChatCompletionResponse.
        :type model: str
        """
        if model is None:
            raise ValueError("Invalid value for `model`, must not be `None`")  # noqa: E501

        self._model = model

    @property
    def service_tier(self) -> str:
        """Gets the service_tier of this CreateChatCompletionResponse.

        The service tier used for processing the request. This field is only included if the `service_tier` parameter is specified in the request.  # noqa: E501

        :return: The service_tier of this CreateChatCompletionResponse.
        :rtype: str
        """
        return self._service_tier

    @service_tier.setter
    def service_tier(self, service_tier: str):
        """Sets the service_tier of this CreateChatCompletionResponse.

        The service tier used for processing the request. This field is only included if the `service_tier` parameter is specified in the request.  # noqa: E501

        :param service_tier: The service_tier of this CreateChatCompletionResponse.
        :type service_tier: str
        """
        allowed_values = [None,"scale", "default"]  # noqa: E501
        if service_tier not in allowed_values:
            raise ValueError(
                "Invalid value for `service_tier` ({0}), must be one of {1}"
                .format(service_tier, allowed_values)
            )

        self._service_tier = service_tier

    @property
    def system_fingerprint(self) -> str:
        """Gets the system_fingerprint of this CreateChatCompletionResponse.

        This fingerprint represents the backend configuration that the model runs with.  Can be used in conjunction with the `seed` request parameter to understand when backend changes have been made that might impact determinism.   # noqa: E501

        :return: The system_fingerprint of this CreateChatCompletionResponse.
        :rtype: str
        """
        return self._system_fingerprint

    @system_fingerprint.setter
    def system_fingerprint(self, system_fingerprint: str):
        """Sets the system_fingerprint of this CreateChatCompletionResponse.

        This fingerprint represents the backend configuration that the model runs with.  Can be used in conjunction with the `seed` request parameter to understand when backend changes have been made that might impact determinism.   # noqa: E501

        :param system_fingerprint: The system_fingerprint of this CreateChatCompletionResponse.
        :type system_fingerprint: str
        """

        self._system_fingerprint = system_fingerprint

    @property
    def object(self) -> str:
        """Gets the object of this CreateChatCompletionResponse.

        The object type, which is always `chat.completion`.  # noqa: E501

        :return: The object of this CreateChatCompletionResponse.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object: str):
        """Sets the object of this CreateChatCompletionResponse.

        The object type, which is always `chat.completion`.  # noqa: E501

        :param object: The object of this CreateChatCompletionResponse.
        :type object: str
        """
        allowed_values = ["chat.completion"]  # noqa: E501
        if object not in allowed_values:
            raise ValueError(
                "Invalid value for `object` ({0}), must be one of {1}"
                .format(object, allowed_values)
            )

        self._object = object

    @property
    def usage(self) -> CompletionUsage:
        """Gets the usage of this CreateChatCompletionResponse.


        :return: The usage of this CreateChatCompletionResponse.
        :rtype: CompletionUsage
        """
        return self._usage

    @usage.setter
    def usage(self, usage: CompletionUsage):
        """Sets the usage of this CreateChatCompletionResponse.


        :param usage: The usage of this CreateChatCompletionResponse.
        :type usage: CompletionUsage
        """

        self._usage = usage
