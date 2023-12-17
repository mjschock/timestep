FROM registry.gitlab.com/timestep-ai/timestep:latest

# Install kubectl with arkade
ENV KUBECTL_VERSION=1.27.4
RUN ark get kubectl --version v${KUBECTL_VERSION}

RUN mkdir -p /home/ubuntu/app
WORKDIR /home/ubuntu/app

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Create virtual env
RUN python -m venv /home/ubuntu/app/.venv

COPY --chown=ubuntu:ubuntu ./pyproject.toml ./poetry.lock* ./
RUN mkdir -p /home/ubuntu/app/src/lib
COPY --chown=ubuntu:ubuntu ./src/lib ./src/lib
RUN poetry install --no-root

COPY --chown=ubuntu:ubuntu . ./
RUN poetry install

EXPOSE 5000

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
# RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
# USER appuser

ENTRYPOINT ["/home/ubuntu/app/docker-entrypoint.sh"]
# CMD ["poetry", "run", "uvicorn", "src.web.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "5000"]
# CMD ["poetry", "run", "python", "-m", "src.web.server"]
CMD ["poetry", "run", "python", "src/web/server.py"]

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
# CMD ["gunicorn", "--bind", "0.0.0.0:5000", "-k", "uvicorn.workers.UvicornWorker", "src.timestep/services/web/src/web/main:app"]
