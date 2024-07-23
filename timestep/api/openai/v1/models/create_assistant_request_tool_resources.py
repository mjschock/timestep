from datetime import date, datetime  # noqa: F401
from typing import Dict, List  # noqa: F401

from timestep.api.openai.v1 import util
from timestep.api.openai.v1.models.base_model import Model
from timestep.api.openai.v1.models.create_assistant_request_tool_resources_code_interpreter import \
    CreateAssistantRequestToolResourcesCodeInterpreter  # noqa: E501
from timestep.api.openai.v1.models.create_assistant_request_tool_resources_file_search import \
    CreateAssistantRequestToolResourcesFileSearch  # noqa: E501


class CreateAssistantRequestToolResources(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, code_interpreter=None, file_search=None):  # noqa: E501
        """CreateAssistantRequestToolResources - a model defined in OpenAPI

        :param code_interpreter: The code_interpreter of this CreateAssistantRequestToolResources.  # noqa: E501
        :type code_interpreter: CreateAssistantRequestToolResourcesCodeInterpreter
        :param file_search: The file_search of this CreateAssistantRequestToolResources.  # noqa: E501
        :type file_search: CreateAssistantRequestToolResourcesFileSearch
        """
        self.openapi_types = {
            'code_interpreter': CreateAssistantRequestToolResourcesCodeInterpreter,
            'file_search': CreateAssistantRequestToolResourcesFileSearch
        }

        self.attribute_map = {
            'code_interpreter': 'code_interpreter',
            'file_search': 'file_search'
        }

        self._code_interpreter = code_interpreter
        self._file_search = file_search

    @classmethod
    def from_dict(cls, dikt) -> 'CreateAssistantRequestToolResources':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CreateAssistantRequest_tool_resources of this CreateAssistantRequestToolResources.  # noqa: E501
        :rtype: CreateAssistantRequestToolResources
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code_interpreter(self) -> CreateAssistantRequestToolResourcesCodeInterpreter:
        """Gets the code_interpreter of this CreateAssistantRequestToolResources.


        :return: The code_interpreter of this CreateAssistantRequestToolResources.
        :rtype: CreateAssistantRequestToolResourcesCodeInterpreter
        """
        return self._code_interpreter

    @code_interpreter.setter
    def code_interpreter(self, code_interpreter: CreateAssistantRequestToolResourcesCodeInterpreter):
        """Sets the code_interpreter of this CreateAssistantRequestToolResources.


        :param code_interpreter: The code_interpreter of this CreateAssistantRequestToolResources.
        :type code_interpreter: CreateAssistantRequestToolResourcesCodeInterpreter
        """

        self._code_interpreter = code_interpreter

    @property
    def file_search(self) -> CreateAssistantRequestToolResourcesFileSearch:
        """Gets the file_search of this CreateAssistantRequestToolResources.


        :return: The file_search of this CreateAssistantRequestToolResources.
        :rtype: CreateAssistantRequestToolResourcesFileSearch
        """
        return self._file_search

    @file_search.setter
    def file_search(self, file_search: CreateAssistantRequestToolResourcesFileSearch):
        """Sets the file_search of this CreateAssistantRequestToolResources.


        :param file_search: The file_search of this CreateAssistantRequestToolResources.
        :type file_search: CreateAssistantRequestToolResourcesFileSearch
        """

        self._file_search = file_search