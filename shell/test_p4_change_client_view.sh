#!/bin/bash

add_or_remove=$1
file_pattern=$2
p4client=$3
tmp_file="/tmp/p4client.$p4client.$$"

usage () {
    cat <<"EOF";
Usage:
    $ ./change_client_view.sh add "//depot/.*?/tm_lib/cec/... .*" <p4_client_name>
    $ ./change_client_view.sh remove "//depot/.*?/tm_lib/cec/... .*" <p4_client_name>

    To apply changes on all branches:
    $ p4 clients -e 'MASTER-*-FIT' | cut -d' ' -f2 > /tmp/clients.txt
    $ while read -r client || [[ -n "$client"  ]]; do ./change_client_view.sh add "//depot/.*?/tm_lib/cec/... .*" $client; done < /tmp/clients.txt
EOF
}

if [[ "$add_or_remove" = "add" ]]; then
    add_to_depot="-($file_pattern)"
elif [[ "$add_or_remove" = "remove" ]]; then
    remove_from_depot="($file_pattern)"
else
    usage
    exit 1
fi

if [[ "$#" -lt 3 ]]; then
    usage
    exit 1
fi

main () {
    export P4CLIENT=$p4client

    p4 client -o $p4client> $tmp_file

    if [ -n "$add_to_depot"  ]; then
        perl -i -pe "s|$add_to_depot|\1|" $tmp_file;
    fi

    if [ -n "$remove_from_depot"  ]; then
        perl -i -pe "s|$remove_from_depot|-\1|" $tmp_file
    fi

    p4 client -i < $tmp_file

    rm $tmp_file

    # p4 sync
}

main
