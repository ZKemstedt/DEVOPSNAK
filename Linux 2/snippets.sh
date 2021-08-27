# clean old images
docker images | grep "<none>" | awk '{print $3}' | xargs docker rmi;

# Copy public key
docker cp keys/dekstop.pub linux2_lab_1:/home/zephyro/dekstop.pub

# ssh key
ssh-keygen -t ed25519


# build new image and run new container
docker-compose up --build

# buildkit global env
# setx DOCKER_BUILDKIT 1
# setx COMPOSE_DOCKER_CLI_BUILD 1
