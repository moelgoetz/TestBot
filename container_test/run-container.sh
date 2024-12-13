#!/bin/bash

docker run \
    -ti \
    --rm \
    --mount type=volume,source="root_home",target="/root" \
    chatbot:latest
