#!/bin/bash

if [ -f artifacs/ollama-linux-amd64.tgz ]; then
    ./update-ollama
fi

podman build -f Dockerfile -t chatbot .
