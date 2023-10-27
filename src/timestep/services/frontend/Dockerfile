FROM registry.gitlab.com/timestep-ai/timestep:latest

ENV QUASAR_CLI_VERSION=2.2.3
RUN npm install -g @quasar/cli@${QUASAR_CLI_VERSION}

WORKDIR /home/ubuntu/src/timestep/platform/services/frontend

COPY --chown=ubuntu:ubuntu package.json package-lock.json ./
RUN npm install

COPY --chown=ubuntu:ubuntu . .
RUN npm run build

EXPOSE 9000

CMD ["quasar", "serve", "dist/spa", "--hostname", "0.0.0.0", "-p", "9000"]
