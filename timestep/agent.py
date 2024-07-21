import os
import time
import uuid

import os
from datetime import datetime
import time
import uuid

from llama_cpp import Llama
from openai.types.fine_tuning.fine_tuning_job import FineTuningJob, Hyperparameters
from openai.types.fine_tuning.fine_tuning_job_event import FineTuningJobEvent
from prefect import flow
from prefect_shell import ShellOperation

import controlflow as cf
from langchain_openai import ChatOpenAI
from openai.types.beta.assistant import Assistant
from openai.types.chat.chat_completion import ChatCompletion
from openai.types.beta.thread import Thread
from openai.types.beta.threads.run import Run
from prefect import flow

from timestep.api.openai.v1.controllers.chat_controller import create_chat_completion
from timestep.database import InstanceStoreSingleton
from timestep.services.assistants_service import create_message, get_assistant, get_run, get_thread, list_messages, modify_run

instance_store = InstanceStoreSingleton()

print('os.environ.get("OPENAI_API_KEY"): ', os.environ.get("OPENAI_API_KEY"))
print('os.environ.get("OPENAI_BASE_URL"): ', os.environ.get("OPENAI_BASE_URL"))

# set the default model
cf.default_model = ChatOpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    base_url=os.environ.get("OPENAI_BASE_URL"),
    temperature=0.0,
)

@flow(log_prints=True)
def hello_world(name: str = "world", goodbye: bool = False):
    print(f"Hello {name} from Prefect! 🤗")

    if goodbye:
        print(f"Goodbye {name}!")

# TODO: move this somewhere more appropriate
# maybe get rid of BackgroundTask and just trigger a run deployment
# @flow(log_prints=True)
# @cf.flow
async def step(run_id: str, token_info: dict, thread_id: str, user: str):
    print('=== run_run ===')
    # run: Run = Run(**await get_run(run_id=run_id, token_info=token_info, thread_id=thread_id, user=user))
    run: Run = await get_run(run_id=run_id, token_info=token_info, thread_id=thread_id, user=user)
    assistant: Assistant = await get_assistant(assistant_id=run.assistant_id, token_info=token_info, user=user)
    thread: Thread = await get_thread(token_info=token_info, thread_id=thread_id, user=user)

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
        order='asc',
        token_info=token_info,
        thread_id=thread_id,
        user=user,
    )

    system_message = {
        "content": "You are a helpful assistant with access to tools. Please be honest and do not hallucinate.",
        "role": "system",
    }

    messages = [system_message] + messages
    print('messages: ', messages)

    def get_message_content(message):
        content = message.get("content")

        if type(content) == list:
            if message.get("role") == "user":
                return [{
                    "text": _content.get("text").get("value"),
                    "type": _content.get("type"),
                } for _content in content]

            else:
                assert len(content) == 1
                return content[0].get("text").get("value")

        else:
            return content

    body = { # CompletionCreateParamsNonStreaming
        "messages": [ {
            "content": get_message_content(message),
            "role": message.get("role"),
        } for message in messages ],
        "model": assistant.model,
        "tools": assistant.tools,
    }
    print('body: ', body)

    # TODO: use service instead?
    chat_completion: ChatCompletion = ChatCompletion(**await create_chat_completion(body=body, token_info=token_info, user=user)) # TODO: handle streaming use case
    print('chat_completion: ', chat_completion)

    choice = chat_completion.choices[0]
    print('choice: ', choice)

    finish_reason = choice.finish_reason
    print('finish_reason: ', finish_reason) # "stop", "length", "tool_calls", "content_filter", "function_call"

    response_message = chat_completion.choices[0].message

    tool_calls = response_message.tool_calls

    if tool_calls:
        raise NotImplementedError

    await create_message(body={
        "content": response_message.content,
        "role": response_message.role,
    }, token_info=token_info, thread_id=thread_id, user=user)

    # time.sleep(1)  # wait for the process to finish

    modify_run_request = {
        "status": "completed",
    }

    await modify_run(modify_run_request=modify_run_request, run_id=run_id, token_info=token_info, thread_id=thread_id, user=user)

    # run: Run = Run(**await get_run(run_id=run_id, token_info=token_info, thread_id=thread_id, user=user))

    # return run

@flow(log_prints=True)
async def train_model(fine_tuning_job_id: str):
    # (.venv) mjschock@pop-os:~/Projects/Timestep-AI/.github-private/submodules/timestep$ 3rdparty/llama-cpp-python/vendor/llama.cpp/llama-finetune --help
    # usage: 3rdparty/llama-cpp-python/vendor/llama.cpp/llama-finetune [options]

    # options:
    #   -h, --help                 show this help message and exit
    #   --model-base FNAME         model path from which to load base model (default '')
    #   --lora-out FNAME           path to save llama lora (default 'ggml-lora-ITERATION-f32.gguf')
    #   --only-write-lora          only save llama lora, don't do any training.  use this if you only want to convert a checkpoint to a lora adapter.
    #   --norm-rms-eps F           RMS-Norm epsilon value (default 0.000010)
    #   --rope-freq-base F         Frequency base for ROPE (default 10000.000000)
    #   --rope-freq-scale F        Frequency scale for ROPE (default 1.000000)
    #   --lora-alpha N             LORA alpha : resulting LORA scaling is alpha/r. (default 4)
    #   --lora-r N                 LORA r: default rank. Also specifies resulting scaling together with lora-alpha. (default 4)
    #   --rank-att-norm N          LORA rank for attention norm tensor, overrides default rank. Norm tensors should generally have rank 1.
    #   --rank-ffn-norm N          LORA rank for feed-forward norm tensor, overrides default rank. Norm tensors should generally have rank 1.
    #   --rank-out-norm N          LORA rank for output norm tensor, overrides default rank. Norm tensors should generally have rank 1.
    #   --rank-tok-embd N          LORA rank for token embeddings tensor, overrides default rank.
    #   --rank-out N               LORA rank for output tensor, overrides default rank.
    #   --rank-wq N                LORA rank for wq tensor, overrides default rank.
    #   --rank-wk N                LORA rank for wk tensor, overrides default rank.
    #   --rank-wv N                LORA rank for wv tensor, overrides default rank.
    #   --rank-wo N                LORA rank for wo tensor, overrides default rank.
    #   --rank-ffn_gate N          LORA rank for ffn_gate tensor, overrides default rank.
    #   --rank-ffn_down N          LORA rank for ffn_down tensor, overrides default rank.
    #   --rank-ffn_up N            LORA rank for ffn_up tensor, overrides default rank.
    #   --train-data FNAME         path from which to load training data (default 'shakespeare.txt')
    #   --checkpoint-in FNAME      path from which to load training checkpoint (default 'checkpoint.gguf')
    #   --checkpoint-out FNAME     path to save training checkpoint (default 'checkpoint-ITERATION.gguf')
    #   --pattern-fn-it STR        pattern in output filenames to be replaced by iteration number (default 'ITERATION')
    #   --fn-latest STR            string to use instead of iteration number for saving latest output (default 'LATEST')
    #   --save-every N             save checkpoint and lora every N iterations. Disabled when N <= 0. (default '10')
    #   -s SEED, --seed SEED       RNG seed (default: -1, use random seed for -1)
    #   -c N, --ctx N              Context size used during training (default 128)
    #   -t N, --threads N          Number of threads (default 6)
    #   -b N, --batch N            Parallel batch size (default 8)
    #   --grad-acc N               Number of gradient accumulation steps (simulates larger batch size of batch*gradacc) (default 1)
    #   --sample-start STR         Sets the starting point for samples after the specified pattern. If empty use every token position as sample start. (default '')
    #   --include-sample-start     Include the sample start in the samples. (default off)
    #   --escape                   process sample start escapes sequences (\n, \r, \t, \', \", \\)
    #   --overlapping-samples      Samples may overlap, will include sample-start of second and following samples. When off, samples will end at begin of next sample. (default off)
    #   --fill-with-next-samples   Samples shorter than context length will be followed by the next (shuffled) samples. (default off)
    #   --separate-with-eos        When fill-with-next-samples, insert end-of-sequence token between samples.
    #   --separate-with-bos        When fill-with-next-samples, insert begin-of-sequence token between samples. (default)
    #   --no-separate-with-eos     When fill-with-next-samples, don't insert end-of-sequence token between samples. (default)
    #   --no-separate-with-bos     When fill-with-next-samples, don't insert begin-of-sequence token between samples.
    #   --sample-random-offsets    Use samples beginning at random offsets. Together with fill-with-next-samples this may help for training endless text generation.
    #   --force-reshuffle          Force a reshuffling of data at program start, otherwise the shuffling of loaded checkpoint is resumed.
    #   --no-flash                 Don't use flash attention 
    #   --use-flash                Use flash attention (default)
    #   --no-checkpointing         Don't use gradient checkpointing
    #   --use-checkpointing        Use gradient checkpointing (default)
    #   --warmup N                 Only for Adam optimizer. Number of warmup steps (default 100)
    #   --cos-decay-steps N        Only for Adam optimizer. Number of cosine decay steps (default 1000)
    #   --cos-decay-restart N      Only for Adam optimizer. Increase of cosine decay steps after restart (default 1.100000)
    #   --cos-decay-min N          Only for Adam optimizer. Cosine decay minimum (default 0.100000)
    #   --enable-restart N         Only for Adam optimizer. Enable restarts of cos-decay 
    #   --disable-restart N        Only for Adam optimizer. Disable restarts of cos-decay (default)
    #   --opt-past N               Number of optimization iterations to track for delta convergence test. Disabled when zero. (default 0)
    #   --opt-delta N              Maximum delta for delta convergence test. Disabled when <= zero. (default 0.000010)
    #   --opt-max-no-improvement N Maximum number of optimization iterations with no improvement. Disabled when <= zero. (default 0)
    #   --epochs N                 Maximum number epochs to process. (default -1)
    #   --adam-iter N              Maximum number of Adam optimization iterations for each batch (default 256)
    #   --adam-alpha N             Adam learning rate alpha (default 0.001000)
    #   --adam-min-alpha N         Adam minimum learning rate alpha - including warmup phase (default 0.000000)
    #   --adam-decay N             AdamW weight decay. Values greater zero enable AdamW instead of regular Adam. (default 0.100000)
    #   --adam-decay-min-ndim N    Minimum number of tensor dimensions to apply AdamW weight decay. Weight decay is not applied to tensors with less n_dims. (default 2)
    #   --adam-beta1 N             AdamW beta1 in interval [0,1). How much to smooth the first moment of gradients. (default 0.900000)
    #   --adam-beta2 N             AdamW beta2 in interval [0,1). How much to smooth the second moment of gradients. (default 0.999000)
    #   --adam-gclip N             AdamW gradient clipping. Disabled when zero. (default 1.000000)
    #   --adam-epsf N              AdamW epsilon for convergence test. Disabled when <= zero. (default 0.000000)
    #   -ngl N, --n-gpu-layers N   Number of model layers to offload to GPU (default 0)

    model_base = f"{os.getcwd()}/3rdparty/llamafile/models/TinyLLama-v0.1-5M-F16.gguf"
    task = "Recipe_NER"
    today = datetime.today().strftime("%Y%m%d")
    working_dir = f"work/{today}"
    os.makedirs(working_dir, exist_ok=True)

    print("=== training model ===")
    print("fine_tuning_job_id: ", fine_tuning_job_id)
    print("fine_tuning_job: ", instance_store._shared_instance_state["fine_tuning_jobs"][fine_tuning_job_id])

    fine_tuning_job: FineTuningJob = instance_store._shared_instance_state["fine_tuning_jobs"].get(fine_tuning_job_id)
    hyperparameters: Hyperparameters = fine_tuning_job.hyperparameters
    max_epochs = -1 if hyperparameters.n_epochs == "auto" else hyperparameters.n_epochs

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

    fine_tuning_job.__setattr__(
        "status",
        "running",
    )

    fine_tuning_job_event = FineTuningJobEvent(
        id=str(uuid.uuid4()),
        created_at=int(time.time()),
        level="info",
        message=f"The job has begun",
        object="fine_tuning.job.event",
    )

    train_data = f"{os.getcwd()}/notebooks/openai-cookbook/examples/tmp_recipe_finetune_training.jsonl"
    # train_data = fine_tuning_job.training_file

    # for long running operations, you can use a context manager
    async with ShellOperation(
        commands=[
            # "curl -O https://masie_web.apps.nsidc.org/pub/DATASETS/NOAA/G02135/north/daily/data/N_seaice_extent_daily_v3.0.csv",
            # f"""{os.getcwd()}/3rdparty/llama-cpp-python/vendor/llama.cpp/llama-finetune \
            # TODO: move llama-finetune to vendored dep and use Python CPP bindings to run llama-cpp
            f"""{os.getcwd()}/3rdparty/llama-cpp-python/vendor/llama.cpp/llama-finetune \
            --epochs {max_epochs} \
            --model-base {model_base} \
            --checkpoint-in "chk-lora-{fine_tuning_job.model}-{task}-LATEST.gguf" \
            --checkpoint-out "chk-lora-{fine_tuning_job.model}-{task}-ITERATION.gguf" \
            --lora-out "lora-{fine_tuning_job.model}-{task}-ITERATION.bin"  \
            --train-data "{train_data}" \
            --save-every 10 \
            --seed {fine_tuning_job.seed} \
            --threads 6 --adam-iter 30 --batch 4 --ctx 64 \
            --use-checkpointing"""
        ],
        working_dir=working_dir,
    ) as download_csv_operation:

        # trigger runs the process in the background
        download_csv_process = await download_csv_operation.trigger()

        # then do other things here in the meantime, like download another file
        ...

        # when you're ready, wait for the process to finish
        await download_csv_process.wait_for_completion()

        # if you'd like to get the output lines, you can use the `fetch_result` method
        output_lines = await download_csv_process.fetch_result()

        for output_line in output_lines:
            fine_tuning_job_event = FineTuningJobEvent(
                id=str(uuid.uuid4()),
                created_at=int(time.time()),
                level="info",
                message=output_line,
                object="fine_tuning.job.event",
            )

            instance_store._shared_instance_state["fine_tuning_job_events"][fine_tuning_job.id].append(fine_tuning_job_event)

        fine_tuning_job.__setattr__(
            "fine_tuned_model",
            "ft:gpt-3.5-turbo-0613:personal:recipe-ner:8PjmcwDH"
        )

        fine_tuning_job_event = FineTuningJobEvent(
            id=str(uuid.uuid4()),
            created_at=int(time.time()),
            level="info",
            message=f"New fine-tuned model created: {fine_tuning_job.fine_tuned_model}",
            object="fine_tuning.job.event",
        )

        instance_store._shared_instance_state["fine_tuning_job_events"][fine_tuning_job.id].append(fine_tuning_job_event)

        fine_tuning_job.__setattr__(
            "status",
            "succeeded",
        )

        fine_tuning_job_event = FineTuningJobEvent(
            id=str(uuid.uuid4()),
            created_at=int(time.time()),
            level="info",
            message="The job has successfully completed",
            object="fine_tuning.job.event",
        )

        instance_store._shared_instance_state["fine_tuning_job_events"][fine_tuning_job.id].append(fine_tuning_job_event)

        base_model: Llama = instance_store._shared_instance_state["models"][fine_tuning_job.model]

        # model = Llama(
        #     chat_format=base_model.chat_format,
        #     lora_base=f"{os.getcwd()}/{base_model.model_path}",
        #     lora_path=f"{os.getcwd()}/{working_dir}/lora-{fine_tuning_job.model}-{task}-ITERATION.bin",
        #     model_path=base_model.model_path,
        #     n_ctx=base_model.n_ctx(),
        # )

        # model = serve_model()

        # instance_store._shared_instance_state["models"][fine_tuning_job.fine_tuned_model] = model

if __name__ == "__main__":
    step()
