#!/bin/bash

# awk '$1 ~ /OUT/ {print "match!"}'
# >>>
# OUT
# match!

# awk "\$1 !~ /OUT/  { print \"Doesn't match!\" }"
# >>>
# 
# Doesn't match!
