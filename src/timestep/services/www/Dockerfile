# FROM node:18-bullseye-slim
# FROM node:18-alpine
# FROM node:18

# FROM ubuntu:20.04
# RUN apt-get update \
#     && apt-get install -y --no-install-recommends mysql-client \
#     && rm -rf /var/lib/apt/lists/*
# ENTRYPOINT ["mysql"]


# RUN groupadd -r node && useradd --no-log-init -r -g node -s /bin/bash node

# ENV YARN_CACHE_FOLDER=/cache/yarn

# WORKDIR /app

# # install dependencies
# # COPY package.json yarn.lock ./
# COPY package.json package-lock.json ./
# # RUN --mount=type=cache,target=/cache/yarn \
# #   yarn install
# # RUN --mount=type=cache,target=/home/base/.npm,uid=999,gid=999 \
# #   npm install
# RUN --mount=type=cache,target=/root/.npm \
#   npm install

# # copy app source
# # COPY . ./

# # CMD ["yarn", "dev"]
# CMD ["npm", "run", "dev"]

# FROM ubuntu:22.04

# RUN apt-get update && apt-get install -y \
#   locales \
#   && rm -rf /var/lib/apt/lists/* \
#   && localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8

# ENV LANG en_US.utf8
# ENV TZ=America/Los_Angeles

# RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# RUN apt-get update && apt-get install -y --no-install-recommends \
#   build-essential \
#   ca-certificates \
#   curl \
#   direnv \
#   git \
#   libbz2-dev \
#   libffi-dev \
#   liblzma-dev \
#   libncursesw5-dev \
#   libnss3-tools \
#   libreadline-dev \
#   libsqlite3-dev \
#   libssl-dev \
#   libxml2-dev \
#   libxmlsec1-dev \
#   sudo \
#   swig \
#   tk-dev \
#   xz-utils \
#   zlib1g-dev \
#   && rm -rf /var/lib/apt/lists/*

# RUN curl -sLS https://get.arkade.dev | sudo sh
# RUN ark system install node --version v18.15.0

# RUN groupadd -r base && useradd --no-log-init -r -g base -s /bin/bash base
# USER base
# WORKDIR /home/base

# FROM alpine:3.18
# RUN apk add --no-cache mysql-client
# ENTRYPOINT ["mysql"]

FROM ubuntu:22.04

RUN apt-get update && apt-get install -y --no-install-recommends \
  # build-essential \
  ca-certificates \
  curl \
  # direnv \
  # git \
  # libbz2-dev \
  # libffi-dev \
  # liblzma-dev \
  # libncursesw5-dev \
  # libnss3-tools \
  # libreadline-dev \
  # libsqlite3-dev \
  # libssl-dev \
  # libxml2-dev \
  # libxmlsec1-dev \
  # sudo \
  # swig \
  # tk-dev \
  # xz-utils \
  # zlib1g-dev \
  && rm -rf /var/lib/apt/lists/*

RUN curl -sLS https://get.arkade.dev | sh
RUN ark system install node --version v18.15.0
RUN npm i -g @quasar/cli

RUN groupadd -r node && useradd --no-log-init -r -g node -s /bin/bash node
# WORKDIR /home/node
# COPY package.json package-lock.json ./
# RUN --mount=type=cache,target=/home/node/.npm,uid=999,gid=999 \
#   npm install
# RUN chown -R node:node /home/node/

USER node
WORKDIR /home/node

COPY --chown=node:node package.json package-lock.json ./
RUN npm install

COPY --chown=node:node . ./
RUN npm run build

CMD ["quasar", "serve", "dist/spa", "-p", "9000"]
