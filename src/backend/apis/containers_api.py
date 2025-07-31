from fastapi import APIRouter, Depends, Request

from backend.services.containers_service import ContainersService

containers_router = APIRouter()


@containers_router.get("/containers")
def list_containers(
    limit: str,
    order: str,
    after: str,
    request: Request,
    service: ContainersService = Depends(),  # noqa: B008
) -> None:
    """List Containers"""
    return service.list_containers(
        limit=int(limit) if limit else None, order=order, after=after
    )


@containers_router.post("/containers")
def create_container(request: Request, service: ContainersService = Depends()) -> None:  # noqa: B008
    """Create Container"""
    return service.create_container()


@containers_router.get("/containers/{container_id}")
def retrieve_container(
    container_id: str,
    request: Request,
    service: ContainersService = Depends(),  # noqa: B008
) -> None:
    """Retrieve Container"""
    return service.retrieve_container(container_id=container_id)


@containers_router.delete("/containers/{container_id}")
def delete_container(
    container_id: str,
    request: Request,
    service: ContainersService = Depends(),  # noqa: B008
) -> None:
    """Delete Container"""
    return service.delete_container(container_id=container_id)


@containers_router.post("/containers/{container_id}/files")
def create_container_file(
    container_id: str,
    request: Request,
    service: ContainersService = Depends(ContainersService),  # noqa: B008
) -> None:
    """
    Create a Container File

    You can send either a multipart/form-data request with the raw file content, or a JSON request with a file ID.
    """
    return service.create_container_file(container_id=container_id)


@containers_router.get("/containers/{container_id}/files")
def list_container_files(
    container_id: str,
    limit: str,
    order: str,
    after: str,
    request: Request,
    service: ContainersService = Depends(),  # noqa: B008
) -> None:
    """List Container files"""
    return service.list_container_files(
        container_id=container_id,
        limit=int(limit) if limit else None,
        order=order,
        after=after,
    )


@containers_router.get("/containers/{container_id}/files/{file_id}")
def retrieve_container_file(
    container_id: str,
    file_id: str,
    request: Request,
    service: ContainersService = Depends(),  # noqa: B008
) -> None:
    """Retrieve Container File"""
    return service.retrieve_container_file(container_id=container_id, file_id=file_id)


@containers_router.delete("/containers/{container_id}/files/{file_id}")
def delete_container_file(
    container_id: str,
    file_id: str,
    request: Request,
    service: ContainersService = Depends(),  # noqa: B008
) -> None:
    """Delete Container File"""
    return service.delete_container_file(container_id=container_id, file_id=file_id)


@containers_router.get("/containers/{container_id}/files/{file_id}/content")
def retrieve_container_file_content(
    container_id: str,
    file_id: str,
    request: Request,
    service: ContainersService = Depends(),  # noqa: B008
) -> None:
    """Retrieve Container File Content"""
    return service.retrieve_container_file_content(
        container_id=container_id, file_id=file_id
    )
