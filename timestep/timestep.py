import logging

import reflex as rx

from timestep.pages import *
from timestep.utils import add_api_routes, create_sky_config, load_kubeconfig

logger = logging.getLogger(__name__)
root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)

class State(rx.State):
    """Define empty state to allow access to rx.State.router."""


# Create the app.
app = rx.App()

logger.debug("debug message")
logger.info("info message")
logger.warning("warn message")
logger.error("error message")
logger.critical("critical message")

# app = add_api_routes(app)

async def api_test(item_id: int):
    return {"my_result": item_id}

app.api.add_api_route("/items/{item_id}", api_test)
