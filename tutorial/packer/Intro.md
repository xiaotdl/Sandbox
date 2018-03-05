# Intro to Packer
Ref: https://www.packer.io/intro/index.html

Packer is an open source tool for creating identical machine images for multiple platforms from a single source configuration.

A machine image is a single static unit that contains a pre-configured operating system and installed software which is used to quickly create new running machines. Machine image formats change for each platform.
Some examples include AMIs for EC2, VMDK/VMX files for VMware, OVF exports for VirtualBox, etc.


## Why Packer?
- Super fast infrastructure deployment.
Packer images allow you to launch completely provisioned and configured machines in seconds

- Multi-provider portability.
Because Packer creates identical images for multiple platforms, you can run production in AWS, staging/QA in a private cloud like OpenStack, and development in desktop virtualization solutions such as VMware or VirtualBox. Each environment is running an identical machine image, giving ultimate portability.

- Improved stability.
Packer installs and configures all the software for a machine at the time the image is built.

- Greater testability.
After a machine image is built, that machine image can be quickly launched and smoke tested to verify that things appear to be working.


## Use Cases
- Continuous Delivery
Packer is lightweight, portable, and command-line driven. This makes it the perfect tool to put in the middle of your continuous delivery pipeline. Packer can be used to generate new machine images for multiple platforms on every change to Chef/Puppet.

- Dev/Prod Parity
Packer helps keep development, staging, and production as similar as possible. Packer can be used to generate images for multiple platforms at the same time. So if you use AWS for production and VMware (perhaps with Vagrant) for development, you can generate both an AMI and a VMware machine using Packer at the same time from the same template.

- Appliance/Demo Creation
Since Packer creates consistent images for multiple platforms in parallel, it is perfect for creating appliances and disposable product demos. As your software changes, you can automatically create appliances with the software pre-installed. Potential users can then get started with your software by deploying it to the environment of their choice.
