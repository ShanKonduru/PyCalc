REM remove all Images 
docker rmi | (docker images -q)

REM Force remove all Images 
docker rmi -f | (docker images -q)

REM remove all Dangling Images
docker image prune

REM Remove all the containers in the docker-machine.
docker rm | (docker ps -aq)

REM Force Remove all the containers in the docker-machine.
docker rm -f | (docker ps -aq)

REM stop containers which are running quitely -q to silence the numeric ids associated with those containers.
docker stop | (docker ps --filter status=running -q)

REM Filter the containers which are stopped or exited state and remove only those. -q quitely.
docker rm | (docker ps --filter status=exited -q)

REM removed all containers in exited state. That means the containers stopped.
docker container prune
