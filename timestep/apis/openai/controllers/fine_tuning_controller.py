import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openai.types.fine_tuning.fine_tuning_job import FineTuningJob
from openai.types.fine_tuning.fine_tuning_job_integration import FineTuningJobIntegration

from timestep.apis.openai.models.create_fine_tuning_job_request import CreateFineTuningJobRequest  # noqa: E501
# from timestep.apis.openai.models.fine_tuning_job import FineTuningJob  # noqa: E501
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


# def create_fine_tuning_job(create_fine_tuning_job_request):  # noqa: E501
def create_fine_tuning_job(body):
    """Creates a fine-tuning job which begins the process of creating a new model from a given dataset.  Response includes details of the enqueued job including job status and the name of the fine-tuned models once complete.  [Learn more about fine-tuning](/docs/guides/fine-tuning) 

     # noqa: E501

    :param create_fine_tuning_job_request: 
    :type create_fine_tuning_job_request: dict | bytes

    :rtype: Union[FineTuningJob, Tuple[FineTuningJob, int], Tuple[FineTuningJob, int, Dict[str, str]]
    """
    # if connexion.request.is_json:
    #     create_fine_tuning_job_request = CreateFineTuningJobRequest.from_dict(connexion.request.get_json())  # noqa: E501

    # Args:
    # model: The name of the model to fine-tune. You can select one of the
    #     supported models.
    # training_file: The ID of an uploaded file that contains training data.
    #     See upload file for how to upload a file.
    #     Your dataset must be formatted as a JSONL file. Additionally, you must upload your file with the purpose fine-tune.
    #     The contents of the file should differ depending on if the model uses the
    #     chat or
    #     completions format.
    #     See the fine-tuning guide for more details.
    # hyperparameters: The hyperparameters used for the fine-tuning job.
    # integrations: A list of integrations to enable for your fine-tuning job.
    # seed: The seed controls the reproducibility of the job. Passing in the same seed and
    #     job parameters should produce the same results, but may differ in rare cases. If a seed is not specified, one will be generated for you.
    # suffix: A string of up to 18 characters that will be added to your fine-tuned model
    #     name.
    #     For example, a suffix of "custom-model-name" would produce a model name like
    #     ft:gpt-3.5-turbo:openai:custom-model-name:7p4lURel.
    # validation_file: The ID of an uploaded file that contains validation data.
    #     If you provide this file, the data is used to generate validation metrics periodically during fine-tuning. These metrics can be viewed in the fine-tuning results file. The same data should not be present in both train and validation files.
    #     Your dataset must be formatted as a JSONL file. You must upload your file with the purpose fine-tune.
    #     See the fine-tuning guide for more details.
    # extra_headers: Send extra headers
    # extra_query: Add additional query parameters to the request
    # extra_body: Add additional JSON properties to the request
    # timeout: Override the client-level default timeout for this request, in seconds

    # print('args: ', args)
    # print('kwargs: ', kwargs)

    # args:  ()
    # kwargs: {
    #     'body': {
    #           'model':'gpt-3.5-turbo',
    #           'training_file': 'tmp_recipe_finetune_training.jsonl',
    #           'suffix': 'recipe-ner',
    #           'validation_file': 'tmp_recipe_finetune_validation.jsonl'
    #     },
    #     'user': 'user_id',
    #     'token_info': {'uid': 'user_id'}}

    print('type(body): ', type(body))

    model = body.get("model")
    training_file = body.get("training_file")
    suffix = body.get("suffix")
    validation_file = body.get("validation_file")

    print('model: ', model)
    print('training_file: ', training_file)
    print('suffix: ', suffix)
    print('validation_file: ', validation_file)

    job = FineTuningJob()

    # return 'do some magic!'

    return job # TODO: job.model_dump(mode="json")


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
