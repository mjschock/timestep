from fastapi import APIRouter, Depends, Request

from backend.services.vector_stores_service import VectorStoresService

vector_stores_router = APIRouter()


@vector_stores_router.get("/vector_stores")
def list_vector_stores(
    limit: str | None = None,
    order: str | None = None,
    after: str | None = None,
    before: str | None = None,
    request: Request = None,
    service: VectorStoresService = Depends(VectorStoresService),  # noqa: B008
):
    """Returns a list of vector stores."""
    # Convert string parameters to appropriate types
    limit_int = int(limit) if limit else 20
    order_str = order if order else "desc"

    return service.list_vector_stores(
        limit=limit_int,
        order=order_str,
        after=after,
        before=before,
    )


@vector_stores_router.post("/vector_stores")
async def create_vector_store(
    request: Request,
    service: VectorStoresService = Depends(VectorStoresService),  # noqa: B008
):
    """Create a vector store."""
    body = await request.json()
    name = body.get("name")
    metadata = body.get("metadata")

    return service.create_vector_store(name=name, metadata=metadata)


@vector_stores_router.get("/vector_stores/{vector_store_id}")
def get_vector_store(
    vector_store_id: str,
    request: Request = None,
    service: VectorStoresService = Depends(VectorStoresService),  # noqa: B008
):
    """Retrieves a vector store."""
    return service.get_vector_store(vector_store_id=vector_store_id)


@vector_stores_router.post("/vector_stores/{vector_store_id}")
async def modify_vector_store(
    vector_store_id: str,
    request: Request,
    service: VectorStoresService = Depends(VectorStoresService),  # noqa: B008
):
    """Modifies a vector store."""
    body = await request.json()
    name = body.get("name")
    metadata = body.get("metadata")

    return service.modify_vector_store(
        vector_store_id=vector_store_id,
        name=name,
        metadata=metadata,
    )


@vector_stores_router.delete("/vector_stores/{vector_store_id}")
def delete_vector_store(
    vector_store_id: str,
    request: Request = None,
    service: VectorStoresService = Depends(VectorStoresService),  # noqa: B008
):
    """Delete a vector store."""
    return service.delete_vector_store(vector_store_id=vector_store_id)


@vector_stores_router.post("/vector_stores/{vector_store_id}/file_batches")
async def create_vector_store_file_batch(
    vector_store_id: str,
    request: Request,
    service: VectorStoresService = Depends(VectorStoresService),  # noqa: B008
):
    """Create a vector store file batch."""
    body = await request.json()
    file_ids = body.get("file_ids", [])

    return service.create_vector_store_file_batch(
        vector_store_id=vector_store_id,
        file_ids=file_ids,
    )


@vector_stores_router.get("/vector_stores/{vector_store_id}/file_batches/{batch_id}")
def get_vector_store_file_batch(
    vector_store_id: str,
    batch_id: str,
    request: Request = None,
    service: VectorStoresService = Depends(VectorStoresService),  # noqa: B008
):
    """Retrieves a vector store file batch."""
    return service.get_vector_store_file_batch(
        vector_store_id=vector_store_id,
        batch_id=batch_id,
    )


@vector_stores_router.post(
    "/vector_stores/{vector_store_id}/file_batches/{batch_id}/cancel",
)
def cancel_vector_store_file_batch(
    vector_store_id: str,
    batch_id: str,
    request: Request = None,
    service: VectorStoresService = Depends(VectorStoresService),  # noqa: B008
):
    """
    Cancel a vector store file batch. This attempts to cancel the processing of files in this batch as soon as possible.
    """
    return service.cancel_vector_store_file_batch(
        vector_store_id=vector_store_id,
        batch_id=batch_id,
    )


@vector_stores_router.get(
    "/vector_stores/{vector_store_id}/file_batches/{batch_id}/files",
)
def list_files_in_vector_store_batch(
    vector_store_id: str,
    batch_id: str,
    limit: str | None = None,
    order: str | None = None,
    after: str | None = None,
    before: str | None = None,
    filter: str | None = None,
    request: Request = None,
    service: VectorStoresService = Depends(VectorStoresService),  # noqa: B008
):
    """Returns a list of vector store files in a batch."""
    # Convert string parameters to appropriate types
    limit_int = int(limit) if limit else 20
    order_str = order if order else "desc"

    return service.list_files_in_vector_store_batch(
        vector_store_id=vector_store_id,
        batch_id=batch_id,
        limit=limit_int,
        order=order_str,
        after=after,
        before=before,
        filter=filter,
    )


@vector_stores_router.get("/vector_stores/{vector_store_id}/files")
def list_vector_store_files(
    vector_store_id: str,
    limit: str | None = None,
    order: str | None = None,
    after: str | None = None,
    before: str | None = None,
    filter: str | None = None,
    request: Request = None,
    service: VectorStoresService = Depends(VectorStoresService),  # noqa: B008
):
    """Returns a list of vector store files."""
    # Convert string parameters to appropriate types
    limit_int = int(limit) if limit else 20
    order_str = order if order else "desc"

    return service.list_vector_store_files(
        vector_store_id=vector_store_id,
        limit=limit_int,
        order=order_str,
        after=after,
        before=before,
        filter=filter,
    )


@vector_stores_router.post("/vector_stores/{vector_store_id}/files")
async def create_vector_store_file(
    vector_store_id: str,
    request: Request,
    service: VectorStoresService = Depends(VectorStoresService),  # noqa: B008
):
    """
    Create a vector store file by attaching a [File](/docs/api-reference/files) to a [vector store](/docs/api-reference/vector-stores/object).
    """
    body = await request.json()
    file_id = body.get("file_id")

    return service.create_vector_store_file(
        vector_store_id=vector_store_id,
        file_id=file_id,
    )


@vector_stores_router.get("/vector_stores/{vector_store_id}/files/{file_id}")
def get_vector_store_file(
    vector_store_id: str,
    file_id: str,
    request: Request = None,
    service: VectorStoresService = Depends(VectorStoresService),  # noqa: B008
):
    """Retrieves a vector store file."""
    return service.get_vector_store_file(
        vector_store_id=vector_store_id,
        file_id=file_id,
    )


@vector_stores_router.delete("/vector_stores/{vector_store_id}/files/{file_id}")
def delete_vector_store_file(
    vector_store_id: str,
    file_id: str,
    request: Request = None,
    service: VectorStoresService = Depends(VectorStoresService),  # noqa: B008
):
    """
    Delete a vector store file. This will remove the file from the vector store but the file itself will not be deleted. To delete the file, use the [delete file](/docs/api-reference/files/delete) endpoint.
    """
    return service.delete_vector_store_file(
        vector_store_id=vector_store_id,
        file_id=file_id,
    )


@vector_stores_router.post("/vector_stores/{vector_store_id}/files/{file_id}")
async def update_vector_store_file_attributes(
    vector_store_id: str,
    file_id: str,
    request: Request,
    service: VectorStoresService = Depends(VectorStoresService),  # noqa: B008
):
    """Update attributes on a vector store file."""
    body = await request.json()
    metadata = body.get("metadata")

    return service.update_vector_store_file_attributes(
        vector_store_id=vector_store_id,
        file_id=file_id,
        metadata=metadata,
    )


@vector_stores_router.get("/vector_stores/{vector_store_id}/files/{file_id}/content")
def retrieve_vector_store_file_content(
    vector_store_id: str,
    file_id: str,
    request: Request = None,
    service: VectorStoresService = Depends(VectorStoresService),  # noqa: B008
):
    """Retrieve the parsed contents of a vector store file."""
    return service.retrieve_vector_store_file_content(
        vector_store_id=vector_store_id,
        file_id=file_id,
    )


@vector_stores_router.post("/vector_stores/{vector_store_id}/search")
async def search_vector_store(
    vector_store_id: str,
    request: Request,
    service: VectorStoresService = Depends(VectorStoresService),  # noqa: B008
):
    """
    Search a vector store for relevant chunks based on a query and file attributes filter.
    """
    body = await request.json()
    query = body.get("query")
    k = body.get("k", 10)

    return service.search_vector_store(
        vector_store_id=vector_store_id,
        query=query,
        k=k,
    )
