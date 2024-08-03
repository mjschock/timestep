async def cancel_batch(batch_id):
    """Cancels an in-progress batch. The batch will be in status &#x60;cancelling&#x60; for up to 10 minutes, before changing to &#x60;cancelled&#x60;, where it will have partial results (if any) available in the output file.

    :param batch_id: The ID of the batch to cancel.
    :type batch_id: str

    :rtype: Union[Batch, Tuple[Batch, int], Tuple[Batch, int, Dict[str, str]]
    """
    raise NotImplementedError


async def create_batch(create_batch_request):
    """Creates and executes a batch from an uploaded file of requests

    :param create_batch_request:
    :type create_batch_request: dict | bytes

    :rtype: Union[Batch, Tuple[Batch, int], Tuple[Batch, int, Dict[str, str]]
    """
    raise NotImplementedError


async def list_batches(after=None, limit=None):
    """List your organization&#39;s batches.

    :param after: A cursor for use in pagination. &#x60;after&#x60; is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after&#x3D;obj_foo in order to fetch the next page of the list.
    :type after: str
    :param limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.
    :type limit: int

    :rtype: Union[ListBatchesResponse, Tuple[ListBatchesResponse, int], Tuple[ListBatchesResponse, int, Dict[str, str]]
    """
    raise NotImplementedError


async def retrieve_batch(batch_id):
    """Retrieves a batch.

    :param batch_id: The ID of the batch to retrieve.
    :type batch_id: str

    :rtype: Union[Batch, Tuple[Batch, int], Tuple[Batch, int, Dict[str, str]]
    """
    raise NotImplementedError
