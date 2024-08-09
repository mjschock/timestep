from httpx import AsyncClient
from openai import AsyncOpenAI
from openai.types import Model, ModelDeleted
from openai.types.beta import Assistant

from timestep.config import Settings

settings = Settings()
token = settings.openai_api_key.get_secret_value()

async def test_delete_model(client: AsyncClient):
    model_id = "test-delete-model"

    response = await client.delete(
        f"/api/openai/v1/models/{model_id}",
    )

    assert response.status_code == 401

    response = await client.delete(
        f"/api/openai/v1/models/{model_id}",
        headers={
            "Authorization": f"Bearer {token}",
        },
    )

    assert response.status_code == 200

async def test_list_models(client: AsyncClient):
    model_ids_to_assistants = {
        "test-list-models-1": None,
        "test-list-models-2": None,
        "test-list-models-3": None,
    }

    response = await client.get(
        "/api/openai/v1/assistants",
        headers={
            "Authorization": f"Bearer {token}",
        },
    )

    assert response.status_code == 200

    assistants_response = response.json()

    # assert assistants_response["object"] == "list"

    assistants: list[Assistant] = [Assistant(**assistant) for assistant in assistants_response["data"]]

    for assistant in assistants:
        if assistant.model in model_ids_to_assistants:
            response = await client.delete(
                f"/api/openai/v1/assistants/{assistant.id}",
                headers={
                    "Authorization": f"Bearer {token}",
                },
            )

            assert response.status_code == 200

    for model_id in model_ids_to_assistants:
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
        model_ids_to_assistants[model_id] = assistant

    response = await client.get(
        "/api/openai/v1/models",
    )

    assert response.status_code == 401

    response = await client.get(
        "/api/openai/v1/models",
        headers={
            "Authorization": f"Bearer {token}",
        },
    )

    assert response.status_code == 200

    models_response = response.json()

    assert models_response["object"] == "list"

    models: list[Model] = [Model(**model) for model in models_response["data"]]

    for model in models:
        if model.id in model_ids_to_assistants:
            assistant = model_ids_to_assistants[model.id]

            assert model.created == assistant.created_at

            response = await client.delete(
                f"/api/openai/v1/assistants/{assistant.id}",
                headers={
                    "Authorization": f"Bearer {token}",
                },
            )

            assert response.status_code == 200

            del model_ids_to_assistants[model.id]

    assert len(model_ids_to_assistants) == 0

# async def test_retrieve_model(client: AsyncClient, openai_client: AsyncOpenAI):
async def test_retrieve_model(client: AsyncClient):
    # assistant: Assistant = await openai_client.beta.assistants.create(
    #     model="gpt-3.5-turbo",
    # )

    model_id = "test-retrieve-model"

    response = await client.get(
        "/api/openai/v1/assistants",
        headers={
            "Authorization": f"Bearer {token}",
        },
    )

    assert response.status_code == 200

    assistants_response = response.json()

    # assert assistants_response["object"] == "list"

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

    response = await client.get(
        f"/api/openai/v1/models/{assistant.model}",
    )

    assert response.status_code == 401

    response = await client.get(
        f"/api/openai/v1/models/{assistant.model}",
        headers={
            "Authorization": f"Bearer {token}",
        },
    )

    assert response.status_code == 200

    model: Model = Model(**response.json())

    assert model.id == assistant.model

    response = await client.delete(
        f"/api/openai/v1/assistants/{assistant.id}",
        headers={
            "Authorization": f"Bearer {token}",
        },
    )

    assert response.status_code == 200
