#!/bin/bash
# Displays body of message
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
