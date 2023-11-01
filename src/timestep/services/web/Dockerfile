FROM registry.gitlab.com/timestep-ai/timestep:latest

RUN mkdir -p /home/ubuntu/app
WORKDIR /home/ubuntu/app

# Create virtual env
RUN python -m venv /home/ubuntu/app/.venv

COPY --chown=ubuntu:ubuntu ./pyproject.toml ./poetry.lock* ./
RUN poetry install --no-root

COPY --chown=ubuntu:ubuntu . ./
RUN poetry install

EXPOSE 5000

ENTRYPOINT ["/home/ubuntu/app/docker-entrypoint.sh"]
CMD ["poetry", "run", "uvicorn", "src.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "5000"]
