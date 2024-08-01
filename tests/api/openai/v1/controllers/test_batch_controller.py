from fastapi.testclient import TestClient

from timestep.server import fastapi_app

client = TestClient(fastapi_app)

def test_cancel_batch():
    response = client.post(
        "/api/openai/v1/batches/batch_id_example/cancel",
    )

    assert response.status_code == 501

def test_create_batch():
    response = client.post(
        "/api/openai/v1/batches",
    )

    assert response.status_code == 501

def test_list_batches():
    response = client.get(
        "/api/openai/v1/batches?after=after_example&limit=20",
    )

    assert response.status_code == 501

def test_retrieve_batch():
    response = client.get(
        "/api/openai/v1/batches/batch_id_example",
    )

    assert response.status_code == 501
