from pathlib import Path
from httpx import AsyncClient
import pytest

from timestep.config import settings



fine_tuning_dataset_file_path = "data/drone_training.jsonl"
fine_tuning_dataset = open(fine_tuning_dataset_file_path, "rb")
fine_tuning_dataset_file_name = Path(fine_tuning_dataset_file_path).name
fine_tuning_dataset_size = Path(fine_tuning_dataset_file_path).stat().st_size
lyft_2021_pdf_file_path = "data/10k/lyft_2021.pdf"
lyft_2021_pdf = open(lyft_2021_pdf_file_path, "rb")
lyft_2021_pdf_file_name = Path(lyft_2021_pdf_file_path).name
lyft_2021_pdf_size = Path(lyft_2021_pdf_file_path).stat().st_size
token = settings.openai_api_key.get_secret_value()


@pytest.mark.order(1)
async def test_create_file(client: AsyncClient):
    response = await client.post(
        "/api/openai/v1/files",
    )

    assert response.status_code == 401

    response = await client.post(
        "/api/openai/v1/files",
        headers={
            "Authorization": f"Bearer {token}",
        },
    )

    assert response.status_code == 400

    response = await client.post(
        "/api/openai/v1/files",
        data={
            "purpose": "assistants",
        },
        files={
            "file": lyft_2021_pdf,
        },
        headers={
            "Authorization": f"Bearer {token}",
        },
    )

    assert response.status_code == 200

    response_json = response.json()

    assert response_json["bytes"] == lyft_2021_pdf_size
    assert response_json["filename"] == lyft_2021_pdf_file_name
    assert response_json["object"] == "file"
    assert response_json["purpose"] == "assistants"

    response = await client.post(
        "/api/openai/v1/files",
        data={
            "purpose": "fine-tune",
        },
        files={
            "file": fine_tuning_dataset,
        },
        headers={
            "Authorization": f"Bearer {token}",
        },
    )

    assert response.status_code == 200

    response_json = response.json()

    assert response_json["bytes"] == fine_tuning_dataset_size
    assert response_json["filename"] == fine_tuning_dataset_file_name
    assert response_json["object"] == "file"
    assert response_json["purpose"] == "fine-tune"

@pytest.mark.order(2)
async def test_delete_file(client: AsyncClient):
    response = await client.delete(
        "/api/openai/v1/files/file_id_example",
    )

    assert response.status_code == 401

async def test_download_file(client: AsyncClient):
    response = await client.get(
        "/api/openai/v1/files/file_id_example/content",
    )

    assert response.status_code == 401

async def test_list_files(client: AsyncClient):
    response = await client.get(
        "/api/openai/v1/files?purpose=purpose_example",
    )

    assert response.status_code == 401

async def test_retrieve_file(client: AsyncClient):
    response = await client.get(
        "/api/openai/v1/files/file_id_example",
    )

    assert response.status_code == 401
