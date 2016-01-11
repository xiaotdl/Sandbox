#!/bin/bash
#
#  This script will generate a pair of auth keys, login to the specified
#  BIGIP box, and add the key to its 'authorized_keys' file, enabling
#  passwordless ssh logins

# test for IP address argument
if [ -z "$1" ]
then
    echo "You must specifiy an IP-Address for a BIGIP"
    exit
fi

# test a successful ping
ping -c 1 -W 2 $1 &>/dev/null
if [ $? -ne 0 ]
then
    echo "Failed to ping address $1. Make sure it is correct."
    exit
fi

BIGIP=$1
FORCENEW=0


if [ -n "$2" ]
then
    # test for valid option...
    if [ "$2" == "-new" ]
    then
        FORCENEW=1
    else
        echo "invalid option $2"
        exit
    fi
fi


echo "--- Setting Up BIGIP $BIGIP ---"

if [ $FORCENEW -eq 1 ]
then
    echo -e 'Generating a new SSH KEY...'
    ssh-keygen -t rsa -N '' -f ~/.ssh/id_rsa -q
fi

echo "Installing SSH KEY to $BIGIP:.ssh/authorized_keys"
echo -e '\n'
echo "Enter root password for $BIGIP"
cat ~/.ssh/id_rsa.pub | ssh root@$BIGIP 'cat >> .ssh/authorized_keys'

echo "--- Finished BIGIP Setup ---"









