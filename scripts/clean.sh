#!/usr/bin/env bash
set -ex

/usr/local/bin/k3s-agent-uninstall.sh || true
/usr/local/bin/k3s-uninstall.sh || true
rm -rf ~/.config/timestep || true
rm ~/.kube/config || true
rm -rf ~/.sky || true
