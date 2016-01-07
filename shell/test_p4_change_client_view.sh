#!/bin/bash
# Example usage:
# modifies $add_to_depot to include files you would like to include
# $ ./change_client_view.sh xili-vm
#
# To apply changes on all branches:
# $ p4 clients -e 'MASTER-*-FIT' | cut -d' ' -f2 > /tmp/clients.txt
# $ while read -r client || [[ -n "$client"  ]]; do ./change_client_view.sh $client; done < /tmp/clients.txt

p4client=$1
add_to_depot="-(//depot/.*?/tm_lib/cec/... .*)"
#remove_from_depot="(//depot/.*?/tm_lib/cec/... .*)"
tmp_file="/tmp/p4client.$p4client.$$"


export P4CLIENT=$p4client

p4 client -o > $tmp_file

if [ -n "$add_to_depot"  ]; then
    echo perl -i -pe "s|$add_to_depot|\1|" $tmp_file;
fi

if [ -n "$remove_from_depot"  ]; then
    echo perl -i -pe "s|$remove_from_depot|-\1|" $tmp_file
fi

p4 client -i < $tmp_file

rm $tmp_file

# p4 sync
