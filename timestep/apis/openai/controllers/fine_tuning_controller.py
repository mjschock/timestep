import time
import uuid
import connexion
from typing import Dict, List
from typing import Tuple
from typing import Union

from openai.types.fine_tuning.fine_tuning_job import FineTuningJob, Hyperparameters
from openai.types.fine_tuning.fine_tuning_job_event import FineTuningJobEvent
from openai.types.fine_tuning.fine_tuning_job_integration import FineTuningJobIntegration
from openai.pagination import SyncCursorPage

from timestep.apis.openai.models.create_fine_tuning_job_request import CreateFineTuningJobRequest  # noqa: E501
# from timestep.apis.openai.models.fine_tuning_job import FineTuningJob  # noqa: E501
from timestep.apis.openai.models.list_fine_tuning_job_checkpoints_response import ListFineTuningJobCheckpointsResponse  # noqa: E501
from timestep.apis.openai.models.list_fine_tuning_job_events_response import ListFineTuningJobEventsResponse  # noqa: E501
from timestep.apis.openai.models.list_paginated_fine_tuning_jobs_response import ListPaginatedFineTuningJobsResponse  # noqa: E501
from timestep.apis.openai import util
from timestep.services.data import fine_tuning_job_events_db, fine_tuning_jobs_db
from timestep.services.training import train_model


def cancel_fine_tuning_job(fine_tuning_job_id):  # noqa: E501
    """Immediately cancel a fine-tune job. 

     # noqa: E501

    :param fine_tuning_job_id: The ID of the fine-tuning job to cancel. 
    :type fine_tuning_job_id: str

    :rtype: Union[FineTuningJob, Tuple[FineTuningJob, int], Tuple[FineTuningJob, int, Dict[str, str]]
    """
    return 'do some magic!'


def create_fine_tuning_job(body, token_info, user):
    """Creates a fine-tuning job which begins the process of creating a new model from a given dataset.  Response includes details of the enqueued job including job status and the name of the fine-tuned models once complete.  [Learn more about fine-tuning](/docs/guides/fine-tuning) 

     # noqa: E501

    :param create_fine_tuning_job_request: 
    :type create_fine_tuning_job_request: dict | bytes

    :rtype: Union[FineTuningJob, Tuple[FineTuningJob, int], Tuple[FineTuningJob, int, Dict[str, str]]
    """

    hyperparameters = Hyperparameters(
        n_epochs="auto",
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
        status="queued", # Literal['validating_files', 'queued', 'running', 'succeeded', 'failed', 'cancelled'],
        training_file=body.get("training_file"),
        validation_file=body.get("validation_file"),
    )

    fine_tuning_jobs_db[fine_tuning_job.id] = fine_tuning_job

    fine_tuning_job_event = FineTuningJobEvent(
        id=str(uuid.uuid4()),
        created_at=int(time.time()),
        level="info",
        message="TODO: figure out what this messages should be...",
        object="fine_tuning.job.event",
    )

    fine_tuning_job_events_db[fine_tuning_job.id] = [fine_tuning_job_event]

    # TODO: make this async, etc.
    train_model(fine_tuning_job_id=fine_tuning_job.id)

    return fine_tuning_job.model_dump(mode="json")


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

    # print("args: ", args)
    # print("kwargs: ", kwargs)

    # TODO: handle AsyncCursorPage
    fine_tuning_job_events: List[FineTuningJobEvent] = fine_tuning_job_events_db[fine_tuning_job_id][-limit:]

    sync_cursor_page: SyncCursorPage[FineTuningJobEvent] = SyncCursorPage(
        data=fine_tuning_job_events,
    )

    return sync_cursor_page.model_dump(mode="json")


def list_fine_tuning_job_checkpoints(fine_tuning_job_id, after=None, limit=None):  # noqa: E501
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
    return 'do some magic!'


def list_paginated_fine_tuning_jobs(after=None, limit=None):  # noqa: E501
    """List your organization&#39;s fine-tuning jobs 

     # noqa: E501

    :param after: Identifier for the last job from the previous pagination request.
    :type after: str
    :param limit: Number of fine-tuning jobs to retrieve.
    :type limit: int

    :rtype: Union[ListPaginatedFineTuningJobsResponse, Tuple[ListPaginatedFineTuningJobsResponse, int], Tuple[ListPaginatedFineTuningJobsResponse, int, Dict[str, str]]
    """
    return 'do some magic!'


def retrieve_fine_tuning_job(fine_tuning_job_id, token_info, user):
    """Get info about a fine-tuning job.  [Learn more about fine-tuning](/docs/guides/fine-tuning) 

     # noqa: E501

    :param fine_tuning_job_id: The ID of the fine-tuning job. 
    :type fine_tuning_job_id: str

    :rtype: Union[FineTuningJob, Tuple[FineTuningJob, int], Tuple[FineTuningJob, int, Dict[str, str]]
    """

    fine_tuning_job: FineTuningJob = fine_tuning_jobs_db.get(fine_tuning_job_id)

    return fine_tuning_job.model_dump(mode="json")
