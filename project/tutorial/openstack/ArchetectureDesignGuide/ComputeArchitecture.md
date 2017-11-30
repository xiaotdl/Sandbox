# OpenStack Architecture Design Guide
https://docs.openstack.org/arch-design/index.html

## Design
https://docs.openstack.org/arch-design/design.html

Designing an OpenStack cloud requires a understanding of the cloud user’s requirements and needs to determine the best possible configuration.

This chapter provides guidance on the decisions you need to make during the design process.

To design, deploy, and configure OpenStack, administrators must understand the logical architecture.

OpenStack modules are one of the following types:
- Daemon
	Runs as a background process. On Linux platforms, a daemon is usually installed as a service.
- Script
	Installs a virtual environment and runs tests.
- Command-line interface (CLI)
	Enables users to submit API calls to OpenStack services through commands.

[OpenStack Logical Architecture](https://docs.openstack.org/arch-design/_images/osog_0001.png)

OpenStack Logical Architecture shows one example of the most common integrated services within OpenStack and how they interact with each other. End users can interact through the dashboard, CLIs, and APIs. All services authenticate through a common Identity service, and individual services interact with each other through public APIs, except where privileged administrator commands are necessary.

### Compute architecture
This section describes some of the choices you need to consider when designing and building your compute nodes. Compute nodes form the resource core of the OpenStack Compute cloud, providing the processing, memory, network and storage resources to run instances.

#### Choosing a CPU
You must ensure that the CPU supports virtualization by way of VT-x for Intel chips and AMD-v for AMD chips.

#### Choosing a hypervisor
A hypervisor provides software to manage virtual machine access to the underlying hardware. The hypervisor creates, manages, and monitors virtual machines. OpenStack Compute (nova) supports many hypervisors to various degrees, including:
- KVM
- LXC
- QEMU
- VMware ESX/ESXi
- Xen
- Hyper-V
- Docker

#### Choosing server hardware
Consider the following factors when selecting compute server hardware:
- Server density
    A measure of how many servers can fit into a given measure of physical space, such as a rack unit [U].
- Resource capacity
    The number of CPU cores, how much RAM, or how much storage a given server delivers.
- Expandability
    The number of additional resources you can add to a server before it reaches capacity.
- Cost
    The relative cost of the hardware weighed against the total amount of capacity available on the hardware based on predetermined requirements.

#### Considerations when choosing hardware

##### Instance density
For a general purpose OpenStack cloud, sizing is an important consideration. The expected or anticipated number of instances that each hypervisor can host is a common meter used in sizing the deployment. The selected server hardware needs to support the expected or anticipated instance density.

##### Host density
Floor weight is an often overlooked consideration.
The data center floor must be able to support the weight of the proposed number of hosts within a rack or set of racks. These factors need to be applied as part of the host density calculation and server hardware selection.

##### Power and cooling density

#### Selecting hardware form factor

#### Scaling your cloud
When designing a OpenStack cloud compute server architecture, you must decide whether you intend to scale up or scale out. Selecting a smaller number of larger hosts, or a larger number of smaller hosts, depends on a combination of factors: cost, power, cooling, physical rack and floor space, support-warranty, and manageability. Typically, the scale out model has been popular for OpenStack because it reduces the number of possible failure domains by spreading workloads across more infrastructure. However, the downside is the cost of additional servers and the datacenter resources needed to power, network, and cool the servers.

#### Overcommitting CPU and RAM
OpenStack allows you to overcommit CPU and RAM on compute nodes. This allows you to increase the number of instances running on your cloud at the cost of reducing the performance of the instances. The Compute service uses the following ratios by default:
- CPU allocation ratio: 16:1
- RAM allocation ratio: 1.5:1

The formula for the number of virtual instances on a compute node is (OR * PC) / VC, where:
- OR: CPU overcommit ratio (virtual cores per physical core)
- PC: Number of physical cores
- VC: Number of virtual cores per instance

#### Instance storage solutions
As part of the architecture design for a compute cluster, you must specify storage for the disk on which the instantiated instance runs. There are three main approaches to providing temporary storage:
- Off compute node storage—shared file system
- On compute node storage—shared file system
- On compute node storage—nonshared file system

In general, the questions you should ask when selecting storage are as follows:
- What are my workloads?
- Do my workloads have IOPS requirements?
- Are there read, write, or random access performance requirements?
- What is my forecast for the scaling of storage for compute?
- What storage is my enterprise currently using? Can it be re-purposed?
- How do I manage the storage operationally?

Compute nodes will be invested in CPU and RAM.
Storage nodes will be invested in block storage.

##### Non-compute node based shared file system
In this option, the disks storing the running instances are hosted in servers outside of the compute nodes.

If you use separate compute and storage hosts, you can treat your compute hosts as *“stateless”*. As long as you do not have any instances currently running on a compute host, you can take it offline or wipe it completely without having any effect on the rest of your cloud. This simplifies maintenance for the compute hosts.

There are several advantages to this approach:
- If a compute node fails, instances are usually easily recoverable.
- Running a dedicated storage system can be operationally simpler.
- You can scale to any number of spindles.
- It may be possible to share the external storage for other purposes.

The main disadvantages to this approach are:
- Depending on design, heavy I/O usage from some instances can affect unrelated instances.
- Use of the network can decrease performance.
- Scalability can be affected by network architecture.

##### On compute node storage—shared file system
In this option, each compute node is specified with a significant amount of disk space, but a distributed file system ties the disks from each compute node into a single mount.

The main advantage of this option is that it scales to external storage when you require additional storage.

However, this option has several disadvantages:
- Running a distributed file system can make you lose your data locality compared with nonshared storage.
- Recovery of instances is complicated by depending on multiple hosts.
- The chassis size of the compute node can limit the number of spindles able to be used in a compute node.
- Use of the network can decrease performance.
- Loss of compute nodes decreases storage availability for all hosts.

##### On compute node storage—nonshared file system¶
In this option, each compute node is specified with enough disks to store the instances it hosts.

There are two main advantages:
- Heavy I/O usage on one compute node does not affect instances on other compute nodes. Direct I/O access can increase performance.
- Each host can have different storage profiles for hosts aggregation and availability zones.

There are several disadvantages:
- If a compute node fails, the data associated with the instances running on that node is lost.
- The chassis size of the compute node can limit the number of spindles able to be used in a compute node.
- Migrations of instances from one node to another are more complicated and rely on features that may not continue to be developed.
- If additional storage is required, this option does not scale.

#### Issues with live migration
Live migration is an integral part of the operations of the cloud. This feature provides the ability to seamlessly move instances from one physical host to another, a necessity for performing upgrades that require reboots of the compute hosts, but only works well with shared storage.

#### Choice of file system
If you want to support shared-storage live migration, you need to configure a distributed file system.

Possible options include:
- NFS (default for Linux)
- Ceph
- GlusterFS
- MooseFS
- Lustre

NFS is the easiest to set up and there is extensive community knowledge about it.


### Network connectivity
The selected server hardware must have the appropriate number of network connections, as well as the right type of network connections, in order to support the proposed architecture. Ensure that, at a minimum, there are at least two diverse network connections coming into each rack.

The following networks with their proposed bandwidth is highly recommended for a basic production OpenStack install:
- Install or OOB network
    Typically used by most distributions and provisioning tools as the network for deploying base software to the OpenStack compute nodes. This network should be connected at a minimum of 1Gb and no routing is usually needed.

- Internal or Management network
    Used as the internal communication network between OpenStack compute and control nodes. Can also be used as a network for iSCSI communication between the compute and iSCSI storage nodes. Again, this should be a minimum of a 1Gb NIC and should be a non-routed network. This interface should be redundant for high availability (HA).

- Tenant network
    A private network that enables communication between each tenant’s instances. If using flat networking and provider networks, this network is optional. This network should also be isolated from all other networks for security compliance. A 1Gb interface should be sufficient and redundant for HA.

- Storage network
    A private network which could be connected to the Ceph frontend or other shared storage. For HA purposes this should be a redundant configuration with suggested 10Gb NICs. This network isolates the storage for the instances away from other networks. Under load, this storage traffic could overwhelm other networks and cause outages on other OpenStack services.

- (Optional) External or Public network
    This network is used to communicate externally from the VMs to the public network space. These addresses are typically handled by the neutron agent on the controller nodes and can also be handled by a SDN other than neutron. However, when using neutron DVR with OVS, this network must be present on the compute node since north and south traffic will not be handled by the controller nodes, but by the compute node itself. For more information on DVR with OVS and compute nodes, see Open vSwitch: High availability using DVR


### Compute server logging
OpenStack produces a great deal of useful logging information, but for the information to be useful for operations purposes, you should consider having a central logging server to send logs to, and a log parsing/analysis system such as Elastic Stack [formerly known as ELK].

Elastic Stack consists of mainly three components:
- Logstash (log intake=input, processing=filter, and output)
- Elasticsearch (log storage, search, and analysis)
- Kibana (log dashboard service).

Server(Logstash) -->
Server(Logstash) --> Cache Server(Optional) --> Elastic Search(Store/Analysis) --> Kibana(Dashboard)
Server(Logstash) -->

These input, output and filter configurations are typically stored in /etc/logstash/conf.d but may vary by linux distribution. Separate configuration files should be created for different logging systems such as syslog, Apache, and OpenStack.
