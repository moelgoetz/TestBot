#!/bin/bash

APP_NAME='/usr/bin/ollama'

echo "Hello, World!"
$APP_NAME serve &
sleep 10
#/usr/bin/ollama pull llama3.2
/usr/bin/ollama run llama3.2
/usr/bin/bash
