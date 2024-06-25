ARG UBUNTU_VERSION=22.04

FROM ubuntu:${UBUNTU_VERSION} as base

ARG CADDY_VERSION
ARG DORA_VERSION
ARG GID
# ARG GOENV_VERSION
ARG LANG
ARG NODENV_VERSION
ARG PYENV_VERSION
ARG UID
ARG TZ

ENV CADDY_VERSION=${CADDY_VERSION:-v2.7.4}
ENV DORA_VERSION=${DORA_VERSION:-v0.3.2}
ENV GID=${GID:-1000}
# ENV GOENV_VERSION=${GOENV_VERSION:-1.20.2}
ENV LANG=${LANG:-en_US.utf8}
ENV NODENV_VERSION=${NODENV_VERSION:-20.14.0}
ENV PYENV_VERSION=${PYENV_VERSION:-3.11.9}
ENV UID=${UID:-1000}
ENV TZ=${TZ:-America/Los_Angeles}

RUN apt-get update && apt-get install -y --no-install-recommends \
  locales \
  && rm -rf /var/lib/apt/lists/* \
  && localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update && apt-get install -y --no-install-recommends \
  build-essential \
  ca-certificates-java \
  clang \
  curl \
  default-jdk \
  direnv \
  figlet \
  git \
  jq \
  libbz2-dev \
  libffi-dev \
  liblzma-dev \
  libncursesw5-dev \
  libnss3-tools \
  libreadline-dev \
  libsqlite3-dev \
  libssl-dev \
  libstdc++-12-dev \
  libxml2-dev \
  libxmlsec1-dev \
  netcat \
  net-tools \
  openssh-server \
  rsync \
  socat \
  sqlite3 \
  sudo \
  swig \
  tk-dev \
  unzip \
  xz-utils \
  zlib1g-dev \
  && rm -rf /var/lib/apt/lists/*

RUN locale

RUN apt-get update && apt-get install -y software-properties-common && add-apt-repository universe
RUN curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
RUN echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | tee /etc/apt/sources.list.d/ros2.list > /dev/null

RUN apt-get update && apt-get install -y --no-install-recommends \
  ros-dev-tools \
  && rm -rf /var/lib/apt/lists/*

RUN apt-get upgrade -y

RUN apt-get update && apt-get install -y --no-install-recommends \
  ros-iron-ros-base \
  && rm -rf /var/lib/apt/lists/*

RUN groupadd --gid ${GID} --system ubuntu && useradd --create-home -g ubuntu --no-log-init --shell /bin/bash --system --uid ${UID} ubuntu

# Allow ubuntu user to run sudo chown without password
RUN echo "ubuntu ALL=(ALL) NOPASSWD: /bin/chown" > /etc/sudoers.d/ubuntu

SHELL [ "/bin/bash", "-c" ]
USER ubuntu
# ENV XDG_CONFIG_HOME=/home/ubuntu/.config
# ENV XDG_DATA_HOME=/home/ubuntu/.local/share
WORKDIR /home/ubuntu

# Install arkade
RUN mkdir -p /home/ubuntu/.local/bin
RUN curl -sLS https://get.arkade.dev | sh
RUN mv arkade /home/ubuntu/.local/bin/arkade
RUN ln -sf /home/ubuntu/.local/bin/arkade /home/ubuntu/.local/bin/ark
ENV PATH="/home/ubuntu/.arkade/bin:/home/ubuntu/.local/bin:${PATH}"

# Install anyenv
RUN git clone https://github.com/anyenv/anyenv ~/.anyenv
ENV PATH="/home/ubuntu/.anyenv/bin:${PATH}"
RUN anyenv install --force-init

# Install caddy with arkade
RUN ark get caddy --version ${CADDY_VERSION}

# Install goenv with anyenv
# RUN anyenv install goenv
# ENV PATH="/home/ubuntu/.anyenv/envs/goenv/shims:/home/ubuntu/.anyenv/envs/goenv/bin:${PATH}"

# # Install ${GOENV_VERSION} with goenv
# RUN eval "$(anyenv init -)" && goenv install ${GOENV_VERSION}

# Install nodenv with anyenv
RUN anyenv install nodenv
ENV PATH="/home/ubuntu/.anyenv/envs/nodenv/shims:/home/ubuntu/.anyenv/envs/nodenv/bin:${PATH}"

# Install ${NODENV_VERSION} with nodenv
RUN eval "$(anyenv init -)" && nodenv install ${NODENV_VERSION}

# Install npm with npm
ENV NPM_VERSION=9.8.1
RUN npm install --global npm@${NPM_VERSION}

# Install pyenv with anyenv
RUN anyenv install pyenv
ENV PATH="/home/ubuntu/.anyenv/envs/pyenv/shims:/home/ubuntu/.anyenv/envs/pyenv/bin:${PATH}"

# Install ${PYENV_VERSION} with pyenv
RUN eval "$(anyenv init -)" && pyenv install ${PYENV_VERSION}

# TODO: install Rust and Dora
# RUN export ARCHITECTURE=$(uname -m) && \
#   wget https://github.com/dora-rs/dora/releases/download/${DORA_VERSION}/dora-${DORA_VERSION}-${ARCHITECTURE}-Linux.zip && \
#   unzip dora-${DORA_VERSION}-${ARCHITECTURE}-Linux.zip && \
#   pip install dora-rs==${DORA_VERSION}
#   PATH=$PATH:$(pwd)

# Install uv
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/home/ubuntu/.cargo/bin:${PATH}"

# # Install pipx with pip
# RUN python3 -m pip install --user pipx

# # Install poetry with pipx
# RUN pipx install poetry

# RUN mkdir -p /home/ubuntu/app
# WORKDIR /home/ubuntu/app

# Create virtual env
# RUN python -m venv /home/ubuntu/.venv
# RUN uv venv
# RUN uv pip install -r requirements.txt

# COPY --chown=ubuntu:ubuntu docker-entrypoint.sh .env .envrc ./
# COPY --chown=ubuntu:ubuntu docker-entrypoint.sh .
# COPY --chown=ubuntu:ubuntu requirements.txt 

ARG API_URL

ENV API_URL=${API_URL:-http://localhost:8000}

# ARG uv=/root/.cargo/bin/uv

# # Install `uv` for faster package boostrapping
# ADD --chmod=755 https://astral.sh/uv/install.sh /install.sh
# RUN /install.sh && rm /install.sh

# # Copy local context to `/app` inside container (see .dockerignore)
# WORKDIR /app
# COPY . .
# RUN mkdir -p /app/data /app/uploaded_files

RUN mkdir -p /home/ubuntu/app
WORKDIR /home/ubuntu/app

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# # Create virtualenv which will be copied into final container
# ENV VIRTUAL_ENV=/app/.venv
ENV VIRTUAL_ENV=/home/ubuntu/app/.venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
# RUN $uv venv

RUN uv venv

# # Install app requirements and reflex inside virtualenv
# RUN uv pip install -r requirements.txt

# Create virtual env
# RUN python -m venv /home/ubuntu/app/.venv
# RUN source /home/ubuntu/app/.venv/bin/activate && pip install --upgrade pip

# COPY --chown=ubuntu:ubuntu ./pyproject.toml ./poetry.lock* ./
# RUN poetry install --no-directory --no-root
COPY --chown=ubuntu:ubuntu requirements.txt ./

# RUN source /home/ubuntu/app/.venv/bin/activate && pip install -r requirements.txt

# Install app requirements and reflex inside virtualenv
RUN uv pip install -r requirements.txt

COPY --chown=ubuntu:ubuntu . ./

# # Deploy templates and prepare app
RUN reflex init

# Export static copy of frontend to /app/.web/_static
RUN API_URL=${API_URL} reflex export --frontend-only --no-zip
# RUN reflex export --frontend-only --no-zip

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
# RUN apt-get update -y && apt-get install -y libpq-dev nodejs sudo && rm -rf /var/lib/apt/lists/*
# USER reflex
# ENV PATH="/app/.venv/bin:$PATH"

# Needed until Reflex properly passes SIGTERM on backend.
STOPSIGNAL SIGKILL

# VOLUME [ "/home/ubuntu/.sky", "/home/ubuntu/.ssh" ]
# VOLUME [ "/home/ubuntu/.local/share/caddy", "/home/ubuntu/.config/caddy", "/home/ubuntu/app/data", "/home/ubuntu/app/uploaded_files" ]

ENTRYPOINT ["/home/ubuntu/app/docker-entrypoint.sh"]
CMD ["--help"]
