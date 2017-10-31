Ref:
https://docs.docker.com/get-started/

## Part 1: Orientation

Modify /etc/sudoers and re-login:
%sudo   ALL=(ALL:ALL) ALL
%docker ALL=(ALL:ALL) ALL

$ docker run hello-world

$ docker --version

=== A brief explanation of containers ===
An **image** is a lightweight, stand-alone, executable package that includes everything needed to run a piece of software, including the code, a runtime, libraries, environment variables, and config files.
A **container** is a runtime instance of an image—what the image becomes in memory when actually executed. It runs completely isolated from the host environment by default, only accessing host files and ports if configured to do so.

=== Conclusion ===
The unit of scale being an **individual, portable executable** has vast implications. It means CI/CD can push updates to any part of a distributed application, system dependencies are not an issue, and resource density is increased. Orchestration of scaling behavior is a matter of spinning up new executables, not new VM hosts.


## Part 2: Containers
Intro:
- Stack
- Services
- Container (you are here)

=== Define a container with a **Dockerfile** ===
Dockerfile will define what goes on in the environment inside your container.
Access to resources like **networking interfaces** and **disk drives** is virtualized
inside this environment, which is isolated from the rest of your system, so you have to
map ports to the outside world, and be specific about what files you want to “copy in”
to that environment.

$ mkdir _docker_ && cd _docker_
=== Prepare Dockerfile ===
$ vim Dockerfile

=== Prepare App files ===
$ vim requirements.txt
$ vim app.py

=== Build the app ===
$ docker build -t friendlyhello .

vagrant@vagrant-ubuntu-trusty-64:~/_docker_$ docker images
REPOSITORY          TAG                 IMAGE ID            CREATED              SIZE
friendlyhello       latest              755eb9c57ea5        About a minute ago   150MB
python              2.7-slim            e9adbdab327d        33 hours ago         138MB
hello-world         latest              05a3bd381fc2        6 weeks ago          1.84kB

=== Run the app ===
$ docker run -p 4000:80 friendlyhello
...

# run as daemon, which returns long container ID
$ docker run -d -p 4000:80 friendlyhello
ca602b317a88a28d12bda844f89b040c4ce11c8125f4d9b4722baa535b3b4b14

$ docker container ls
CONTAINER ID        IMAGE               COMMAND             CREATED              STATUS              PORTS                  NAMES
ca602b317a88        friendlyhello       "python app.py"     About a minute ago   Up About a minute   0.0.0.0:4000->80/tcp   distracted_jepsen

$ docker ps
CONTAINER ID        IMAGE                       COMMAND             CREATED             STATUS              PORTS                  NAMES
37e3404fa3f9        xiaotdl/get-started:part2   "python app.py"     5 seconds ago       Up 4 seconds        0.0.0.0:4000->80/tcp   confident_hodgkin

$ docker stop 37e3404fa3f9

=== Share your image ===
A registry is a collection of repositories,
a repository is a collection of images—sort of like a GitHub repository, except the code is already built.
The docker CLI uses Docker’s public registry by default.

==> Log in with your Docker ID
If you don’t have a Docker account, sign up for one at cloud.docker.com.
$ docker login

==> Tag the image
The notation for associating a local image with a repository on a registry is username/repository:tag
The tag is optional, but recommended, since it is the mechanism that registries use to give Docker images a version.
The syntax of the command is:
$ docker tag image username/repository:tag
For example:
$ docker tag friendlyhello john/get-started:part2

==> Publish the image
$ docker push username/repository:tag
Once complete, the results of this upload are publicly available.
If you log in to Docker Hub, you will see the new image there, with its pull command.

==> Pull and run the image from the remote repository
From now on, you can use docker run and run your app on any machine with this command:
$ docker run -p 4000:80 username/repository:tag
If the image isn’t available locally on the machine, Docker will pull it from the repository.
Note: If you don’t specify the :tag portion of these commands, the tag of :latest will be assumed,
both when you build and when you run images.

==> Docker image location
vagrant@vagrant-ubuntu-trusty-64:~/_docker_$ docker info 2>/dev/null| grep 'Storage Driver' -A 1
Storage Driver: aufs
 Root Dir: /var/lib/docker/aufs

root@vagrant-ubuntu-trusty-64:/var/lib/docker/aufs/diff# du -hs * | sort -hr
87M  14e45ea226f48fb9c854c51e18441cdadce80f4470d10c7f7ce11eb7ee94359b
47M  03a3b0a65ecc4d583bdf62b7e9ea73ddbca43f00970498c024534e258bf3860b
14M  62cdbef845428c74e4e89dd6ceb30dcec1e9ea5979490eb39eae82b150328ec5


## Part 3: Services
Scale our application by running this container in a service.

Prerequisites:
- Install Docker version 1.13 or higher.
- Get Docker Compose.
- Be sure your image works as a deployed container.
  Run this command, slotting in your info for username, repo, and tag:
    $ docker run -p 80:80 username/repo:tag
  Then visit http://localhost/.



=== Overview of Docker Compose ===
  Overview: https://docs.docker.com/compose/overview/
  Download: https://github.com/docker/compose/releases
  Install: https://docs.docker.com/compose/install/#install-compose
  # On Linux
  $ sudo curl -L https://github.com/docker/compose/releases/download/1.16.1/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
  $ sudo chmod +x /usr/local/bin/docker-compose
  # test installation
  $ docker-compose --version
  docker-compose version 1.16.1, build 1719ceb


  Compose is a tool for defining and running multi-container Docker applications.
  With Compose, you use a YAML file to configure your application’s services. Then, with a single command, you create and start all the services from your configuration.
  Using Compose is basically a three-step process:
  1. Define your app’s environment with a Dockerfile so it can be reproduced anywhere.
  2. Define the services that make up your app in docker-compose.yml so they can be run together in an isolated environment.
  3. Lastly, run "docker-compose up" and Compose will start and run your entire app.

A docker-compose.yml looks like this:
version: '3'
services:
  web:
    build: .
    ports:
    - "5000:5000"
    volumes:
    - .:/code
    - logvolume01:/var/log
    links:
    - redis
  redis:
    image: redis
volumes:
  logvolume01: {}

Compose has commands for managing the whole lifecycle of your application:
- Start, stop, and rebuild services
- View the status of running services
- Stream the log output of running services
- Run a one-off command on a service

=== Introduction ===
In part 3, we scale our application and enable load-balancing.
To do this, we must go one level up in the hierarchy of a distributed application: the service.
- Stack
- Services (you are here)
- Container (covered in part 2)

=== About services ===
In a distributed application, different pieces of the app are called “services.”
Imagine a video sharing site:
- a service for storing application data in a database
- a service for video transcoding in the background after a user uploads something
- a service for the front-end, and so on.
Services are really just “containers in production.”
A service only runs one image, but it codifies the way that image runs—what ports it should use, how many replicas of the container should run so the service has the capacity it needs, and so on.
Scaling a service changes the number of container instances running that piece of software, assigning more computing resources to the service in the process.
Luckily it’s very easy to define, run, and scale services with the Docker platform – just write a docker-compose.yml file.

=== Your first docker-compose.yml file ===
A docker-compose.yml file is a YAML file that defines how Docker containers should behave in production.

==> docker-compose.yml
version: "3"
services:
  web:
    # replace username/repo:tag with your name and image details
    image: username/repo:tag
    deploy:
      replicas: 5
      resources:
        limits:
          cpus: "0.1"
          memory: 50M
      restart_policy:
        condition: on-failure
    ports:
      - "80:80"
    networks:
      - webnet
networks:
  webnet:

=== Run your new load-balanced app ===
Before we can use the docker stack deploy command we’ll first run:
$ docker swarm init
To be explained in part 4. If you don’t run docker swarm init you’ll get an error that “this node is not a swarm manager.”

Now let’s run it. You have to give your app a name. Here, it is set to getstartedlab:
$ docker stack deploy -c docker-compose.yml getstartedlab
Creating network getstartedlab_webnet
Creating service getstartedlab_web

Our single service stack is running 5 container instances of our deployed image on one host. Let’s investigate.
Get the service ID for the one service in our application:
$ docker service ls
ID                  NAME                MODE                REPLICAS            IMAGE                       PORTS
kl50tsj0o6xc        getstartedlab_web   replicated          5/5                 xiaotdl/get-started:part2   *:80->80/tcp
:*

getstartedlab_web => where getstarted is app name, web is service name.

$ docker service ps kl50tsj0o6xc<service_id>
ID                  NAME                  IMAGE                       NODE                       DESIRED STATE       CURRENT STATE          ERROR               PORTS
m4nqy8x0jwh4        getstartedlab_web.1   xiaotdl/get-started:part2   vagrant-ubuntu-trusty-64   Running             Running 23 hours ago                       
icjeuxhlb0kf        getstartedlab_web.2   xiaotdl/get-started:part2   vagrant-ubuntu-trusty-64   Running             Running 23 hours ago                       
3a86acsscbzz        getstartedlab_web.3   xiaotdl/get-started:part2   vagrant-ubuntu-trusty-64   Running             Running 23 hours ago                       
031ixty7d9tj        getstartedlab_web.4   xiaotdl/get-started:part2   vagrant-ubuntu-trusty-64   Running             Running 23 hours ago                       
4hotarap32z6        getstartedlab_web.5   xiaotdl/get-started:part2   vagrant-ubuntu-trusty-64   Running             Running 23 hours ago                       

$ docker inspect --format='{{.Status.ContainerStatus.ContainerID}}' m4nqy8x0jwh4<task>
2231e0ffeaaf6c7ed1025f7c369b8cf27105d24cb627b9ce106c19c3cc785704

$ docker inspect --format="{{index .Config.Labels \"com.docker.swarm.task.id\"}}" 2231e0ffeaaf<container>
m4nqy8x0jwh4ifosajf3xpbzf

=== Scale the app ===
You can scale the app by changing the replicas value in docker-compose.yml, saving the change, and re-running the docker stack deploy command:

$ docker stack deploy -c docker-compose.yml getstartedlab
$ docker service ls
ID                  NAME                MODE                REPLICAS            IMAGE                       PORTS
kl50tsj0o6xc        getstartedlab_web   replicated          3/3                 xiaotdl/get-started:part2   *:80->80/tcp
:*

=== Take down the app and the swarm ===
Take the app down with docker stack rm:
$ docker stack rm getstartedlab
This removes the app, but our one-node swarm is still up and running (as shown by docker node ls).
$ docker node ls
ID                            HOSTNAME                   STATUS              AVAILABILITY        MANAGER STATUS
t4rgouuutxu7tryvutfrzjzen *   vagrant-ubuntu-trusty-64   Ready               Active              Leader

Take down the swarm:
$ docker swarm leave --force

Note: Compose files like this are used to define applications with Docker, and can be uploaded to cloud providers using Docker Cloud

###Part3 Services Recap

Some commands to explore at this stage:

docker stack ls                                            # List stacks or apps
docker stack deploy -c <composefile> <appname>  # Run the specified Compose file
docker service ls                 # List running services associated with an app
docker service ps <service>                  # List tasks associated with an app
docker inspect <task or container>                   # Inspect task or container
docker container ls -q                                      # List container IDs
docker stack rm <appname>                             # Tear down an application
docker swarm leave --force      # Take down a single node swarm from the manager


## Part 4: Swarms

Prerequisites:
- Get Docker Machine

== Docker Machine Overview ==
  - Install: https://docs.docker.com/machine/install-machine/
  - Install on Linux:
      $ curl -L https://github.com/docker/machine/releases/download/v0.13.0/docker-machine-`uname -s`-`uname -m` >/tmp/docker-machine &&
      chmod +x /tmp/docker-machine &&
      sudo cp /tmp/docker-machine /usr/local/bin/docker-machine
  - Verify install:
      $ docker-machine version
      docker-machine version 0.13.0, build 9ba6da9

You can use Docker Machine to:
- Install and run Docker on Mac or Windows
- Provision and manage multiple remote Docker hosts
- Provision Swarm clusters


=== What is Docker Machine? ===
Docker Machine is a tool that lets you install **Docker Engine** on virtual hosts,
and manage the hosts with docker-machine commands.
Using docker-machine commands, you can
    - start, inspect, stop, and restart a managed host,
    - upgrade the Docker client and daemon,
    - configure a Docker client to talk to your host.

=== Why should I use it? ===
Docker Machine enables you to provision multiple remote Docker hosts on various flavors of Linux.

### Intro
In part3, we defined how it should run in production by turning it into a service, scaling it up 5x in the process.
In part4, you deploy this application onto a cluster, running it on multiple machines.
Multi-container, multi-machine applications are made possible by joining multiple machines into a **“Dockerized” cluster** called a **swarm**.

### Understanding Swarm clusters
A **swarm** is a group of machines that are running Docker and joined into a cluster.
After that has happened, you continue to run the Docker commands you’re used to, but now they are executed on a cluster by a **swarm manager**.
The **machines in a swarm** can be physical or virtual. After joining a swarm, they are referred to as **nodes**.
In short:
**a swarm** => a group of machines(run Docker + join cluster)
**a swarm manager** => from where you run Docker commands
**a swarm node** => the single machine(virtual/physical) that belongs to the swarm

Swarm managers can use several strategies to run containers, such as
“emptiest node” – which fills the least utilized machines with containers.
“global” - which ensures that each machine gets exactly one instance of the specified container
You instruct the swarm manager to use these strategies in the Compose file.

Swarm managers are the only machines in a swarm that can execute your commands,
or authorize other machines to join the swarm as **workers**.
Workers are just there to provide capacity and do not have the authority to tell any other machine
what it can and cannot do.

Up until now, you have been using Docker in a **single-host mode** on your local machine.
But Docker also can be switched into **swarm mode**, and that’s what enables the use of swarms.
Enabling swarm mode instantly makes the current machine a swarm manager.

### Set up your swarm
A swarm is made up of multiple nodes, which can be either physical or virtual machines.
The basic concept is simple enough: run "docker swarm init" to **enable swarm mode**
and make your current machine a swarm manager, then run "docker swarm join" on other machines to have them **join the swarm as workers**.

### Create a cluster
First, you’ll need a hypervisor that can create virtual machines (VMs), so install Oracle VirtualBox for your machine’s OS.

==> Install VirtualBox
// Add source:
vagrant@vagrant-ubuntu-trusty-64:~$ sudo echo deb http://download.virtualbox.org/virtualbox/debian yakkety contrib >> /etc/apt/sources.list
// Add Oracle public key:
vagrant@vagrant-ubuntu-trusty-64:~$ wget -q https://www.virtualbox.org/download/oracle_vbox.asc -O- | sudo apt-key add -
OK
// Install VirtualBox
vagrant@vagrant-ubuntu-trusty-64:~$ sudo apt-get update
(optional) sudo apt-get install dkms
vagrant@vagrant-ubuntu-trusty-64:~$ sudo apt-get install virtualbox-5.2

Now, create a couple of VMs using docker-machine, using the VirtualBox driver:
$ docker-machine create --driver virtualbox myvm1
$ docker-machine create --driver virtualbox myvm2
_I used vagrant to create two VMs instead._


vagrant@trusty64-1:~$ docker swarm init --advertise-addr 192.168.99.100
>>>
Swarm initialized: current node (s4h2ix8mdtnklp88ejuvpcski) is now a manager.

To add a worker to this swarm, run the following command:

    docker swarm join --token SWMTKN-1-3gt71v570v1ds9tlxlonilywh94m4vu9v7godul0ed60ock0bt-a0xz373mbo7tx8c1tfcxdqgnw 192.168.99.100:2377

    To add a manager to this swarm, run 'docker swarm join-token manager' and follow the instructions.
<<<

==> Ports 2377 and 2376
Always run docker swarm init and docker swarm join with port 2377 (the swarm management port), or no port at all and let it take the default.
The machine IP addresses returned by docker-machine ls include port 2376, which is the Docker daemon port. 

vagrant@trusty64-2:~$ docker swarm join --token SWMTKN-1-3gt71v570v1ds9tlxlonilywh94m4vu9v7godul0ed60ock0bt-a0xz373mbo7tx8c1tfcxdqgnw 192.168.99.100:2377
This node joined a swarm as a worker.

vagrant@trusty64-1:~$ docker node ls
ID                            HOSTNAME            STATUS              AVAILABILITY        MANAGER STATUS
s4h2ix8mdtnklp88ejuvpcski *   trusty64-1          Ready               Active              Leader
ahv765ifioki4nwfszkw91l6z     trusty64-2          Ready               Active     


### Deploy your app on the swarm cluster
### Deploy the app on the swarm manager
vagrant@trusty64-1:~/_docker_$ docker stack deploy -c docker-compose.yml getstartedlab
Creating network getstartedlab_webnet
Creating service getstartedlab_web

You’ll see that the services (and associated containers) have been distributed between both myvm1 and myvm2
vagrant@trusty64-1:~$ docker stack ps getstartedlab
ID                  NAME                  IMAGE                       NODE                DESIRED STATE       CURRENT STATE            ERROR               PORTS
zd1rlhfm7yrj        getstartedlab_web.1   xiaotdl/get-started:part2   trusty64-2          Running             Running 23 seconds ago                       
52ami6df1rd7        getstartedlab_web.2   xiaotdl/get-started:part2   trusty64-1          Running             Running 33 seconds ago                       
p988az6k2d1k        getstartedlab_web.3   xiaotdl/get-started:part2   trusty64-2          Running             Running 23 seconds ago 

vagrant@trusty64-1:~$ docker container ls
CONTAINER ID        IMAGE                       COMMAND             CREATED             STATUS              PORTS               NAMES
1e964a5e1257        xiaotdl/get-started:part2   "python app.py"     6 minutes ago       Up 6 minutes        80/tcp              getstartedlab_web.2.52ami6df1rd7s7juw25f0ex3y
vagrant@trusty64-2:~$ docker container ls
CONTAINER ID        IMAGE                       COMMAND             CREATED             STATUS              PORTS               NAMES
7c7125cb2090        xiaotdl/get-started:part2   "python app.py"     6 minutes ago       Up 6 minutes        80/tcp              getstartedlab_web.3.p988az6k2d1k6ixj3dcrekepp
f04809a26203        xiaotdl/get-started:part2   "python app.py"     6 minutes ago       Up 6 minutes        80/tcp              getstartedlab_web.1.zd1rlhfm7yrj0k9m6hsbdjq03

Visit either node will show a round-robin visited host:
e.g. http://127.0.0.1:8080/
The reason both IP addresses work is that nodes in a swarm participate in an ingress routing mesh.
This ensures that a service deployed at a certain port within your swarm always has that port reserved to itself, no matter what node is actually running the container.
[graph](https://docs.docker.com/engine/swarm/images/ingress-routing-mesh.png)

### Cleanup and reboot
==> Stacks and swarms
You can tear down the stack with docker stack rm. For example:
$ docker stack rm getstartedlab

==> Restarting Docker machines
$ docker-machine start myvm1
$ docker-machine start myvm2

### Part4 Swarm Recap
docker-machine create --driver virtualbox myvm1 # Create a VM (Mac, Win7, Linux)
docker-machine create -d hyperv --hyperv-virtual-switch "myswitch" myvm1 # Win10
docker-machine env myvm1                # View basic information about your node
docker-machine ssh myvm1 "docker node ls"         # List the nodes in your swarm
docker-machine ssh myvm1 "docker node inspect <node ID>"        # Inspect a node
docker-machine ssh myvm1 "docker swarm join-token -q worker"   # View join token
docker-machine ssh myvm1   # Open an SSH session with the VM; type "exit" to end
docker node ls                # View nodes in swarm (while logged on to manager)
docker-machine ssh myvm2 "docker swarm leave"  # Make the worker leave the swarm
docker-machine ssh myvm1 "docker swarm leave -f" # Make master leave, kill swarm
docker-machine ls # list VMs, asterisk shows which VM this shell is talking to
docker-machine start myvm1            # Start a VM that is currently not running
docker-machine env myvm1      # show environment variables and command for myvm1
eval $(docker-machine env myvm1)         # Mac command to connect shell to myvm1
& "C:\Program Files\Docker\Docker\Resources\bin\docker-machine.exe" env myvm1 | Invoke-Expression   # Windows command to connect shell to myvm1
docker stack deploy -c <file> <app>  # Deploy an app; command shell must be set to talk to manager (myvm1), uses local Compose file
docker-machine scp docker-compose.yml myvm1:~ # Copy file to node's home dir (only required if you use ssh to connect to manager and deploy the app)
docker-machine ssh myvm1 "docker stack deploy -c <file> <app>"   # Deploy an app using ssh (you must have first copied the Compose file to myvm1)
eval $(docker-machine env -u)     # Disconnect shell from VMs, use native docker
docker-machine stop $(docker-machine ls -q)               # Stop all running VMs
docker-machine rm $(docker-machine ls -q) # Delete all VMs and their disk images


## Part 5: Stacks

### Introduction
**A stack** is a group of interrelated services that share dependencies, and can be orchestrated and scaled together.
A single stack is capable of defining and coordinating the functionality of an entire application (though very complex applications may want to use multiple stacks).

### Add a new service and redeploy
Modify docker-compose.yml file to have visualizer service, then redeploy.
$ docker stack deploy -c docker-compose.yml getstartedlab

Check web service run on http://192.168.99.101:80/
Check visualizer service run on http://192.168.99.101:8080/

vagrant@trusty64-1:~/_docker_$ docker stack ps getstartedlab
ID                  NAME                         IMAGE                             NODE                DESIRED STATE       CURRENT STATE           ERROR               PORTS
igbwodvxz0qf        getstartedlab_visualizer.1   dockersamples/visualizer:stable   trusty64-1          Running             Running 2 minutes ago                       
lmb2km6r943x        getstartedlab_web.1          xiaotdl/get-started:part2         trusty64-1          Running             Running 2 minutes ago
...


Modify docker-compose.yml file to have redis service, modify redis.volumes to save to localhost, then redeploy.
$ docker stack deploy -c docker-compose.yml getstartedlab

vagrant@trusty64-1:~/_docker_$ docker service ls
ID                  NAME                       MODE                REPLICAS            IMAGE                             PORTS
dy8khz4zeks9        getstartedlab_redis        replicated          1/1                 redis:latest                      *:6379->6379/tcp
sag8z5aqk9z7        getstartedlab_visualizer   replicated          1/1                 dockersamples/visualizer:stable   *:8080->8080/tcp
j4up1i3wv80m        getstartedlab_web          replicated          5/5                 xiaotdl/get-started:part2         *:80->80/tcp
:*


### Recap
You learned that stacks are inter-related services all running in concert.
You learned that to add more services to your stack, you insert them in your Compose file.
Finally, you learned that by using a combination of placement constraints and volumes you can create a permanent home for persisting data, so that your app’s data survives when the container is torn down and redeployed.


## Part 6: Deploy your app

### Deploy your app on a cloud provider
Connect to your swarm via **Docker Cloud**. There are a couple of different ways to connect:

From the Docker Cloud web interface in Swarm mode, select Swarms at the top of the page, click the swarm you want to connect to, and copy-paste the given command into a command line terminal.

==> RUN SOME SWARM COMMANDS TO VERIFY THE DEPLOYMENT
List nodes.
$ docker node ls
List services.
$ docker service ls
List tasks for a service.
$ docker service ps <service_id>

==> OPEN PORTS TO SERVICES ON CLOUD PROVIDER MACHINES
These are the ports you need to expose for each service:

Services,Type,Protocol,Port
web,HTTP,TCP,80
visualizer,HTTP,TCP,8080
redis,TCP,TCP,6379

### Cleanup Stack
$ docker stack rm getstartedlab
