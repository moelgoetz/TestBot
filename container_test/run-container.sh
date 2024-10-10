#!/bin/bash

podman run \
    -ti \
    --rm \
    --mount type=volume,source="root_home",target="/root" \
    chatbot:latest
