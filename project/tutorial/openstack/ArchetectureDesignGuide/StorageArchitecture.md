## Storage architecture
https://docs.openstack.org/arch-design/design-storage.html

### Storage concepts
Storage is found in many parts of the OpenStack cloud environment.
It is important to understand the distinction between ephemeral storage and persistent storage:
- Ephemeral storage
    If you only deploy OpenStack Compute service (nova), by default your users do not have access to any form of persistent storage. The disks associated with VMs are ephemeral, meaning that from the user’s point of view they disappear when a virtual machine is terminated.
- Persistent storage
    Persistent storage means that the storage resource outlives any other resource and is always available, regardless of the state of a running instance.

OpenStack clouds explicitly support three types of *persistent storage*:
- Object Storage
- Block Storage
- File-based storage.

#### Object storage
Object storage is implemented in OpenStack by the Object Storage service (swift). Users access binary objects through a REST API. If your intended users need to archive or manage large datasets, you should provide them with Object Storage service. Additional benefits include:
- OpenStack can store your virtual machine (VM) images inside of an Object Storage system, as an alternative to storing the images on a file system.
- Integration with OpenStack Identity, and works with the OpenStack Dashboard.
- Better support for distributed deployments across multiple datacenters through support for asynchronous eventual consistency replication.

You should consider using the OpenStack Object Storage service if you eventually plan on distributing your storage cluster across multiple data centers.

#### Block storage
Block storage is implemented in OpenStack by the Block Storage service (cinder). Because these volumes are persistent, they can be detached from one instance and re-attached to another instance and the data remains intact.

The Block Storage service supports multiple back ends in the form of drivers. Your choice of a storage back end must be supported by a block storage driver.

Most block storage drivers allow the instance to have direct access to the underlying storage hardware’s block device. This helps increase the overall read/write IO. However, support for utilizing files as volumes is also well established, with full support for NFS, GlusterFS and others.

These drivers work a little differently than a traditional block storage driver. On an NFS or GlusterFS file system, a single file is created and then mapped as a virtual volume into the instance. This mapping and translation is similar to how OpenStack utilizes QEMU’s file-based virtual machines stored in /var/lib/nova/instances.

#### File-based storage
In multi-tenant OpenStack cloud environment, the Shared File Systems service (manila) provides a set of services for management of shared file systems. The Shared File Systems service supports multiple back-ends in the form of drivers, and can be configured to provision shares from one or more back-ends. Share servers are virtual machines that export file shares using different file system protocols such as NFS, CIFS, GlusterFS, or HDFS.

The Shared File Systems service is persistent storage and can be mounted to any number of client machines. It can also be detached from one instance and attached to another instance without data loss. During this process the data are safe unless the Shared File Systems service itself is changed or removed.

### Storage architecture
Before choosing a storage architecture, a few generic questions should be answered:
- Will the storage architecture scale linearly as the cloud grows and what are its limits?
- What is the desired attachment method: NFS, iSCSI, FC, or other?
- Is the storage proven with the OpenStack platform?
- What is the level of support provided by the vendor within the community?
- What OpenStack features and enhancements does the cinder driver enable?
- Does it include tools to help troubleshoot and resolve performance issues?
- Is it interoperable with all of the projects you are planning on using in your cloud?

#### Choosing storage back ends

#### Selecting storage hardware
- Cost
    Storage can be a significant portion of the overall system cost. For an organization that is concerned with vendor support, a commercial storage solution is advisable, although it comes with a higher price tag. If initial capital expenditure requires minimization, designing a system based on commodity hardware would apply. The trade-off is potentially higher support costs and a greater risk of incompatibility and interoperability issues.
- Performance
    Performance of block based storage is typically measured in the maximum read and write operations to non-contiguous storage locations per second. This measurement typically applies to SAN, hard drives, and solid state drives. While IOPS can be broadly measured and is not an official benchmark, many vectors like to be used by vendors to communicate performance levels. Since there are no real standards for measuring IOPS, vendor test results may vary, sometimes wildly. However, along with transfer rate which measures the speed that data can be transferred to contiguous storage locations, IOPS can be used in a performance evaluation. Typically, transfer rate is represented by a bytes per second calculation but IOPS is measured by an integer.
- To calculate IOPS for a single drive you could use:
    IOPS = 1 / (AverageLatency + AverageSeekTime) For example: Average Latency for Single Disk = 2.99ms or .00299 seconds Average Seek Time for Single Disk = 4.7ms or .0047 seconds IOPS = 1/(.00299 + .0047) IOPS = 130
- To calculate maximum IOPS for a disk array:
    Maximum Read IOPS: In order to accurately calculate maximum read IOPS for a disk array, multiply the IOPS for each disk by the maximum read or write IOPS per disk. maxReadIOPS = nDisks * diskMaxIOPS For example, 15 10K Spinning Disks would be measured the following way: maxReadIOPS = 15 * 130 maxReadIOPS = 1950
- Maximum write IOPS per array:
    Determining the maximum write IOPS is a little different because most administrators configure disk replication using RAID and since the RAID controller requires IOPS itself, there is a write penalty. The severity of the write penalty is determined by the type of RAID used.

- What about SSD? DRAM SSD?
    In an HDD, data transfer is sequential. The actual read/write head “seeks” a point in the hard drive to execute the operation. Seek time is significant. Transfer rate can also be influenced by file system fragmentation and the layout. Finally, the mechanical nature of hard disks also has certain performance limitations.

    In an SSD, data transfer is not sequential; it is random so it is faster. Therhmarks for small read/writes:


    HDDs: Small reads – 175 IOPs, Small writes – 280 IOPs
    Flash SSDs: Small reads – 1075 IOPs (6x), Small writes – 21 IOPs (0.1x)
    DRAM SSDs: Small reads – 4091 IOPs (23x), Small writes – 4184 IOPs (14x)
