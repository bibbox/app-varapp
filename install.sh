#!/usr/bin/env bash

chmod -R 777 data

docker network create bibbox-default-network

docker-compose up -d
