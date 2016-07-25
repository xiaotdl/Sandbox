#!/bin/bash

# # ${variable:-defaultvalue}
# column=${1:-9}
# awk '{print $'$column'}'

# same as >>>
# one-liner
awk '{print $column}' column=${1:-9}
# <<<
