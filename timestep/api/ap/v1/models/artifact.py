from datetime import date, datetime  # noqa: F401
from typing import Dict, List  # noqa: F401

from timestep.api.ap.v1 import util
from timestep.api.ap.v1.models.base_model import Model


class Artifact(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(
        self, artifact_id=None, agent_created=None, file_name=None, relative_path=None
    ):  # noqa: E501
        """Artifact - a model defined in OpenAPI

        :param artifact_id: The artifact_id of this Artifact.  # noqa: E501
        :type artifact_id: str
        :param agent_created: The agent_created of this Artifact.  # noqa: E501
        :type agent_created: bool
        :param file_name: The file_name of this Artifact.  # noqa: E501
        :type file_name: str
        :param relative_path: The relative_path of this Artifact.  # noqa: E501
        :type relative_path: str
        """
        self.openapi_types = {
            "artifact_id": str,
            "agent_created": bool,
            "file_name": str,
            "relative_path": str,
        }

        self.attribute_map = {
            "artifact_id": "artifact_id",
            "agent_created": "agent_created",
            "file_name": "file_name",
            "relative_path": "relative_path",
        }

        self._artifact_id = artifact_id
        self._agent_created = agent_created
        self._file_name = file_name
        self._relative_path = relative_path

    @classmethod
    def from_dict(cls, dikt) -> "Artifact":
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Artifact of this Artifact.  # noqa: E501
        :rtype: Artifact
        """
        return util.deserialize_model(dikt, cls)

    @property
    def artifact_id(self) -> str:
        """Gets the artifact_id of this Artifact.

        ID of the artifact.  # noqa: E501

        :return: The artifact_id of this Artifact.
        :rtype: str
        """
        return self._artifact_id

    @artifact_id.setter
    def artifact_id(self, artifact_id: str):
        """Sets the artifact_id of this Artifact.

        ID of the artifact.  # noqa: E501

        :param artifact_id: The artifact_id of this Artifact.
        :type artifact_id: str
        """
        if artifact_id is None:
            raise ValueError(
                "Invalid value for `artifact_id`, must not be `None`"
            )  # noqa: E501

        self._artifact_id = artifact_id

    @property
    def agent_created(self) -> bool:
        """Gets the agent_created of this Artifact.

        Whether the artifact has been created by the agent.  # noqa: E501

        :return: The agent_created of this Artifact.
        :rtype: bool
        """
        return self._agent_created

    @agent_created.setter
    def agent_created(self, agent_created: bool):
        """Sets the agent_created of this Artifact.

        Whether the artifact has been created by the agent.  # noqa: E501

        :param agent_created: The agent_created of this Artifact.
        :type agent_created: bool
        """
        if agent_created is None:
            raise ValueError(
                "Invalid value for `agent_created`, must not be `None`"
            )  # noqa: E501

        self._agent_created = agent_created

    @property
    def file_name(self) -> str:
        """Gets the file_name of this Artifact.

        Filename of the artifact.  # noqa: E501

        :return: The file_name of this Artifact.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name: str):
        """Sets the file_name of this Artifact.

        Filename of the artifact.  # noqa: E501

        :param file_name: The file_name of this Artifact.
        :type file_name: str
        """
        if file_name is None:
            raise ValueError(
                "Invalid value for `file_name`, must not be `None`"
            )  # noqa: E501

        self._file_name = file_name

    @property
    def relative_path(self) -> str:
        """Gets the relative_path of this Artifact.

        Relative path of the artifact in the agent's workspace.  # noqa: E501

        :return: The relative_path of this Artifact.
        :rtype: str
        """
        return self._relative_path

    @relative_path.setter
    def relative_path(self, relative_path: str):
        """Sets the relative_path of this Artifact.

        Relative path of the artifact in the agent's workspace.  # noqa: E501

        :param relative_path: The relative_path of this Artifact.
        :type relative_path: str
        """

        self._relative_path = relative_path
