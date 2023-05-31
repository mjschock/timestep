#!/usr/bin/env bash

mkdir -p dist/.ssh

comment="m@mjschock.com"

ssh-keygen -t rsa -C $comment -f ./dist/.ssh/id_rsa -N ""
