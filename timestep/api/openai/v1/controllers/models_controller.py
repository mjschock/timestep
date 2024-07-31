from typing import Dict, Tuple, Union

import connexion
from openai.types.model import Model

from timestep.api.openai.v1 import util
from timestep.api.openai.v1.models.delete_model_response import (  # noqa: E501
    DeleteModelResponse,
)
from timestep.api.openai.v1.models.list_models_response import (  # noqa: E501
    ListModelsResponse,
)
from timestep.api.openai.v1.models.model import Model  # noqa: E501
from timestep.services import model_service


def delete_model(model):  # noqa: E501
    """Delete a fine-tuned model. You must have the Owner role in your organization to delete a model.

     # noqa: E501

    :param model: The model to delete
    :type model: str

    :rtype: Union[DeleteModelResponse, Tuple[DeleteModelResponse, int], Tuple[DeleteModelResponse, int, Dict[str, str]]
    """
    raise NotImplementedError


def list_models():  # noqa: E501
    """Lists the currently available models, and provides basic information about each one such as the owner and availability.

     # noqa: E501


    :rtype: Union[ListModelsResponse, Tuple[ListModelsResponse, int], Tuple[ListModelsResponse, int, Dict[str, str]]
    """
    raise NotImplementedError


def retrieve_model(model: str, token_info: dict, user: str):
    """Retrieves a model instance, providing basic information about the model such as the owner and permissioning.

     # noqa: E501

    :param model: The ID of the model to use for this request
    :type model: str

    :rtype: Union[Model, Tuple[Model, int], Tuple[Model, int, Dict[str, str]]
    """
    # print('args: ', args)
    # print('kwargs: ', kwargs)

    model_info = model_service.retrieve_model(model_id=model)

    print("model_info: ", model_info)

    return Model(
        id=model,
        created=0,
        object="model",
        owned_by=user,
    ).model_dump(mode="json")
