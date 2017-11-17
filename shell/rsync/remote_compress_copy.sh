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



# Copy VM Template between ESX hosts
~ # rsync -avzh --sparse --progress vmfs/volumes/ISCSI-Vol01/fit-t-bigiq-5.3.0/ root@10.192.197.22:/vmfs/volumes/ISCSI-Vol0/fit-t-bigiq-5.3.0.sparse

# Download rsync static binary on ESX hosts
https://wiki.contribs.org/Backup_of_ESXi_Virtual_Machines_using_Affa
$ wget http://mirror.contribs.org/smeserver/contribs/michaelw/sme7/Affa2/affa-esxi-setup-02.tgz
$ tar xvzf affa-esxi-setup-02.tgz
$ scp bexi/rsync-static root@10.192.197.22:/bin/rsync
$ ssh root@10.192.197.22 'chmod +x /bin/rsync'

