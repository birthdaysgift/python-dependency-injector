#!/usr/bin/env bash

docker compose up \
    --no-attach=redis \
    --abort-on-container-exit \
    --exit-code-from producer

docker container rm \
    faststream-example-producer \
    faststream-example-consumer \
    faststream-example-redis

docker image rm \
    faststream-example-producer \
    faststream-example-consumer
