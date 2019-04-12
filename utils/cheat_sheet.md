https://docs.docker.com/engine/docker-overview/

## Docker Command Cheat-sheet

| Description                                      | Commands                                                         |
| ------------------------------------------------ | ---------------------------------------------------------------- |
| Docker CLI                                       | `docker`                                                         |
| Docker help                                      | `docker container --help`                                        |
| Docker version                                   | `docker version`                                                 |
| Docker info                                      | `docker info`                                                    |
| Docker tool box IP address                       | `docker-machine ip`                                              |
| List images                                      | `docker image ls`                                                |
| List running containers                          | `docker container ls`                                            |
| List all containers                              | `docker container ls --all`                                      |
| List all containers in quiet mode                | `docker container ls -aq`                                        |
| ---                                              | ---                                                              |
| Build app                                        | `docker build --tag=mytagforapp`                                 |
| Run app                                          | `docker run -p 4000:80 mytagforapp`                              |
| Run app in background                            | `docker run -d -p 4000:80 mytagforapp`                           |
| Stop running app                                 | `docker container stop CONTAINER_ID`                             |
| Force shutdown container                         | `docker container kill <hash>`                                   |
| Remove specified container in machine            | `docker container rm <hash>`                                     |
| Remove all containers                            | `docker container rm \$(docker container ls -a -q)`              |
| List all images in machine                       | `docker image ls -a`                                             |
| Remove specified image in machine                | `docker image rm <image id>`                                     |
| Remove all images in machine                     | `docker image rm \$(docker image ls -a -q)`                      |
| Login to docker                                  | `docker login`                                                   |
| Tag image for upload to registry                 | `docker tag <image> username/repository:tag`                     |
| Upload tagged image to registry                  | `docker push username/repository:tag`                            |
| Run image from a registry                        | `docker run username/repository:tag`                             |
| List stacks or apps                              | `docker stack ls`                                                |
| ---                                              | ---                                                              |
| Run the specified Compose file                   | `docker stack deploy -c <compose file> <app name>`               |
| List running services                            | `docker service ls`                                              |
| List tasks associated with an app                | `docker service ps <service>`                                    |
| Inspect task or container                        | `docker service ps <task or container>`                          |
| List container IDs                               | `docker container ls -q`                                         |
| Tear down an app                                 | `docker stack rm <app name>`                                     |
| Take down a single node swarm from the manager   | `docker swarm leave --force`                                     |
| ---                                              | ---                                                              |
| Create a VM (Mac, Linux)                         | `docker-machine create --driver virtualbox myvm1`                |
| View basic info about your node                  | `docker-machine env myvm1`                                       |
| List the nodes in your swarm                     | `docker-machine ssh myvm1 "docker node ls"`                      |
| Inspect a node                                   | `docker-machine ssh myvm1 "docker node inspect <node ID>"`       |
| View join token                                  | `docker-machine ssh myvm1 "docker swarm join-token -q worker"`   |
| Open ssh session with the VM                     | `docker-machine ssh myvm1`                                       |
| View nodes in swarm (while logged on to manager) | `docker node ls`                                                 |
| Make the worker nodoe leave the swarm            | `docker-machine ssh myvm2 "docker swarm leave"`                  |
| Make master leave, kill swarm                    | `docker-machine ssh myvm1 "docker swarm leave -f"`               |
| List VMs (\* shows which VM is running)          | `docker-machine ls`                                              |
| Start a new VM                                   | `docker-machine start myvm3`                                     |
| Show environment variables and command for myvm1 | `docker-machine env myvm1`                                       |
| Mac command to connect shell to myvm1            | `eval$(docker-machine env myvm1)`                                |
| Deploy an app (myvm1 as command shell)           | `docker stack deploy -c <file> <app>`                            |
| Copy file to node's home dir                     | `docker-machine scp docker-compose.yml myvm1:~`                  |
| Deploy an app using ssh (Compose file copied)    | `docker-machine ssh myvm1 "docker stack deploy -c <file> <app>"` |
| Disconnect shell from VMs, use native docker     | `eval $(docker-machine env -u)`                                  |
| Stop all running VMs                             | `docker-machine stop $(docker-machine ls -q)`                    |
| Delete all VMs and their disk images             | `docker-machine rm $(docker-machine ls -q)`                      |

## Proxy server sttings (Linux)

#### Set proxy server, replace host:port with values for your servers

`ENV http_proxy host:port`
`ENV https_proxy host:port`

## DNS settings

Edit the configuration file at `/etc/docker/daemon.json` with the dns key

First item is your DNS server, second item is Google's DNS, which can be used when the first one is not available.

```
{
"dns": ["your_dns_address", "8.8.8.8"]
}
```
