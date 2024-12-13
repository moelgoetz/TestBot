#!/bin/bash

if [ -f artifacs/ollama-linux-arm64.tgz ]; then
    ./update-ollama.sh
fi

docker build -f Dockerfile -t chatbot .
