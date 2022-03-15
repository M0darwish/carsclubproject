#!/bin/bash

echo "Setup stage"

# make sure jq & curl is installed
sudo apt-get update
sudo apt-get install -y curl jq

# #install docker
curl https://get.docker.com | sudo bash

# #adds jenkins to docker group:
sudo usermod -aG docker jenkins

#install docker-compose
#set which version to download (latest)
version=$(curl -s https://api.github.com/repos/docker/compose/releases/latest | jq -r '.tag_name')
# download to /usr/local/bin/docker-compose
sudo curl -L "https://github.com/docker/compose/releases/download/${version}/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
# make the file executable
sudo chmod +x /usr/local/bin/docker-compose

#Docker login
docker login --username $DOCKER_HUB_CREDS_USR --password $DOCKER_HUB_CREDS_PSW