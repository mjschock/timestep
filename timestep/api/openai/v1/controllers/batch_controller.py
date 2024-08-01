import connexion

from timestep.api.openai.v1.models.create_batch_request import (  # noqa: E501
    CreateBatchRequest,
)


def cancel_batch(batch_id):  # noqa: E501
    """Cancels an in-progress batch. The batch will be in status &#x60;cancelling&#x60; for up to 10 minutes, before changing to &#x60;cancelled&#x60;, where it will have partial results (if any) available in the output file.

     # noqa: E501

    :param batch_id: The ID of the batch to cancel.
    :type batch_id: str

    :rtype: Union[Batch, Tuple[Batch, int], Tuple[Batch, int, Dict[str, str]]
    """
    raise NotImplementedError


def create_batch(create_batch_request):  # noqa: E501
    """Creates and executes a batch from an uploaded file of requests

     # noqa: E501

    :param create_batch_request:
    :type create_batch_request: dict | bytes

    :rtype: Union[Batch, Tuple[Batch, int], Tuple[Batch, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        create_batch_request = CreateBatchRequest.from_dict(
            connexion.request.get_json()
        )  # noqa: E501
    raise NotImplementedError


def list_batches(after=None, limit=None):  # noqa: E501
    """List your organization&#39;s batches.

     # noqa: E501

    :param after: A cursor for use in pagination. &#x60;after&#x60; is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after&#x3D;obj_foo in order to fetch the next page of the list.
    :type after: str
    :param limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.
    :type limit: int

    :rtype: Union[ListBatchesResponse, Tuple[ListBatchesResponse, int], Tuple[ListBatchesResponse, int, Dict[str, str]]
    """
    raise NotImplementedError


def retrieve_batch(batch_id):  # noqa: E501
    """Retrieves a batch.

     # noqa: E501

    :param batch_id: The ID of the batch to retrieve.
    :type batch_id: str

    :rtype: Union[Batch, Tuple[Batch, int], Tuple[Batch, int, Dict[str, str]]
    """
    raise NotImplementedError
