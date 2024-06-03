import logging

import reflex as rx

logger = logging.getLogger(__name__)


def add_api_routes(app: rx.App):
    # TODO: https://github.com/Significant-Gravitas/AutoGPT/blob/master/forge/forge/agent_protocol/middlewares.py
    # app.add_middleware(...)

    # TODO: Investigate autogen usage w/ agent protocol
    # - https://microsoft.github.io/autogen/docs/reference/agentchat/contrib/agent_eval/task/#task
    # - https://microsoft.github.io/autogen/blog/2023/11/26/Agent-AutoBuild#step-5-execute-the-task

    logger.debug("debug message")
    logger.info("info message")
    logger.warning("warn message")
    logger.error("error message")
    logger.critical("critical message")

    return app
