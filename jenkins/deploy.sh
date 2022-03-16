#!/bin/bash

echo "Deploy stage"

scp docker-compose.yaml jenkins@Swarm-manager:/home/jenkins/docker-compose.yaml
ssh jenkins@Swarm-manager \
    MYSQL_ROOT_PASSWORD=$MYSQL_ROOT_PASSWORD \
    SECRET_KEY=$SECRET_KEY \
    docker stack deploy --compose-file docker-compose.yaml carclubapp
