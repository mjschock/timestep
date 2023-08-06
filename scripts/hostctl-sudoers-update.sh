#!/usr/bin/env bash

# Update sudoers so that we don't need to enter a password for sudo when running hostctl only
echo "$USER ALL=(ALL) NOPASSWD: $(which hostctl)" | sudo tee /etc/sudoers.d/hostctl
