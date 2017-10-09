# Ref:
# https://www.centos.org/docs/5/html/Deployment_Guide-en-US/s1-rpm-using.html

# install
rpm -ivh foo-1.0-1.i386.rpm
# force install regardless of if there is one already
rpm -ivh --replacepkgs foo-1.0-1.i386.rpm


# upgrade
rpm -Uvh foo-2.0-1.i386.rpm


# uninstall
rpm -e foo


# querying <-q>
# -a - queries all currently installed packages
# -f <filename> - queryies rpm db which package owns <filename>, <filename> needs to be abs path
# -p <packagefile>
# query opts
# -i - displays pkg info, like name, description, release etc.
# -l - displays the list of files the pkg contains.
# -s - displays the state of all files in the pkg.
# -d - displays the list of files marked as documentation (man, info, README, etc.).
# -c - displays the list of files marked as configuration files, for user to config after installation.
rpm -qa
rpm -qi openssh
rpm -ql openssh


# verify
rpm -V
