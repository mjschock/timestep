import time
import uuid
from typing import List, Optional

from openai.types.beta.thread import Thread
from openai.types.beta.threads.message import Message, MessageContent
from openai.types.beta.threads.run import Run
from openai.types.beta.threads.text import Text
from openai.types.beta.threads.text_content_block import TextContentBlock

from timestep.database import InstanceStoreSingleton


# def get_run(thread_id, run_id):  # noqa: E501
async def get_run(run_id, thread_id, token_info, user):
    """Retrieves a run.

     # noqa: E501

    :param thread_id: The ID of the [thread](/docs/api-reference/threads) that was run.
    :type thread_id: str
    :param run_id: The ID of the run to retrieve.
    :type run_id: str

    :rtype: Union[RunObject, Tuple[RunObject, int], Tuple[RunObject, int, Dict[str, str]]
    """
    print("=== get_run ===")

    # return InstanceStoreSingleton()._shared_instance_state["runs"].get(run_id).model_dump(mode="json")
    return InstanceStoreSingleton()._shared_instance_state["runs"].get(run_id)


# def modify_run(thread_id, run_id, modify_run_request):  # noqa: E501
async def modify_run(modify_run_request, run_id, token_info, thread_id, user, **kwargs):
    """Modifies a run.

     # noqa: E501

    :param thread_id: The ID of the [thread](/docs/api-reference/threads) that was run.
    :type thread_id: str
    :param run_id: The ID of the run to modify.
    :type run_id: str
    :param modify_run_request:
    :type modify_run_request: dict | bytes

    :rtype: Union[RunObject, Tuple[RunObject, int], Tuple[RunObject, int, Dict[str, str]]
    """
    # if connexion.request.is_json:
    #     modify_run_request = ModifyRunRequest.from_dict(connexion.request.get_json())  # noqa: E501

    print("=== modify_run ===")
    print("modify_run_request: ", modify_run_request)
    # print('args: ', args)
    print("kwargs: ", kwargs)

    run: Run = Run(
        **await get_run(
            run_id=run_id, token_info=token_info, thread_id=thread_id, user=user
        )
    )

    run.status = modify_run_request.get("status")

    InstanceStoreSingleton()._shared_instance_state["runs"][run_id] = run

    # return run.model_dump(mode="json")
    return run
