#!/bin/bash

docker-compose build
docker-compose up -d
docker exec -it postgres psql -U root test
