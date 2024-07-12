import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from timestep.apis.openai.models.create_fine_tuning_job_request import CreateFineTuningJobRequest  # noqa: E501
from timestep.apis.openai.models.fine_tuning_job import FineTuningJob  # noqa: E501
from timestep.apis.openai.models.list_fine_tuning_job_checkpoints_response import ListFineTuningJobCheckpointsResponse  # noqa: E501
from timestep.apis.openai.models.list_fine_tuning_job_events_response import ListFineTuningJobEventsResponse  # noqa: E501
from timestep.apis.openai.models.list_paginated_fine_tuning_jobs_response import ListPaginatedFineTuningJobsResponse  # noqa: E501
from timestep.apis.openai import util


def cancel_fine_tuning_job(fine_tuning_job_id):  # noqa: E501
    """Immediately cancel a fine-tune job. 

     # noqa: E501

    :param fine_tuning_job_id: The ID of the fine-tuning job to cancel. 
    :type fine_tuning_job_id: str

    :rtype: Union[FineTuningJob, Tuple[FineTuningJob, int], Tuple[FineTuningJob, int, Dict[str, str]]
    """
    return 'do some magic!'


def create_fine_tuning_job(create_fine_tuning_job_request):  # noqa: E501
    """Creates a fine-tuning job which begins the process of creating a new model from a given dataset.  Response includes details of the enqueued job including job status and the name of the fine-tuned models once complete.  [Learn more about fine-tuning](/docs/guides/fine-tuning) 

     # noqa: E501

    :param create_fine_tuning_job_request: 
    :type create_fine_tuning_job_request: dict | bytes

    :rtype: Union[FineTuningJob, Tuple[FineTuningJob, int], Tuple[FineTuningJob, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        create_fine_tuning_job_request = CreateFineTuningJobRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def list_fine_tuning_events(fine_tuning_job_id, after=None, limit=None):  # noqa: E501
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
    return 'do some magic!'


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


def retrieve_fine_tuning_job(fine_tuning_job_id):  # noqa: E501
    """Get info about a fine-tuning job.  [Learn more about fine-tuning](/docs/guides/fine-tuning) 

     # noqa: E501

    :param fine_tuning_job_id: The ID of the fine-tuning job. 
    :type fine_tuning_job_id: str

    :rtype: Union[FineTuningJob, Tuple[FineTuningJob, int], Tuple[FineTuningJob, int, Dict[str, str]]
    """
    return 'do some magic!'
