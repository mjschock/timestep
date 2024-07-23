from datetime import date, datetime  # noqa: F401
from typing import Dict, List  # noqa: F401

from timestep.api.openai.v1 import util
from timestep.api.openai.v1.models.base_model import Model
from timestep.api.openai.v1.models.modify_assistant_request_tool_resources_code_interpreter import \
    ModifyAssistantRequestToolResourcesCodeInterpreter  # noqa: E501
from timestep.api.openai.v1.models.modify_assistant_request_tool_resources_file_search import \
    ModifyAssistantRequestToolResourcesFileSearch  # noqa: E501


class ModifyAssistantRequestToolResources(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, code_interpreter=None, file_search=None):  # noqa: E501
        """ModifyAssistantRequestToolResources - a model defined in OpenAPI

        :param code_interpreter: The code_interpreter of this ModifyAssistantRequestToolResources.  # noqa: E501
        :type code_interpreter: ModifyAssistantRequestToolResourcesCodeInterpreter
        :param file_search: The file_search of this ModifyAssistantRequestToolResources.  # noqa: E501
        :type file_search: ModifyAssistantRequestToolResourcesFileSearch
        """
        self.openapi_types = {
            'code_interpreter': ModifyAssistantRequestToolResourcesCodeInterpreter,
            'file_search': ModifyAssistantRequestToolResourcesFileSearch
        }

        self.attribute_map = {
            'code_interpreter': 'code_interpreter',
            'file_search': 'file_search'
        }

        self._code_interpreter = code_interpreter
        self._file_search = file_search

    @classmethod
    def from_dict(cls, dikt) -> 'ModifyAssistantRequestToolResources':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ModifyAssistantRequest_tool_resources of this ModifyAssistantRequestToolResources.  # noqa: E501
        :rtype: ModifyAssistantRequestToolResources
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code_interpreter(self) -> ModifyAssistantRequestToolResourcesCodeInterpreter:
        """Gets the code_interpreter of this ModifyAssistantRequestToolResources.


        :return: The code_interpreter of this ModifyAssistantRequestToolResources.
        :rtype: ModifyAssistantRequestToolResourcesCodeInterpreter
        """
        return self._code_interpreter

    @code_interpreter.setter
    def code_interpreter(self, code_interpreter: ModifyAssistantRequestToolResourcesCodeInterpreter):
        """Sets the code_interpreter of this ModifyAssistantRequestToolResources.


        :param code_interpreter: The code_interpreter of this ModifyAssistantRequestToolResources.
        :type code_interpreter: ModifyAssistantRequestToolResourcesCodeInterpreter
        """

        self._code_interpreter = code_interpreter

    @property
    def file_search(self) -> ModifyAssistantRequestToolResourcesFileSearch:
        """Gets the file_search of this ModifyAssistantRequestToolResources.


        :return: The file_search of this ModifyAssistantRequestToolResources.
        :rtype: ModifyAssistantRequestToolResourcesFileSearch
        """
        return self._file_search

    @file_search.setter
    def file_search(self, file_search: ModifyAssistantRequestToolResourcesFileSearch):
        """Sets the file_search of this ModifyAssistantRequestToolResources.


        :param file_search: The file_search of this ModifyAssistantRequestToolResources.
        :type file_search: ModifyAssistantRequestToolResourcesFileSearch
        """

        self._file_search = file_search