#!/bin/bash

## escape single quote with "'"
echo '/bin/sh -c '"'"'echo 123'"'"''
# >>> /bin/sh -c 'echo 123'

## escape double quote with '"'
echo '/bin/sh -c ''"''echo 123''"'''
# >>> /bin/sh -c "echo 123"
