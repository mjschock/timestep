FROM registry.gitlab.com/timestep-ai/timestep:latest

USER root

# Install Litestream
RUN wget https://github.com/benbjohnson/litestream/releases/download/v0.3.13/litestream-v0.3.13-linux-amd64.deb && \
    dpkg -i litestream-v0.3.13-linux-amd64.deb && \
    rm litestream-v0.3.13-linux-amd64.deb

RUN apt-get update && apt-get install -y --no-install-recommends \
  dos2unix \
  && rm -rf /var/lib/apt/lists/*

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
RUN poetry install --no-directory --no-root

COPY --chown=ubuntu:ubuntu . ./
RUN poetry install --no-root

EXPOSE 8000

ENTRYPOINT ["/home/ubuntu/app/docker-entrypoint.sh"]
CMD ["poetry", "run", "python", "main.py"]
