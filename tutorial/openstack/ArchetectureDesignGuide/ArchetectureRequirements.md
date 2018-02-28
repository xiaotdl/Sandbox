# OpenStack Architecture Design Guide
https://docs.openstack.org/arch-design/index.html

## Architecture requirements
https://docs.openstack.org/arch-design/arch-requirements.html

### Enterprise requirements

#### Cost
As a general guideline, increasing the complexity of a cloud architecture increases the cost of building and maintaining it. For example, a hybrid or multi-site cloud architecture involving multiple vendors and technical architectures may require higher setup and operational costs because of the need for more sophisticated orchestration and brokerage tools than in other architectures. However, overall operational costs might be lower by virtue of using a cloud brokerage tool to deploy the workloads to the most cost effective platform.

Consider the following costs categories when designing a cloud:
- Compute resources
- Networking resources
- Storage
- Replication
- Management
- Operational costs

It is important to minimize capital expenditure (CapEx) at all layers of the stack.

#### Time-to-market
The ability to deliver services or products within a flexible time frame is a common business factor when building a cloud. Allowing users to self-provision and gain access to compute, network, and storage resources on-demand may decrease time-to-market for new products and applications.

You must balance the time required to build a new cloud platform against the time saved by migrating users away from legacy platforms.

#### Revenue oppotunity
Revenue opportunities vary based on the intent and use case of the cloud. The requirements of a commercial, customer-facing product are often very different from an internal, private cloud. You must consider what features make your design most attractive to your users.

#### Capacity planning and scalability
Capacity and the placement of workloads are key design considerations for clouds. A long-term capacity plan for these designs must incorporate growth over time to prevent permanent consumption of more expensive external clouds. To avoid this scenario, account for future applications’ capacity requirements and plan growth appropriately.

It is difficult to predict the amount of load a particular application might incur if the number of users fluctuates, or the application experiences an unexpected increase in use. It is possible to define application requirements in terms of vCPU, RAM, bandwidth, storage, or other resources and plan appropriately. However, other clouds might not use the same meter or even the same oversubscription rates.

#### Performance
Performance is a critical consideration when designing any cloud, and becomes increasingly important as size and complexity grow. While single-site, private clouds can be closely controlled, multi-site and hybrid deployments require more careful planning to reduce problems such as network latency between sites.

Using native OpenStack tools can help improve performance.
For example, you can use Telemetry to measure performance and the Orchestration service (heat) to react to changes in demand.

##### Cloud resource deployment
    The cloud user expects repeatable, dependable, and deterministic processes for launching and deploying cloud resources. You could deliver this through a web-based interface or publicly available API endpoints. All appropriate options for requesting cloud resources must be available through some type of user interface, a command-line interface (CLI), or API endpoints.

##### Consumption Model
    - Cloud users expect a fully self-service and on-demand consumption model. When an OpenStack cloud reaches the massively scalable size, expect consumption as a service in each and every way.
    - Massively scalable OpenStack clouds require extensive metering and monitoring functionality to maximize the operational efficiency by keeping the operator informed about the status and state of the infrastructure. This includes full scale metering of the hardware and software status. A corresponding framework of logging and alerting is also required to store and enable operations to act on the meters provided by the metering and monitoring solutions. The cloud operator also needs a solution that uses the data provided by the metering and monitoring solution to provide capacity planning and capacity trending analysis.

##### Location
    For many use cases the proximity of the user to their workloads has a direct influence on the performance of the application and therefore should be taken into consideration in the design. Certain applications require zero to minimal latency that can only be achieved by deploying the cloud in multiple locations. These locations could be in different data centers, cities, countries or geographical regions, depending on the user requirement and location of the users.

##### Input-Output requirements
    Input-Output performance requirements require researching and modeling before deciding on a final storage framework.

##### Scale
    Scaling storage solutions in a storage-focused OpenStack architecture design is driven by initial requirements, including IOPS, capacity, bandwidth, and future needs. Planning capacity based on projected needs over the course of a budget cycle is important for a design. The architecture should balance cost and capacity, while also allowing flexibility to implement new technologies and methods as they become available.


#### Network
    It is important to consider the functionality, security, scalability, availability, and testability of the network when choosing a CMP and cloud provider.

- Decide on a network framework and design minimum functionality tests. This ensures testing and functionality persists during and after upgrades.
- Scalability across multiple cloud providers may dictate which underlying network framework you choose in different cloud providers. It is important to present the network API functions and to verify that functionality persists across all cloud endpoints chosen.
- High availability implementations vary in functionality and design. Examples of some common methods are active-hot-standby, active-passive, and active-active. Development of high availability and test frameworks is necessary to insure understanding of functionality and limitations.
- Consider the security of data between the client and the endpoint, and of traffic that traverses the multiple clouds.

#### Compliance and geo-location
    An organization may have certain legal obligations and regulatory compliance measures which could require certain workloads or data to not be located in certain regions.

#### Auditing

#### Security

#### Service level agreements (SLA)

#### Application readiness
    Some applications are tolerant of a lack of synchronized object storage, while others may need those objects to be replicated and available across regions. Understanding how the cloud implementation impacts new and existing applications is important for risk mitigation, and the overall success of a cloud project. Applications may have to be written or rewritten for an infrastructure with little to no redundancy, or with the cloud in mind.

#### Migration, availability, site loss and recovery
- Disaster recovery and business continuity
	Cheaper storage makes the public cloud suitable for maintaining backup applications.
- Migration scenarios
	Hybrid cloud architecture enables the migration of applications between different clouds.
- Provider availability or implementation details
	Business changes can affect provider availability. Likewise, changes in a provider’s service can disrupt a hybrid cloud environment or increase costs.
- Provider API changes
	Consumers of external clouds rarely have control over provider changes to APIs, and changes can break compatibility. Using only the most common and basic APIs can minimize potential conflicts.
- Image portability
	As of the Kilo release, there is no common image format that is usable by all clouds. Conversion or recreation of images is necessary if migrating between clouds. To simplify deployment, use the smallest and simplest images feasible, install only what is necessary, and use a deployment manager such as Chef or Puppet. Do not use golden images to speed up the process unless you repeatedly deploy the same images on the same cloud.
- API differences
	Avoid using a hybrid cloud deployment with more than just OpenStack (or with different versions of OpenStack) as API changes can cause compatibility issues.
- Business or technical diversity
	Organizations leveraging cloud-based services can embrace business diversity and utilize a hybrid cloud design to spread their workloads across multiple cloud providers. This ensures that no single cloud provider is the sole host for an application.


### Operational requirements

#### Network design
The network design for an OpenStack cluster includes decisions regarding the interconnect needs within the cluster, the need to allow clients to access their resources, and the access requirements for operators to administrate the cluster. You should consider the bandwidth, latency, and reliability of these networks.

Consider additional design decisions about monitoring and alarming. If you are using an external provider, service level agreements (SLAs) are typically defined in your contract. Operational considerations such as bandwidth, latency, and jitter can be part of the SLA.

#### SLA considerations
Service-level agreements (SLAs) define the levels of availability that will impact the design of an OpenStack cloud to provide redundancy and high availability.

SLA terms that affect the design include:
- API availability guarantees implying multiple infrastructure services and highly available load balancers.
- Network uptime guarantees affecting switch design, which might require redundant switching and power.
- Networking security policy requirements.

In any environment larger than just a few hosts, there are two areas that might be subject to a SLA:
- Data Plane
	services that provide virtualization, networking, and storage. Customers usually require these services to be continuously available.
- Control Plane
	ancillary services such as API endpoints, and services that control CRUD operations. The services in this category are usually subject to a different SLA expectation and may be better suited on separate hardware or containers from the Data Plane services.

There are many services outside the realms of pure OpenStack code which affects the ability of a cloud design to meet SLAs, including:
- Database services, such as MySQL or PostgreSQL.
- Services providing RPC, such as RabbitMQ.
- External network attachments.
- Physical constraints such as power, rack space, network cabling, etc.
- Shared storage including SAN based arrays, storage clusters such as Ceph, and/or NFS services.

#### Support and maintenance
The maintenance function of an operator should be taken into consideration:
- Maintenance tasks
    Operating system patching, hardware/firmware upgrades, and datacenter related changes, as well as minor and release upgrades to OpenStack components are all ongoing operational tasks. The six monthly release cycle of the OpenStack projects needs to be considered as part of the cost of ongoing maintenance. The solution should take into account storage and network maintenance and the impact on underlying workloads.
- Reliability and availability
    Reliability and availability depend on the many supporting components’ availability and on the level of precautions taken by the service provider. This includes network, storage systems, datacenter, and operating systems.

#### Logging and monitoring
Specific meters that are critically important to capture include:
- Image disk utilization
- Response time to the Compute API

#### Management software

#### Database software

#### Operator access to systems


### High availability

#### Data plane and control plane
- Data Plane services
    This includes the core services required to maintain availability of running Compute service instances, networks, storage, and additional services running on top of those resources. These services are generally expected to be available all the time.
- Control Plane services
    The remaining services, responsible for create, read, update and delete (CRUD) operations, metering, monitoring, and so on, are often referred to as the Control Plane. The SLA is likely to dictate a lower uptime requirement for these services.

The services comprising an OpenStack cloud have a number of requirements that you need to understand in order to be able to meet SLA terms. For example, in order to provide the Compute service a minimum of storage, message queueing and database services are necessary as well as the networking between them.

The separation between Control and Data Planes enables rapid maintenance with a limited effect on customer operations.

#### Eliminating single points of failure within each site
OpenStack lends itself to deployment in a highly available manner where it is expected that at least 2 servers be utilized. These can run all the services involved from the message queuing service, for example RabbitMQ or QPID, and an appropriately deployed database service such as MySQL or MariaDB. As services in the cloud are scaled out, back-end services will need to scale too. Monitoring and reporting on server utilization and response times, as well as load testing your systems, will help determine scale out decisions.

#### Eliminating single points of failure in a multi-region design
Some services are commonly shared between multiple regions, including the Identity service and the Dashboard. In this case, it is necessary to ensure that the databases backing the services are replicated, and that access to multiple workers across each site can be maintained in the event of losing a single region.

#### Site loss and recovery

#### Replicating inter-site data
Traditionally, replication has been the best method of protecting object store implementations. A variety of replication methods exist in storage architectures, for example synchronous and asynchronous mirroring. Most object stores and back-end storage systems implement methods for replication at the storage subsystem layer. Object stores also tailor replication techniques to fit a cloud’s requirements.

Organizations must find the right balance between data integrity and data availability. Replication strategy may also influence disaster recovery methods.

Replication across different racks, data centers, and geographical regions increases focus on determining and ensuring data locality. The ability to guarantee data is accessed from the nearest or fastest storage can be necessary for applications to perform well.




