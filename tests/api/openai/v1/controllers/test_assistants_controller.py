from httpx import AsyncClient
from openai.types.beta import Assistant

from timestep.config import settings


token = settings.openai_api_key.get_secret_value()

assistant_id = "default_assistant_id"
message_id = "default_message_id"
thread_id = "default_thread_id"
run_id = "default_run_id"
step_id = "default_step_id"

async def test_cancel_run(client: AsyncClient):
    response = await client.post(
        f"/api/openai/v1/threads/{thread_id}/runs/{run_id}/cancel",
    )

    assert response.status_code == 401

async def test_create_assistant(client: AsyncClient):
    model_id = "test-create-assistant"

    response = await client.get(
        "/api/openai/v1/assistants",
        headers={
            "Authorization": f"Bearer {token}",
        },
    )

    assert response.status_code == 200

    assistants_response = response.json()
    assistants: list[Assistant] = [Assistant(**assistant) for assistant in assistants_response["data"]]

    for assistant in assistants:
        if assistant.model == model_id:
            response = await client.delete(
                f"/api/openai/v1/assistants/{assistant.id}",
                headers={
                    "Authorization": f"Bearer {token}",
                },
            )

            assert response.status_code == 200

    response = await client.post(
        "/api/openai/v1/assistants",
    )

    assert response.status_code == 401

    response = await client.post(
        "/api/openai/v1/assistants",
        headers={
            "Authorization": f"Bearer {token}",
        },
        json={
            "model": model_id,
        },
    )

    assert response.status_code == 200

    assistant: Assistant = Assistant(**response.json())

    assert assistant.model == model_id

    response = await client.delete(
        f"/api/openai/v1/assistants/{assistant.id}",
        headers={
            "Authorization": f"Bearer {token}",
        },
    )

    assert response.status_code == 200

async def test_create_message(client: AsyncClient):
    response = await client.post(
        f"/api/openai/v1/threads/{thread_id}/messages",
    )

    assert response.status_code == 401

async def test_create_run(client: AsyncClient):
    response = await client.post(
        f"/api/openai/v1/threads/{thread_id}/runs",
    )

    assert response.status_code == 401

async def test_create_thread(client: AsyncClient):
    response = await client.post(
        "/api/openai/v1/threads",
    )

    assert response.status_code == 401

async def test_create_thread_and_run(client: AsyncClient):
    response = await client.post(
        "/api/openai/v1/threads/runs",
    )

    assert response.status_code == 401

async def test_delete_assistant(client: AsyncClient):
    model_id = "test-delete-assistant"

    response = await client.get(
        "/api/openai/v1/assistants",
        headers={
            "Authorization": f"Bearer {token}",
        },
    )

    assert response.status_code == 200

    assistants_response = response.json()

    assistants: list[Assistant] = [Assistant(**assistant) for assistant in assistants_response["data"]]

    for assistant in assistants:
        if assistant.model == model_id:
            response = await client.delete(
                f"/api/openai/v1/assistants/{assistant.id}",
                headers={
                    "Authorization": f"Bearer {token}",
                },
            )

            assert response.status_code == 200

    response = await client.post(
        "/api/openai/v1/assistants",
        headers={
            "Authorization": f"Bearer {token}",
        },
        json={
            "model": model_id,
        },
    )

    assert response.status_code == 200

    assistant: Assistant = Assistant(**response.json())

    response = await client.delete(
        f"/api/openai/v1/assistants/{assistant.id}",
    )

    assert response.status_code == 401

    response = await client.delete(
        f"/api/openai/v1/assistants/{assistant.id}",
        headers={
            "Authorization": f"Bearer {token}",
        },
    )

    assert response.status_code == 200

async def test_delete_message(client: AsyncClient):
    response = await client.delete(
        f"/api/openai/v1/threads/{thread_id}/messages/{message_id}",
    )

    assert response.status_code == 401

async def test_delete_thread(client: AsyncClient):
    response = await client.delete(
        f"/api/openai/v1/threads/{thread_id}",
    )

    assert response.status_code == 401

async def test_get_assistant(client: AsyncClient):
    response = await client.get(
        f"/api/openai/v1/assistants/{assistant_id}",
    )

    assert response.status_code == 401

async def test_get_message(client: AsyncClient):
    response = await client.get(
        f"/api/openai/v1/threads/{thread_id}/messages/{message_id}",
    )

    assert response.status_code == 401

async def test_get_run(client: AsyncClient):
    response = await client.get(
        f"/api/openai/v1/threads/{thread_id}/runs/{run_id}",
    )

    assert response.status_code == 401

async def test_get_run_step(client: AsyncClient):
    response = await client.get(
        f"/api/openai/v1/threads/{thread_id}/runs/{run_id}/steps/{step_id}",
    )

    assert response.status_code == 401

async def test_get_thread(client: AsyncClient):
    response = await client.get(
        f"/api/openai/v1/threads/{thread_id}",
    )

    assert response.status_code == 401

async def test_list_assistants(client: AsyncClient):
    response = await client.get(
        "/api/openai/v1/assistants",
    )

    assert response.status_code == 401

async def test_list_messages(client: AsyncClient):
    response = await client.get(
        f"/api/openai/v1/threads/{thread_id}/messages",
    )

    assert response.status_code == 401

async def test_list_run_steps(client: AsyncClient):
    response = await client.get(
        f"/api/openai/v1/threads/{thread_id}/runs/{run_id}/steps",
    )

    assert response.status_code == 401

async def test_list_runs(client: AsyncClient):
    response = await client.get(
        f"/api/openai/v1/threads/{thread_id}/runs",
    )

    assert response.status_code == 401

async def test_modify_assistant(client: AsyncClient):
    response = await client.post(
        f"/api/openai/v1/assistants/{assistant_id}",
    )

    assert response.status_code == 401

async def test_modify_message(client: AsyncClient):
    response = await client.post(
        f"/api/openai/v1/threads/{thread_id}/messages/{message_id}",
    )

    assert response.status_code == 401

async def test_modify_run(client: AsyncClient):
    response = await client.post(
        f"/api/openai/v1/threads/{thread_id}/runs/{run_id}",
    )

    assert response.status_code == 401

async def test_modify_thread(client: AsyncClient):
    response = await client.post(
        f"/api/openai/v1/threads/{thread_id}",
    )

    assert response.status_code == 401

async def test_submit_tool_ouputs_to_run(client: AsyncClient):
    response = await client.post(
        f"/api/openai/v1/threads/{thread_id}/runs/{run_id}/submit_tool_outputs",
    )

    assert response.status_code == 401
