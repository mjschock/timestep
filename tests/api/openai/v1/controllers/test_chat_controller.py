from fastapi.testclient import TestClient

def test_create_chat_completion(client: TestClient):
    response = client.post(
        "/api/openai/v1/chat/completions",
    )

    assert response.status_code == 401

    token = "sk-no-key-required"

    response = client.post(
        "/api/openai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {token}",
        },
    )

    assert response.status_code == 400

    response = client.post(
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

    from importlib.resources import files
    # from pytest_notebook import example_nbs
    from pytest_notebook.nb_regression import NBRegressionFixture

    fixture = NBRegressionFixture(exec_timeout=50)
    fixture.diff_color_words = False

    # with files(example_nbs) as example_nbs_path:
    #     nb_regression = NBRegressionFixture(example_nbs_path)
    #     nb_regression.check_notebook("openai_chat_completion.ipynb", response.json())

    # with files("3rdparty/openai-cookbook").joinpath("notebooks/Scratch.ipynb") as path:
        # fixture.check(str(path))
    # fixture.check("3rdparty/openai-cookbook/examples/gpt4o/introduction_to_gpt4o.ipynb", response.json())
    # fixture.check("notebooks/Scratch.ipynb", response.json())
