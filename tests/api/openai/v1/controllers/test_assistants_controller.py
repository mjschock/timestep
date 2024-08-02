from fastapi.testclient import TestClient

assistant_id = "default_assistant_id"
message_id = "default_message_id"
thread_id = "default_thread_id"
run_id = "default_run_id"
step_id = "default_step_id"

def test_cancel_run(client: TestClient):
    response = client.post(
        f"/api/openai/v1/threads/{thread_id}/runs/{run_id}/cancel",
    )

    assert response.status_code == 401

def test_create_assistant(client: TestClient):
    response = client.post(
        "/api/openai/v1/assistants",
    )

    assert response.status_code == 401

def test_create_message(client: TestClient):
    response = client.post(
        f"/api/openai/v1/threads/{thread_id}/messages",
    )

    assert response.status_code == 401

def test_create_run(client: TestClient):
    response = client.post(
        f"/api/openai/v1/threads/{thread_id}/runs",
    )

    assert response.status_code == 401

def test_create_thread(client: TestClient):
    response = client.post(
        "/api/openai/v1/threads",
    )

    assert response.status_code == 401

def test_create_thread_and_run(client: TestClient):
    response = client.post(
        "/api/openai/v1/threads/runs",
    )

    assert response.status_code == 401

def test_delete_assistant(client: TestClient):
    response = client.delete(
        f"/api/openai/v1/assistants/{assistant_id}",
    )

    assert response.status_code == 401

def test_delete_message(client: TestClient):
    response = client.delete(
        f"/api/openai/v1/threads/{thread_id}/messages/{message_id}",
    )

    assert response.status_code == 401

def test_delete_thread(client: TestClient):
    response = client.delete(
        f"/api/openai/v1/threads/{thread_id}",
    )

    assert response.status_code == 401

def test_get_assistant(client: TestClient):
    response = client.get(
        f"/api/openai/v1/assistants/{assistant_id}",
    )

    assert response.status_code == 401

def test_get_message(client: TestClient):
    response = client.get(
        f"/api/openai/v1/threads/{thread_id}/messages/{message_id}",
    )

    assert response.status_code == 401

def test_get_run(client: TestClient):
    response = client.get(
        f"/api/openai/v1/threads/{thread_id}/runs/{run_id}",
    )

    assert response.status_code == 401

def test_get_run_step(client: TestClient):
    response = client.get(
        f"/api/openai/v1/threads/{thread_id}/runs/{run_id}/steps/{step_id}",
    )

    assert response.status_code == 401

def test_get_thread(client: TestClient):
    response = client.get(
        f"/api/openai/v1/threads/{thread_id}",
    )

    assert response.status_code == 401

def test_list_assistants(client: TestClient):
    response = client.get(
        "/api/openai/v1/assistants",
    )

    assert response.status_code == 401

def test_list_messages(client: TestClient):
    response = client.get(
        f"/api/openai/v1/threads/{thread_id}/messages",
    )

    assert response.status_code == 401

def test_list_run_steps(client: TestClient):
    response = client.get(
        f"/api/openai/v1/threads/{thread_id}/runs/{run_id}/steps",
    )

    assert response.status_code == 401

def test_list_runs(client: TestClient):
    response = client.get(
        f"/api/openai/v1/threads/{thread_id}/runs",
    )

    assert response.status_code == 401

def test_modify_assistant(client: TestClient):
    response = client.post(
        f"/api/openai/v1/assistants/{assistant_id}",
    )

    assert response.status_code == 401

def test_modify_message(client: TestClient):
    response = client.post(
        f"/api/openai/v1/threads/{thread_id}/messages/{message_id}",
    )

    assert response.status_code == 401

def test_modify_run(client: TestClient):
    response = client.post(
        f"/api/openai/v1/threads/{thread_id}/runs/{run_id}",
    )

    assert response.status_code == 401

def test_modify_thread(client: TestClient):
    response = client.post(
        f"/api/openai/v1/threads/{thread_id}",
    )

    assert response.status_code == 401

def test_submit_tool_ouputs_to_run(client: TestClient):
    response = client.post(
        f"/api/openai/v1/threads/{thread_id}/runs/{run_id}/submit_tool_outputs",
    )

    assert response.status_code == 401
