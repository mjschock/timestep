# FROM python:3.11 as requirements-stage

# RUN groupadd -r base && useradd --no-log-init -r -g base base
# USER base
# WORKDIR /home/base

# RUN python3 -m pip install --user pipx
# RUN python3 -m pipx ensurepath
# ENV PATH=/home/base/.local/bin:$PATH

# RUN pipx install poetry==1.5.1
# COPY --chown=base:base ./pyproject.toml ./poetry.lock* /home/base/
# RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

# RUN pip install --no-cache-dir --upgrade -r /home/base/requirements.txt
# COPY ./app /home/base/app

# # CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
# CMD ["uvicorn", "app.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]

# FROM osrf/ros:humble-simulation-jammy
FROM gazebo:gzserver8

# RUN apt-get update && apt-get install -y \
#   # golang-github-caddyserver-certmagic-dev \
#   curl \
#   && rm -rf /var/lib/apt/lists/*

# RUN curl -sLS https://get.arkade.dev | sudo sh

# RUN groupadd -r base && useradd --no-log-init -r -g base base
# USER base
# WORKDIR /home/base

# RUN ark get caddy

CMD [ "tail", "-f", "/dev/null" ]
# CMD [ "caddy", "file-server", "--listen", "80" ]
