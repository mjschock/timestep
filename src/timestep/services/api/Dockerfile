FROM registry.gitlab.com/timestep-ai/timestep:latest

WORKDIR /home/ubuntu/src/timestep/services/api

COPY --chown=ubuntu:ubuntu . ./

CMD ["poetry", "run", "uvicorn", "app.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "5000"]
