FROM registry.gitlab.com/timestep-ai/timestep:latest

ARG QUASAR_CLI_VERSION
ENV QUASAR_CLI_VERSION=${QUASAR_CLI_VERSION:-2.2.3}
RUN npm install -g @quasar/cli@${QUASAR_CLI_VERSION}

RUN mkdir -p /home/ubuntu/app/node_modules && chown -R ubuntu:ubuntu /home/ubuntu/app
WORKDIR /home/ubuntu/app

COPY --chown=ubuntu:ubuntu package*.json ./
# RUN npm ci
RUN npm install

COPY --chown=ubuntu:ubuntu . .
RUN npm run build

EXPOSE 9000

CMD ["quasar", "serve", "dist/spa", "--hostname", "0.0.0.0", "-p", "9000"]
