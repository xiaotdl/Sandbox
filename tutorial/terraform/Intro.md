# Intro to Terraform
https://www.terraform.io/intro/index.html

## What is Terraform
Terraform is a tool for building, changing, and versioning infrastructure safely and efficiently.
Terraform can manage existing and popular service providers as well as custom in-house solutions.

Configuration files describe to Terraform the components needed to run a single application or your entire datacenter. Terraform generates an execution plan describing what it will do to reach the desired state, and then executes it to build the described infrastructure. As the configuration changes, Terraform is able to determine what changed and create incremental execution plans which can be applied.

The infrastructure Terraform can manage includes low-level components such as compute instances, storage, and networking, as well as high-level components such as DNS entries, SaaS features, etc.

The key features of Terraform are:
- Infrastructure as Code
    Infrastructure is described using a high-level configuration syntax. This allows a blueprint of your datacenter to be versioned and treated as you would any other code.
    Additionally, infrastructure can be shared and re-used.

- Execution Plan
    Terraform has a "planning" step where it generates an execution plan. The execution plan shows what Terraform will do when you call apply. This lets you avoid any surprises when Terraform manipulates infrastructure.

- Resource Graph
    Terraform builds a graph of all your resources, and parallelizes the creation and modification of any non-dependent resources.
    Because of this, Terraform builds infrastructure as efficiently as possible, and operators get insight into dependencies in their infrastructure.

- Change Automation
    Complex changesets can be applied to your infrastructure with minimal human interaction. With the previously mentioned execution plan and resource graph, you know exactly what Terraform will change and in what order, avoiding many possible human errors.


## Use Cases
- Multi-Tier Applications
- Self-Service Clusters
- Software Demos
    Software writers can provide a Terraform configuration to create, provision and bootstrap a demo on cloud providers like AWS. This allows end users to easily demo the software on their own infrastructure, and even enables tweaking parameters like cluster size to more rigorously test tools at any scale.
- Disposable Environments
- Software Defined Networking
- Resource Schedulers
- Multi-Cloud Deployment


## Terraform vs. Other Software
Terraform provides a flexible abstraction of resources and providers. This model allows for representing everything from physical hardware, virtual machines, and containers, to email and DNS providers. Because of this flexibility, Terraform can be used to solve many different problems.

### vs. Chef, Puppet, etc.
Configuration management tools install and manage software on a machine that **already exists**. Terraform is not a configuration management tool, and it allows existing tooling to focus on their strengths: bootstrapping and initializing resources.

### vs. CloudFormation, Heat, etc.
Tools like CloudFormation, Heat, etc. allow the details of an infrastructure to be codified into a configuration file. The configuration files allow the infrastructure to be elastically created, modified and destroyed. Terraform is inspired by the problems they solve.

Terraform similarly uses configuration files to detail the infrastructure setup, but it goes further by being both cloud-agnostic and enabling multiple providers and services to be combined and composed.
For example, Terraform can be used to orchestrate an AWS and OpenStack cluster simultaneously, while enabling 3rd-party providers like Cloudflare and DNSimple to be integrated to provide CDN and DNS services. This enables Terraform to represent and manage the entire infrastructure with its supporting services, instead of only the subset that exists within a single provider.
It provides **a single unified syntax**, instead of requiring operators to use independent and non-interoperable tools for each platform and service.

### vs. Boto, Fog, etc.
Libraries like Boto, Fog, etc. are used to provide native access to cloud providers and services by using their APIs. Some libraries are focused on specific clouds, while others attempt to bridge them all and mask the semantic differences. Using a client library only provides low-level access to APIs, requiring application developers to create their own tooling to build and manage their infrastructure.

Terraform is not intended to give low-level programmatic access to providers, but instead provides a high level syntax for describing how cloud resources and services should be created, provisioned, and combined. Terraform is very flexible, using a plugin-based model to support providers and provisioners, giving it the ability to support almost any service that exposes APIs.

### vs. Custom Solutions
These tools require time and resources to build and maintain. As tools of necessity, they represent the minimum viable features needed by an organization, being built to handle only the immediate needs. As a result, they are often hard to extend and difficult to maintain. Because the tooling must be updated in lockstep with any new features or infrastructure, it becomes the limiting factor for how quickly the infrastructure can evolve.

Terraform is designed to tackle these challenges. It provides a simple, unified syntax, allowing almost any resource to be managed without learning new tooling. By capturing all the resources required, the dependencies between them can be resolved automatically so that operators do not need to remember and reason about them. Removing the burden of building the tool allows operators to focus on their infrastructure and not the tooling.
