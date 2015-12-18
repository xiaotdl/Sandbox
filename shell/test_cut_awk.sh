## <awk>

# Let's generate some numbers and print them on groups of 5:

`seq 12 | xargs -n5`
# >>>
# 1 2 3 4 5
# 6 7 8 9 10
# 11 12

# Let's print the penultimate on each line:

`seq 12 | xargs -n5 | awk '{NF--; print $NF}'`
# >>>
# 4
# 9
# 11



## <cut>
`cut -d':' -f1 /etc/passwd`
# >>>
# root
# daemon
# bin
# sys
# sync
# games
# bala

`grep "/bin/bash" /etc/passwd | cut -d':' -f1-4,6,7`
# >>>
# root:x:0:0:/root:/bin/bash
# bala:x:1000:1000:/home/bala:/bin/bash
