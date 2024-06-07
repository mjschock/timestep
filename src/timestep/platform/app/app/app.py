"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import logging

import reflex as rx

import app.api.agents.api_router as agents_api_router

# import app.api.assistants.api_router as assistants_api_router
import app.api.bots.slack as bots_api_router

# import app.api.services.api_router as services_api_router
from app import __version__

logger = logging.getLogger(__name__)


class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        # rx.vstack(
        #     rx.heading("Timestep AI"),
        # rx.text(
        #     "Get started by editing ",
        #     rx.code(f"{config.app_name}/{config.app_name}.py"),
        #     size="5",
        # ),
        # rx.link(
        #     rx.button("Check out our docs!"),
        #     href="https://reflex.dev/docs/getting-started/introduction/",
        #     is_external=True,
        # ),
        # spacing="5",
        # justify="center",
        # min_height="85vh",
        # ),
        # rx.logo(),
    )


app = rx.App()

app.add_page(index)


async def get_version():
    return {"version": __version__}


app.api.add_api_route(
    "/api/version",
    endpoint=get_version,
    methods=["GET"],
)

agents_api_router.add_api_routes(app)
# assistants_api_router.add_api_routes(app)
bots_api_router.add_api_routes(app)
# services_api_router.add_api_routes(app)


# # @asynccontextmanager
# async def lifespan(app: FastAPI):
#     # Load the ML model
#     # ml_models["answer_to_everything"] = fake_answer_to_everything_ml_model
#     # yield
#     # # Clean up the ML models and release the resources
#     # ml_models.clear()

#     load_kubeconfig(overwrite=True)

#     await sky.check.check(
#         clouds=None,
#         quiet=False,
#         verbose=True,
#     )

#     logger.warn("Checking sky status")

#     await sky.status(
#         refresh=True,
#     )

#     service_statuses = await sky.serve.core.status()
#     print(service_statuses)
#     logger.warn(service_statuses)

# app.register_lifespan_task(
#     task=lifespan,
# )
