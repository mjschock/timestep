# # This Dockerfile is used to deploy a simple single-container Reflex app instance.
# FROM python:3.11

# # Copy local context to `/app` inside container (see .dockerignore)
# WORKDIR /app
# COPY . .

# # Install app requirements and reflex in the container
# RUN pip install -r requirements.txt

# # Deploy templates and prepare app
# RUN reflex init

# # Download all npm dependencies and compile frontend
# RUN reflex export --frontend-only --no-zip

# # Needed until Reflex properly passes SIGTERM on backend.
# STOPSIGNAL SIGKILL

# # Always apply migrations before starting the backend.
# CMD [ -d alembic ] && reflex db migrate; reflex run --env prod

# This docker file is intended to be used with docker compose to deploy a production
# instance of a Reflex app.

# Stage 1: init
# FROM python:3.11 as init

# ARG uv=/root/.cargo/bin/uv

# # Install `uv` for faster package boostrapping
# ADD --chmod=755 https://astral.sh/uv/install.sh /install.sh
# RUN /install.sh && rm /install.sh

# # Copy local context to `/app` inside container (see .dockerignore)
# WORKDIR /app
# COPY . .
# RUN mkdir -p /app/data /app/uploaded_files

# # Create virtualenv which will be copied into final container
# ENV VIRTUAL_ENV=/app/.venv
# ENV PATH="$VIRTUAL_ENV/bin:$PATH"
# RUN $uv venv

# # Install app requirements and reflex inside virtualenv
# RUN $uv pip install -r requirements.txt

# # Deploy templates and prepare app
# RUN reflex init
# # ENV API_URL=https://app.timestep.local

# # RUN API_URL=${API_URL} reflex init

# # Export static copy of frontend to /app/.web/_static
# RUN reflex export --frontend-only --no-zip
# # TODO: API_URL=http://app.example.com:8000 reflex export --frontend-only --no-zip

# # Copy static files out of /app to save space in backend image
# RUN mv .web/_static /tmp/_static
# RUN rm -rf .web && mkdir .web
# RUN mv /tmp/_static .web/_static

# # Stage 2: copy artifacts into slim image 
# FROM python:3.11-slim
# WORKDIR /app
# RUN adduser --disabled-password --home /app reflex
# COPY --chown=reflex --from=init /app /app
# # Install libpq-dev for psycopg2 (skip if not using postgres).
# RUN apt-get update -y && apt-get install -y libpq-dev && rm -rf /var/lib/apt/lists/*
# USER reflex
# ENV PATH="/app/.venv/bin:$PATH"

# # Needed until Reflex properly passes SIGTERM on backend.
# STOPSIGNAL SIGKILL

# # Always apply migrations before starting the backend.
# # CMD reflex db migrate && reflex run --env prod --backend-only
# CMD reflex run --env prod --backend-only

ARG VERSION=8.2.0

FROM registry.gitlab.com/timestep-ai/timestep:${VERSION} as base

USER root

# Install Litestream
# RUN wget https://github.com/benbjohnson/litestream/releases/download/v0.3.13/litestream-v0.3.13-linux-amd64.deb && \
#     dpkg -i litestream-v0.3.13-linux-amd64.deb && \
#     rm litestream-v0.3.13-linux-amd64.deb

# RUN apt-get update && apt-get install -y --no-install-recommends \
#   dos2unix \
#   && rm -rf /var/lib/apt/lists/*

# RUN mkdir -p /home/ubuntu/.sky && chown ubuntu:ubuntu /home/ubuntu/.sky
# RUN mkdir -p /home/ubuntu/.ssh && chown ubuntu:ubuntu /home/ubuntu/.ssh

USER ubuntu

# Install kubectl with arkade
ENV KUBECTL_VERSION=1.27.4
RUN ark get kubectl --version v${KUBECTL_VERSION}

RUN mkdir -p /home/ubuntu/app
WORKDIR /home/ubuntu/app

# RUN npm install --global newman

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Create virtual env
RUN python -m venv /home/ubuntu/app/.venv

# COPY --chown=ubuntu:ubuntu ./pyproject.toml ./poetry.lock* ./
# RUN poetry install --no-directory --no-root
COPY --chown=ubuntu:ubuntu requirements.txt ./

COPY --chown=ubuntu:ubuntu . ./
# RUN poetry install --no-root
# RUN pip install -r requirements.txt
RUN source /home/ubuntu/app/.venv/bin/activate && pip install -r requirements.txt

RUN source /home/ubuntu/app/.venv/bin/activate && reflex init

# RUN source /home/ubuntu/app/.venv/bin/activate && reflex export --frontend-only --no-zip

# Needed until Reflex properly passes SIGTERM on backend.
STOPSIGNAL SIGKILL

EXPOSE 8000

# CMD ["poetry", "run", "python", "main.py"]
# CMD ["reflex", "run", "--env", "prod", "--backend-only"]
# CMD ["reflex", "run", "--env", "prod"]

# Apply migrations before starting the backend.
# CMD [ -d alembic ] && reflex db migrate; \
    # caddy start && reflex run --env prod --backend-only --loglevel debug

# CMD [ "reflex", "run", "--env", "prod", "--backend-only" ]
CMD ["reflex", "run", "--env", "prod", "--loglevel", "debug"]
