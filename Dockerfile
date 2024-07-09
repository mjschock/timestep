# This Dockerfile is used to deploy a single-container Reflex app instance
# to services like Render, Railway, Heroku, GCP, and others.

# It uses a reverse proxy to serve the frontend statically and proxy to backend
# from a single exposed port, expecting TLS termination to be handled at the
# edge by the given platform.
FROM python:3.11

# If the service expects a different port, provide it here (f.e Render expects port 10000)
ARG PORT=8080
# Only set for local/direct access. When TLS is used, the API_URL is assumed to be the same as the frontend.
ARG API_URL
ENV PORT=$PORT API_URL=${API_URL:-http://localhost:$PORT}

# Install Caddy server inside image
RUN apt-get update -y && apt-get install -y caddy pipx && rm -rf /var/lib/apt/lists/*

RUN groupadd --system admin && useradd --gid admin --no-log-init --shell /bin/bash --system admin
SHELL [ "/bin/bash", "-c" ]
USER admin
WORKDIR /home/admin

RUN pipx ensurepath
RUN pipx install timestep==10.0.25

# Create a simple Caddyfile to serve as reverse proxy
RUN cat > Caddyfile <<EOF
:{\$PORT}

encode gzip

@backend_routes path /docs /_event/* /openapi.json /ping /_upload /_upload/*
handle @backend_routes {
	reverse_proxy localhost:8000
}

@llamafile_server_routes path /v1/*
handle @llamafile_server_routes {
	rewrite /v1/engines/copilot-codex/completions /infill?{query}
	reverse_proxy localhost:8484
}

# root * /srv
root * /home/admin/.web/_static
route {
	try_files {path} {path}/ /404.html
	file_server
}
EOF

# Copy local context to `/app` inside container (see .dockerignore)
COPY --chown=admin:admin . .

# Create virtualenv which will be copied into final container
ENV VIRTUAL_ENV=/home/admin/.venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
# RUN $uv venv
RUN python -m venv .venv

# Install app requirements and reflex inside virtualenv
# RUN $uv pip install -r requirements.txt

# Install app requirements and reflex in the container
RUN source .venv/bin/activate && pip install -r requirements.txt

# Deploy templates and prepare app
RUN source .venv/bin/activate && reflex init

# Download all npm dependencies and compile frontend
# RUN reflex export --frontend-only --no-zip && mv .web/_static/* /srv/ && rm -rf .web
RUN source .venv/bin/activate && reflex export --frontend-only --no-zip

# Needed until Reflex properly passes SIGTERM on backend.
STOPSIGNAL SIGKILL

EXPOSE $PORT

# Apply migrations before starting the backend.
CMD [ -d alembic ] && reflex db migrate; \
    caddy start && reflex run --env prod --backend-only --loglevel debug
