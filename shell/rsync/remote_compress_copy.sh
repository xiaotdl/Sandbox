# Ref:
# https://download.samba.org/pub/rsync/rsync.html
# https://einverne.github.io/post/2017/07/rsync-introduction.html
# == rsync ==
# -a, --archive               archive mode; equals -rlptgoD (no -H,-A,-X)
# -v, --verbose               increase verbosity
# -z, --compress              compress file data during the transfer
# -h, --human-readable        output numbers in a human-readable format
#     --progress              show progress during transfer
# -e, --rsh=COMMAND           specify the remote shell to use
rsync -avzhe ssh --progress /home/files/ root@remoteip:/path/to/files/
