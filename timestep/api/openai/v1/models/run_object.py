from datetime import date, datetime  # noqa: F401
from typing import Dict, List  # noqa: F401

from timestep.api.openai.v1 import util
from timestep.api.openai.v1.models.assistant_object_tools_inner import \
    AssistantObjectToolsInner  # noqa: E501
from timestep.api.openai.v1.models.assistants_api_response_format_option import \
    AssistantsApiResponseFormatOption  # noqa: E501
from timestep.api.openai.v1.models.assistants_api_tool_choice_option import \
    AssistantsApiToolChoiceOption  # noqa: E501
from timestep.api.openai.v1.models.base_model import Model
from timestep.api.openai.v1.models.run_completion_usage import \
    RunCompletionUsage  # noqa: E501
from timestep.api.openai.v1.models.run_object_incomplete_details import \
    RunObjectIncompleteDetails  # noqa: E501
from timestep.api.openai.v1.models.run_object_last_error import \
    RunObjectLastError  # noqa: E501
from timestep.api.openai.v1.models.run_object_required_action import \
    RunObjectRequiredAction  # noqa: E501
from timestep.api.openai.v1.models.truncation_object import \
    TruncationObject  # noqa: E501


class RunObject(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, object=None, created_at=None, thread_id=None, assistant_id=None, status=None, required_action=None, last_error=None, expires_at=None, started_at=None, cancelled_at=None, failed_at=None, completed_at=None, incomplete_details=None, model=None, instructions=None, tools=[], metadata=None, usage=None, temperature=None, top_p=None, max_prompt_tokens=None, max_completion_tokens=None, truncation_strategy=None, tool_choice=None, parallel_tool_calls=True, response_format=None):  # noqa: E501
        """RunObject - a model defined in OpenAPI

        :param id: The id of this RunObject.  # noqa: E501
        :type id: str
        :param object: The object of this RunObject.  # noqa: E501
        :type object: str
        :param created_at: The created_at of this RunObject.  # noqa: E501
        :type created_at: int
        :param thread_id: The thread_id of this RunObject.  # noqa: E501
        :type thread_id: str
        :param assistant_id: The assistant_id of this RunObject.  # noqa: E501
        :type assistant_id: str
        :param status: The status of this RunObject.  # noqa: E501
        :type status: str
        :param required_action: The required_action of this RunObject.  # noqa: E501
        :type required_action: RunObjectRequiredAction
        :param last_error: The last_error of this RunObject.  # noqa: E501
        :type last_error: RunObjectLastError
        :param expires_at: The expires_at of this RunObject.  # noqa: E501
        :type expires_at: int
        :param started_at: The started_at of this RunObject.  # noqa: E501
        :type started_at: int
        :param cancelled_at: The cancelled_at of this RunObject.  # noqa: E501
        :type cancelled_at: int
        :param failed_at: The failed_at of this RunObject.  # noqa: E501
        :type failed_at: int
        :param completed_at: The completed_at of this RunObject.  # noqa: E501
        :type completed_at: int
        :param incomplete_details: The incomplete_details of this RunObject.  # noqa: E501
        :type incomplete_details: RunObjectIncompleteDetails
        :param model: The model of this RunObject.  # noqa: E501
        :type model: str
        :param instructions: The instructions of this RunObject.  # noqa: E501
        :type instructions: str
        :param tools: The tools of this RunObject.  # noqa: E501
        :type tools: List[AssistantObjectToolsInner]
        :param metadata: The metadata of this RunObject.  # noqa: E501
        :type metadata: object
        :param usage: The usage of this RunObject.  # noqa: E501
        :type usage: RunCompletionUsage
        :param temperature: The temperature of this RunObject.  # noqa: E501
        :type temperature: float
        :param top_p: The top_p of this RunObject.  # noqa: E501
        :type top_p: float
        :param max_prompt_tokens: The max_prompt_tokens of this RunObject.  # noqa: E501
        :type max_prompt_tokens: int
        :param max_completion_tokens: The max_completion_tokens of this RunObject.  # noqa: E501
        :type max_completion_tokens: int
        :param truncation_strategy: The truncation_strategy of this RunObject.  # noqa: E501
        :type truncation_strategy: TruncationObject
        :param tool_choice: The tool_choice of this RunObject.  # noqa: E501
        :type tool_choice: AssistantsApiToolChoiceOption
        :param parallel_tool_calls: The parallel_tool_calls of this RunObject.  # noqa: E501
        :type parallel_tool_calls: bool
        :param response_format: The response_format of this RunObject.  # noqa: E501
        :type response_format: AssistantsApiResponseFormatOption
        """
        self.openapi_types = {
            'id': str,
            'object': str,
            'created_at': int,
            'thread_id': str,
            'assistant_id': str,
            'status': str,
            'required_action': RunObjectRequiredAction,
            'last_error': RunObjectLastError,
            'expires_at': int,
            'started_at': int,
            'cancelled_at': int,
            'failed_at': int,
            'completed_at': int,
            'incomplete_details': RunObjectIncompleteDetails,
            'model': str,
            'instructions': str,
            'tools': List[AssistantObjectToolsInner],
            'metadata': object,
            'usage': RunCompletionUsage,
            'temperature': float,
            'top_p': float,
            'max_prompt_tokens': int,
            'max_completion_tokens': int,
            'truncation_strategy': TruncationObject,
            'tool_choice': AssistantsApiToolChoiceOption,
            'parallel_tool_calls': bool,
            'response_format': AssistantsApiResponseFormatOption
        }

        self.attribute_map = {
            'id': 'id',
            'object': 'object',
            'created_at': 'created_at',
            'thread_id': 'thread_id',
            'assistant_id': 'assistant_id',
            'status': 'status',
            'required_action': 'required_action',
            'last_error': 'last_error',
            'expires_at': 'expires_at',
            'started_at': 'started_at',
            'cancelled_at': 'cancelled_at',
            'failed_at': 'failed_at',
            'completed_at': 'completed_at',
            'incomplete_details': 'incomplete_details',
            'model': 'model',
            'instructions': 'instructions',
            'tools': 'tools',
            'metadata': 'metadata',
            'usage': 'usage',
            'temperature': 'temperature',
            'top_p': 'top_p',
            'max_prompt_tokens': 'max_prompt_tokens',
            'max_completion_tokens': 'max_completion_tokens',
            'truncation_strategy': 'truncation_strategy',
            'tool_choice': 'tool_choice',
            'parallel_tool_calls': 'parallel_tool_calls',
            'response_format': 'response_format'
        }

        self._id = id
        self._object = object
        self._created_at = created_at
        self._thread_id = thread_id
        self._assistant_id = assistant_id
        self._status = status
        self._required_action = required_action
        self._last_error = last_error
        self._expires_at = expires_at
        self._started_at = started_at
        self._cancelled_at = cancelled_at
        self._failed_at = failed_at
        self._completed_at = completed_at
        self._incomplete_details = incomplete_details
        self._model = model
        self._instructions = instructions
        self._tools = tools
        self._metadata = metadata
        self._usage = usage
        self._temperature = temperature
        self._top_p = top_p
        self._max_prompt_tokens = max_prompt_tokens
        self._max_completion_tokens = max_completion_tokens
        self._truncation_strategy = truncation_strategy
        self._tool_choice = tool_choice
        self._parallel_tool_calls = parallel_tool_calls
        self._response_format = response_format

    @classmethod
    def from_dict(cls, dikt) -> 'RunObject':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RunObject of this RunObject.  # noqa: E501
        :rtype: RunObject
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this RunObject.

        The identifier, which can be referenced in API endpoints.  # noqa: E501

        :return: The id of this RunObject.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this RunObject.

        The identifier, which can be referenced in API endpoints.  # noqa: E501

        :param id: The id of this RunObject.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def object(self) -> str:
        """Gets the object of this RunObject.

        The object type, which is always `thread.run`.  # noqa: E501

        :return: The object of this RunObject.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object: str):
        """Sets the object of this RunObject.

        The object type, which is always `thread.run`.  # noqa: E501

        :param object: The object of this RunObject.
        :type object: str
        """
        allowed_values = ["thread.run"]  # noqa: E501
        if object not in allowed_values:
            raise ValueError(
                "Invalid value for `object` ({0}), must be one of {1}"
                .format(object, allowed_values)
            )

        self._object = object

    @property
    def created_at(self) -> int:
        """Gets the created_at of this RunObject.

        The Unix timestamp (in seconds) for when the run was created.  # noqa: E501

        :return: The created_at of this RunObject.
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at: int):
        """Sets the created_at of this RunObject.

        The Unix timestamp (in seconds) for when the run was created.  # noqa: E501

        :param created_at: The created_at of this RunObject.
        :type created_at: int
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def thread_id(self) -> str:
        """Gets the thread_id of this RunObject.

        The ID of the [thread](/docs/api-reference/threads) that was executed on as a part of this run.  # noqa: E501

        :return: The thread_id of this RunObject.
        :rtype: str
        """
        return self._thread_id

    @thread_id.setter
    def thread_id(self, thread_id: str):
        """Sets the thread_id of this RunObject.

        The ID of the [thread](/docs/api-reference/threads) that was executed on as a part of this run.  # noqa: E501

        :param thread_id: The thread_id of this RunObject.
        :type thread_id: str
        """
        if thread_id is None:
            raise ValueError("Invalid value for `thread_id`, must not be `None`")  # noqa: E501

        self._thread_id = thread_id

    @property
    def assistant_id(self) -> str:
        """Gets the assistant_id of this RunObject.

        The ID of the [assistant](/docs/api-reference/assistants) used for execution of this run.  # noqa: E501

        :return: The assistant_id of this RunObject.
        :rtype: str
        """
        return self._assistant_id

    @assistant_id.setter
    def assistant_id(self, assistant_id: str):
        """Sets the assistant_id of this RunObject.

        The ID of the [assistant](/docs/api-reference/assistants) used for execution of this run.  # noqa: E501

        :param assistant_id: The assistant_id of this RunObject.
        :type assistant_id: str
        """
        if assistant_id is None:
            raise ValueError("Invalid value for `assistant_id`, must not be `None`")  # noqa: E501

        self._assistant_id = assistant_id

    @property
    def status(self) -> str:
        """Gets the status of this RunObject.

        The status of the run, which can be either `queued`, `in_progress`, `requires_action`, `cancelling`, `cancelled`, `failed`, `completed`, `incomplete`, or `expired`.  # noqa: E501

        :return: The status of this RunObject.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status: str):
        """Sets the status of this RunObject.

        The status of the run, which can be either `queued`, `in_progress`, `requires_action`, `cancelling`, `cancelled`, `failed`, `completed`, `incomplete`, or `expired`.  # noqa: E501

        :param status: The status of this RunObject.
        :type status: str
        """
        allowed_values = ["queued", "in_progress", "requires_action", "cancelling", "cancelled", "failed", "completed", "incomplete", "expired"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def required_action(self) -> RunObjectRequiredAction:
        """Gets the required_action of this RunObject.


        :return: The required_action of this RunObject.
        :rtype: RunObjectRequiredAction
        """
        return self._required_action

    @required_action.setter
    def required_action(self, required_action: RunObjectRequiredAction):
        """Sets the required_action of this RunObject.


        :param required_action: The required_action of this RunObject.
        :type required_action: RunObjectRequiredAction
        """
        if required_action is None:
            raise ValueError("Invalid value for `required_action`, must not be `None`")  # noqa: E501

        self._required_action = required_action

    @property
    def last_error(self) -> RunObjectLastError:
        """Gets the last_error of this RunObject.


        :return: The last_error of this RunObject.
        :rtype: RunObjectLastError
        """
        return self._last_error

    @last_error.setter
    def last_error(self, last_error: RunObjectLastError):
        """Sets the last_error of this RunObject.


        :param last_error: The last_error of this RunObject.
        :type last_error: RunObjectLastError
        """
        if last_error is None:
            raise ValueError("Invalid value for `last_error`, must not be `None`")  # noqa: E501

        self._last_error = last_error

    @property
    def expires_at(self) -> int:
        """Gets the expires_at of this RunObject.

        The Unix timestamp (in seconds) for when the run will expire.  # noqa: E501

        :return: The expires_at of this RunObject.
        :rtype: int
        """
        return self._expires_at

    @expires_at.setter
    def expires_at(self, expires_at: int):
        """Sets the expires_at of this RunObject.

        The Unix timestamp (in seconds) for when the run will expire.  # noqa: E501

        :param expires_at: The expires_at of this RunObject.
        :type expires_at: int
        """
        if expires_at is None:
            raise ValueError("Invalid value for `expires_at`, must not be `None`")  # noqa: E501

        self._expires_at = expires_at

    @property
    def started_at(self) -> int:
        """Gets the started_at of this RunObject.

        The Unix timestamp (in seconds) for when the run was started.  # noqa: E501

        :return: The started_at of this RunObject.
        :rtype: int
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at: int):
        """Sets the started_at of this RunObject.

        The Unix timestamp (in seconds) for when the run was started.  # noqa: E501

        :param started_at: The started_at of this RunObject.
        :type started_at: int
        """
        if started_at is None:
            raise ValueError("Invalid value for `started_at`, must not be `None`")  # noqa: E501

        self._started_at = started_at

    @property
    def cancelled_at(self) -> int:
        """Gets the cancelled_at of this RunObject.

        The Unix timestamp (in seconds) for when the run was cancelled.  # noqa: E501

        :return: The cancelled_at of this RunObject.
        :rtype: int
        """
        return self._cancelled_at

    @cancelled_at.setter
    def cancelled_at(self, cancelled_at: int):
        """Sets the cancelled_at of this RunObject.

        The Unix timestamp (in seconds) for when the run was cancelled.  # noqa: E501

        :param cancelled_at: The cancelled_at of this RunObject.
        :type cancelled_at: int
        """
        if cancelled_at is None:
            raise ValueError("Invalid value for `cancelled_at`, must not be `None`")  # noqa: E501

        self._cancelled_at = cancelled_at

    @property
    def failed_at(self) -> int:
        """Gets the failed_at of this RunObject.

        The Unix timestamp (in seconds) for when the run failed.  # noqa: E501

        :return: The failed_at of this RunObject.
        :rtype: int
        """
        return self._failed_at

    @failed_at.setter
    def failed_at(self, failed_at: int):
        """Sets the failed_at of this RunObject.

        The Unix timestamp (in seconds) for when the run failed.  # noqa: E501

        :param failed_at: The failed_at of this RunObject.
        :type failed_at: int
        """
        if failed_at is None:
            raise ValueError("Invalid value for `failed_at`, must not be `None`")  # noqa: E501

        self._failed_at = failed_at

    @property
    def completed_at(self) -> int:
        """Gets the completed_at of this RunObject.

        The Unix timestamp (in seconds) for when the run was completed.  # noqa: E501

        :return: The completed_at of this RunObject.
        :rtype: int
        """
        return self._completed_at

    @completed_at.setter
    def completed_at(self, completed_at: int):
        """Sets the completed_at of this RunObject.

        The Unix timestamp (in seconds) for when the run was completed.  # noqa: E501

        :param completed_at: The completed_at of this RunObject.
        :type completed_at: int
        """
        if completed_at is None:
            raise ValueError("Invalid value for `completed_at`, must not be `None`")  # noqa: E501

        self._completed_at = completed_at

    @property
    def incomplete_details(self) -> RunObjectIncompleteDetails:
        """Gets the incomplete_details of this RunObject.


        :return: The incomplete_details of this RunObject.
        :rtype: RunObjectIncompleteDetails
        """
        return self._incomplete_details

    @incomplete_details.setter
    def incomplete_details(self, incomplete_details: RunObjectIncompleteDetails):
        """Sets the incomplete_details of this RunObject.


        :param incomplete_details: The incomplete_details of this RunObject.
        :type incomplete_details: RunObjectIncompleteDetails
        """
        if incomplete_details is None:
            raise ValueError("Invalid value for `incomplete_details`, must not be `None`")  # noqa: E501

        self._incomplete_details = incomplete_details

    @property
    def model(self) -> str:
        """Gets the model of this RunObject.

        The model that the [assistant](/docs/api-reference/assistants) used for this run.  # noqa: E501

        :return: The model of this RunObject.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model: str):
        """Sets the model of this RunObject.

        The model that the [assistant](/docs/api-reference/assistants) used for this run.  # noqa: E501

        :param model: The model of this RunObject.
        :type model: str
        """
        if model is None:
            raise ValueError("Invalid value for `model`, must not be `None`")  # noqa: E501

        self._model = model

    @property
    def instructions(self) -> str:
        """Gets the instructions of this RunObject.

        The instructions that the [assistant](/docs/api-reference/assistants) used for this run.  # noqa: E501

        :return: The instructions of this RunObject.
        :rtype: str
        """
        return self._instructions

    @instructions.setter
    def instructions(self, instructions: str):
        """Sets the instructions of this RunObject.

        The instructions that the [assistant](/docs/api-reference/assistants) used for this run.  # noqa: E501

        :param instructions: The instructions of this RunObject.
        :type instructions: str
        """
        if instructions is None:
            raise ValueError("Invalid value for `instructions`, must not be `None`")  # noqa: E501

        self._instructions = instructions

    @property
    def tools(self) -> List[AssistantObjectToolsInner]:
        """Gets the tools of this RunObject.

        The list of tools that the [assistant](/docs/api-reference/assistants) used for this run.  # noqa: E501

        :return: The tools of this RunObject.
        :rtype: List[AssistantObjectToolsInner]
        """
        return self._tools

    @tools.setter
    def tools(self, tools: List[AssistantObjectToolsInner]):
        """Sets the tools of this RunObject.

        The list of tools that the [assistant](/docs/api-reference/assistants) used for this run.  # noqa: E501

        :param tools: The tools of this RunObject.
        :type tools: List[AssistantObjectToolsInner]
        """
        if tools is None:
            raise ValueError("Invalid value for `tools`, must not be `None`")  # noqa: E501
        if tools is not None and len(tools) > 20:
            raise ValueError("Invalid value for `tools`, number of items must be less than or equal to `20`")  # noqa: E501

        self._tools = tools

    @property
    def metadata(self) -> object:
        """Gets the metadata of this RunObject.

        Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.   # noqa: E501

        :return: The metadata of this RunObject.
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata: object):
        """Sets the metadata of this RunObject.

        Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.   # noqa: E501

        :param metadata: The metadata of this RunObject.
        :type metadata: object
        """
        if metadata is None:
            raise ValueError("Invalid value for `metadata`, must not be `None`")  # noqa: E501

        self._metadata = metadata

    @property
    def usage(self) -> RunCompletionUsage:
        """Gets the usage of this RunObject.


        :return: The usage of this RunObject.
        :rtype: RunCompletionUsage
        """
        return self._usage

    @usage.setter
    def usage(self, usage: RunCompletionUsage):
        """Sets the usage of this RunObject.


        :param usage: The usage of this RunObject.
        :type usage: RunCompletionUsage
        """
        if usage is None:
            raise ValueError("Invalid value for `usage`, must not be `None`")  # noqa: E501

        self._usage = usage

    @property
    def temperature(self) -> float:
        """Gets the temperature of this RunObject.

        The sampling temperature used for this run. If not set, defaults to 1.  # noqa: E501

        :return: The temperature of this RunObject.
        :rtype: float
        """
        return self._temperature

    @temperature.setter
    def temperature(self, temperature: float):
        """Sets the temperature of this RunObject.

        The sampling temperature used for this run. If not set, defaults to 1.  # noqa: E501

        :param temperature: The temperature of this RunObject.
        :type temperature: float
        """

        self._temperature = temperature

    @property
    def top_p(self) -> float:
        """Gets the top_p of this RunObject.

        The nucleus sampling value used for this run. If not set, defaults to 1.  # noqa: E501

        :return: The top_p of this RunObject.
        :rtype: float
        """
        return self._top_p

    @top_p.setter
    def top_p(self, top_p: float):
        """Sets the top_p of this RunObject.

        The nucleus sampling value used for this run. If not set, defaults to 1.  # noqa: E501

        :param top_p: The top_p of this RunObject.
        :type top_p: float
        """

        self._top_p = top_p

    @property
    def max_prompt_tokens(self) -> int:
        """Gets the max_prompt_tokens of this RunObject.

        The maximum number of prompt tokens specified to have been used over the course of the run.   # noqa: E501

        :return: The max_prompt_tokens of this RunObject.
        :rtype: int
        """
        return self._max_prompt_tokens

    @max_prompt_tokens.setter
    def max_prompt_tokens(self, max_prompt_tokens: int):
        """Sets the max_prompt_tokens of this RunObject.

        The maximum number of prompt tokens specified to have been used over the course of the run.   # noqa: E501

        :param max_prompt_tokens: The max_prompt_tokens of this RunObject.
        :type max_prompt_tokens: int
        """
        if max_prompt_tokens is None:
            raise ValueError("Invalid value for `max_prompt_tokens`, must not be `None`")  # noqa: E501
        if max_prompt_tokens is not None and max_prompt_tokens < 256:  # noqa: E501
            raise ValueError("Invalid value for `max_prompt_tokens`, must be a value greater than or equal to `256`")  # noqa: E501

        self._max_prompt_tokens = max_prompt_tokens

    @property
    def max_completion_tokens(self) -> int:
        """Gets the max_completion_tokens of this RunObject.

        The maximum number of completion tokens specified to have been used over the course of the run.   # noqa: E501

        :return: The max_completion_tokens of this RunObject.
        :rtype: int
        """
        return self._max_completion_tokens

    @max_completion_tokens.setter
    def max_completion_tokens(self, max_completion_tokens: int):
        """Sets the max_completion_tokens of this RunObject.

        The maximum number of completion tokens specified to have been used over the course of the run.   # noqa: E501

        :param max_completion_tokens: The max_completion_tokens of this RunObject.
        :type max_completion_tokens: int
        """
        if max_completion_tokens is None:
            raise ValueError("Invalid value for `max_completion_tokens`, must not be `None`")  # noqa: E501
        if max_completion_tokens is not None and max_completion_tokens < 256:  # noqa: E501
            raise ValueError("Invalid value for `max_completion_tokens`, must be a value greater than or equal to `256`")  # noqa: E501

        self._max_completion_tokens = max_completion_tokens

    @property
    def truncation_strategy(self) -> TruncationObject:
        """Gets the truncation_strategy of this RunObject.


        :return: The truncation_strategy of this RunObject.
        :rtype: TruncationObject
        """
        return self._truncation_strategy

    @truncation_strategy.setter
    def truncation_strategy(self, truncation_strategy: TruncationObject):
        """Sets the truncation_strategy of this RunObject.


        :param truncation_strategy: The truncation_strategy of this RunObject.
        :type truncation_strategy: TruncationObject
        """
        if truncation_strategy is None:
            raise ValueError("Invalid value for `truncation_strategy`, must not be `None`")  # noqa: E501

        self._truncation_strategy = truncation_strategy

    @property
    def tool_choice(self) -> AssistantsApiToolChoiceOption:
        """Gets the tool_choice of this RunObject.


        :return: The tool_choice of this RunObject.
        :rtype: AssistantsApiToolChoiceOption
        """
        return self._tool_choice

    @tool_choice.setter
    def tool_choice(self, tool_choice: AssistantsApiToolChoiceOption):
        """Sets the tool_choice of this RunObject.


        :param tool_choice: The tool_choice of this RunObject.
        :type tool_choice: AssistantsApiToolChoiceOption
        """
        if tool_choice is None:
            raise ValueError("Invalid value for `tool_choice`, must not be `None`")  # noqa: E501

        self._tool_choice = tool_choice

    @property
    def parallel_tool_calls(self) -> bool:
        """Gets the parallel_tool_calls of this RunObject.

        Whether to enable [parallel function calling](/docs/guides/function-calling/parallel-function-calling) during tool use.  # noqa: E501

        :return: The parallel_tool_calls of this RunObject.
        :rtype: bool
        """
        return self._parallel_tool_calls

    @parallel_tool_calls.setter
    def parallel_tool_calls(self, parallel_tool_calls: bool):
        """Sets the parallel_tool_calls of this RunObject.

        Whether to enable [parallel function calling](/docs/guides/function-calling/parallel-function-calling) during tool use.  # noqa: E501

        :param parallel_tool_calls: The parallel_tool_calls of this RunObject.
        :type parallel_tool_calls: bool
        """
        if parallel_tool_calls is None:
            raise ValueError("Invalid value for `parallel_tool_calls`, must not be `None`")  # noqa: E501

        self._parallel_tool_calls = parallel_tool_calls

    @property
    def response_format(self) -> AssistantsApiResponseFormatOption:
        """Gets the response_format of this RunObject.


        :return: The response_format of this RunObject.
        :rtype: AssistantsApiResponseFormatOption
        """
        return self._response_format

    @response_format.setter
    def response_format(self, response_format: AssistantsApiResponseFormatOption):
        """Sets the response_format of this RunObject.


        :param response_format: The response_format of this RunObject.
        :type response_format: AssistantsApiResponseFormatOption
        """
        if response_format is None:
            raise ValueError("Invalid value for `response_format`, must not be `None`")  # noqa: E501

        self._response_format = response_format
