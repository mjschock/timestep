from fastapi.testclient import TestClient

from timestep.server import fastapi_app

client = TestClient(fastapi_app)

def test_cancel_run():
    response = client.post(
        "/api/openai/v1/threads/thread_id_example/runs/run_id_example/cancel",
    )

    assert response.status_code == 501

def test_create_assistant():
    response = client.post(
        "/api/openai/v1/assistants",
    )

    assert response.status_code == 501

def test_create_message():
    response = client.post(
        "/api/openai/v1/threads/thread_id_example/messages",
    )

    assert response.status_code == 501

def test_create_run():
    response = client.post(
        "/api/openai/v1/threads/thread_id_example/runs",
    )

    assert response.status_code == 501

def test_create_thread():
    response = client.post(
        "/api/openai/v1/threads",
    )

    assert response.status_code == 501

def test_create_thread_and_run():
    response = client.post(
        "/api/openai/v1/threads/runs",
    )

    assert response.status_code == 501

def test_delete_assistant():
    response = client.delete(
        "/api/openai/v1/assistants/assistant_id_example",
    )

    assert response.status_code == 501

def test_delete_message():
    response = client.delete(
        "/api/openai/v1/threads/thread_id_example/messages/message_id_example",
    )

    assert response.status_code == 501

def test_delete_thread():
    response = client.delete(
        "/api/openai/v1/threads/thread_id_example",
    )

    assert response.status_code == 501

def test_get_assistant():
    response = client.get(
        "/api/openai/v1/assistants/assistant_id_example",
    )

    assert response.status_code == 501

def test_get_message():
    response = client.get(
        "/api/openai/v1/threads/thread_id_example/messages/message_id_example",
    )

    assert response.status_code == 501

def test_get_run():
    response = client.get(
        "/api/openai/v1/threads/thread_id_example/runs/run_id_example",
    )

    assert response.status_code == 501

def test_get_run_step():
    response = client.get(
        "/api/openai/v1/threads/thread_id_example/runs/run_id_example/steps/step_id_example",
    )

    assert response.status_code == 501

def test_get_thread():
    response = client.get(
        "/api/openai/v1/threads/thread_id_example",
    )

    assert response.status_code == 501

def test_list_assistants():
    response = client.get(
        "/api/openai/v1/assistants",
    )

    assert response.status_code == 501

def test_list_messages():
    response = client.get(
        "/api/openai/v1/threads/thread_id_example/messages",
    )

    assert response.status_code == 501

def test_list_run_steps():
    response = client.get(
        "/api/openai/v1/threads/thread_id_example/runs/run_id_example/steps",
    )

    assert response.status_code == 501

def test_list_runs():
    response = client.get(
        "/api/openai/v1/threads/thread_id_example/runs",
    )

    assert response.status_code == 501

def test_modify_assistant():
    response = client.post(
        "/api/openai/v1/assistants/assistant_id_example",
    )

    assert response.status_code == 501

def test_modify_message():
    response = client.post(
        "/api/openai/v1/threads/thread_id_example/messages/message_id_example",
    )

    assert response.status_code == 501

def test_modify_run():
    response = client.post(
        "/api/openai/v1/threads/thread_id_example/runs/run_id_example",
    )

    assert response.status_code == 501

def test_modify_thread():
    response = client.post(
        "/api/openai/v1/threads/thread_id_example",
    )

    assert response.status_code == 501

def test_submit_tool_ouputs_to_run():
    response = client.post(
        "/api/openai/v1/threads/thread_id_example/runs/run_id_example/submit_tool_outputs",
    )

    assert response.status_code == 501
