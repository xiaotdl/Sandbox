# OpenStack Virtual Machine Image Guide
https://docs.openstack.org/image-guide/

This guide describes how to obtain, create, and modify virtual machine images that are compatible with OpenStack.

## Introduction

An OpenStack Compute cloud is not very useful unless you have virtual machine images (a.k.a. “virtual appliances”). This guide describes how to obtain, create, and modify virtual machine images that are compatible with OpenStack.

### What is a virtual machine image?
A virtual machine image is a single file which contains a virtual disk that has a bootable operating system installed on it.

Virtual machine images come in different formats:
- AKI/AMI/ARI
    The AKI/AMI/ARI format was the initial image format supported by Amazon EC2. The image consists of three files:
    - AKI (Amazon Kernel Image)
        A kernel file that the hypervisor will load initially to boot the image. For a Linux machine, this would be a vmlinuz file.
    - AMI (Amazon Machine Image)
        This is a virtual machine image in raw format, as described above.
    - ARI (Amazon Ramdisk Image)
        An optional ramdisk file mounted at boot time. For a Linux machine, this would be an initrd file.

- ISO
    The ISO format is a disk image formatted with the read-only ISO 9660 (also known as ECMA-119) filesystem commonly used for CDs and DVDs. While we do not normally think of ISO as a virtual machine image format, since ISOs contain bootable filesystems with an installed operating system, you can treat them the same as you treat other virtual machine image files.

- OVF
    OVF (Open Virtualization Format) is a packaging format for virtual machines, defined by the Distributed Management Task Force (DMTF) standards group. An OVF package contains one or more image files, a .ovf XML metadata file that contains information about the virtual machine, and possibly other files as well.

    An OVF package can be distributed in different ways. For example, it could be distributed as a set of discrete files, or as a tar archive file with an .ova (open virtual appliance/application) extension.

    OpenStack Compute does not currently have support for OVF packages, so you will need to extract the image file(s) from an OVF package if you wish to use it with OpenStack.

- QCOW2
    The QCOW2 (QEMU copy-on-write version 2) format is commonly used with the KVM hypervisor. It has some additional features over the raw format, such as:
    - Using sparse representation, so the image size is smaller.
    - Support for snapshots.
    Because qcow2 is sparse, qcow2 images are typically smaller than raw images. Smaller images mean faster uploads, so it is often faster to convert a raw image to qcow2 for uploading instead of uploading the raw file directly.

- Raw
    The raw image format is the simplest one, and is natively supported by both KVM and Xen hypervisors. You can think of a raw image as being the bit-equivalent of a block device file, created as if somebody had copied, say, /dev/sda to a file using the dd command.

- UEC tarball
    A UEC (Ubuntu Enterprise Cloud) tarball is a gzipped tarfile that contains an AMI file, AKI file, and ARI file.

- VDI
    VirtualBox uses the VDI (Virtual Disk Image) format for image files. None of the OpenStack Compute hypervisors support VDI directly, so you will need to convert these files to a different format to use them with OpenStack.

- VHD
    Microsoft Hyper-V uses the VHD (Virtual Hard Disk) format for images.

- VHDX
    The version of Hyper-V that ships with Microsoft Server 2012 uses the newer VHDX format, which has some additional features over VHD such as support for larger disk sizes and protection against data corruption during power failures.

- VMDK
    VMware ESXi hypervisor uses the VMDK (Virtual Machine Disk) format for images.


### Disk and container formats for images
When you add an image to the Image service, you can specify its disk and container formats.

#### Disk formats
The disk format of a virtual machine image is the format of the underlying disk image. Virtual appliance vendors have different formats for laying out the information contained in a virtual machine disk image.

Set the disk format for your image to one of the following values:
- aki
    An Amazon kernel image.
- ami
    An Amazon machine image.
- ari
    An Amazon ramdisk image.
- iso
    An archive format for the data contents of an optical disc, such as CD-ROM.
- qcow2
    Supported by the QEMU emulator that can expand dynamically and supports Copy on Write.
- raw
    An unstructured disk image format; if you have a file without an extension it is possibly a raw format.
- vdi
    Supported by VirtualBox virtual machine monitor and the QEMU emulator.
- vhd
    The VHD disk format, a common disk format used by virtual machine monitors from VMware, Xen, Microsoft, VirtualBox, and others.
- vhdx
    The VHDX disk format, an enhanced version of the VHD format, which supports larger disk sizes among other features.
- vmdk
    Common disk format supported by many common virtual machine monitors.

#### Container formats
The container format indicates whether the virtual machine image is in a file format that also contains metadata about the actual virtual machine.
You can set the container format for your image to one of the following values:
- aki
    An Amazon kernel image.
- ami
    An Amazon machine image.
- ari
    An Amazon ramdisk image.
- bare
    The image does not have a container or metadata envelope.
- docker
    A docker container format.
- ova
    An OVF package in a tarfile.
- ovf
    The OVF container format.

### Image metadata
Image metadata can help end users determine the nature of an image, and is used by associated OpenStack components and drivers which interface with the Image service.

Add metadata to image service by using '--property key=value' parameter with the openstack image create or openstack image set command. More than one property can be specified.
```
$ openstack image set
    --property architecture=arm \
    --property hypervisor_type=qemu \
    image_name_or_id
```

## Get images
The simplest way to obtain a virtual machine image that works with OpenStack is to download one that someone else has already created. Most of the images contain the cloud-init package to support the SSH key pair and user data injection. Because many of the images disable SSH password authentication by default, boot the image with an injected key pair. You can SSH into the instance with the private key and default login account. See Configure access and security for instances for more information on how to create and inject key pairs with OpenStack.

#### CentOS
The CentOS project maintains official images for direct download.
- [CentOS 6 images](http://cloud.centos.org/centos/6/images/)
- [CentOS 7 images](http://cloud.centos.org/centos/7/images/)

In a CentOS cloud image, the login account is "centos".

#### CirrOS (test)
CirrOS is a minimal Linux distribution that was designed for use as a test image on clouds such as OpenStack Compute.

In a CirrOS image, the login account is "cirros". The password is "cubswin:)".

#### Debian
Debian provides images for direct download.
http://cdimage.debian.org/cdimage/openstack/

In a Debian image, the login account is "debian".

#### Fedora
The Fedora project maintains a list of official cloud images at Fedora download page.
https://alt.fedoraproject.org/cloud/

In a Fedora cloud image, the login account is "fedora".

#### Microsoft Windows
https://cloudbase.it/windows-cloud-images/

Cloudbase Solutions hosts Windows Cloud Images that runs on Hyper-V, KVM, and XenServer/XCP.

#### Ubuntu
Canonical maintains an official set of Ubuntu-based images.
http://cloud-images.ubuntu.com/

In an Ubuntu cloud image, the login account is "ubuntu".

#### openSUSE and SUSE Linux Enterprise Server
The openSUSE community provides images for openSUSE.

#### Red Hat Enterprise Linux
Red Hat maintains official Red Hat Enterprise Linux cloud images.
A valid Red Hat Enterprise Linux subscription is required to download these images.

In a RHEL cloud image, the login account is "cloud-user".


## Image requirements

### Linux
For a Linux-based image to have full functionality in an OpenStack Compute cloud, there are a few requirements. For some of these, you can fulfill the requirements by installing the cloud-init package.

Read this section before you create your own image to be sure that the image supports the OpenStack features that you plan to use.
- Disk partitions and resize root partition on boot (cloud-init)
- No hard-coded MAC address information
- SSH server running
- Disable firewall
- Access instance using ssh public key (cloud-init)
- Process user data and other metadata (cloud-init)
- Paravirtualized Xen support in Linux kernel (Xen hypervisor only with Linux kernel version < 3.0)

### Disk partitions and resize root partition on boot (cloud-init)

#### Xen: one ext3/ext4 partition (no LVM)
...

#### Non-Xen with cloud-init/cloud-tools: one ext3/ext4 partition (no LVM)
Depending on your distribution, the simplest way to support this is to install in your image:
- the cloud-init package,
- the cloud-utils package, which, on Ubuntu and Debian, also contains the growpart tool for extending partitions,
- if you use Fedora, CentOS 7, or RHEL 7, the cloud-utils-growpart package, which contains the growpart tool for extending partitions,
- if you use Ubuntu or Debian, the cloud-initramfs-growroot package , which supports resizing root partition on the first boot.

With these packages installed, the image performs the root partition resize on boot. For example, in the /etc/rc.local file.

If you can install the cloud-init and cloud-utils packages, we recommend that when you create your images, you create a single ext3 or ext4 partition (not managed by LVM).

#### Non-Xen without cloud-init/cloud-tools: LVM
...

### No hard-coded MAC address information
You must remove the network persistence rules in the image because they cause the network interface in the instance to come up as an interface other than eth0. This is because your image has a record of the MAC address of the network interface card when it was first installed, and this MAC address is different each time the instance boots. You should alter the following files:
- Replace /etc/udev/rules.d/70-persistent-net.rules with an empty file (contains network persistence rules, including MAC address).
- Replace /lib/udev/rules.d/75-persistent-net-generator.rules with an empty file (this generates the file above).
- Remove the HWADDR line from /etc/sysconfig/network-scripts/ifcfg-eth0 on Fedora-based images.

 Note:
 If you delete the network persistent rules files, you may get a udev kernel warning at boot time, which is why we recommend replacing them with empty files instead.

### Ensure ssh server runs
You must install an ssh server into the image and ensure that it starts up on boot, or you cannot connect to your instance by using ssh when it boots inside of OpenStack. This package is typically called openssh-server.

### Disable firewal
In general, we recommend that you disable any firewalls inside of your image and use OpenStack security groups to restrict access to instances. The reason is that having a firewall installed on your instance can make it more difficult to troubleshoot networking issues if you cannot connect to your instance.

### Access instance by using ssh public key (cloud-init)
The typical way that users access virtual machines running on OpenStack is to ssh using public key authentication. For this to work, your virtual machine image must be configured to download the ssh public key from the OpenStack metadata service or config drive, at boot time.

If both the XenAPI agent and cloud-init are present in an image, cloud-init handles ssh-key injection. The system assumes cloud-init is present when the image has the cloud_init_installed property.

#### Use cloud-init to fetch the public key

#### Write a custom script to fetch the public key
To fetch the ssh public key and add it to the root account, edit the /etc/rc.local file and add the following lines before the line touch /var/lock/subsys/local. This code fragment is taken from [the rackerjoe oz-image-build CentOS 6 template](https://github.com/rcbops/oz-image-build/blob/master/templates/centos60_x86_64.tdl).

```
if [ ! -d /root/.ssh ]; then
  mkdir -p /root/.ssh
  chmod 700 /root/.ssh
fi

# Fetch public key using HTTP
ATTEMPTS=30
FAILED=0
while [ ! -f /root/.ssh/authorized_keys ]; do
  curl -f http://169.254.169.254/latest/meta-data/public-keys/0/openssh-key > /tmp/metadata-key 2>/dev/null
  if [ $? -eq 0 ]; then
    cat /tmp/metadata-key >> /root/.ssh/authorized_keys
    chmod 0600 /root/.ssh/authorized_keys
    restorecon /root/.ssh/authorized_keys
    rm -f /tmp/metadata-key
    echo "Successfully retrieved public key from instance metadata"
    echo "*****************"
    echo "AUTHORIZED KEYS"
    echo "*****************"
    cat /root/.ssh/authorized_keys
    echo "*****************"
  else
    FAILED=`expr $FAILED + 1`
    if [ $FAILED -ge $ATTEMPTS ]; then
      echo "Failed to retrieve public key from instance metadata after $FAILED attempts, quitting"
      break
    fi
    echo "Could not retrieve public key from instance metadata (attempt #$FAILED/$ATTEMPTS), retrying in 5 seconds..."
    sleep 5
  fi
done
```

#### Process user data and other metadata (cloud-init)
In addition to the ssh public key, an image might need additional information from OpenStack, such as to povide user data to instances, that the user submitted when requesting the image. For example, you might want to set the host name of the instance when it is booted. Or, you might wish to configure your image so that it executes user data content as a script on boot.

The easiest way to support this type of functionality is to install the cloud-init package into your image, which is configured by default to treat user data as an executable script, and sets the host name.

#### Ensure image writes boot log to console
You must configure the image so that the kernel writes the boot log to the ttyS0 device. In particular, the console=tty0 console=ttyS0,115200n8 arguments must be passed to the kernel on boot.

#### Paravirtualized Xen support in the kernel (Xen hypervisor only)

#### Manage the image cache


### Modify images
Once you have obtained a virtual machine image, you may want to make some changes to it before uploading it to the Image service. Here we describe several tools available that allow you to modify images.

#### guestfish
The guestfish program is a tool from the libguestfs project that allows you to modify the files inside of a virtual machine image.

- start a guestfish session
```
# guestfish --rw -a centos63_desktop.img

Welcome to guestfish, the libguestfs filesystem interactive shell for
editing virtual machine filesystems.

Type: 'help' for help on commands
'man' to read the manual
'quit' to quit the shell

><fs>
```

We must first use the run command at the guestfish prompt before we can do anything else. This will launch a virtual machine, which will be used to perform all of the file manipulations.
```
><fs> run
```

#### guestmount


### Create images manually

#### Example: CentOS image

#### Example: Ubuntu image

#### Example: Fedora image

#### Example: Microsoft Windows image

#### Example: FreeBSD image


### Tool support for image creation
...
- Packer
	Packer is a tool for creating machine images for multiple platforms from a single source configuration.


### Converting between image formats
Converting images from one format to another is generally straightforward.

#### qemu-img convert: raw, qcow2, qed, vdi, vmdk, vhd
The qemu-img convert command can do conversion between multiple formats, including qcow2, qed, raw, vdi, vhd, and vmdk.

qemu-img format strings
Image format       Argument to qemu-img
------------------+---------------------
QCOW2 (KVM, Xen)   qcow2
QED (KVM)		   qed
raw				   raw
VDI (VirtualBox)   vdi
VHD (Hyper-V)	   vpc
VMDK (VMware)	   vmdk

This example will convert a raw image file named image.img to a qcow2 image file.
```
$ qemu-img convert -f raw -O qcow2 image.img image.qcow2
```

Run the following command to convert a vmdk image file to a raw image file.
```
$ qemu-img convert -f vmdk -O raw image.vmdk image.img
```

#### VBoxManage: VDI (VirtualBox) to raw
```
$ VBoxManage clonehd ~/VirtualBox\ VMs/image.vdi image.img --format raw
```


### Image sharing





































































































