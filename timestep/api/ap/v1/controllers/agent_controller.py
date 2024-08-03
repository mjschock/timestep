async def create_agent_task(*args, **kwargs):
    """Creates a task for the agent.

     # noqa: E501

    :param task_request_body:
    :type task_request_body: dict | bytes

    :rtype: Union[Task, Tuple[Task, int], Tuple[Task, int, Dict[str, str]]
    """
    # if connexion.request.is_json:
    #     task_request_body = TaskRequestBody.from_dict(
    #         connexion.request.get_json()
    #     )  # noqa: E501
    # raise NotImplementedError

    print(f"args: {args}")
    print(f"kwargs: {kwargs}")

    return {
        "ok": True,
    }


async def download_agent_task_artifact(task_id, artifact_id):  # noqa: E501
    """Download a specified artifact.

     # noqa: E501

    :param task_id: ID of the task
    :type task_id: str
    :param artifact_id: ID of the artifact
    :type artifact_id: str

    :rtype: Union[file, Tuple[file, int], Tuple[file, int, Dict[str, str]]
    """
    raise NotImplementedError


async def execute_agent_task_step(task_id, step_request_body=None):  # noqa: E501
    """Execute a step in the specified agent task.

     # noqa: E501

    :param task_id: ID of the task
    :type task_id: str
    :param step_request_body:
    :type step_request_body: dict | bytes

    :rtype: Union[Step, Tuple[Step, int], Tuple[Step, int, Dict[str, str]]
    """
    raise NotImplementedError


async def get_agent_task(task_id):  # noqa: E501
    """Get details about a specified agent task.

     # noqa: E501

    :param task_id: ID of the task
    :type task_id: str

    :rtype: Union[Task, Tuple[Task, int], Tuple[Task, int, Dict[str, str]]
    """
    raise NotImplementedError


async def get_agent_task_step(task_id, step_id):  # noqa: E501
    """Get details about a specified task step.

     # noqa: E501

    :param task_id: ID of the task
    :type task_id: str
    :param step_id: ID of the step
    :type step_id: str

    :rtype: Union[Step, Tuple[Step, int], Tuple[Step, int, Dict[str, str]]
    """
    raise NotImplementedError


async def list_agent_task_artifacts(
    task_id, current_page=None, page_size=None
):  # noqa: E501
    """List all artifacts that have been created for the given task.

     # noqa: E501

    :param task_id: ID of the task
    :type task_id: str
    :param current_page: Page number
    :type current_page: int
    :param page_size: Number of items per page
    :type page_size: int

    :rtype: Union[TaskArtifactsListResponse, Tuple[TaskArtifactsListResponse, int], Tuple[TaskArtifactsListResponse, int, Dict[str, str]]
    """
    raise NotImplementedError


async def list_agent_task_steps(
    task_id, current_page=None, page_size=None
):  # noqa: E501
    """List all steps for the specified task.

     # noqa: E501

    :param task_id: ID of the task.
    :type task_id: str
    :param current_page: Page number
    :type current_page: int
    :param page_size: Number of items per page
    :type page_size: int

    :rtype: Union[TaskStepsListResponse, Tuple[TaskStepsListResponse, int], Tuple[TaskStepsListResponse, int, Dict[str, str]]
    """
    raise NotImplementedError


# def list_agent_tasks(current_page=None, page_size=None):  # noqa: E501
async def list_agent_tasks(*args, **kwargs):
    """List all tasks that have been created for the agent.

     # noqa: E501

    :param current_page: Page number
    :type current_page: int
    :param page_size: Number of items per page
    :type page_size: int

    :rtype: Union[TaskListResponse, Tuple[TaskListResponse, int], Tuple[TaskListResponse, int, Dict[str, str]]
    """
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")

    raise NotImplementedError


async def upload_agent_task_artifacts(task_id, file, relative_path=None):  # noqa: E501
    """Upload an artifact for the specified task.

     # noqa: E501

    :param task_id: ID of the task
    :type task_id: str
    :param file: File to upload.
    :type file: str
    :param relative_path: Relative path of the artifact in the agent&#39;s workspace.
    :type relative_path: str

    :rtype: Union[Artifact, Tuple[Artifact, int], Tuple[Artifact, int, Dict[str, str]]
    """
    raise NotImplementedError
