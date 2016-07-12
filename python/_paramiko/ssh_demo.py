#!/usr/bin/env python

import paramiko


USERNAME = "root"
PASSWORD = "default"
HOSTNAME = "10.192.10.206"
COMMAND = "cat /VERSION"

PORT = 22

try:
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.WarningPolicy())

    client.connect(HOSTNAME, port=PORT, username=USERNAME, password=PASSWORD)

    stdin, stdout, stderr = client.exec_command(COMMAND)
    print stdout.read(),

finally:
    client.close()
