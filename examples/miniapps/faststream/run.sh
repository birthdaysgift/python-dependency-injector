#!/usr/bin/env bash

docker compose up \
    --no-attach=redis \
    --abort-on-container-exit \
    --exit-code-from producer

