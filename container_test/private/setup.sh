#!/bin/bash

# exit on any error
set -e

# add some comforts
echo "alias ll='ls -lAF'" >> /root/.bashrc

# install dependencies
apt-get update && apt-get install -y \
    curl \
    pciutils || exit 1

# install ollama
#tar -C /usr -xzf ollama-linux-amd64.tgz

# post-build cleanup
rm -rf /var/lib/apt/lists/*
