import os
import httpx
from httpx import AsyncClient
#import papermill as pm
import pytest
import respx

from timestep.config import Settings

settings = Settings()
token = settings.openai_api_key.get_secret_value()

# @pytest.mark.respx(base_url="http://openai.local")
async def test_create_chat_completion(client: AsyncClient, httpx_mock, monkeypatch):
    response = await client.post(
        "/api/openai/v1/chat/completions",
    )

    assert response.status_code == 401

    response = await client.post(
        "/api/openai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {token}",
        },
    )

    assert response.status_code == 400

    response = await client.post(
        "/api/openai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {token}",
        },
        json={
            "model": "gpt-3.5-turbo",
            "messages": [
                {
                    "role": "system",
                    "content": "You are a helpful assistant.",
                },
                {
                    "role": "user",
                    "content": "Hello, how are you?",
                },
            ],
        },
    )

    assert response.status_code == 200

    # httpx_mock.add_response(url="http://openai.local/v1/engines")

    # with httpx.Client():
    #     # pm.execute_notebook(
    #     #     "tests/ipynb/Scratch.ipynb",
    #     #     "tests/ipynb/Scratch_output.ipynb",
    #     #     # parameters=dict(response=response.json())
    #     # )

    #     base_url = os.getenv("OPENAI_BASE_URL").replace("/api/openai/v1", "")

    #     # assert base_url == "http://localhost:8000", f"Unexpected base_url: {base_url}"
    #     assert base_url == "http://openai.local", f"Unexpected base_url: {base_url}"

    #     client = httpx.Client(base_url=base_url, headers={"Authorization": f"Bearer {token}"})

    #     response = client.get("/v1/engines")

    #     # print(response.json())
    #     print(response)

    #     # assert response.status_code == 200
    #     # assert response.json()["data"][0]["id"] == "copilot-codex"

    #     # monkeypatch.setattr(
    #     #     # httpx.HTTPTransport,
    #     #     httpx.Client,
    #     #     "__"
    #     #     # "handle_request",
    #     #     # mocked_handle_request,
    #     # )

    #     with monkeypatch.context() as m:
    #         # m.setattr(httpx, "Client", lambda: "/")


    #         with respx.mock:
    #             pm.execute_notebook(
    #                 "tests/ipynb/Scratch.ipynb",
    #                 "tests/ipynb/Scratch_output.ipynb",
    #                 # parameters=dict(response=response.json())
    #             )
