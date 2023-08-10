ARG UBUNTU_VERSION

FROM ubuntu:${UBUNTU_VERSION:-22.04} as base

ARG GOENV_VERSION
ARG NODENV_VERSION
ARG PYENV_VERSION

ENV GOENV_VERSION=${GOENV_VERSION:-1.20.2}
ENV NODENV_VERSION=${NODENV_VERSION:-18.15.0}
ENV PYENV_VERSION=${PYENV_VERSION:-3.11.3}

RUN apt-get update && apt-get install -y \
  locales \
  && rm -rf /var/lib/apt/lists/* \
  && localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8

ENV LANG en_US.utf8
ENV TZ=America/Los_Angeles

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update && apt-get install -y --no-install-recommends \
  build-essential \
  ca-certificates-java \
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

RUN groupadd -r ubuntu && useradd --create-home --no-log-init -r -g ubuntu -s /bin/bash ubuntu
# RUN chown -R ubuntu:ubuntu /home/ubuntu

SHELL [ "/bin/bash", "-c" ]
USER ubuntu
WORKDIR /home/ubuntu

ENV PATH="/home/ubuntu/.arkade/bin:/home/ubuntu/.local/bin:${PATH}"

RUN git clone https://github.com/anyenv/anyenv ~/.anyenv
ENV PATH="/home/ubuntu/.anyenv/bin:${PATH}"
RUN anyenv install --force-init

RUN anyenv install nodenv
ENV PATH="/home/ubuntu/.anyenv/envs/nodenv/shims:/home/ubuntu/.anyenv/envs/nodenv/bin:${PATH}"
RUN eval "$(anyenv init -)" && nodenv install ${NODENV_VERSION}
ENV CDKTF_CLI_VERSION=latest
RUN npm install --global cdktf-cli@${CDKTF_CLI_VERSION}

RUN anyenv install pyenv
ENV PATH="/home/ubuntu/.anyenv/envs/pyenv/shims:/home/ubuntu/.anyenv/envs/pyenv/bin:${PATH}"
RUN eval "$(anyenv init -)" && pyenv install ${PYENV_VERSION}
RUN python3 -m pip install --user pipx
RUN pipx install poetry
COPY --chown=ubuntu:ubuntu ./pyproject.toml ./poetry.lock* ./
ENV CMAKE_VERSION=3.27.1
RUN pip install --user CMake==${CMAKE_VERSION}
RUN poetry install --no-root

COPY --chown=ubuntu:ubuntu . ./
RUN poetry install

RUN curl -sLS https://get.arkade.dev | sh
RUN mv arkade /home/ubuntu/.local/bin/arkade
RUN ln -sf /home/ubuntu/.local/bin/arkade /home/ubuntu/.local/bin/ark
ENV TERRAFORM_VERSION=1.5.5
RUN ark get terraform --version ${TERRAFORM_VERSION}
RUN terraform --version

RUN poetry run cdktf get

ENTRYPOINT ["/home/ubuntu/docker-entrypoint.sh"]
CMD ["--help"]
