FROM registry.gitlab.com/timestep-ai/timestep:latest

# Install caddy with arkade
ENV CADDY_VERSION=v2.7.4
RUN ark get caddy --version ${CADDY_VERSION}

RUN mkdir -p /home/ubuntu/app
WORKDIR /home/ubuntu/app

COPY --chown=ubuntu:ubuntu . .

# TODO: Remove frontend from .gitignore, build it here and update the Caddyfile to serve the dist files

EXPOSE 2019

# CMD ["caddy", "run", "--config", "src/Caddyfile", "--adapter", "caddyfile"]

CMD ["caddy", "run", "--config", "Caddyfile", "--adapter", "caddyfile"]
