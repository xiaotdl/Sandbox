#!/usr/bin/env python

import os
import paramiko

USERNAME = "root"
PASSWORD = "default"
HOSTNAME = "10.192.10.206"
PORT = 22

t = paramiko.Transport((HOSTNAME, PORT))
try:
    t.connect(username=USERNAME, password=PASSWORD)
    sftp = paramiko.SFTPClient.from_transport(t)
    os.system("echo haha > demo1.txt")
    sftp.put('demo1.txt', '/shared/demo1.txt')
    sftp.get('/shared/demo1.txt', 'demo2.txt')
finally:
    t.close()
