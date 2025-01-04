#!/usr/bin/env bash
set -e # exit on error

if [ -f /usr/local/bin/k3s-agent-uninstall.sh ]; then
    echo "Uninstalling k3s agent"
    /usr/local/bin/k3s-agent-uninstall.sh
fi

if [ -f /usr/local/bin/k3s-uninstall.sh ]; then
    echo "Uninstalling k3s server"
    /usr/local/bin/k3s-uninstall.sh
fi

if [ -d ~/.config/timestep ]; then
    echo "Removing timestep config"
    rm -rf ~/.config/timestep
fi

# if [ -f ~/.kube/config ]; then
#     echo "Removing kube config"
#     rm ~/.kube/config
# fi

if [ -d ~/.sky ]; then
    echo "Removing sky config"
    rm -rf ~/.sky

    mkdir ~/.sky

    cat <<EOF > ~/.sky/config.yaml
serve:
    controller:
        resources:
            cpus: 1+
            disk_size: 2
EOF
fi

if [ -d dist ]; then
    echo "Removing dist"
    rm -rf dist
fi

if [ -d timestep-ai ]; then
    echo "Removing timestep-ai"
    rm -rf timestep-ai
fi
