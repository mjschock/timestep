import logging

from fastapi import FastAPI
import reflex as rx
from reflex.constants import LogLevel

from timestep.pages import *
from timestep.utils import create_sky_config, load_kubeconfig, serve, train
from timestep.routes.sky_router import add_api_routes as add_sky_api_routes
from rxconfig import config

log_level: LogLevel = config.get_value("loglevel").name
print("log_level: ", log_level)

# root_logger = logging.getLogger()
# root_logger.setLevel(level=log_level)
                     
# logger = logging.getLogger(__name__)
# logger.setLevel(level=root_logger.getEffectiveLevel())

# loggers = [logging.getLogger(name) for name in logging.root.manager.loggerDict]
# # print('loggers: ', loggers)

# # logger = logging.getLogger('fastapi')
# logger = logging.getLogger('uvicorn')

# print(f"=== {__name__} ===", flush=True)
# logger.debug("debug message")
# logger.info("info message")
# logger.warning("warn message")
# logger.error("error message")
# logger.critical("critical message")

# Configure logging
# logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='w',
#                     format='%(name)s - %(levelname)s - %(message)s')
# logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

# # Example of logging
# logging.debug("This is a debug message")
# logging.info("This is an info message")
# logging.warning("This is a warning message")
# logging.error("This is an error message")
# logging.critical("This is a critical message")

# logger = logging

root_logger = logging.getLogger()
root_logger.setLevel(level=log_level)

# create logger
logger = logging.getLogger(__name__)
# logger.setLevel(level=log_level)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(level=log_level)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
# logger.addHandler(ch)
root_logger.addHandler(ch)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')

# loggers = ['fastapi', 'uvicorn', 'reflex']

# for _logger in loggers:
#     print(f'{_logger} level: {logging.getLogger(_logger).getEffectiveLevel()}')

class State(rx.State):
    """Define empty state to allow access to rx.State.router."""


# Create the app.
app = rx.App()

app = add_sky_api_routes(app)

async def lifespan(app: FastAPI):
    logger.info('=== lifespace ===')
    create_sky_config(overwrite=True)

app.register_lifespan_task(
    task=lifespan,
    # task_kwargs={
    #     "logger": logger,
    # }
)
