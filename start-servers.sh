#!/bin/bash
DOCKER_CONFIG=${DOCKER_CONFIG:-$HOME/.docker}
if [ ! -f ${DOCKER_CONFIG}/cli-plugins/docker-compose ]
then
  echo "Installing Docker compose plugin v3"
  mkdir -p $DOCKER_CONFIG/cli-plugins
  curl -SL https://github.com/docker/compose/releases/download/v2.12.2/docker-compose-linux-x86_64 -o $DOCKER_CONFIG/cli-plugins/docker-compose
  chmod +x $DOCKER_CONFIG/cli-plugins/docker-compose
fi
docker compose down
docker compose up -d
docker exec lab3-client-keycloak-1 /opt/keycloak/bin/reset-credentials.sh