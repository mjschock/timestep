from fastapi.testclient import TestClient

default_artifact_id = "default_artifact_id"
default_step_id = "default_step_id"
default_task_id = "default_task_id"

async def test_create_agent_task(client: TestClient):
    response = client.post(
        "/api/ap/v1/agent/tasks",
    )

    assert response.status_code == 400

def test_download_agent_task_artifact(client: TestClient):
    response = client.get(
        f"/api/ap/v1/agent/tasks/{default_task_id}/artifacts/{default_artifact_id}",
    )

    assert response.status_code == 500

def test_execute_agent_task_step(client: TestClient):
    response = client.post(
        f"/api/ap/v1/agent/tasks/{default_task_id}/steps",
    )

    assert response.status_code == 400

def test_get_agent_task(client: TestClient):
    response = client.get(
        f"/api/ap/v1/agent/tasks/{default_task_id}",
    )

    assert response.status_code == 500

def test_get_agent_task_step(client: TestClient):
    response = client.get(
        f"/api/ap/v1/agent/tasks/{default_task_id}/steps/{default_step_id}",
    )

    assert response.status_code == 500

def test_list_agent_task_artifacts(client: TestClient):
    response = client.get(
        f"/api/ap/v1/agent/tasks/{default_task_id}/artifacts?current_page=1&page_size=10",
    )

    assert response.status_code == 500

def test_list_agent_task_steps(client: TestClient):
    response = client.get(
        f"/api/ap/v1/agent/tasks/{default_task_id}/steps?current_page=1&page_size=10",
    )

    assert response.status_code == 500

def test_list_agent_tasks(client: TestClient):
    response = client.get(
        f"/api/ap/v1/agent/tasks?current_page=1&page_size=10",
    )

    assert response.status_code == 500

def test_upload_agent_task_artifacts(client: TestClient):
    response = client.post(
        f"/api/ap/v1/agent/tasks/{default_task_id}/artifacts",
    )

    assert response.status_code == 500
