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

    # model_info = model_service.retrieve_model(model_id=model)

    # print("model_info: ", model_info)

    # return Model(
    #     id=model,
    #     created=0,
    #     object="model",
    #     owned_by=user,
    # ).model_dump(mode="json")

    raise NotImplementedError
