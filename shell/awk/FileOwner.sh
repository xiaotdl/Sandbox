#!/bin/bash

awk '\
BEGIN   { print "File\tOwner" } \
        { print $9, "\t", $3}   \
END     { print " - DONE -" } \
'

# >>>
# $ ls -l | bash test_fileowner.sh
# FileOwner
# awk.doc.txt      xili
# test_fileowner.sh    xili
#  - DONE -
