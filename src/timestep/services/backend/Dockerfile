FROM registry.gitlab.com/timestep-ai/timestep:latest

USER root

# Install Litestream
RUN wget https://github.com/benbjohnson/litestream/releases/download/v0.3.13/litestream-v0.3.13-linux-amd64.deb && \
    dpkg -i litestream-v0.3.13-linux-amd64.deb && \
    rm litestream-v0.3.13-linux-amd64.deb

RUN apt-get update && apt-get install -y --no-install-recommends \
  dos2unix \
  && rm -rf /var/lib/apt/lists/*

# COPY litestream.yml /etc/litestream.yml

RUN mkdir -p /home/ubuntu/.sky && chown ubuntu:ubuntu /home/ubuntu/.sky
RUN mkdir -p /home/ubuntu/.ssh && chown ubuntu:ubuntu /home/ubuntu/.ssh

USER ubuntu

# Install kubectl with arkade
ENV KUBECTL_VERSION=1.27.4
RUN ark get kubectl --version v${KUBECTL_VERSION}

RUN mkdir -p /home/ubuntu/app
WORKDIR /home/ubuntu/app

RUN npm install --global newman

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Create virtual env
RUN python -m venv /home/ubuntu/app/.venv

COPY --chown=ubuntu:ubuntu ./pyproject.toml ./poetry.lock* ./
RUN poetry install --no-root

COPY --chown=ubuntu:ubuntu . ./
RUN poetry install

# COPY litestream.yml /etc/litestream.yml
# RUN mkdir -p /home/ubuntu/.sky && chown ubuntu:ubuntu /home/ubuntu/.sky
# RUN mkdir -p /home/ubuntu/.ssh && chown ubuntu:ubuntu /home/ubuntu/.ssh

# EXPOSE 5000
EXPOSE 8000

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
# RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
# USER appuser

ENTRYPOINT ["/home/ubuntu/app/docker-entrypoint.sh"]
# CMD ["poetry", "run", "uvicorn", "src.web.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "5000"]
# CMD ["poetry", "run", "python", "-m", "src.web.server"]
# CMD ["poetry", "run", "python", "src/web/server.py"]

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
# CMD ["gunicorn", "--bind", "0.0.0.0:5000", "-k", "uvicorn.workers.UvicornWorker", "src.timestep/services/web/src/web/main:app"]

CMD ["poetry", "run", "python", "main.py"]

# ENV ENVIRONMENT=prod

# CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--proxy-headers"]
