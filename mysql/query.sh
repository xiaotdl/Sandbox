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
DB_HOST='localhost'
DB_USER='root'
DB_PASSWD='default'
DB_NAME='mysql'

echo mysql --host=$DB_HOST --user=$DB_USER --password=$DB_PASSWD $DB_NAME -e \""$QUERY"\"
mysql --host=$DB_HOST --user=$DB_USER --password=$DB_PASSWD $DB_NAME -e "$QUERY"
