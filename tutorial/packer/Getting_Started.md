# Getting Started

## Install Packer

## Build an Image

### The Template
The configuration file used to define what image we want built and how is called a template in Packer terminology. The format of a template is simple JSON. JSON struck the best balance between human-editable and machine-editable, allowing both hand-made templates as well as machine generated templates to easily be made.


### Your First Image
$ packer build \
    -var 'aws_access_key=YOUR ACCESS KEY' \
    -var 'aws_secret_key=YOUR SECRET KEY' \
    example.json
...
==> Builds finished. The artifacts of successful builds are:
--> amazon-ebs: AMIs were created:

us-east-1: ami-19601070


### Managing the Image

### See more examples
{
    "variables": {
        "aws_access_key": "{{env `AWS_ACCESS_KEY_ID`}}",
        "aws_secret_key": "{{env `AWS_SECRET_ACCESS_KEY`}}",
        "region":         "us-east-1"
    },
    "builders": [
        {
            "access_key": "{{user `aws_access_key`}}",
            "ami_name": "packer-linux-aws-demo-{{timestamp}}",
            "instance_type": "t2.micro",
            "region": "us-east-1",
            "secret_key": "{{user `aws_secret_key`}}",
            "source_ami_filter": {
              "filters": {
              "virtualization-type": "hvm",
              "name": "ubuntu/images/*ubuntu-xenial-16.04-amd64-server-*",
              "root-device-type": "ebs"
              },
              "owners": ["099720109477"],
              "most_recent": true
            },
            "ssh_username": "ubuntu",
            "type": "amazon-ebs"
        }
    ],
    "provisioners": [
        {
            "type": "file",
            "source": "./welcome.txt",
            "destination": "/home/ubuntu/"
        },
        {
            "type": "shell",
            "inline":[
                "ls -al /home/ubuntu",
                "cat /home/ubuntu/welcome.txt"
            ]
        },
        {
            "type": "shell",
            "script": "./example.sh"
        }
    ]
}

### A Windows Example


## Provision
The real utility of Packer comes from being able to install and configure software into the images as well. This stage is also known as the provision step. Packer fully supports automated provisioning in order to install software onto the machines prior to turning them into images.

### Configuring Provisioners
{
  "variables": ["..."],
  "builders": ["..."],

  "provisioners": [{
    "type": "shell",
    "inline": [
      "sleep 30",
      "sudo apt-get update",
      "sudo apt-get install -y redis-server"
    ]
  }]
}

Note: The sleep 30 in the example above is very important. Because Packer is able to detect and SSH into the instance as soon as SSH is available, Ubuntu actually doesn't get proper amounts of time to initialize. The sleep makes sure that the OS properly initializes.

### Build


## Parallel Builds
Packer can create multiple images for multiple platforms in parallel, all configured from a single template.

As an example, Packer is able to make an AMI and a VMware virtual machine in parallel provisioned with the same scripts, resulting in near-identical images. The AMI can be used for production, the VMware machine can be used for development.

### Template
  "builders": [{
    "type": "amazon-ebs",
    "access_key": "{{user `aws_access_key`}}",
    "secret_key": "{{user `aws_secret_key`}}",
    "region": "us-east-1",
    "source_ami": "ami-fce3c696",
    "instance_type": "t2.micro",
    "ssh_username": "ubuntu",
    "ami_name": "packer-example {{timestamp}}"
  },{
    "type": "digitalocean",
    "api_token": "{{user `do_api_token`}}",
    "image": "ubuntu-14-04-x64",
    "region": "nyc3",
    "size": "512mb",
    "ssh_username": "root"
  }],

### Build
Packer builds both the Amazon and DigitalOcean images in parallel. It outputs information about each in different colors (although you can't see that in the block above).



## Vagrant Boxes
Packer also has the ability to take the results of a builder (such as an AMI or plain VMware image) and turn it into a Vagrant box.

This is done using post-processors. These take an artifact created by a previous builder or post-processor and transforms it into a new one. In the case of the Vagrant post-processor, it takes an artifact from a builder and transforms it into a Vagrant box file.

### Enabling the Post-Processor
{
  "builders": ["..."],
  "provisioners": ["..."],
  "post-processors": ["vagrant"]
}

When using post-processors, Vagrant removes intermediary artifacts since they're usually not wanted. Only the final artifact is preserved. This behavior can be changed, of course. Changing this behavior is covered in the documentation.


## Next Steps
https://www.packer.io/docs/index.html
The documentation is less of a guide and more of a reference of all the overall features and options of Packer.
