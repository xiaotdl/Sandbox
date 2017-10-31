#ref: https://www.digitalocean.com/community/tutorials/how-to-use-rsync-to-sync-local-and-remote-directories-on-a-vps

# -a, a combination flag.
# It stands for "archive" and syncs recursively and preserves symbolic links, special and device files, modification times, group, owner, and permissions.
# -v, verbose
# -h, human readable


mkdir dir1
touch dir1/f{1..3}

mkdir -p dir2/path/to/dir1

rsync -avh dir1/ dir2/path/to/dir1

tree dir1 dir2


# >>>
# building file list ... done
# f1
# f2
# f3
#
# sent 240 bytes  received 86 bytes  652.00 bytes/sec
# total size is 0  speedup is 0.00
# dir1
# ├── f1
# ├── f2
# └── f3
# dir2
# └── path
#     └── to
#         └── dir1
#             ├── f1
#             ├── f2
#             └── f3
