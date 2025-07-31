from fastapi import HTTPException


class ContainersService:
    def list_containers(self, limit: int | None, order: str, after: str | None) -> None:
        raise HTTPException(status_code=501, detail="Not implemented")

    def create_container(self) -> None:
        raise HTTPException(status_code=501, detail="Not implemented")

    def retrieve_container(self, container_id: str) -> None:
        raise HTTPException(status_code=501, detail="Not implemented")

    def delete_container(self, container_id: str) -> None:
        raise HTTPException(status_code=501, detail="Not implemented")

    def create_container_file(self, container_id: str) -> None:
        raise HTTPException(status_code=501, detail="Not implemented")

    def list_container_files(
        self, container_id: str, limit: int | None, order: str, after: str | None
    ) -> None:
        raise HTTPException(status_code=501, detail="Not implemented")

    def retrieve_container_file(self, container_id: str, file_id: str) -> None:
        raise HTTPException(status_code=501, detail="Not implemented")

    def delete_container_file(self, container_id: str, file_id: str) -> None:
        raise HTTPException(status_code=501, detail="Not implemented")

    def retrieve_container_file_content(self, container_id: str, file_id: str) -> None:
        raise HTTPException(status_code=501, detail="Not implemented")
