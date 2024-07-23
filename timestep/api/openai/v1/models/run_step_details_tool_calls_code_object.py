from datetime import date, datetime  # noqa: F401
from typing import Dict, List  # noqa: F401

from timestep.api.openai.v1 import util
from timestep.api.openai.v1.models.base_model import Model
from timestep.api.openai.v1.models.run_step_details_tool_calls_code_object_code_interpreter import \
    RunStepDetailsToolCallsCodeObjectCodeInterpreter  # noqa: E501


class RunStepDetailsToolCallsCodeObject(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, type=None, code_interpreter=None):  # noqa: E501
        """RunStepDetailsToolCallsCodeObject - a model defined in OpenAPI

        :param id: The id of this RunStepDetailsToolCallsCodeObject.  # noqa: E501
        :type id: str
        :param type: The type of this RunStepDetailsToolCallsCodeObject.  # noqa: E501
        :type type: str
        :param code_interpreter: The code_interpreter of this RunStepDetailsToolCallsCodeObject.  # noqa: E501
        :type code_interpreter: RunStepDetailsToolCallsCodeObjectCodeInterpreter
        """
        self.openapi_types = {
            'id': str,
            'type': str,
            'code_interpreter': RunStepDetailsToolCallsCodeObjectCodeInterpreter
        }

        self.attribute_map = {
            'id': 'id',
            'type': 'type',
            'code_interpreter': 'code_interpreter'
        }

        self._id = id
        self._type = type
        self._code_interpreter = code_interpreter

    @classmethod
    def from_dict(cls, dikt) -> 'RunStepDetailsToolCallsCodeObject':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RunStepDetailsToolCallsCodeObject of this RunStepDetailsToolCallsCodeObject.  # noqa: E501
        :rtype: RunStepDetailsToolCallsCodeObject
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this RunStepDetailsToolCallsCodeObject.

        The ID of the tool call.  # noqa: E501

        :return: The id of this RunStepDetailsToolCallsCodeObject.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this RunStepDetailsToolCallsCodeObject.

        The ID of the tool call.  # noqa: E501

        :param id: The id of this RunStepDetailsToolCallsCodeObject.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def type(self) -> str:
        """Gets the type of this RunStepDetailsToolCallsCodeObject.

        The type of tool call. This is always going to be `code_interpreter` for this type of tool call.  # noqa: E501

        :return: The type of this RunStepDetailsToolCallsCodeObject.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this RunStepDetailsToolCallsCodeObject.

        The type of tool call. This is always going to be `code_interpreter` for this type of tool call.  # noqa: E501

        :param type: The type of this RunStepDetailsToolCallsCodeObject.
        :type type: str
        """
        allowed_values = ["code_interpreter"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def code_interpreter(self) -> RunStepDetailsToolCallsCodeObjectCodeInterpreter:
        """Gets the code_interpreter of this RunStepDetailsToolCallsCodeObject.


        :return: The code_interpreter of this RunStepDetailsToolCallsCodeObject.
        :rtype: RunStepDetailsToolCallsCodeObjectCodeInterpreter
        """
        return self._code_interpreter

    @code_interpreter.setter
    def code_interpreter(self, code_interpreter: RunStepDetailsToolCallsCodeObjectCodeInterpreter):
        """Sets the code_interpreter of this RunStepDetailsToolCallsCodeObject.


        :param code_interpreter: The code_interpreter of this RunStepDetailsToolCallsCodeObject.
        :type code_interpreter: RunStepDetailsToolCallsCodeObjectCodeInterpreter
        """
        if code_interpreter is None:
            raise ValueError("Invalid value for `code_interpreter`, must not be `None`")  # noqa: E501

        self._code_interpreter = code_interpreter
