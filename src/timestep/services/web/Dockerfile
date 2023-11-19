FROM registry.gitlab.com/timestep-ai/timestep:latest

# Install kubectl with arkade
ENV KUBECTL_VERSION=1.27.4
RUN ark get kubectl --version v${KUBECTL_VERSION}

RUN mkdir -p /home/ubuntu/app
WORKDIR /home/ubuntu/app

# Create virtual env
RUN python -m venv /home/ubuntu/app/.venv

COPY --chown=ubuntu:ubuntu ./pyproject.toml ./poetry.lock* ./
RUN mkdir -p /home/ubuntu/app/src/lib
COPY --chown=ubuntu:ubuntu ./src/lib ./src/lib
RUN poetry install --no-root

COPY --chown=ubuntu:ubuntu . ./
RUN poetry install

EXPOSE 5000

ENTRYPOINT ["/home/ubuntu/app/docker-entrypoint.sh"]
CMD ["poetry", "run", "uvicorn", "src.web.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "5000"]
