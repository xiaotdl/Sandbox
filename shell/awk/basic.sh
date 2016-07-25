#!/bin/bash

# print everything
# awk '{print $0}'
# $ ll | bash basic.sh
# >>>
# ...


# modify some fields
# awk '{$1=""; $3=""; print}'
# $ ll | bash basic.sh
# >>>
# ...


# only print some fields
# awk '{print $1, $3;}'
# $ ll | bash basic.sh
# >>>
# ...


# == Input Field Separator Variable (FS) ==
# awk -F" " '{if ($3 == "xili") print $3, $9}'
# $ ll | bash basic.sh
# >>>
# ...


# == Output Field Separator Variable (OFS) ==


# == The Number of Fields Variable (NF) ==
# awk '{
#     if (NF == 8) {
#         print $3, $8;
#     } else if (NF == 9) {
#         print $3, $9;\
#     }
# }'


# == Last Field Variable ($NF) ==
# awk '{ if (NF == 9) print $NF}'


# == The Number of Records Variable (NR) ==
# By default, one record refers to one line.
# awk '{print NR, $0}'


# == The Record Seperator Variable (RS) ==
# == The Output Record Separator Variable (ORS) ==

# == The Current Filename Variable (FILENAME) ==
# awk '{print "reading", FILENAME}' # XXX Doesn't work!
# $ bash basic.sh < <file>
# >>>
# 


# == Associative Arrays ==
# count files created by each user
awk '{
    if (NR != 1)
    username[$3]++;
}
END {
    for (i in username) {
        print username[i], i;
    }
}'
# $ ll | bash basic.sh
# >>>
# 1 root
# 8 xili
