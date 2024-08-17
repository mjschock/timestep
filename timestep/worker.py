import os
import time
from typing import List, Optional

import controlflow as cf
import httpx
import openai
import typer
from langchain_openai import ChatOpenAI
from openai.pagination import AsyncCursorPage, SyncCursorPage
from openai.types.beta.assistant import Assistant
from openai.types.beta.thread import Thread
from openai.types.beta.threads.image_file_content_block import ImageFileContentBlock
from openai.types.beta.threads.image_url_content_block import ImageURLContentBlock
from openai.types.beta.threads.message import Attachment, Message, MessageContent
from openai.types.beta.threads.run import AssistantTool, Run
from openai.types.beta.threads.runs import (
    MessageCreationStepDetails,
    RunStep,
    ToolCallsStepDetails,
)
from openai.types.beta.threads.runs.message_creation_step_details import MessageCreation
from openai.types.beta.threads.runs.tool_calls_step_details import (
    ToolCall,
    ToolCallsStepDetails,
)
from openai.types.beta.threads.text_content_block import TextContentBlock
from openai.types.chat.chat_completion import ChatCompletion, Choice
from openai.types.chat.chat_completion_assistant_message_param import (
    ChatCompletionAssistantMessageParam,
)
from openai.types.chat.chat_completion_chunk import ChatCompletionChunk
from openai.types.chat.chat_completion_function_message_param import (
    ChatCompletionFunctionMessageParam,
)
from openai.types.chat.chat_completion_message import ChatCompletionMessage
from openai.types.chat.chat_completion_message_param import ChatCompletionMessageParam
from openai.types.chat.chat_completion_message_tool_call import (
    ChatCompletionMessageToolCall,
)
from openai.types.chat.chat_completion_stream_options_param import (
    ChatCompletionStreamOptionsParam,
)
from openai.types.chat.chat_completion_system_message_param import (
    ChatCompletionSystemMessageParam,
)
from openai.types.chat.chat_completion_tool_choice_option_param import (
    ChatCompletionToolChoiceOptionParam,
)
from openai.types.chat.chat_completion_tool_message_param import (
    ChatCompletionToolMessageParam,
)
from openai.types.chat.chat_completion_tool_param import ChatCompletionToolParam
from openai.types.chat.chat_completion_user_message_param import (
    ChatCompletionUserMessageParam,
)
from openai.types.file_object import FileObject
from openai.types.fine_tuning.fine_tuning_job import FineTuningJob, Hyperparameters
from openai.types.shared_params.function_definition import FunctionDefinition
from openai.types.shared_params.function_parameters import FunctionParameters
from prefect import flow, get_run_logger, task
from prefect.context import get_run_context
from prefect.flow_runs import pause_flow_run
from prefect.variables import Variable
from prefect_shell import ShellOperation
from pydantic import BaseModel

from timestep.config import settings

app_dir = typer.get_app_dir("timestep")
cf.default_model = ChatOpenAI(
    api_key=settings.openai_api_key.get_secret_value(),
    base_url=settings.openai_base_url,
    temperature=0.0,
)
openai_async_client = openai.AsyncOpenAI(
    api_key=settings.openai_api_key.get_secret_value(),
    base_url=settings.openai_base_url,
)


class RunInput(BaseModel):
    agent_id: str
    instructions: str
    thread_id: str
    tools: List[AssistantTool] = []


class RunOutput(BaseModel):
    steps: List[RunStep] = []


# class RunStepInput(RunInput):  # TODO: StepInput?
#     pass
#     # agent_id: str
#     # instructions: str = ""
#     # thread_id: str
#     # tools: List[AssistantTool] = []


# class RunStepOutput(BaseModel):  # TODO: StepOutput?
#     chat_completion: ChatCompletion
#     finish_reason: str
#     step_details: dict


async def lock_thread(flow, flow_run, state):
    logger = get_run_logger()
    logger.info("lock_thread")

    thread_id = get_run_context().parameters["thread_id"]
    logger.info(f"thread_id: {thread_id}")

    # lock the thread_id
    await Variable.set(f"lock_{thread_id}", "locked")

    raise NotImplementedError("Need to implement a lock mechanism")


async def unlock_thread(flow, flow_run, state):
    logger = get_run_logger()
    logger.info("unlock_thread")

    thread_id = get_run_context().parameters["thread_id"]
    logger.info(f"thread_id: {thread_id}")

    # unlock the thread_id
    await Variable.set(f"lock_{thread_id}", "unlocked")

    raise NotImplementedError("Need to implement an unlock mechanism")


@flow(
    log_prints=True,
    on_completion=[unlock_thread],
    on_running=[lock_thread],
)
# @cf.flow(timeout_seconds=300)
async def agent_flow(run_input: RunInput) -> RunOutput:
    # See https://platform.openai.com/docs/assistants/deep-dive/managing-threads-and-messages
    # for more information on managing threads and messages

    logger = get_run_logger()
    logger.info(f"run_input: {run_input}")

    agent_id = run_input.agent_id
    logger.info(f"agent_id: {agent_id}")

    thread_id = run_input.thread_id  # TODO: introduce a lock on the thread_id
    logger.info(f"thread_id: {thread_id}")

    assistant: Assistant = await openai_async_client.beta.assistants.retrieve(
        assistant_id=agent_id
    )
    logger.info(f"assistant: {assistant}")

    # flow_run_id = cf.context.get("flow_run_id")
    flow_run_id = get_run_context().flow_run.id
    run_id = str(flow_run_id).replace("-", "")

    run_output = RunOutput(
        **await Variable.get(
            f"run_{run_id}", default=RunOutput().model_dump(mode="json")
        )
    )

    step_count = 0

    while step_count < 10:
        # run_step_input = RunStepInput(
        #     agent_id=agent_id,
        #     instructions=run_input.instructions,
        #     thread_id=thread_id,
        #     tools=run_input.tools,
        # )

        # TODO: optionally, allow the agent to learn from this thread
        # run_step_output: RunStepOutput = await agent_step_task(run_step_input)
        # run_step: RunStep = await agent_step_task(run_input)

        async_cursor_page: AsyncCursorPage[Message] = (
            await openai_async_client.beta.threads.messages.list(
                order="asc", thread_id=thread_id
            )
        )
        logger.info(f"async_cursor_page: {async_cursor_page}")

        messages: List[Message] = async_cursor_page.data
        logger.info(f"messages: {messages}")

        chat_completion_message_params: List[ChatCompletionMessageParam] = []

        for message in messages:
            content: List[MessageContent] = message.content

            for _content in content:
                if type(_content) == TextContentBlock:
                    chat_completion_message_params.append(
                        ChatCompletionUserMessageParam(
                            content=_content.text.value,
                            role=message.role,
                        )
                    )

                else:
                    logger.info(f"_content: {_content}")

                    raise NotImplementedError(
                        f"Unsupported content type: {type(_content)}"
                    )

        logger.info(f"chat_completion_message_params: {chat_completion_message_params}")

        chat_completion_tool_params = build_chat_completion_tool_params(
            run_input, assistant
        )

        logger.info(f"chat_completion_tool_params: {chat_completion_tool_params}")

        chat_completion: ChatCompletion = (
            await openai_async_client.chat.completions.create(
                messages=chat_completion_message_params,
                model=assistant.model,
                tools=chat_completion_tool_params,
            )
        )

        logger.info(f"chat_completion: {chat_completion}")

        choices: List[Choice] = chat_completion.choices
        logger.info(f"choices: {choices}")

        if len(choices) > 1:
            raise NotImplementedError("Multiple choices not yet supported")

        first_choice: Choice = choices[
            0
        ]  # TODO: check out Choice.logprobs for picking the best choice
        logger.info(f"first_choice: {first_choice}")

        # finish_reason: Literal["stop", "length", "tool_calls", "content_filter", "function_call"]
        # """The reason the model stopped generating tokens.

        # This will be `stop` if the model hit a natural stop point or a provided stop
        # sequence, `length` if the maximum number of tokens specified in the request was
        # reached, `content_filter` if content was omitted due to a flag from our content
        # filters, `tool_calls` if the model called a tool, or `function_call`
        # (deprecated) if the model called a function.
        # """
        finish_reason: str = first_choice.finish_reason
        logger.info(f"finish_reason: {finish_reason}")

        chat_completion_message: ChatCompletionMessage = first_choice.message
        logger.info(f"chat_completion_message: {chat_completion_message}")

        tool_calls: List[ChatCompletionMessageToolCall] | None = (
            chat_completion_message.tool_calls
        )
        logger.info(f"tool_calls: {tool_calls}")

        # Step Details: https://platform.openai.com/docs/api-reference/run-steps/step-object#run-steps/step-object-step_details
        if tool_calls:
            # Set the run status to "requires_action" and "required_action.type" to "submit_tool_outputs"
            # Pause this flow run until the required action is completed (e.g. label = await pause_flow_run(wait_for_input=Animal, timeout=60 * 60))
            step_details = ToolCallsStepDetails(
                tool_calls=tool_calls,
                type="tool_calls",
            )

            raise NotImplementedError

        else:
            # Message Creation Run Step
            message: Message = await openai_async_client.beta.threads.messages.create(
                thread_id=thread_id,
                # content: str | Iterable[MessageContentPartParam],
                content=chat_completion_message.content,
                # role: Literal['user', 'assistant'],
                role=chat_completion_message.role,
                # run_id=run_id, # TODO: add run_id to the message created here
                # attachments: Iterable[Attachment] | NotGiven | None = NOT_GIVEN,
                # metadata: object | NotGiven | None = NOT_GIVEN,
                # extra_headers: Headers | None = None,
                # extra_query: Query | None = None,
                # extra_body: Body | None = None,
                # timeout: float | Timeout | NotGiven | None = NOT_GIVEN
            )

            step_details = MessageCreationStepDetails(
                message_creation=MessageCreation(
                    message_id=message.id,
                ),
                type="message_creation",
            )

        # run_step_output = RunStepOutput(
        #     chat_completion=chat_completion,
        #     finish_reason=finish_reason,
        #     step_details=step_details,
        # )

        # return run_step_output

        run_step = RunStep(
            id=f"step-{step_count}",
            created_at=int(time.time()),
            assistant_id=agent_id,
            object="thread.run.step",
            run_id=run_id,
            status="completed",
            step_details=step_details,
            thread_id=thread_id,
            type=step_details.type,
        )

        # run_output["steps"].append(run_step_output)
        # run_output.steps.append(run_step_output)
        run_output.steps.append(run_step)
        await Variable.set(f"run_{run_id}", run_output.model_dump(mode="json"))
        # await Variable.set("run_output", run_output)

        step_count += 1

        # if run_step_output.finish_reason == "stop":
        # if True:
        if finish_reason == "stop":
            break

        else:
            raise NotImplementedError(
                # f"Unsupported finish_reason: {run_step_output.finish_reason}"
                f"Unsupported finish_reason: {finish_reason}"
            )

    return run_output


def build_chat_completion_tool_params(run_input, assistant):
    chat_completion_tool_params: List[ChatCompletionToolParam] = []
    # chat_completion_tool_params: [
    #     {'function': {'description': 'code_interpreter', 'name': 'code_interpreter', 'parameters': {}}, 'type': 'function'},
    #     {'function': {'description': 'file_search', 'name': 'file_search', 'parameters': {}}, 'type': 'function'},
    #     {'function': {'description': 'function', 'name': 'function', 'parameters': {}}, 'type': 'function'}]
    # See https://platform.openai.com/docs/assistants/tools/code-interpreter; TODO: use default input: str, outputs: list, etc for code_interpreter tool
    # See https://platform.openai.com/docs/assistants/tools/file-search: TODO index the files as documents if not already done using pypdf plust lightweight OCR model for blank pages, get good set of default function signature (like above)

    # Function tool example:
    #   "name": "get_current_weather",
    #   "description": "Get the current weather in a given location",
    #   "parameters": {
    #     "type": "object",
    #     "properties": {
    #       "location": {
    #         "type": "string",
    #         "description": "The city and state, e.g. San Francisco, CA",
    #       },
    #       "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
    #     },
    #     "required": ["location"],
    #   },

    # for tool in run_step_input.tools or assistant.tools:
    tools = run_input.tools or assistant.tools

    print("run_input.tools: ", run_input.tools)

    for tool in run_input.tools:
        print("tool: ", tool)
        print("type(tool): ", type(tool))

    print("assistant.tools: ", assistant.tools)

    for tool in assistant.tools:
        print("tool: ", tool)
        print("type(tool): ", type(tool))

    for tool in tools:
        assert tool.type in [
            "code_interpreter",
            "file_search",
            "function",
        ], f"Unsupported tool type: {tool.type}"

        function_description: str = tool.type
        function_name: str = tool.type
        function_parameters: FunctionParameters = dict()

        chat_completion_tool_params.append(
            ChatCompletionToolParam(
                function=FunctionDefinition(
                    description=function_description,
                    name=function_name,
                    parameters=function_parameters,
                ),
                type="function",
            )
        )

    return chat_completion_tool_params


# @task
# # @cf.task(timeout_seconds=60)
# # async def agent_step_task(run_step_input: RunStepInput):
# # async def agent_step_task(run_step_input: Run) -> RunStep:
# async def agent_step_task(run_step_input: RunInput) -> RunStep:
#     logger = get_run_logger()
#     logger.info(f"run_step_input: {run_step_input}")

#     agent_id = run_step_input.agent_id
#     logger.info(f"agent_id: {agent_id}")

#     thread_id = run_step_input.thread_id
#     logger.info(f"thread_id: {thread_id}")


# @task
# async def select_fine_tuning_job_by_id(id: str):
#     async with await SqlAlchemyConnector.load(block_name) as connector:
#         # results = await connector.fetch_one(f"SELECT * FROM fine_tuning_jobs WHERE id = '{unhyphenated_id}';") # TODO: use prepared statement equivalent
#         results = await connector.fetch_one(
#             f"""SELECT
#                     created_at,
#                     error,
#                     estimated_finish,
#                     fine_tuned_model,
#                     finished_at,
#                     hyperparameters,
#                     integrations,
#                     model,
#                     object,
#                     organization_id,
#                     result_files,
#                     seed,
#                     status,
#                     trained_tokens,
#                     training_file,
#                     validation_file
#                 FROM fine_tuning_jobs
#                 WHERE id = :id;""",
#             parameters={"id": str(uuid.UUID(id, version=4)).replace("-", "")},
#         )
#         print("results: ", results)

#         return FineTuningJob(
#             id=id,
#             created_at=results[0],
#             error=json.loads(results[1]),
#             estimated_finish=results[2],
#             fine_tuned_model=results[3],
#             finished_at=results[4],
#             hyperparameters=json.loads(results[5]),
#             integrations=json.loads(results[6]),
#             model=results[7],
#             object=results[8],
#             organization_id=results[9],
#             result_files=json.loads(results[10]),
#             seed=results[11],
#             status=results[12],
#             trained_tokens=results[13],
#             training_file=results[14],
#             validation_file=results[15],
#         )
#         # return results

#     # return all_rows


@flow(log_prints=True)
async def agent_train_step_flow(fine_tuning_job_id: str, suffix: Optional[str] = None):
    logger = get_run_logger()
    logger.info("INFO level log message.")

    print("=== training model ===")
    print("fine_tuning_job_id: ", fine_tuning_job_id)

    working_dir = f"{app_dir}/work/{fine_tuning_job_id}"
    os.makedirs(working_dir, exist_ok=True)

    # fine_tuning_job: FineTuningJob = instance_store._shared_instance_state["fine_tuning_jobs"].get(fine_tuning_job_id)
    # fine_tuning_job: FineTuningJob = await select_fine_tuning_job_by_id(
    #     fine_tuning_job_id
    # )

    openai_client = openai.OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),
        base_url=os.environ.get("OPENAI_BASE_URL"),
    )

    fine_tuning_job: FineTuningJob = (
        openai_client.fine_tuning.jobs.retrieve(  # TODO: is there an async version?
            fine_tuning_job_id=fine_tuning_job_id,
        )
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

    print("training_file_object: ", training_file_object)

    if validation_file_id:
        validation_file_object: FileObject = openai_client.files.retrieve(
            file_id=validation_file_id
        )

        print("validation_file_object: ", validation_file_object)

    # str(uuid.UUID(id, version=4)).replace("-", "")

    # for long running operations, you can use a context manager
    async with ShellOperation(
        commands=[
            # TODO: https://github.com/ggerganov/llama.cpp/blob/master/docs/backend/SYCL.md
            f"git clone https://github.com/ggerganov/llama.cpp {app_dir}/3rdparty/llama.cpp",
            f"make -C {app_dir}/3rdparty/llama.cpp",  # TODO: handle windows, termux, etc.
            f"""{app_dir}/3rdparty/llama.cpp/llama-finetune \
--adam-iter 30 \
--batch 8 \
--checkpoint-in "chk-lora-{fine_tuning_job.model}-{fine_tuning_job.id}-LATEST.gguf" \
--checkpoint-out "chk-lora-{fine_tuning_job.model}-{fine_tuning_job.id}-ITERATION.gguf" \
--ctx 64 \
--epochs {max_epochs} \
--lora-out "lora-{fine_tuning_job.model}-{fine_tuning_job.id}-ITERATION.bin"  \
--model-base {model_path} \
--n-gpu-layers 0 \
--save-every 10 \
--seed {fine_tuning_job.seed} \
--threads 6 \
--train-data "{app_dir}/data/{training_file_object.id}/{training_file_object.filename}" \
--use-checkpointing
            """,
        ],
        env={
            "CMAKE_ARGS": os.getenv("CMAKE_ARGS", ""),
        },
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
# def main(work_type="train_agent"):
def main(thread_id=None):
    raise NotImplementedError

    # flow_run: FlowRun = await run_deployment(
    #     idempotency_key=thread_id,
    #     name="agent-flow/agent-flow-deployment",
    #     parameters={
    #         "inputs": {
    #             "agent_id": assistant_id,
    #             "thread_id": thread_id,
    #         }
    #     },
    #     # job_variables={"env": {"MY_ENV_VAR": "staging"}},
    #     timeout=0,  # don't wait for the run to finish
    # )


if __name__ == "__main__":
    # main(work_type="train_agent")
    main()
