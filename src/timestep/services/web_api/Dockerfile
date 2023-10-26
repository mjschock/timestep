FROM registry.gitlab.com/timestep-ai/timestep:latest

# WORKDIR /home/ubuntu/src/timestep/services/api/app
WORKDIR /home/ubuntu/src/timestep/platform/services/web_api

# COPY --chown=ubuntu:ubuntu ./app /home/ubuntu/src/timestep/services/api/app/
COPY --chown=ubuntu:ubuntu . /home/ubuntu/src/timestep/platform/services/web_api

EXPOSE 5000

# CMD ["poetry", "run", "uvicorn", "app.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "5000"]
CMD ["poetry", "run", "uvicorn", "service.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "5000"]
