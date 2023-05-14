#!/bin/sh

primary="timestep"
context="k3s-cluster"

getNodeIP() {
    echo $(multipass list | grep $1 | awk '{print $3}')
}

installK3sPrimaryNode() {
    PRIMARY_IP=$(getNodeIP $1)

    k3sup install \
        --context "$context" \
        --ip "$PRIMARY_IP" \
        --local-path ./src/conf/kube.yaml \
        --merge \
        --ssh-key "${PRIVATE_SSH_KEY_PATH}" \
        --user ubuntu
        # --user "$USER"
}

installK3sPrimaryNode $primary
