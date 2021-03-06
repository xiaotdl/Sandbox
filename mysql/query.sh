#!/bin/bash

usage () {
    cat <<"EOF";
Usage:
    $ ./query.sh <query>
Example:
    $ ./query.sh "select user, host from mysql.user;"
EOF
}

if [[ "$#" -ne 1 ]]; then
    usage
    exit 1
fi


QUERY=$1
DB_HOST='127.0.0.1'
DB_USER='root'
DB_PASSWD='default'
DB_NAME='mysql'

echo mysql --host=$DB_HOST --user=$DB_USER --password=$DB_PASSWD --execute=\""$QUERY"\" $DB_NAME
mysql --host=$DB_HOST --user=$DB_USER --password=$DB_PASSWD --execute="$QUERY" $DB_NAME
