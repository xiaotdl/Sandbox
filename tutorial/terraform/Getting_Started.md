# Getting Started
https://www.terraform.io/intro/getting-started/install.html

## Install Terraform
https://www.terraform.io/downloads.html

After downloading Terraform, unzip the package. Terraform runs as a single binary named terraform. Any other files in the package can be safely removed and Terraform will still function.

### Verifying the installation
```
$ terraform
Usage: terraform [--version] [--help] <command> [args]

The available commands for execution are listed below.
The most common, useful commands are shown first, followed by
less common or more advanced commands. If you're just getting
started with Terraform, stick with the common commands. For the
other commands, please read the help and docs before usage.

Common commands:
    apply              Builds or changes infrastructure
    console            Interactive console for Terraform interpolations
# ...
```


## Build Infrastructure
We'll build infrastructure on AWS for the getting started guide since it is popular and generally understood.

### Configuration
The set of files used to describe infrastructure in Terraform is simply known as a _Terraform configuration_.
We're going to write our first configuration now to launch _a single AWS EC2 instance_.

The format of the configuration files is [documented here](https://www.terraform.io/docs/configuration/index.html).
Configuration files can also be JSON, but we recommend only using JSON when the configuration is generated by a machine.

example.tf
```
provider "aws" {
  access_key = "ACCESS_KEY_HERE"
  secret_key = "SECRET_KEY_HERE"
  region     = "us-east-1"
}

resource "aws_instance" "example" {
  ami           = "ami-2757f631"
  instance_type = "t2.micro"
}
```

The provider block:
    is used to configure the named provider, in our case "aws." A provider is responsible for creating and managing resources. Multiple provider blocks can exist if a Terraform configuration is composed of multiple providers, which is a common situation.

The resource block:
    defines a resource that exists within the infrastructure. A resource might be a physical component such as an EC2 instance, or it can be a logical resource such as a Heroku application.
    The resource block has two strings before opening the block:
    - the resource type
    - the resource name.
In our example, the resource type is "aws_instance" and the name is "example."
The prefix of the type maps to the provider. In our case "aws_instance" automatically tells Terraform that it is managed by the "aws" provider.

### Initialization
The first command to run for a new configuration -- or after checking out an existing configuration from version control -- is `terraform init`, which initializes various local settings and data that will be used by subsequent commands.

```
terraform init
```

### Apply Changes
This output shows the execution plan, describing which actions Terraform will take in order to change real infrastructure to match the configuration. The output format is similar to the diff format generated by tools such as Git. The output has a + next to aws_instance.example, meaning that Terraform will create this resource. Beneath that, it shows the attributes that will be set. When the value displayed is <computed>, it means that the value won't be known until the resource is created.

```
$ terraform apply
# ...

+ aws_instance.example
    ami:                      "ami-2757f631"
    availability_zone:        "<computed>"
    ebs_block_device.#:       "<computed>"
    ephemeral_block_device.#: "<computed>"
    instance_state:           "<computed>"
    instance_type:            "t2.micro"
    key_name:                 "<computed>"
    placement_group:          "<computed>"
    private_dns:              "<computed>"
    private_ip:               "<computed>"
    public_dns:               "<computed>"
    public_ip:                "<computed>"
    root_block_device.#:      "<computed>"
    security_groups.#:        "<computed>"
    source_dest_check:        "true"
    subnet_id:                "<computed>"
    tenancy:                  "<computed>"
    vpc_security_group_ids.#: "<computed>"
```

Terraform also wrote some data into the terraform.tfstate file. This state file is extremely important; it keeps track of the IDs of created resources so that Terraform knows what it is managing. This file must be saved and distributed to anyone who might run Terraform. It is generally recommended to setup remote state when working with Terraform, to share the state automatically, but this is not necessary for simple situations like this Getting Started guide.

You can inspect the current state using terraform show:
```
$ terraform show
aws_instance.example:
  id = i-32cf65a8
  ami = ami-2757f631
  availability_zone = us-east-1a
  instance_state = running
  instance_type = t2.micro
  private_ip = 172.31.30.244
  public_dns = ec2-52-90-212-55.compute-1.amazonaws.com
  public_ip = 52.90.212.55
  subnet_id = subnet-1497024d
  vpc_security_group_ids.# = 1
  vpc_security_group_ids.3348721628 = sg-67652003
```

### Provisioning
The EC2 instance we launched at this point is based on the AMI given, but has no additional software installed. If you're running an image-based infrastructure (perhaps creating images with Packer), then this is all you need.

However, many infrastructures still require some sort of initialization or software provisioning step. Terraform supports provisioners, which we'll cover a little bit later in the getting started guide, in order to do this.


## Change Infrastructure

### Configuration
```
resource "aws_instance" "example" {
  ami           = "ami-b374d5a5"
  instance_type = "t2.micro"
}
```
We've changed the AMI from being an Ubuntu 16.04 LTS AMI to being an Ubuntu 16.10 AMI. Terraform configurations are meant to be changed like this. You can also completely remove resources and Terraform will know to destroy the old one.

### Apply Changes
```
$ terraform apply
# ...

-/+ aws_instance.example
    ami:                      "ami-2757f631" => "ami-b374d5a5" (forces new resource)
    availability_zone:        "us-east-1a" => "<computed>"
    ebs_block_device.#:       "0" => "<computed>"
    ephemeral_block_device.#: "0" => "<computed>"
    instance_state:           "running" => "<computed>"
    instance_type:            "t2.micro" => "t2.micro"
    private_dns:              "ip-172-31-17-94.ec2.internal" => "<computed>"
    private_ip:               "172.31.17.94" => "<computed>"
    public_dns:               "ec2-54-82-183-4.compute-1.amazonaws.com" => "<computed>"
    public_ip:                "54.82.183.4" => "<computed>"
    subnet_id:                "subnet-1497024d" => "<computed>"
    vpc_security_group_ids.#: "1" => "<computed>"
```

The prefix -/+ means that Terraform will destroy and recreate the resource, rather than updating it in-place. While some attributes can be updated in-place (which are shown with the ~ prefix), changing the AMI for an EC2 instance requires recreating it. Terraform handles these details for you, and the execution plan makes it clear what Terraform will do.

## Destroy Infrastructure
```
$ terraform destroy
# ...

- aws_instance.example
```

## Resource Dependencies
Terraform configurations can contain multiple resources, multiple resource types, and these types can even span multiple providers.

On this page, we'll show a basic example of multiple resources and how to reference the attributes of other resources to configure subsequent resources.

### Assigning an Elastic IP
```
resource "aws_eip" "ip" {
  instance = "${aws_instance.example.id}"
}
```
We use an interpolation(${}) to use an attribute from the EC2 instance we managed earlier.

### Apply Changes
Terraform created the EC2 instance before creating the Elastic IP address. Due to the interpolation expression that passes the ID of the EC2 instance to the Elastic IP address, Terraform is able to infer a dependency, and knows it must create the instance first.

### Implicit and Explicit Dependencies
Terraform uses this dependency information to determine the correct order in which to create the different resources. In the example above, Terraform knows that the aws_instance must be created before the aws_eip.

Implicit dependencies via interpolation expressions are the primary way to inform Terraform about these relationships, and should be used whenever possible.

Sometimes there are dependencies between resources that are not visible to Terraform. The depends_on argument is accepted by any resource and accepts a list of resources to create explicit dependencies for.

```
# New resource for the S3 bucket our application will use.
resource "aws_s3_bucket" "example" {
  # NOTE: S3 bucket names must be unique across _all_ AWS accounts, so
  # this name must be changed before applying this example to avoid naming
  # conflicts.
  bucket = "terraform_getting_started_guide"
  acl    = "private"
}

# Change the aws_instance we declared earlier to now include "depends_on"
resource "aws_instance" "example" {
  ami           = "ami-2757f631"
  instance_type = "t2.micro"

  # Tells Terraform that this EC2 instance must be created only after the
  # S3 bucket has been created.
  depends_on = ["aws_s3_bucket.example"]
}
```

### Non-Dependent Resources
They can be created in parallel with the other resources. Where possible, Terraform will perform operations concurrently to reduce the total time taken to apply changes.


## Provision
If you're using an image-based infrastructure (perhaps with images created with Packer), then what you've learned so far is good enough. But if you need to do some initial setup on your instances, then provisioners let you upload files, run shell scripts, or install and trigger other software like configuration management tools, etc.

### Defining a Provisioner
To define a provisioner, modify the resource block defining the "example" EC2 instance to look like the following:

```
resource "aws_instance" "example" {
    ami = "ami-b374d5a5"
    instance_type = "t2.micro"

    provisioner "local-exec" {
        command = "echo ${aws_instance.example.public_ip} > ip_address.txt"
    }
}
```

This adds a provisioner block within the resource block. Multiple provisioner blocks can be added to define multiple provisioning steps. Terraform supports multiple provisioners, but for this example we are using the local-exec provisioner.

The local-exec provisioner executes a command locally on the machine running Terraform. We're using this provisioner versus the others so we don't have to worry about specifying any connection info right now.

### Running Provisioners
Provisioners are only run when a resource is created. They are not a replacement for configuration management and changing the software of an already-running server, and are instead just meant as a way to bootstrap a server. For configuration management, you should use Terraform provisioning to invoke a real configuration management solution.

### Failed Provisioners and Tainted Resources
If a resource successfully creates but fails during provisioning, Terraform will error and mark the resource as "tainted." A resource that is tainted has been physically created, but can't be considered safe to use since provisioning failed.

When you generate your next execution plan, Terraform will not attempt to restart provisioning on the same resource because it isn't guaranteed to be safe. Instead, Terraform will remove any tainted resources and create new resources, attempting to provision them again after creation.

Terraform also does not automatically roll back and destroy the resource during the apply when the failure happens, because that would go against the execution plan: the execution plan would've said a resource will be created, but does not say it will ever be deleted.

### Destroy Provisioners
Provisioners can also be defined that run only during a destroy operation. These are useful for performing system cleanup, extracting data, etc.

For many resources, using built-in cleanup mechanisms is recommended if possible (such as init scripts), but provisioners can be used if necessary.

The getting started guide won't show any destroy provisioner examples. If you need to use destroy provisioners, please see the provisioner documentation.


## Input Variables
To become truly shareable and version controlled, we need to parameterize the configurations. This page introduces input variables as a way to do this.

### Defining Variables
Let's first extract our access key, secret key, and region into a few variables. Create another file variables.tf with the following contents.
Note: that the file can be named anything, since Terraform loads all files ending in .tf in a directory.
```
variable "access_key" {}
variable "secret_key" {}
variable "region" {
    default = "us-east-1"
}
```

This defines three variables within your Terraform configuration. The first two have empty blocks {}. The third sets a default. If a default value is set, the variable is optional. Otherwise, the variable is required. If you run terraform plan now, Terraform will prompt you for the values for unset string variables.

### Using Variables in Configuration
```
provider "aws" {
  access_key = "${var.access_key}"
  secret_key = "${var.secret_key}"
  region     = "${var.region}"
}
```

### Assigning Variables
There are multiple ways to assign variables. Below is also the order in which variable values are chosen. The following is the descending order of precedence in which variables are considered.

#### Command-line flags
You can set variables directly on the command-line with the -var flag. Any command in Terraform that inspects the configuration accepts this flag, such as apply, plan, and refresh:

```
$ terraform apply \
  -var 'access_key=foo' \
  -var 'secret_key=bar'
# ...
```

#### From a file
To persist variable values, create a file and assign variables within this file. Create a file named terraform.tfvars with the following contents:
```
access_key = "foo"
secret_key = "bar"
```

For all files which match terraform.tfvars or \*.auto.tfvars present in the current directory, Terraform automatically loads them to populate variables. If the file is named something else, you can use the -var-file flag directly to specify a file. These files are the same syntax as Terraform configuration files. And like Terraform configuration files, these files can also be JSON.

We don't recommend saving usernames and password to version control, But you can create a local secret variables file and use -var-file to load it.

You can use multiple -var-file arguments in a single command, with some checked in to version control and others not checked in. For example:
```
$ terraform apply \
  -var-file="secret.tfvars" \
  -var-file="production.tfvars"
```

#### From environment variables
Terraform will read environment variables in the form of TF_VAR_name to find the value for a variable. For example, the TF_VAR_access_key variable can be set to set the access_key variable.

Note: Environment variables can only populate string-type variables. List and map type variables must be populated via one of the other mechanisms.
»

#### UI Input
If you execute terraform apply with certain variables unspecified, Terraform will ask you to input their values interactively. These values are not saved, but this provides a convenient workflow when getting started with Terraform. UI Input is not recommended for everyday use of Terraform.

#### Variable Defaults
If no value is assigned to a variable via any of these methods and the variable has a default key in its declaration, that value will be used for the variable.


### Lists
Lists are defined either explicitly or implicitly
```
# implicitly by using brackets [...]
variable "cidrs" { default = []  }

# explicitly
variable "cidrs" { type = "list"  }
```

You can specify lists in a terraform.tfvars file:
```
cidrs = [ "10.0.0.0/16", "10.1.0.0/16"  ]
```

### Maps
```
variable "amis" {
  type = "map"
  default = {
    "us-east-1" = "ami-b374d5a5"
    "us-west-2" = "ami-4b32be2b"
  }
}
```

A variable can have a map type assigned explicitly, or it can be implicitly declared as a map by specifying a default value that is a map. The above demonstrates both.
```
resource "aws_instance" "example" {
  ami           = "${lookup(var.amis, var.region)}"
  instance_type = "t2.micro"
}
```
This introduces a new type of interpolation: a function call. The lookup function does a dynamic lookup in a map for a key. The key is var.region, which specifies that the value of the region variables is the key.

While we don't use it in our example, it is worth noting that you can also do a static lookup of a map directly with
```
${var.amis["us-east-1"]}
```

### Assigning Maps
We set defaults above, but maps can also be set using the -var and -var-file values. For example:
```
$ terraform apply -var 'amis={ us-east-1 = "foo", us-west-2 = "bar" }'
# ...
```

Here is an example of setting a map's keys from a file. Starting with these variable definitions:
```
variable "region" {}
variable "amis" {
  type = "map"
}
```

You can specify keys in a terraform.tfvars file:
```
amis = {
  "us-east-1" = "ami-abc123"
  "us-west-2" = "ami-def456"
}
```

And access them via lookup():
```
output "ami" {
  value = "${lookup(var.amis, var.region)}"
}
```

Like so:
```
$ terraform apply -var region=us-west-2
```

## Output Variables
In this page, we introduce output variables as a way to organize data to be easily queried and shown back to the Terraform user.

When building potentially complex infrastructure, Terraform stores hundreds or thousands of attribute values for all your resources. But as a user of Terraform, you may only be interested in a few values of importance, such as a load balancer IP, VPN address, etc.

Outputs are a way to tell Terraform what data is important. This data is outputted when apply is called, and can be queried using the terraform output command.

### Defining Outputs
Let's define an output to show us the public IP address of the elastic IP address that we create. Add this to any of your \*.tf files:
```
output "ip" {
  value = "${aws_eip.ip.public_ip}"
}
```

This defines an output variable named "ip". The value field specifies what the value will be, and almost always contains one or more interpolations, since the output data is typically dynamic. In this case, we're outputting the public_ip attribute of the elastic IP address.

Multiple output blocks can be defined to specify multiple output variables.

### Viewing Outputs
Run terraform apply to populate the output. This only needs to be done once after the output is defined. The apply output should change slightly. At the end you should see this:
```
$ terraform apply
...

Apply complete! Resources: 0 added, 0 changed, 0 destroyed.

Outputs:
  ip = 50.17.232.209
```

apply highlights the outputs. You can also query the outputs after apply-time using terraform output:
```
$ terraform output ip
50.17.232.209
```

## Modules
Up to this point, we've been configuring Terraform by editing Terraform configurations directly. As our infrastructure grows, this practice has a few key problems: a lack of organization, a lack of reusability, and difficulties in management for teams.

Modules in Terraform are self-contained packages of Terraform configurations that are managed as a group. Modules are used to create reusable components, improve organization, and to treat pieces of infrastructure as a black box.

This section of the getting started will cover the basics of using modules. Writing modules is covered in more detail in the modules documentation.

### Using Modules
The Terraform Registry includes a directory of ready-to-use modules for various common purposes, which can serve as larger building-blocks for your infrastructure.

In this example, we're going to use the Consul Terraform module for AWS, which will set up a complete Consul cluster. This and other modules can found via the search feature on the Terraform Registry site.

```
provider "aws" {
  access_key = "AWS ACCESS KEY"
  secret_key = "AWS SECRET KEY"
  region     = "us-east-1"
}

module "consul" {
  source = "hashicorp/consul/aws"

  aws_region  = "us-east-1" # should match provider region
  num_servers = "3"
}
```

After adding a new module to configuration, it is necessary to run (or re-run) terraform init to obtain and install the new module's source code:
```
$ terraform init
# ...
```

### Apply Changes
With the Consul module (and its dependencies) installed, we can now apply these changes to create the resources described within.
```
$ terraform apply
  + module.consul.module.consul_clients.aws_autoscaling_group.autoscaling_group
      id:                                        <computed>
      ...
```

The module.consul.module.consul_clients prefix shown above indicates not only that the resource is from the module "consul" block we wrote, but in fact that this module has its own module "consul_clients" block within it. Modules can be nested to decompose complex systems into managable components.

### Module Outputs
Module can also produce output values, similar to resource attributes.

Add the following to the end of the existing configuration file created above:
```
output "consul_server_asg_name" {
  value = "${module.consul.asg_name_servers}"
}
```

The syntax for referencing module outputs is ${module.NAME.OUTPUT}, where NAME is the module name given in the header of the module configuration block and OUTPUT is the name of the output to reference.

### More on Module Doc
For more information on modules, the types of sources supported, how to write modules, and more.
Read the [in-depth module documentation](https://www.terraform.io/docs/modules/index.html).


## Remote Backends
We've now seen how to build, change, and destroy infrastructure from a local machine. This is great for testing and development, however in production environments it is more responsible to run Terraform remotely and store a master Terraform state remotely.

Terraform Enterprise is HashiCorp's commercial solution and also acts as a remote backend. Terraform Enterprise allows teams to easily version, audit, and collaborate on infrastructure changes. Each proposed change generates a Terraform plan which can be reviewed and collaborated on as a team. When a proposed change is accepted, the Terraform logs are stored, resulting in a linear history of infrastructure states to help with auditing and policy enforcement. Additional benefits to running Terraform remotely include moving access credentials off of developer machines and releasing local machines from long-running Terraform processes.

Terraform supports a feature known as remote backends to support this. Backends are the recommended way to use Terraform in a team environment.


## Next Steps
That concludes the getting started guide for Terraform. Hopefully you're now able to not only see what Terraform is useful for, but you're also able to put this knowledge to use to improve building your own infrastructure.

We've covered the basics for all of these features in this guide.

As a next step, the following resources are available:
- [Documentation](https://www.terraform.io/docs/index.html)
    The documentation is an in-depth reference guide to all the features of Terraform, including technical details about the internals of how Terraform operates.

- [Examples](https://www.terraform.io/intro/examples/index.html)
    The examples have more full featured configuration files, showing some of the possibilities with Terraform.

- [Import](https://www.terraform.io/docs/import/index.html)
    The import section of the documentation covers importing existing infrastructure into Terraform.
