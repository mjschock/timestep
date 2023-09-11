ARG UBUNTU_VERSION=22.04

FROM ubuntu:${UBUNTU_VERSION} as base

ARG GOENV_VERSION
ARG NODENV_VERSION
ARG PYENV_VERSION

ENV GOENV_VERSION=${GOENV_VERSION:-1.20.2}
ENV LANG en_US.utf8
ENV NODENV_VERSION=${NODENV_VERSION:-18.17.1}
ENV PYENV_VERSION=${PYENV_VERSION:-3.11.3}
ENV TZ=America/Los_Angeles

RUN apt-get update && apt-get install -y --no-install-recommends \
  locales=2.35-0ubuntu3.1 \
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
  net-tools \
  sudo \
  swig \
  tk-dev \
  unzip \
  xz-utils \
  zlib1g-dev \
  && rm -rf /var/lib/apt/lists/*

# RUN apt-get update && apt-get install -y software-properties-common && add-apt-repository universe
# RUN curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
# RUN echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | tee /etc/apt/sources.list.d/ros2.list > /dev/null

# RUN apt-get update && apt-get install -y --no-install-recommends \
#   ros-iron-ros-base \
#   && rm -rf /var/lib/apt/lists/*

# RUN add-apt-repository ppa:deadsnakes/ppa && apt-get update && apt-get install -y --no-install-recommends \
#   python-is-python3 \
#   python3.11 \
#   python3.11-dev \
#   python3.11-distutils \
#   python3.11-venv \
#   && rm -rf /var/lib/apt/lists/*

# RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 110
# RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 111
# RUN update-alternatives --config python3 --skip-auto

RUN groupadd --gid 123 --system ubuntu && useradd --create-home -g ubuntu --no-log-init --shell /bin/bash --system --uid 1001 ubuntu

SHELL [ "/bin/bash", "-c" ]
USER ubuntu
WORKDIR /home/ubuntu

# Install arkade
RUN mkdir -p /home/ubuntu/.local/bin
RUN curl -sLS https://get.arkade.dev | sh
RUN mv arkade /home/ubuntu/.local/bin/arkade
RUN ln -sf /home/ubuntu/.local/bin/arkade /home/ubuntu/.local/bin/ark
ENV PATH="/home/ubuntu/.arkade/bin:/home/ubuntu/.local/bin:${PATH}"

# Install terraform with arkade
ENV TERRAFORM_VERSION=1.5.5
RUN ark get terraform --version ${TERRAFORM_VERSION}

# Install k3sup with arkade
ENV K3SUP_VERSION=0.12.14
RUN ark get k3sup --version ${K3SUP_VERSION}

# Install anyenv
RUN git clone https://github.com/anyenv/anyenv ~/.anyenv
ENV PATH="/home/ubuntu/.anyenv/bin:${PATH}"
RUN anyenv install --force-init

# Install goenv with anyenv
RUN anyenv install goenv
ENV PATH="/home/ubuntu/.anyenv/envs/goenv/shims:/home/ubuntu/.anyenv/envs/goenv/bin:${PATH}"

# Install ${GOENV_VERSION} with goenv
RUN eval "$(anyenv init -)" && goenv install ${GOENV_VERSION}

# Install Kompose with go
ENV KOMPOSE_VERSION=latest
RUN go install github.com/kubernetes/kompose@${KOMPOSE_VERSION}

# Install nodenv with anyenv
RUN anyenv install nodenv
ENV PATH="/home/ubuntu/.anyenv/envs/nodenv/shims:/home/ubuntu/.anyenv/envs/nodenv/bin:${PATH}"

# Install ${NODENV_VERSION} with nodenv
RUN eval "$(anyenv init -)" && nodenv install ${NODENV_VERSION}

# Install cdktf-cli with npm
ENV CDKTF_CLI_VERSION=latest
RUN npm install --global cdktf-cli@${CDKTF_CLI_VERSION}

# Install pyenv with anyenv
RUN anyenv install pyenv
ENV PATH="/home/ubuntu/.anyenv/envs/pyenv/shims:/home/ubuntu/.anyenv/envs/pyenv/bin:${PATH}"

# Install ${PYENV_VERSION} with pyenv
RUN eval "$(anyenv init -)" && pyenv install ${PYENV_VERSION}

# Install pipx with pip
RUN python3 -m pip install --user pipx

# Install poetry with pipx
RUN pipx install poetry

# Create virtual env
RUN python -m venv /home/ubuntu/.venv

# Install CMake with pip
ENV CMAKE_VERSION=3.27.1
RUN pip install --user CMake==${CMAKE_VERSION}

# Install pyproject dependencies with poetry
COPY --chown=ubuntu:ubuntu ./pyproject.toml ./poetry.lock* ./
RUN poetry install --no-root

# Generate cdktf imports with cdktf (requires cdktf-cli from npm, cdktf-lib from poetry, and terraform from arkade)
# RUN mkdir -p src/timestep/infra/imports
# COPY --chown=ubuntu:ubuntu ./src/timestep/infra/imports/ ./src/timestep/infra/imports/
# COPY --chown=ubuntu:ubuntu ./cdktf.json ./
# RUN poetry run cdktf get --language python --log-level WARNING --output src/timestep/infra/imports

# Copy the rest of the project and install it with poetry
COPY --chown=ubuntu:ubuntu . ./
RUN poetry install

VOLUME /home/ubuntu/secrets
ENTRYPOINT ["/home/ubuntu/docker-entrypoint.sh"]
CMD ["--help"]
