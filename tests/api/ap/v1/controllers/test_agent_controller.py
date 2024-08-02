from httpx import AsyncClient

default_artifact_id = "default_artifact_id"
default_step_id = "default_step_id"
default_task_id = "default_task_id"

async def test_create_agent_task(client: AsyncClient):
    response = await client.post(
        "/api/ap/v1/agent/tasks",
    )

    assert response.status_code == 400

async def test_download_agent_task_artifact(client: AsyncClient):
    response = await client.get(
        f"/api/ap/v1/agent/tasks/{default_task_id}/artifacts/{default_artifact_id}",
    )

    assert response.status_code == 500

async def test_execute_agent_task_step(client: AsyncClient):
    response = await client.post(
        f"/api/ap/v1/agent/tasks/{default_task_id}/steps",
    )

    assert response.status_code == 400

async def test_get_agent_task(client: AsyncClient):
    response = await client.get(
        f"/api/ap/v1/agent/tasks/{default_task_id}",
    )

    assert response.status_code == 500

async def test_get_agent_task_step(client: AsyncClient):
    response = await client.get(
        f"/api/ap/v1/agent/tasks/{default_task_id}/steps/{default_step_id}",
    )

    assert response.status_code == 500

async def test_list_agent_task_artifacts(client: AsyncClient):
    response = await client.get(
        f"/api/ap/v1/agent/tasks/{default_task_id}/artifacts?current_page=1&page_size=10",
    )

    assert response.status_code == 500

async def test_list_agent_task_steps(client: AsyncClient):
    response = await client.get(
        f"/api/ap/v1/agent/tasks/{default_task_id}/steps?current_page=1&page_size=10",
    )

    assert response.status_code == 500

async def test_list_agent_tasks(client: AsyncClient):
    response = await client.get(
        f"/api/ap/v1/agent/tasks?current_page=1&page_size=10",
    )

    assert response.status_code == 500

async def test_upload_agent_task_artifacts(client: AsyncClient):
    response = await client.post(
        f"/api/ap/v1/agent/tasks/{default_task_id}/artifacts",
    )

    assert response.status_code == 500
