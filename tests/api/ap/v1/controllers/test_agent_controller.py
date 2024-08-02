from fastapi.testclient import TestClient

from timestep.server import fastapi_app

client = TestClient(fastapi_app)

def test_create_agent_task(client: TestClient):
    response = client.post(
        "/api/ap/v1/agent/tasks",
    )

    assert response.status_code == 400

def test_download_agent_task_artifact(client: TestClient):
    response = client.get(
        "/api/ap/v1/agent/tasks/50da533e-3904-4401-8a07-c49adf88b5eb/artifacts/1e41533e-3904-4401-8a07-c49adf8893de",
    )

    assert response.status_code == 500

def test_execute_agent_task_step(client: TestClient):
    response = client.post(
        "/api/ap/v1/agent/tasks/50da533e-3904-4401-8a07-c49adf88b5eb/steps",
    )

    assert response.status_code == 400

def test_get_agent_task(client: TestClient):
    response = client.get(
        "/api/ap/v1/agent/tasks/1d5a533e-3904-4401-8a07-c49adf88b981",
    )

    assert response.status_code == 500

def test_get_agent_task_step(client: TestClient):
    response = client.get(
        "/api/ap/v1/agent/tasks/50da533e-3904-4401-8a07-c49adf88b5eb/steps/28ca533e-3904-4401-8a07-c49adf8891c2",
    )

    assert response.status_code == 500

def test_list_agent_task_artifacts(client: TestClient):
    response = client.get(
        "/api/ap/v1/agent/tasks/50da533e-3904-4401-8a07-c49adf88b5eb/artifacts?current_page=1&page_size=10",
    )

    assert response.status_code == 500

def test_list_agent_task_steps(client: TestClient):
    response = client.get(
        "/api/ap/v1/agent/tasks/50da533e-3904-4401-8a07-c49adf88b5eb/steps?current_page=1&page_size=10",
    )

    assert response.status_code == 500

def test_list_agent_tasks(client: TestClient):
    response = client.get(
        "/api/ap/v1/agent/tasks?current_page=1&page_size=10",
    )

    assert response.status_code == 500

def test_upload_agent_task_artifacts(client: TestClient):
    response = client.post(
        "/api/ap/v1/agent/tasks/50da533e-3904-4401-8a07-c49adf88b5eb/artifacts",
    )

    assert response.status_code == 500
