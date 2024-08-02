from fastapi.testclient import TestClient

def test_cancel_fine_tuning_job(client: TestClient):
    response = client.post(
        "/api/openai/v1/fine_tuning/jobs/ft-AF1WoRqd3aJAHsqc9NY7iL8F/cancel",
    )

    assert response.status_code == 401

def test_create_fine_tuning_job(client: TestClient):
    response = client.post(
        "/api/openai/v1/fine_tuning/jobs",
    )

    assert response.status_code == 401

def test_list_fine_tuning_events(client: TestClient):
    response = client.get(
        "/api/openai/v1/fine_tuning/jobs/ft-AF1WoRqd3aJAHsqc9NY7iL8F/events?after=after_example&limit=20",
    )

    assert response.status_code == 401

def test_list_fine_tuning_job_checkpoints(client: TestClient):
    response = client.get(
        "/api/openai/v1/fine_tuning/jobs/ft-AF1WoRqd3aJAHsqc9NY7iL8F/checkpoints?after=after_example&limit=10",
    )

    assert response.status_code == 401

def test_list_paginated_fine_tuning_jobs(client: TestClient):
    response = client.get(
        "/api/openai/v1/fine_tuning/jobs?after=after_example&limit=20",
    )

    assert response.status_code == 401

def test_retrieve_fine_tuning_job(client: TestClient):
    response = client.get(
        "/api/openai/v1/fine_tuning/jobs/ft-AF1WoRqd3aJAHsqc9NY7iL8F",
    )

    assert response.status_code == 401
