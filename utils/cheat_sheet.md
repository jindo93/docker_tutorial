https://docs.docker.com/engine/docker-overview/

#### List Docker CLI commands

`docker`
`docker container --help`

#### Display Docker version and info

`docker --version`
`docker version`
`docker info`

#### Execute Docker image

`docker run hello-world`

#### List Docker images

`docker image ls`

#### List Docker containers (running, all, all in quiet mode)

`docker container ls`
`docker container ls --all`
`docker container ls -aq`

#### Build Docker App

`docker build --tag=mytagforapp`

#### Run Docker App

`docker run -p 4000:80 mytagforapp`

#### Run Docker App in background

`docker run -d -p 4000:80 friendlyhello`

#### Stop Docker App

`docker container stop CONTAINER_ID`

#### Force shutdown of the specified container

`docker container kill <hash>`

#### Remove specified container from this machine

`docker container rm <hash>`

#### Remove all containers

`docker container rm \$(docker container ls -a -q)`

#### List all images on this machine

`docker image ls -a`

#### Remove specified image from this machine

`docker image rm <image id>`

#### Remove all images from this machine

`docker image rm \$(docker image ls -a -q)`

#### Log in this CLI session using your Docker credentials

`docker login`

#### Tag <image> for upload to registry

`docker tag <image> username/repository:tag`

#### Upload tagged image to registry

`docker push username/repository:tag`

#### Run image from a registry

`docker run username/repository:tag`

#### List stacks or apps

`docker stack ls`

#### Run the specified Compose file

`docker stack deploy -c <composefile> <appname>`

#### List running services associated with an app

`docker service ls`

#### List tasks associated with an app

`docker service ps <service>`

#### Inspect task or container

`docker inspect <task or container>`

#### List container IDs

`docker container ls -q`

#### Tear down an application

`docker stack rm <appname>`

#### Take down a single node swarm from the manager

`docker swarm leave --force`

## Proxy server sttings (Linux)

#### Set proxy server, replace host:port with values for your servers

`ENV http_proxy host:port`
`ENV https_proxy host:port`

## DNS settings

#### Edit the configuration file at /etc/docker/daemon.json with the dns key

#### First item is your DNS server, second item is Google's DNS, which can be used when the first one is not available.

```
{
"dns": ["your_dns_address", "8.8.8.8"]
}
```

#### Find docker toolbox ip address

`docker-machine ip`
