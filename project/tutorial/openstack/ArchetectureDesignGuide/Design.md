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





