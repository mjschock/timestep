import os

import mlflow

MLFLOW_TRACKING_URI = os.getenv("MLFLOW_TRACKING_URI")

print(f"MLFLOW_TRACKING_URI: {MLFLOW_TRACKING_URI}")


def main():
    mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
    mlflow.transformers.autolog()

    # messages to use as input examples
    messages = [
        {
            "role": "system",
            "content": "Please use the provided tools to answer user queries.",
        },
        {"role": "user", "content": "What's the weather in Singapore?"},
    ]

    input_example = {
        "messages": messages,
    }

    code_path = "/root/sky_workdir/agent.py"

    # # log the model
    with mlflow.start_run():
        model_info = mlflow.pyfunc.log_model(
            artifact_path="weather-model",
            # artifacts={"snapshot": snapshot_location},
            artifacts={"snapshot": "/root/sky_workdir/lora_model"},
            python_model=code_path,
            input_example=input_example,
        )

        # Register the auto-logged model
        # model_uri = f"runs:/{run_id}/model"
        model_uri = model_info.model_uri
        registered_model_name = "RayMLflowIntegration"
        mv = mlflow.register_model(model_uri, registered_model_name)
        print(f"Name: {mv.name}")
        print(f"Version: {mv.version}")

    print("Successfully logged the model at the following URI: ", model_info.model_uri)


if __name__ == "__main__":
    main()
