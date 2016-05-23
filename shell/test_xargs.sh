#!/bin/bash

# # == expects input from stdin and output to stdout ==
# $ xargs
# hi
# what up dude
# <Ctrl+d>
# hi what up dude
# 
# # == specify delimiter using -d option ==
# $ xargs -d\n
# hi
# what up dude
# <Ctrl+d>
# hi
# what up dude

# == basic ==
echo a b c d e f | xargs
# >>>
# a b c d e f

# == -n: limit output per line ==
echo a b c d e f | xargs -n 3
# >>>
# a b c
# d e f

# # == -p: prompt user before execution ==
# echo a b c d e f| xargs -p -n 3
# # >>>
# # /bin/echo a b c?...y
# # a b c
# # /bin/echo d e f?...y
# # d e f

# == -t: print the command along with output ==
echo a b c d e f| xargs -t
# >>>
# /bin/echo a b c d e f
# a b c d e f

# == xargs + find ==
# most popular use cases, find certain type of files and delete them
find . -name "*.sh" | xargs echo

# == xargs + grep ==
grep -RIl echo . | xargs grep -RIl xargs

# == xargs + find + grep ==
find . -name '*.sh' | xargs grep echo


echo EOF
