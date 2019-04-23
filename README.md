# docker_tutorial

### A repository to keep track of my learning for my own reference and for anyone getting started.

### Initially used Docker tutorial from the main Docker website.

- https://docs.docker.com/get-started

### Overview: https://docs.docker.com/engine/docker-overview/

### Building Docker App

1. Define a container with Dockerfile
2. Write files for the app
3. (Optional) Run the app
4. Build the app

### Sharing & Storing image

1. Log-in
2. Tag the image
3. Push image into the repo

### Deploy App

1. Make docker-compose.yml

##### Defines how Docker containers should behave in production

2. Run `docker swarm init`

##### Enable swarm mode and make your current machine a swarm manager

3. Give the app a name
   Run `docker stack deploy -c docker-compose.yml myappname`

### Scale Docker App

- Change the `replicas` value in `docker-compose.yml`, saving the change, and re-running the `docker stack deploy` command

### Take down the app and the swarm

Run `docker stack rm getstartedlab`
Run `docker swarm leave --force`

### Docker App Hierarchy

- Stack
- Services
- Containers

## Docker file

- Defines what goes on in the environment inside your container.
- Access to resources like networking interfaces and disk drives is virtualized inside this environment, which is isolated from the rest of your system, so you need to map ports to the outside world, and be specific about what files you want to `copy in` to that environment.
- Afterwards, though, you can expect that the build of your app defined in this Dockerfile behaves the same wherever it runs.

### Proxy servers

- Peroxy servers can block connections to your web app once it`s up and running.

### DNS

- DNS misconfigurations can generate problems with pip.
- You need to set your own DNS server address to make pip work properly.

### Port mapping

- This port remapping of 4000:80 demonstrates the difference between EXPOSE within the Dockerfile and what the publish value is set to when running docker run -p. In later steps, map port 4000 on the host to port 80 in the container and use http://localhost

### Docker Architecture

#### Docker daemon:

- Listens for Docker API requests and manages Docker objects such as images, containers, networks, and volumes.
- A daemon can also communicate with other daemons to manage Docker services

#### Docker client:

- The primary way that many Docker users interact with Docker.
- When you use commands such as `docker run`, the client sends these commands to `dockerd`, which carries them out.
- The `docker` command uses the Docker API.
- The Docker client can communicate with more than one daemon.

#### Docker registries:

- Stores Docker images.
- Docker Hub is a public registry that anyone can use, and Docker is configured to look for images on Docker Hub by default.
- You can even run your own private registry.
- Docker Datacenter (DDC) includes Docker Trusted Registry (DTR).
- When you use `docker pull` or `docker run` commands, the required images are pulled from your configured registry.
- When you use the `docker push` command, your image is pushed to your configured registry.

#### Docker objects:

- Images:

  - Read-only template with instructions for creating a Docker container.
  - Can be based on another image, with some additional customization.
  - To build your own image, you create a Dockerfile with a simple syntax for defining the steps needed to create the image and run it.
  - Each instruction in a Dockerfile creates a layer in the image.
  - When you change the Dockerfile and rebuild the image, only those layers which have changed are rebuilt.

- Containers:

  - Runnable instance of an image.
  - You can create, start, stop, move,or delete a container using the Docker API or CLI.
  - You can connect a container to one or more network, attach storage to it, or even create a new image based on its current state.
  - A container is relatively well isolated from other containers and its host machine.
  - You can control how isolated a container's network, storage, or other underlying subsystems are from other containers or from the host machine.
  - A container is defined by its image as well as any configuration options you provide to it when you create or start it.
  - When a container is removed, any changes to its state that are not stored in persistent storage disappear.

- Services:
  - Allows you to scale containers across multiple Docker daemons, which all work together as a swarm with multiple managers and workers.
  - Each member of a swarm is a Docker daemon, and the daemons all communicate using the Docker API.
    A service allows you to define the desired state, such as the number of replicas of the service that must be available at any given time.
  - By default, the service is load-balanced across all worker nodes.

#### Underlying technology:

- Docker is written in Go and takes advantage of several features of the Linux kernel to deliver its functionality.

- Namespaces:

  - Docker uses a technology called `namespaces` to provide the isolated workspace called the container. When you run a container, Docker creates a set of namespaces for that container.
  - These namespaces provide a layer of isolation. Each aspect of a container runs in a separate namespace and its access is limited to that namespace.
  - Docker Engine uses namespaces such as the following on Linux:
    - The `pid` namespace: Process isolation (PID: Process ID).
    - The `net` namespace: Managing network interfaces (NET: Networking).
    - The `ipc` namespace: Managing access to IPC resources (IPC: InterProcess Communication).
    - The `mnt` namespace: Managing filesystem mount points (MNT: Mount).
    - The `uts` namespace: Isolating kernel and version identifiers. (UTS: Unix Timesharing System).

- Control groups:

  - Docker Engine on Linux also relies on another technology called control groups (`cgroups`).
  - A `cgroup` limits an application to a specific set of resources.
  - Control groups allow Docker Engine to share available hardware resources to containers and optionally enforce limits and constraints. For example, you can limit the memory available to a specific container.

- Union file system:

  - Union file systems, or UnionFS, are file systems that operate by creating layers, making them very lightweight and fast.
  - Docker Engine uses UnionFS to provide the building blocks for containers.
  - Docker Engine can use multiple UnionFS variants, including AUFS, btrfs, vfs, and DeviceMapper.

- Container format:
  - Docker Engine combines the namespaces, control groups, and UnionFS into a wrapper called a container format.
  - The default container format is `libcontainer`.
  - In the future, Docker may support other container formats by integrating with technologies such as BSD Jails or Solaris Zones.

### Swarm Clusters:

- A swarm is a group of machines that are running Docker and joined into a cluster.
- Afterwards, you continue to run the Docker commands you're used to, but now they are executed on a cluster by a **swarm manager**.
- The machines in a swarm can be physical or virtual. They are referred to as **nodes** after joining a swarm.
- Swarm managers can use several strategies to run containers:
  - `emptiest node` fills the least utilized machines with containers.
  - `global` ensures that each machine gets exactly one instance of the speficied container.
- You instruct the swarm manager to use these strategies inthe Compose file.
- Swarm managers are the only machines in a swarm that can execute your commands, or authorize other machines to join the swarm as workers.
- **Workers** are just there to provide capacity and do not have the authority to tell any other machine what it can and cannot do.
- Docker **swarm mode** enables the use of swarms; swarm mode instantly makes the current machine a swarm manager.

### Set-up your swarm:

`docker swarm init` enable swarm mode
`docker swarm join` on other machines to join the swarm as workers

### Stack

- A stack is a group of interrelated services that share dependencies, and can be orchestrated and scaled together. A single stack is capable of defining and coordinating the functionality of an entire application (though very complex applications may want to use multiple stacks).

#### Redis

- Redis always runs on the manager, so it's always using the same filesystem.
- Redis accesses an arbitrary directory in the host's file system as `/data` inside the container, which is where Redis stores data.
  - Together, this is creating a "source of truth" in your host's physical filesystem for the Redis data. Without this, Redis would store its data in `/data` inside the container's filesystem, which would get wiped out if that container were ever redeployed.
- The source of truth has two components:
  1. The placement constraint you put on the Redis service, ensuring that it always uses the same host.
  2. The volume you created that lets the container access `./data` (on the host) as `/data` (inside the Redis container).
     While containers comde and go, the files stored on `./data` on the specified host persists, enabling continuity.
