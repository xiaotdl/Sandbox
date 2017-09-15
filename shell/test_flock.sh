#!/bin/bash
# flock - manage locks from shell scripts
# Ref: https://linuxaria.com/howto/linux-shell-introduction-to-flock

set -x # debug
set -e # exit immediately upon failure

scriptname=$(basename $0)
lock="/var/run/lock/${scriptname}"

exec 200>$lock                      # open $lock file for reading and assign file handle 200
flock -n 200 || exit 1              # -n,-nb,-nonblock: fail rather than wait if the lock can't be acquired

## The code:
pid=$$
echo $pid 1>&200
sleep 60
echo "Hello world"
