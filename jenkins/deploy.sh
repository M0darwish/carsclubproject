#!/bin/bash

echo "Deploy stage"

scp docker-compose.yaml jenkins@Swarm-manager:/home/jenkins/docker-compose.yaml
ssh jenkins@Swarm-manager docker stack deploy --compose-file docker-compose.yaml carclubapp