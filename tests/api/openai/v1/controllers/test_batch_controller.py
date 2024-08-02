from fastapi.testclient import TestClient

def test_cancel_batch(client: TestClient):
    response = client.post(
        "/api/openai/v1/batches/batch_id_example/cancel",
    )

    assert response.status_code == 401

def test_create_batch(client: TestClient):
    response = client.post(
        "/api/openai/v1/batches",
    )

    assert response.status_code == 401

def test_list_batches(client: TestClient):
    response = client.get(
        "/api/openai/v1/batches?after=after_example&limit=20",
    )

    assert response.status_code == 401

def test_retrieve_batch(client: TestClient):
    response = client.get(
        "/api/openai/v1/batches/batch_id_example",
    )

    assert response.status_code == 401
