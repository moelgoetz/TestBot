#!/bin/bash

# exit on any error
set -e

# install dependencies
apt-get update
apt-get install -y \
    curl \
    pciutils

# install ollama
curl -fsSL https://ollama.com/install.sh | sh

# post-build cleanup
rm -rf /var/lib/apt/lists/*




# install dependencies
#zypper in -y \
#    ollama \
#    systemd

