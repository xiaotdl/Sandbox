#!/usr/bin/expect
# Ref: http://www.thegeekstuff.com/2010/10/expect-examples

# 🍺 ssh root@10.192.219.152
# Password:
# You are required to change your password immediately (root enforced)
# Changing password for root.
# (current) UNIX password:
# New BIG-IP password:
# Retype new BIG-IP password:
# Last login: Tue Sep 19 09:04:46 2017 from 192.168.87.101
# [root@localhost:Active (worry) tandalone] config # exit
# logout
# Connection to 10.192.219.152 closed.

set timeout 20

#ssh root@10.192.219.152 'echo success'

set user "root"
set ip "10.192.219.152"
set old_password "default"
set new_password "f5site02"

spawn ssh "$user\@$ip"

expect "Password:"

send "$old_password\r";

expect "(current) UNIX password:"

send "$old_password\r";

expect "New BIG-IP password:"

send "$new_password\r";

expect "Retype new BIG-IP password:"

send "$new_password\r";

expect "Last login:"

send "exit\r";

#interact
