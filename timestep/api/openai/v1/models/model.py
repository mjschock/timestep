from datetime import date, datetime  # noqa: F401
from typing import Dict, List  # noqa: F401

from timestep.api.openai.v1 import util
from timestep.api.openai.v1.models.base_model import Model


class Model(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, created=None, object=None, owned_by=None):  # noqa: E501
        """Model - a model defined in OpenAPI

        :param id: The id of this Model.  # noqa: E501
        :type id: str
        :param created: The created of this Model.  # noqa: E501
        :type created: int
        :param object: The object of this Model.  # noqa: E501
        :type object: str
        :param owned_by: The owned_by of this Model.  # noqa: E501
        :type owned_by: str
        """
        self.openapi_types = {
            'id': str,
            'created': int,
            'object': str,
            'owned_by': str
        }

        self.attribute_map = {
            'id': 'id',
            'created': 'created',
            'object': 'object',
            'owned_by': 'owned_by'
        }

        self._id = id
        self._created = created
        self._object = object
        self._owned_by = owned_by

    @classmethod
    def from_dict(cls, dikt) -> 'Model':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Model of this Model.  # noqa: E501
        :rtype: Model
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this Model.

        The model identifier, which can be referenced in the API endpoints.  # noqa: E501

        :return: The id of this Model.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this Model.

        The model identifier, which can be referenced in the API endpoints.  # noqa: E501

        :param id: The id of this Model.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created(self) -> int:
        """Gets the created of this Model.

        The Unix timestamp (in seconds) when the model was created.  # noqa: E501

        :return: The created of this Model.
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created: int):
        """Sets the created of this Model.

        The Unix timestamp (in seconds) when the model was created.  # noqa: E501

        :param created: The created of this Model.
        :type created: int
        """
        if created is None:
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def object(self) -> str:
        """Gets the object of this Model.

        The object type, which is always \"model\".  # noqa: E501

        :return: The object of this Model.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object: str):
        """Sets the object of this Model.

        The object type, which is always \"model\".  # noqa: E501

        :param object: The object of this Model.
        :type object: str
        """
        allowed_values = ["model"]  # noqa: E501
        if object not in allowed_values:
            raise ValueError(
                "Invalid value for `object` ({0}), must be one of {1}"
                .format(object, allowed_values)
            )

        self._object = object

    @property
    def owned_by(self) -> str:
        """Gets the owned_by of this Model.

        The organization that owns the model.  # noqa: E501

        :return: The owned_by of this Model.
        :rtype: str
        """
        return self._owned_by

    @owned_by.setter
    def owned_by(self, owned_by: str):
        """Sets the owned_by of this Model.

        The organization that owns the model.  # noqa: E501

        :param owned_by: The owned_by of this Model.
        :type owned_by: str
        """
        if owned_by is None:
            raise ValueError("Invalid value for `owned_by`, must not be `None`")  # noqa: E501

        self._owned_by = owned_by