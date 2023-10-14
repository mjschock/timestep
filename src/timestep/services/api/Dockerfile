# FROM registry.gitlab.com/timestep-ai/timestep:latest

# WORKDIR /home/ubuntu/src/timestep/services/api

# COPY --chown=ubuntu:ubuntu . ./

# CMD ["poetry", "run", "uvicorn", "app.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "5000"]

FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11

# ARG DOCKER_IMAGE_REF
# ENV DOCKER_IMAGE_REF=$DOCKER_IMAGE_REF

# RUN echo "Bulding Docker image ref: $DOCKER_IMAGE_REF"

# ARG IMAGE_TASK="registry.gitlab.com/timestep-ai/timestep/api"
# ENV IMAGE_TASK=$IMAGE_TASK

WORKDIR /app/

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

# Copy poetry.lock* in case it doesn't exist in the repo
COPY ./app/pyproject.toml ./app/poetry.lock* /app/

# Allow installing dev dependencies to run tests
ARG INSTALL_DEV=false
RUN bash -c "if [ $INSTALL_DEV == 'true' ] ; then poetry install --no-root ; else poetry install --no-root --no-dev ; fi"

# For development, Jupyter remote kernel, Hydrogen
# Using inside the container:
# jupyter lab --ip=0.0.0.0 --allow-root --NotebookApp.custom_display_url=http://127.0.0.1:8888
ARG INSTALL_JUPYTER=false
RUN bash -c "if [ $INSTALL_JUPYTER == 'true' ] ; then pip install jupyterlab ; fi"

COPY ./app /app
ENV PYTHONPATH=/app
