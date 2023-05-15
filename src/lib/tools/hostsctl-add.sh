#!/usr/bin/env bash

ip=$(jq '.timestep."localhost-ipv4"' dist/deploy/infra/outputs.json)

hostctl backup --host-file /etc/hosts --path data/backups

echo sudo $(which hostctl) add domains timestep-ai kubernetes.localhost --host-file /etc/hosts --ip $ip
echo sudo $(which hostctl) add domains timestep-ai example1.kubernetes.localhost --host-file /etc/hosts --ip $ip
echo sudo $(which hostctl) add domains timestep-ai example2.kubernetes.localhost --host-file /etc/hosts --ip $ip

echo sudo $(which hostctl) remove timestep-ai
