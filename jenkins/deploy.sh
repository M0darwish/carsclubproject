#!/bin/bash

echo "Deploy stage"

scp nginx jenkins@Swarm-manager:/home/jenkins/nginx #solve lining the service issue
scp docker-compose.yaml jenkins@Swarm-manager:/home/jenkins/docker-compose.yaml
ssh jenkins@Swarm-manager \
    MYSQL_ROOT_PASSWORD=$MYSQL_ROOT_PASSWORD \
    SECRET_KEY=$SECRET_KEY \
    docker stack deploy --compose-file docker-compose.yaml carclubapp
