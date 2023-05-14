#!/usr/bin/env bash
set -e

if [ "$1" = 'timestep' ]; then
    # chown -R timestep "$TIMESTEP_DATA"

    # if [ -z "$(ls -A "$TIMESTEP_DATA")" ]; then
    #     gosu timestep initdb
    # fi

    exec gosu timestep "$@"
fi

exec "$@"
