# sort numeric
$ <> | sort -g

# sort with header skipped
$ lsmod | awk 'NR == 1; NR > 1 {print $0 | "sort"}'

