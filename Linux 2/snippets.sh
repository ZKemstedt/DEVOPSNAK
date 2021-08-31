# clean old images
# https://www.digitalocean.com/community/tutorials/how-to-remove-docker-images-containers-and-volumes#:~:text=Remove%20a%20container%20upon%20exit,docker%20run%20%2D%2Drm%20image_name
docker images | grep "<none>" | awk '{print $3}' | xargs docker rmi;

# Copy public key
docker cp keys/dekstop.pub linux2_lab_1:/home/zephyro/dekstop.pub

# ssh key
ssh-keygen -t ed25519

# Running, Stopping containers
# https://docs.docker.com/compose/gettingstarted/
docker-compose up
    --build
    -d, -detach

docker-compose stop
docker-compose down
    --volumes



# to enable buildkit on windows
# setx DOCKER_BUILDKIT 1
# setx COMPOSE_DOCKER_CLI_BUILD 1
