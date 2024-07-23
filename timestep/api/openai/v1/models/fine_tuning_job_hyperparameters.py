from datetime import date, datetime  # noqa: F401
from typing import Dict, List  # noqa: F401

from timestep.api.openai.v1 import util
from timestep.api.openai.v1.models.base_model import Model
from timestep.api.openai.v1.models.fine_tuning_job_hyperparameters_n_epochs import \
    FineTuningJobHyperparametersNEpochs  # noqa: E501


class FineTuningJobHyperparameters(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, n_epochs=None):  # noqa: E501
        """FineTuningJobHyperparameters - a model defined in OpenAPI

        :param n_epochs: The n_epochs of this FineTuningJobHyperparameters.  # noqa: E501
        :type n_epochs: FineTuningJobHyperparametersNEpochs
        """
        self.openapi_types = {
            'n_epochs': FineTuningJobHyperparametersNEpochs
        }

        self.attribute_map = {
            'n_epochs': 'n_epochs'
        }

        self._n_epochs = n_epochs

    @classmethod
    def from_dict(cls, dikt) -> 'FineTuningJobHyperparameters':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The FineTuningJob_hyperparameters of this FineTuningJobHyperparameters.  # noqa: E501
        :rtype: FineTuningJobHyperparameters
        """
        return util.deserialize_model(dikt, cls)

    @property
    def n_epochs(self) -> FineTuningJobHyperparametersNEpochs:
        """Gets the n_epochs of this FineTuningJobHyperparameters.


        :return: The n_epochs of this FineTuningJobHyperparameters.
        :rtype: FineTuningJobHyperparametersNEpochs
        """
        return self._n_epochs

    @n_epochs.setter
    def n_epochs(self, n_epochs: FineTuningJobHyperparametersNEpochs):
        """Sets the n_epochs of this FineTuningJobHyperparameters.


        :param n_epochs: The n_epochs of this FineTuningJobHyperparameters.
        :type n_epochs: FineTuningJobHyperparametersNEpochs
        """
        if n_epochs is None:
            raise ValueError("Invalid value for `n_epochs`, must not be `None`")  # noqa: E501

        self._n_epochs = n_epochs