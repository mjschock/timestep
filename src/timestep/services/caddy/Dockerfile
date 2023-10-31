FROM registry.gitlab.com/timestep-ai/timestep:latest

# Install caddy with arkade
ENV CADDY_VERSION=v2.7.4
RUN ark get caddy --version ${CADDY_VERSION}

WORKDIR /home/ubuntu/src/timestep/services/caddy

COPY --chown=ubuntu:ubuntu . .

EXPOSE 2019

CMD ["caddy", "run", "--config", "/home/ubuntu/src/timestep/services/caddy/Caddyfile", "--adapter", "caddyfile"]
