FROM bitnami/postgresql-repmgr:16.0.0

USER root

RUN apt-get update && apt-get install -y \
    postgresql-common && \
    /usr/share/postgresql-common/pgdg/apt.postgresql.org.sh && \
    apt-get update && apt-get install -y \
    postgresql-16-pgvector \
    && rm -rf /var/lib/apt/lists/*

USER 1001
