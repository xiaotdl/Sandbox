#!/bin/bash

# Deps:
# sudo apt-get install sshpass

# Ref: http://unix.stackexchange.com/questions/107800/using-while-loop-to-ssh-to-multiple-servers
# Issue:
#   while read will read from stdin, while sshpass would also reads stdin,
#   so it winds up eating the rest of the file
# Workaround:
#   This works on any POSIX-compatible shell
# e.g.
#   exec 3<&0;                    # use file descriptor 3 as a backup of the original stdin
#   while read HOST;
#   do
#       ssh $HOST "uname -a" <&3; # uses it for ssh's stdin,
#   done < servers.txt;
#   exec 3<&-                     # closes the backup FD when done.

# debug
#set -x

FILE=files/bigips.txt

exec 3<&0

while read name mgmtIP rest;
do
    echo -n "host: $name, ip: $mgmtIP, output=> "
    pwd='default'
    user='root'
    hostname=$mgmtIP
    cmd="tmsh list sys global-settings hostname | grep hostname | sed 's/^[ \t ]*//;s/[ \t ]*$//'"
    sshpass -p $pwd ssh \
        -o UserKnownHostsFile=/dev/null \
        -o StrictHostKeyChecking=no \
        -o LogLevel=quiet \
        $user@$hostname $cmd \
        <&3
done < $FILE

exec 3<&-
