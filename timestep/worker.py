import json
import os
import uuid
from typing import Optional

import controlflow as cf
import httpx
import openai
import typer
from langchain_openai import ChatOpenAI
from openai.types.beta.assistant import Assistant
from openai.types.beta.thread import Thread
from openai.types.beta.threads.run import Run
from openai.types.chat.chat_completion import ChatCompletion
from openai.types.file_object import FileObject
from openai.types.fine_tuning.fine_tuning_job import FineTuningJob, Hyperparameters
from prefect import flow, get_run_logger, task
from prefect.deployments import run_deployment
from prefect.deployments.flow_runs import FlowRun
from prefect_shell import ShellOperation
from prefect_sqlalchemy import AsyncDriver, ConnectionComponents, SqlAlchemyConnector

from timestep.worker import train_model

# from timestep.api.openai.v1.controllers.chat_controller import create_chat_completion
# from timestep.database import InstanceStoreSingleton
# from timestep.services.assistants_service import create_message, get_assistant, get_run, get_thread, list_messages, modify_run

# instance_store = InstanceStoreSingleton()

app_dir = typer.get_app_dir(__package__)
block_name = "timestep-ai-sql-alchemy-connector-block"
connector = SqlAlchemyConnector(
    connection_info=ConnectionComponents(
        driver=AsyncDriver.SQLITE_AIOSQLITE, database=f"{app_dir}/database.db"
    )
)

# set the default model
cf.default_model = ChatOpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    base_url=os.environ.get("OPENAI_BASE_URL"),
    temperature=0.0,
)

openai_client = openai.OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    base_url=os.environ.get("OPENAI_BASE_URL"),
)

# @task(log_prints=True)
# async def say_hello(name: str):
#     print(f"Hello, {name}!")

#     typer.echo("def say_hello(name: str):")

# @cf.task
# def divide_numbers(a: int, b: int) -> float:
#     """Divide two numbers."""
#     pass

# @cf.flow
# def my_flow():
#     try:
#         result = divide_numbers(10, 0)
#         print(result)
#     except ValueError as e:
#         print(f"Error: {str(e)}")


@cf.flow
def iterative_task_flow():
    task = cf.Task("Generate a comprehensive report on AI trends")

    while task.is_incomplete():
        task.run_once()

        # Optionally, you can add logic here to modify the task,
        # create new tasks, or make decisions based on other results

        # if some_condition:
        if True:
            break  # Allows for early termination if needed

    return task.result


@flow
async def agent_flow(inputs: dict):
    logger = get_run_logger()
    logger.info("INFO level log message.")
    logger.debug("DEBUG level log message.")
    logger.error("ERROR level log message.")
    logger.warn("WARN level log message.")

    typer.echo("agent flow")

    print("inputs: ", inputs)

    await connector.save(block_name, overwrite=True)

    # for name in inputs:
    #     await say_hello(name)

    if "run_id" in inputs:
        print("=== run_id ===")

        # my_flow()
        raise NotImplementedError(
            "TODO: just use OpenAI lib to invoke model with messages right now"
        )

        result = iterative_task_flow()
        print("result: ", result)

        # async with cf.Flow() as greeting_flow:
        # with cf.Flow():
        #     task = cf.Task('What is 2 + 2?')
        #     # task.run_once(
        #     # task.run_once()
        #     await task.run_once_async()
        #     result = task.result
        #     print('result: ', result)

        # with cf.Flow() as agent_run_flow:
        #     agent = cf.Agent(
        #         name="Marvin",
        #         instructions="You are a helpful assistant. Answer the question.",
        #     )

        #     print('agent: ', agent)
        #     model = agent.get_model()
        #     print('model: ', model)

        #     logger.info("INFO level log message.")
        #     logger.debug("DEBUG level log message.")
        #     logger.error("ERROR level log message.")
        #     logger.warn("WARN level log message.")

        #     typer.echo("agent flow")

        # task = cf.Task("Write a generic 12-week proposal to get funding to implement agent serving and training with small local models")

        # agent_run_flow.run_once()

    else:
        fine_tuning_job_id = inputs["fine_tuning_job_id"]
        suffix = inputs.get("suffix")

        await train_model(fine_tuning_job_id=fine_tuning_job_id, suffix=suffix)


# TODO: move this somewhere more appropriate
# maybe get rid of BackgroundTask and just trigger a run deployment
# @flow(log_prints=True)
# @cf.flow
async def step(run_id: str, token_info: dict, thread_id: str, user: str):
    print("=== run_run ===")
    # run: Run = Run(**await get_run(run_id=run_id, token_info=token_info, thread_id=thread_id, user=user))
    run: Run = await get_run(
        run_id=run_id, token_info=token_info, thread_id=thread_id, user=user
    )
    assistant: Assistant = await get_assistant(
        assistant_id=run.assistant_id, token_info=token_info, user=user
    )
    thread: Thread = await get_thread(
        token_info=token_info, thread_id=thread_id, user=user
    )

    # # TODO: use ControlFlow to run_once...
    # @cf.flow
    # def run_run_flow():
    #     agent = cf.Agent(
    #         name=assistant.name,
    #         description=assistant.description,
    #         instructions=assistant.instructions,
    #         # memory
    #         # tools=,
    #         # ...
    #     )

    #     task = cf.Task(
    #         "Tell me something I don't know",
    #         # objective=
    #         # instructions=
    #         agents=[agent]
    #     )

    #     return task

    # result = run_run_flow()

    # print('result: ', result)

    # messages: List[Message] = list_messages(
    # SyncCursorPage[Message] = await list_messages(
    messages = await list_messages(
        limit=-1,
        order="asc",
        token_info=token_info,
        thread_id=thread_id,
        user=user,
    )

    system_message = {
        "content": "You are a helpful assistant with access to tools. Please be honest and do not hallucinate.",
        "role": "system",
    }

    messages = [system_message] + messages
    print("messages: ", messages)

    def get_message_content(message):
        content = message.get("content")

        if type(content) == list:
            if message.get("role") == "user":
                return [
                    {
                        "text": _content.get("text").get("value"),
                        "type": _content.get("type"),
                    }
                    for _content in content
                ]

            else:
                assert len(content) == 1
                return content[0].get("text").get("value")

        else:
            return content

    body = {  # CompletionCreateParamsNonStreaming
        "messages": [
            {
                "content": get_message_content(message),
                "role": message.get("role"),
            }
            for message in messages
        ],
        "model": assistant.model,
        "tools": assistant.tools,
    }
    print("body: ", body)

    # TODO: use service instead?
    chat_completion: ChatCompletion = ChatCompletion(
        **await create_chat_completion(body=body, token_info=token_info, user=user)
    )  # TODO: handle streaming use case
    print("chat_completion: ", chat_completion)

    choice = chat_completion.choices[0]
    print("choice: ", choice)

    finish_reason = choice.finish_reason
    print(
        "finish_reason: ", finish_reason
    )  # "stop", "length", "tool_calls", "content_filter", "function_call"

    response_message = chat_completion.choices[0].message

    tool_calls = response_message.tool_calls

    if tool_calls:
        raise NotImplementedError

    await create_message(
        body={
            "content": response_message.content,
            "role": response_message.role,
        },
        token_info=token_info,
        thread_id=thread_id,
        user=user,
    )

    # time.sleep(1)  # wait for the process to finish

    modify_run_request = {
        "status": "completed",
    }

    await modify_run(
        modify_run_request=modify_run_request,
        run_id=run_id,
        token_info=token_info,
        thread_id=thread_id,
        user=user,
    )

    # run: Run = Run(**await get_run(run_id=run_id, token_info=token_info, thread_id=thread_id, user=user))

    # return run


@task
# async def select_fine_tuning_job_by_id(id: str) -> list:
async def select_fine_tuning_job_by_id(id: str):
    async with await SqlAlchemyConnector.load(block_name) as connector:
        # results = await connector.fetch_one(f"SELECT * FROM fine_tuning_jobs WHERE id = '{unhyphenated_id}';") # TODO: use prepared statement equivalent
        results = await connector.fetch_one(
            f"""SELECT 
                    created_at,
                    error,
                    estimated_finish,
                    fine_tuned_model,
                    finished_at,
                    hyperparameters,
                    integrations,
                    model,
                    object,
                    organization_id,
                    result_files,
                    seed,
                    status,
                    trained_tokens,
                    training_file,
                    validation_file
                FROM fine_tuning_jobs
                WHERE id = :id;""",
            parameters={"id": str(uuid.UUID(id, version=4)).replace("-", "")},
        )
        print("results: ", results)

        return FineTuningJob(
            id=id,
            created_at=results[0],
            error=json.loads(results[1]),
            estimated_finish=results[2],
            fine_tuned_model=results[3],
            finished_at=results[4],
            hyperparameters=json.loads(results[5]),
            integrations=json.loads(results[6]),
            model=results[7],
            object=results[8],
            organization_id=results[9],
            result_files=json.loads(results[10]),
            seed=results[11],
            status=results[12],
            trained_tokens=results[13],
            training_file=results[14],
            validation_file=results[15],
        )
        # return results

    # return all_rows


@flow(log_prints=True)
async def train_model(fine_tuning_job_id: str, suffix: Optional[str] = None):
    logger = get_run_logger()
    logger.info("INFO level log message.")
    logger.debug("DEBUG level log message.")
    logger.debug("ERROR level log message.")

    print("=== training model ===")
    print("fine_tuning_job_id: ", fine_tuning_job_id)

    working_dir = f"work/{fine_tuning_job_id}"
    os.makedirs(working_dir, exist_ok=True)

    # fine_tuning_job: FineTuningJob = instance_store._shared_instance_state["fine_tuning_jobs"].get(fine_tuning_job_id)
    fine_tuning_job: FineTuningJob = await select_fine_tuning_job_by_id(
        fine_tuning_job_id
    )
    print("fine_tuning_job: ", fine_tuning_job)

    hyperparameters: Hyperparameters = fine_tuning_job.hyperparameters
    max_epochs = -1 if hyperparameters.n_epochs == "auto" else hyperparameters.n_epochs

    # model: Llama = instance_store._shared_instance_state["models"][fine_tuning_job.model]
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f'{os.environ.get("OPENAI_BASE_URL").split("/api")[0]}/v2/models/{fine_tuning_job.model}'
        )
        print("response: ", response)
        model_info = response.json()
        print("model_info: ", model_info)

    model_path: str = model_info.get("model_path")
    print("model_path: ", model_path)

    lora_base: str = model_info.get("lora_base")
    print("lora_base: ", lora_base)

    lora_path: str = model_info.get("lora_path")
    print("lora_path: ", lora_path)

    lora_scale: str = model_info.get("lora_scale")
    print("lora_scale: ", lora_scale)

    # fine_tuning_job = FineTuningJob(
    #     id=str(uuid.uuid4()),
    #     created_at=int(time.time()),
    #     hyperparameters=hyperparameters,
    #     model=body.get("model"),
    #     object="fine_tuning.job",
    #     organization_id="organization_id",
    #     result_files=[],
    #     seed=body.get("seed", 42),
    #     status="queued", # Literal['validating_files', 'queued', 'running', 'succeeded', 'failed', 'cancelled'],
    #     training_file=body.get("training_file"),
    #     validation_file=body.get("validation_file"),
    # )

    # fine_tuning_jobs_timestep.db[fine_tuning_job.id] = fine_tuning_job

    # fine_tuning_job.__setattr__(
    #     "status",
    #     "running",
    # )

    # fine_tuning_job_event = FineTuningJobEvent(
    #     id=str(uuid.uuid4()),
    #     created_at=int(time.time()),
    #     level="info",
    #     message=f"The job has begun",
    #     object="fine_tuning.job.event",
    # )

    # # train_data = f"{os.getcwd()}/notebooks/openai-cookbook/examples/tmp_recipe_finetune_training.jsonl"
    # # train_data = fine_tuning_job.training_file
    training_file_id = fine_tuning_job.training_file
    validation_file_id = fine_tuning_job.validation_file

    # print('training_file_id: ', training_file_id)
    # print('validation_file_id: ', validation_file_id)

    # training_file_object = instance_store._shared_instance_state["file_objects"][training_file_id]
    # validation_file_object = instance_store._shared_instance_state["file_objects"][validation_file_id]

    training_file_object: FileObject = openai_client.files.retrieve(
        file_id=training_file_id
    )
    validation_file_object: FileObject = openai_client.files.retrieve(
        file_id=validation_file_id
    )

    print("training_file_object: ", training_file_object)
    print("validation_file_object: ", validation_file_object)

    # str(uuid.UUID(id, version=4)).replace("-", "")

    # for long running operations, you can use a context manager
    async with ShellOperation(
        commands=[
            # TODO: move llama-finetune to vendored dep and use Python CPP bindings to run llama-cpp
            # TODO: git clone llama-cpp-python if not present
            # TODO: run make in llama-cpp-python to get vendor folder
            # TODO: run make in llam.cpp folder to get llama-finetune
            # TODO: --sample-start "<s>" \
            f"""{os.getcwd()}/3rdparty/llama-cpp-python/vendor/llama.cpp/llama-finetune \
--adam-iter 30 \
--batch 4 \
--checkpoint-in "chk-lora-{fine_tuning_job.model}-{fine_tuning_job.id}-LATEST.gguf" \
--checkpoint-out "chk-lora-{fine_tuning_job.model}-{fine_tuning_job.id}-ITERATION.gguf" \
--ctx 64 \
--epochs {max_epochs} \
--lora-out "lora-{fine_tuning_job.model}-{fine_tuning_job.id}-ITERATION.bin"  \
--model-base {model_path} \
--save-every 10 \
--seed {fine_tuning_job.seed} \
--threads 6 \
--train-data "{os.getcwd()}/data/{training_file_object.id}/{training_file_object.filename}" \
--use-checkpointing
            """
        ],
        working_dir=working_dir,
    ) as llama_finetune_operation:

        # trigger runs the process in the background
        llama_finetune_process = await llama_finetune_operation.trigger()

        # then do other things here in the meantime, like download another file
        ...

        # when you're ready, wait for the process to finish
        await llama_finetune_process.wait_for_completion()

        # if you'd like to get the output lines, you can use the `fetch_result` method
        output_lines = await llama_finetune_process.fetch_result()
        print("output_lines: ", output_lines)

    #     for output_line in output_lines:
    #         print('output_line: ', output_line)

    #         fine_tuning_job_event = FineTuningJobEvent(
    #             id=str(uuid.uuid4()),
    #             created_at=int(time.time()),
    #             level="info",
    #             message=output_line,
    #             object="fine_tuning.job.event",
    #         )

    #         instance_store._shared_instance_state["fine_tuning_job_events"][fine_tuning_job.id].append(fine_tuning_job_event)

    #     fine_tuning_job.__setattr__(
    #         "fine_tuned_model",
    #         # "ft:gpt-3.5-turbo-0613:personal:recipe-ner:8PjmcwDH"
    #         f"ft:{fine_tuning_job.model}:{fine_tuning_job.organization_id}:{suffix}:{fine_tuning_job.id}"
    #     )

    #     fine_tuning_job_event = FineTuningJobEvent(
    #         id=str(uuid.uuid4()),
    #         created_at=int(time.time()),
    #         level="info",
    #         message=f"New fine-tuned model created: {fine_tuning_job.fine_tuned_model}",
    #         object="fine_tuning.job.event",
    #     )

    #     instance_store._shared_instance_state["fine_tuning_job_events"][fine_tuning_job.id].append(fine_tuning_job_event)

    #     fine_tuning_job.__setattr__(
    #         "status",
    #         "succeeded",
    #     )

    #     fine_tuning_job_event = FineTuningJobEvent(
    #         id=str(uuid.uuid4()),
    #         created_at=int(time.time()),
    #         level="info",
    #         message="The job has successfully completed",
    #         object="fine_tuning.job.event",
    #     )

    #     instance_store._shared_instance_state["fine_tuning_job_events"][fine_tuning_job.id].append(fine_tuning_job_event)

    #     base_model: Llama = instance_store._shared_instance_state["models"][fine_tuning_job.model]

    #     # model = Llama(
    #     #     chat_format=base_model.chat_format,
    #     #     lora_base=f"{os.getcwd()}/{base_model.model_path}",
    #     #     lora_path=f"{os.getcwd()}/{working_dir}/lora-{fine_tuning_job.model}-{task}-ITERATION.bin",
    #     #     model_path=base_model.model_path,
    #     #     n_ctx=base_model.n_ctx(),
    #     # )

    #     # model = serve_model()

    #     # instance_store._shared_instance_state["models"][fine_tuning_job.fine_tuned_model] = model


# async def main():
def main(work_type="training"):
    # run_deployment(
    #     name="agent-flow/agent-flow-deployment",
    #     parameters={"names": ["Alice", "Bob"]},
    #     timeout=0,
    # )

    flow_run: FlowRun = run_deployment(
        # idempotency_key=fine_tuning_job.id,
        name="agent-flow/agent-flow-deployment",
        # parameters={"names": ["Alice", "Bob"]},
        parameters={
            "inputs": {
                # "fine_tuning_job_id": fine_tuning_job.id,
                # "suffix": suffix,
            },
            "work_type": work_type,
        },
        # job_variables={"env": {"MY_ENV_VAR": "staging"}},
        timeout=0,  # don't wait for the run to finish
    )

    print("flow_run: ", flow_run)


if __name__ == "__main__":
    # create your first deployment to automate your flow
    # agent_flow.serve(name="your-first-deployment")
    main()
