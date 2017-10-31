# Docker overview

## The Docker platform
Docker provides tooling and a platform to manage the lifecycle of your containers:
- Develop your application and its supporting components using containers.
- The container becomes the unit for distributing and testing your application.
- When you’re ready, deploy your application into your production environment, as a container or an orchestrated service. This works the same whether your production environment is a local data center, a cloud provider, or a hybrid of the two.

## Docker Engine
Docker Engine is a client-server application with these major components:
- A server which is a type of long-running program called a daemon process (the dockerd command).
- A REST API which specifies interfaces that programs can use to talk to the daemon and instruct it what to do.
- A command line interface (CLI) client (the docker command), which is just a wrapper of Docker REST API.

## What can I use Docker for?
- Fast, consistent delivery of your applications
    Docker streamlines the development lifecycle by allowing developers to work in standardized environments using local containers
    ,which provide your applications and services. Containers are great for continuous integration and continuous development (CI/CD) workflows.
- Responsive deployment and scaling
- Running more workloads on the same hardware

## Docker architecture
### The Docker daemon (dockerd)
    The Docker daemon listens for Docker API requests and manages Docker objects such as images, containers, networks, and volumes. A daemon can also communicate with other daemons to manage Docker services.
### The Docker client (docker)
### Docker registries
    A Docker registry stores Docker images.
    **Docker Hub** and **Docker Cloud** are public registries that anyone can use, and Docker is configured to look for images on Docker Hub by default.
### Docker objects
#### IMAGES
    An image is a read-only template with instructions for creating a Docker container. Often, an image is based on another image, with some additional customization.
    To build your own image, you create a Dockerfile with a simple syntax for defining the steps needed to create the image and run it.
    **Each instruction** in a Dockerfile creates **a layer** in the image.
    When you change the Dockerfile and rebuild the image, only those layers which have changed are rebuilt.
#### CONTAINERS
    A container is a runnable instance of an image.
    You can create, start, stop, move, or delete a container using the Docker API or CLI.
    You can connect a container to one or more networks, attach storage to it, or even create a new image based on its current state. (docker container commit, Create a new image from a container's changes.)
    When a container is removed, any changes to its state that are not stored in persistent storage disappear.
#### SERVICES
Services allow you to scale containers across multiple Docker daemons, which all work together as a swarm with multiple managers and workers.
By default, the service is load-balanced across all worker nodes. To the consumer, the Docker service appears to be a single application.


## The underlying technology
### Namespaces
Docker Engine uses namespaces such as the following on Linux:
The pid namespace: Process isolation (PID: Process ID).
The net namespace: Managing network interfaces (NET: Networking).
The ipc namespace: Managing access to IPC resources (IPC: InterProcess Communication).
The mnt namespace: Managing filesystem mount points (MNT: Mount).
The uts namespace: Isolating kernel and version identifiers. (UTS: Unix Timesharing System).
### Control groups
A cgroup limits an application to a specific set of resources.
Control groups allow Docker Engine to share available hardware resources to containers and optionally enforce limits and constraints.
### Union file systems
### Container format
Docker Engine combines the namespaces, control groups, and UnionFS into a wrapper called a container format.
The default container format is **libcontainer**.
