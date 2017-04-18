#!/bin/bash
for i in `seq ${2} ${3}`
do
    ping -c 1 ${1}.${i} > /dev/null 2>&1
    if [ $? -eq 0 ]; then
        echo "${1}.${i} success."
    else
        echo "${1}.${i} fail."
    fi
done


# >>>
# xxxx@xxxxxx:~$ bash test.sh 10.140.0 100 103
# 10.140.0.100 success.
# 10.140.0.101 fail.
# 10.140.0.102 fail.
# 10.140.0.103 fail.
