from datetime import date, datetime  # noqa: F401
from typing import Dict, List  # noqa: F401

from timestep.api.openai.v1 import util
from timestep.api.openai.v1.models.base_model import Model
from timestep.api.openai.v1.models.run_step_delta_step_details_tool_calls_code_output_image_object import \
    RunStepDeltaStepDetailsToolCallsCodeOutputImageObject  # noqa: E501
from timestep.api.openai.v1.models.run_step_delta_step_details_tool_calls_code_output_image_object_image import \
    RunStepDeltaStepDetailsToolCallsCodeOutputImageObjectImage  # noqa: E501
from timestep.api.openai.v1.models.run_step_delta_step_details_tool_calls_code_output_logs_object import \
    RunStepDeltaStepDetailsToolCallsCodeOutputLogsObject  # noqa: E501


class RunStepDeltaStepDetailsToolCallsCodeObjectCodeInterpreterOutputsInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, index=None, type=None, logs=None, image=None):  # noqa: E501
        """RunStepDeltaStepDetailsToolCallsCodeObjectCodeInterpreterOutputsInner - a model defined in OpenAPI

        :param index: The index of this RunStepDeltaStepDetailsToolCallsCodeObjectCodeInterpreterOutputsInner.  # noqa: E501
        :type index: int
        :param type: The type of this RunStepDeltaStepDetailsToolCallsCodeObjectCodeInterpreterOutputsInner.  # noqa: E501
        :type type: str
        :param logs: The logs of this RunStepDeltaStepDetailsToolCallsCodeObjectCodeInterpreterOutputsInner.  # noqa: E501
        :type logs: str
        :param image: The image of this RunStepDeltaStepDetailsToolCallsCodeObjectCodeInterpreterOutputsInner.  # noqa: E501
        :type image: RunStepDeltaStepDetailsToolCallsCodeOutputImageObjectImage
        """
        self.openapi_types = {
            'index': int,
            'type': str,
            'logs': str,
            'image': RunStepDeltaStepDetailsToolCallsCodeOutputImageObjectImage
        }

        self.attribute_map = {
            'index': 'index',
            'type': 'type',
            'logs': 'logs',
            'image': 'image'
        }

        self._index = index
        self._type = type
        self._logs = logs
        self._image = image

    @classmethod
    def from_dict(cls, dikt) -> 'RunStepDeltaStepDetailsToolCallsCodeObjectCodeInterpreterOutputsInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RunStepDeltaStepDetailsToolCallsCodeObject_code_interpreter_outputs_inner of this RunStepDeltaStepDetailsToolCallsCodeObjectCodeInterpreterOutputsInner.  # noqa: E501
        :rtype: RunStepDeltaStepDetailsToolCallsCodeObjectCodeInterpreterOutputsInner
        """
        return util.deserialize_model(dikt, cls)

    @property
    def index(self) -> int:
        """Gets the index of this RunStepDeltaStepDetailsToolCallsCodeObjectCodeInterpreterOutputsInner.

        The index of the output in the outputs array.  # noqa: E501

        :return: The index of this RunStepDeltaStepDetailsToolCallsCodeObjectCodeInterpreterOutputsInner.
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index: int):
        """Sets the index of this RunStepDeltaStepDetailsToolCallsCodeObjectCodeInterpreterOutputsInner.

        The index of the output in the outputs array.  # noqa: E501

        :param index: The index of this RunStepDeltaStepDetailsToolCallsCodeObjectCodeInterpreterOutputsInner.
        :type index: int
        """
        if index is None:
            raise ValueError("Invalid value for `index`, must not be `None`")  # noqa: E501

        self._index = index

    @property
    def type(self) -> str:
        """Gets the type of this RunStepDeltaStepDetailsToolCallsCodeObjectCodeInterpreterOutputsInner.

        Always `logs`.  # noqa: E501

        :return: The type of this RunStepDeltaStepDetailsToolCallsCodeObjectCodeInterpreterOutputsInner.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this RunStepDeltaStepDetailsToolCallsCodeObjectCodeInterpreterOutputsInner.

        Always `logs`.  # noqa: E501

        :param type: The type of this RunStepDeltaStepDetailsToolCallsCodeObjectCodeInterpreterOutputsInner.
        :type type: str
        """
        allowed_values = ["logs", "image"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def logs(self) -> str:
        """Gets the logs of this RunStepDeltaStepDetailsToolCallsCodeObjectCodeInterpreterOutputsInner.

        The text output from the Code Interpreter tool call.  # noqa: E501

        :return: The logs of this RunStepDeltaStepDetailsToolCallsCodeObjectCodeInterpreterOutputsInner.
        :rtype: str
        """
        return self._logs

    @logs.setter
    def logs(self, logs: str):
        """Sets the logs of this RunStepDeltaStepDetailsToolCallsCodeObjectCodeInterpreterOutputsInner.

        The text output from the Code Interpreter tool call.  # noqa: E501

        :param logs: The logs of this RunStepDeltaStepDetailsToolCallsCodeObjectCodeInterpreterOutputsInner.
        :type logs: str
        """

        self._logs = logs

    @property
    def image(self) -> RunStepDeltaStepDetailsToolCallsCodeOutputImageObjectImage:
        """Gets the image of this RunStepDeltaStepDetailsToolCallsCodeObjectCodeInterpreterOutputsInner.


        :return: The image of this RunStepDeltaStepDetailsToolCallsCodeObjectCodeInterpreterOutputsInner.
        :rtype: RunStepDeltaStepDetailsToolCallsCodeOutputImageObjectImage
        """
        return self._image

    @image.setter
    def image(self, image: RunStepDeltaStepDetailsToolCallsCodeOutputImageObjectImage):
        """Sets the image of this RunStepDeltaStepDetailsToolCallsCodeObjectCodeInterpreterOutputsInner.


        :param image: The image of this RunStepDeltaStepDetailsToolCallsCodeObjectCodeInterpreterOutputsInner.
        :type image: RunStepDeltaStepDetailsToolCallsCodeOutputImageObjectImage
        """

        self._image = image
