FROM registry.gitlab.com/timestep-ai/timestep:latest

# Install caddy with arkade
ENV CADDY_VERSION=v2.7.4
RUN ark get caddy --version ${CADDY_VERSION}

WORKDIR /home/ubuntu/src/timestep/platform/services/caddy

# COPY --chown=ubuntu:ubuntu . /home/ubuntu/src/timestep/platform/services/caddy
COPY --chown=ubuntu:ubuntu . .

EXPOSE 2019

# CMD ["poetry", "run", "uvicorn", "app.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "5000"]
# CMD ["poetry", "run", "uvicorn", "service.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "5000"]

CMD ["caddy", "run", "--config", "/home/ubuntu/src/timestep/platform/services/caddy/Caddyfile", "--adapter", "caddyfile"]

# # Install caddy with arkade
# ENV CADDY_VERSION=v2.7.4
# RUN ark get caddy --version ${CADDY_VERSION}
