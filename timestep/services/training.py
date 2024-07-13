import os
from datetime import datetime
import time
import uuid

from openai.types.fine_tuning.fine_tuning_job import FineTuningJob, Hyperparameters
from openai.types.fine_tuning.fine_tuning_job_event import FineTuningJobEvent
from openai.types.fine_tuning.fine_tuning_job_integration import FineTuningJobIntegration

from prefect import flow
from prefect_shell import ShellOperation

from timestep.services.data import fine_tuning_job_events_db, fine_tuning_jobs_db

@flow
def train_model(fine_tuning_job_id: str):
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

    print("=== training model ===")
    print("fine_tuning_job_id: ", fine_tuning_job_id)
    print("fine_tuning_job: ", fine_tuning_jobs_db[fine_tuning_job_id])

    fine_tuning_job: FineTuningJob = fine_tuning_jobs_db.get(fine_tuning_job_id)
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

    # fine_tuning_jobs_db[fine_tuning_job.id] = fine_tuning_job

    fine_tuning_job.__setattr__(
        "status",
        "running",
    )

    # for short running operations, you can use the `run` method
    # which automatically manages the context
    ShellOperation(
        commands=[
            "mkdir -p data",
            "mkdir -p data/${today}"
        ],
        env={"today": today}
    ).run()

    # for long running operations, you can use a context manager
    with ShellOperation(
        commands=[
            # "curl -O https://masie_web.apps.nsidc.org/pub/DATASETS/NOAA/G02135/north/daily/data/N_seaice_extent_daily_v3.0.csv",
            f"""{os.getcwd()}/3rdparty/llama-cpp-python/vendor/llama.cpp/llama-finetune \
            --epochs {max_epochs} \
            --model-base {model_base} \
            --checkpoint-in "chk-lora-TinyLLama-v0.1-5M-F16-{task}-LATEST.gguf" \
            --checkpoint-out "chk-lora-TinyLLama-v0.1-5M-F16-{task}-ITERATION.gguf" \
            --lora-out "lora-TinyLLama-v0.1-5M-F16-{task}-ITERATION.bin" \
            --train-data "/home/mjschock/Projects/Timestep-AI/.github-private/submodules/timestep/notebooks/training_dataset.txt" \
            --save-every 10 \
            --seed {fine_tuning_job.seed} \
            --threads 6 --adam-iter 30 --batch 4 --ctx 64 \
            --use-checkpointing"""
        ],
        working_dir=f"data/{today}",
    ) as download_csv_operation:

        # trigger runs the process in the background
        download_csv_process = download_csv_operation.trigger()

        # then do other things here in the meantime, like download another file
        ...

        # when you're ready, wait for the process to finish
        download_csv_process.wait_for_completion()

        # if you'd like to get the output lines, you can use the `fetch_result` method
        output_lines = download_csv_process.fetch_result()

        for output_line in output_lines:
            fine_tuning_job_event = FineTuningJobEvent(
                id=str(uuid.uuid4()),
                created_at=int(time.time()),
                level="info",
                message=output_line,
                object="fine_tuning.job.event",
            )

            fine_tuning_job_events_db[fine_tuning_job.id].append(fine_tuning_job_event)

        fine_tuning_job.__setattr__(
            "status",
            "succeeded",
        )

if __name__ == "__main__":
    train_model()
