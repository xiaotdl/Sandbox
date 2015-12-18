import socket
import sys
from thread import *

host = ''
port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((host, port))
except socket.error as e:
    print (str(e))

s.listen(5)
print 'Waiting for a connection...'
def threaded_client(conn):
    conn.send('Welcome, type your info\n')
    while True:
        data = conn.recv(2048)
        reply = 'Server output: ' + data
        if not data:
            break
        conn.sendall(reply)
    conn.close()


while True:
    conn, addr = s.accept()
    print 'connected to: %s:%s' % (addr[0], addr[1])
    start_new_thread(threaded_client, (conn,))

# >>>
# server side:
# ➜  ~ python test.py
# Waiting for a connection...
# connected to: 127.0.0.1:53901

# client side:
# ➜  ~  telnet 127.0.0.1 5555
# Trying 127.0.0.1...
# Connected to localhost.
# Escape character is '^]'.capitalizeWelcome, type your info
# hello
# Server output: hello
