FROM registry.gitlab.com/timestep-ai/timestep:latest

WORKDIR /home/ubuntu/src/timestep/platform/services/web

COPY --chown=ubuntu:ubuntu . .

EXPOSE 5000

CMD ["poetry", "run", "uvicorn", "service.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "5000"]
