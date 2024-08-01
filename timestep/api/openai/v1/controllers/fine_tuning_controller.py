import time
import uuid
from typing import List

from openai.pagination import SyncCursorPage
from openai.types.fine_tuning.fine_tuning_job import FineTuningJob, Hyperparameters
from openai.types.fine_tuning.fine_tuning_job_event import FineTuningJobEvent
from prefect.deployments import run_deployment
from prefect.deployments.flow_runs import FlowRun

# from timestep.database import InstanceStoreSingleton  # noqa: E501

# from timestep.worker import train_model

# instance_store = InstanceStoreSingleton()


def cancel_fine_tuning_job(fine_tuning_job_id):  # noqa: E501
    """Immediately cancel a fine-tune job.

     # noqa: E501

    :param fine_tuning_job_id: The ID of the fine-tuning job to cancel.
    :type fine_tuning_job_id: str

    :rtype: Union[FineTuningJob, Tuple[FineTuningJob, int], Tuple[FineTuningJob, int, Dict[str, str]]
    """
    raise NotImplementedError


# def create_fine_tuning_job(create_fine_tuning_job_request):  # noqa: E501
async def create_fine_tuning_job(body, token_info, user):
    """Creates a fine-tuning job which begins the process of creating a new model from a given dataset.  Response includes details of the enqueued job including job status and the name of the fine-tuned models once complete.  [Learn more about fine-tuning](/docs/guides/fine-tuning)

     # noqa: E501

    :param create_fine_tuning_job_request:
    :type create_fine_tuning_job_request: dict | bytes

    :rtype: Union[FineTuningJob, Tuple[FineTuningJob, int], Tuple[FineTuningJob, int, Dict[str, str]]
    """
    hyperparameters = Hyperparameters(
        # n_epochs="auto",
        n_epochs=1,
    )
    suffix = body.get("suffix")

    fine_tuning_job = FineTuningJob(
        id=str(uuid.uuid4()),
        created_at=int(time.time()),
        hyperparameters=hyperparameters,
        model=body.get("model"),
        object="fine_tuning.job",
        organization_id="organization_id",
        result_files=[],
        seed=body.get("seed", 42),
        status="queued",  # Literal['validating_files', 'queued', 'running', 'succeeded', 'failed', 'cancelled'],
        training_file=body.get("training_file"),
        validation_file=body.get("validation_file"),
    )

    # instance_store._shared_instance_state["fine_tuning_jobs"][fine_tuning_job.id] = fine_tuning_job
    instance_store.insert(fine_tuning_job)

    fine_tuning_job_id = fine_tuning_job.id

    fine_tuning_job = instance_store.select(FineTuningJob, id=fine_tuning_job_id)
    # assert uuid.UUID(fine_tuning_job.id, version=4) == uuid.UUID(fine_tuning_job_id, version=4)
    # assert uuid.UUID(fine_tuning_job.id) == uuid.UUID(fine_tuning_job_id)
    print("type(fine_tuning_job.id):", type(fine_tuning_job.id))
    assert str(fine_tuning_job.id) == fine_tuning_job_id

    fine_tuning_job_event = FineTuningJobEvent(
        id=str(uuid.uuid4()),
        created_at=int(time.time()),
        level="info",
        message="TODO: figure out what this messages should be...",
        object="fine_tuning.job.event",
    )

    instance_store._shared_instance_state["fine_tuning_job_events"][
        fine_tuning_job.id
    ] = [fine_tuning_job_event]

    # TODO: make this async, etc.
    # await train_model(fine_tuning_job_id=fine_tuning_job.id, suffix=suffix)
    flow_run: FlowRun = await run_deployment(
        idempotency_key=fine_tuning_job.id,
        name="agent-flow/agent-flow-deployment",
        # parameters={"names": ["Alice", "Bob"]},
        parameters={
            "inputs": {
                "fine_tuning_job_id": fine_tuning_job.id,
                "suffix": suffix,
            },
            "work_type": "train_agent",
        },
        # job_variables={"env": {"MY_ENV_VAR": "staging"}},
        timeout=0,  # don't wait for the run to finish
    )

    print("flow_run: ", flow_run)

    return fine_tuning_job.model_dump(mode="json")


# def list_fine_tuning_events(fine_tuning_job_id, after=None, limit=None):  # noqa: E501
def list_fine_tuning_events(fine_tuning_job_id, limit, token_info, user):
    """Get status updates for a fine-tuning job.

     # noqa: E501

    :param fine_tuning_job_id: The ID of the fine-tuning job to get events for.
    :type fine_tuning_job_id: str
    :param after: Identifier for the last event from the previous pagination request.
    :type after: str
    :param limit: Number of events to retrieve.
    :type limit: int

    :rtype: Union[ListFineTuningJobEventsResponse, Tuple[ListFineTuningJobEventsResponse, int], Tuple[ListFineTuningJobEventsResponse, int, Dict[str, str]]
    """
    # TODO: handle AsyncCursorPage?
    fine_tuning_job_events: List[FineTuningJobEvent] = (
        instance_store._shared_instance_state["fine_tuning_job_events"][
            fine_tuning_job_id
        ][-limit:]
    )

    sync_cursor_page: SyncCursorPage[FineTuningJobEvent] = SyncCursorPage(
        data=fine_tuning_job_events,
    )

    return sync_cursor_page.model_dump(mode="json")


def list_fine_tuning_job_checkpoints(
    fine_tuning_job_id, after=None, limit=None
):  # noqa: E501
    """List checkpoints for a fine-tuning job.

     # noqa: E501

    :param fine_tuning_job_id: The ID of the fine-tuning job to get checkpoints for.
    :type fine_tuning_job_id: str
    :param after: Identifier for the last checkpoint ID from the previous pagination request.
    :type after: str
    :param limit: Number of checkpoints to retrieve.
    :type limit: int

    :rtype: Union[ListFineTuningJobCheckpointsResponse, Tuple[ListFineTuningJobCheckpointsResponse, int], Tuple[ListFineTuningJobCheckpointsResponse, int, Dict[str, str]]
    """
    raise NotImplementedError


def list_paginated_fine_tuning_jobs(after=None, limit=None):  # noqa: E501
    """List your organization&#39;s fine-tuning jobs

     # noqa: E501

    :param after: Identifier for the last job from the previous pagination request.
    :type after: str
    :param limit: Number of fine-tuning jobs to retrieve.
    :type limit: int

    :rtype: Union[ListPaginatedFineTuningJobsResponse, Tuple[ListPaginatedFineTuningJobsResponse, int], Tuple[ListPaginatedFineTuningJobsResponse, int, Dict[str, str]]
    """
    raise NotImplementedError


# def retrieve_fine_tuning_job(fine_tuning_job_id):  # noqa: E501
def retrieve_fine_tuning_job(fine_tuning_job_id: str, token_info: dict, user: str):
    """Get info about a fine-tuning job.  [Learn more about fine-tuning](/docs/guides/fine-tuning)

     # noqa: E501

    :param fine_tuning_job_id: The ID of the fine-tuning job.
    :type fine_tuning_job_id: str

    :rtype: Union[FineTuningJob, Tuple[FineTuningJob, int], Tuple[FineTuningJob, int, Dict[str, str]]
    """
    # fine_tuning_job: FineTuningJob = instance_store._shared_instance_state["fine_tuning_jobs"].get(fine_tuning_job_id)
    fine_tuning_job: FineTuningJob = instance_store.select(
        FineTuningJob,
        # uuid.UUID(fine_tuning_job_id, version=4),
        id=fine_tuning_job_id,
    )

    return fine_tuning_job.model_dump(mode="json")
