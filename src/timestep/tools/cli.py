import asyncio
import os

# from agent_protocol.models import StepRequestBody
from agent_protocol_client import (
    AgentApi,
    ApiClient,
    Configuration,
    StepRequestBody,
    TaskRequestBody,
)

default_agent_id = os.environ.get("DEFAULT_AGENT_ID")
primary_domain_name = os.environ.get("PRIMARY_DOMAIN_NAME")

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
# https://$$PRIMARY_DOMAIN_NAME/api/agents/<agent_id>
configuration = Configuration(
    host=f"https://{primary_domain_name}/api/agents/{default_agent_id}"
)


async def main():
    # Enter a context with an instance of the API client
    async with ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = AgentApi(api_client)
        task_request_body = TaskRequestBody(input="Write 'Hello world!' to hi.txt.")

        response = await api_instance.create_agent_task(
            task_request_body=task_request_body
        )
        print("The response of AgentApi->create_agent_task:\n")
        print(response)
        print("\n\n")

        task_id = response.task_id
        i = 1

        while (
            step := await api_instance.execute_agent_task_step(
                # task_id=task_id, step_request_body=StepRequestBody(input=i)
                task_id=task_id,
                step_request_body=StepRequestBody(input=str(i)),
            )
        ) and step.is_last is False:
            print("The response of AgentApi->execute_agent_task_step:\n")
            print(step)
            print("\n\n")
            i += 1

        print("Agent finished its work!")

        artifacts = await api_instance.list_agent_task_artifacts(task_id=task_id)
        for artifact in artifacts:
            if artifact.file_name == "hi.txt":
                content = await api_instance.download_agent_task_artifact(
                    task_id=task_id, artifact_id=artifact.artifact_id
                )
                print(f"The content of the hi.txt is {content})")
                break
        else:
            print("The agent did not create the hi.txt file.")


asyncio.run(main())
