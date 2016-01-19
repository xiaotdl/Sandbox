# Socket server example in python
# ref: http://www.binarytides.com/python-socket-programming-tutorial/
"""
Socket as a server:
    1. Create a socket
    2. (bind)    Bind a socket to an IP and port
    3. (listen)  Put socket in listening mode
    4. (accept)  Accept a connection
    5. (send)    Send some data
    6. (recv)    Receive a reply
    7. (sendall) Send some data
    8. (close)   Close the socket
"""

import socket   # for sockets
import sys      # for exit
from thread import *    # use multiple threads to handle multiple connections


HOST = ''   # Symbolic name meaning all available interfaces
PORT = 8888 # Arbitrary non-previleged port

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created successfully!'

# == socket.bind() ==
# bind a socket to an ip address and port
try:
    sock.bind((HOST, PORT))
except socket.error, msg:
    print ('Failed to bind socket:\n' +
            'Error code: %s\n' % msg[0] +
            'Error message: %s\n' % msg[1])
    sys.exit()
print 'Socket bind successfully!'

# == socket.listen() ==
# put socket in listening mode, behaves like a server
sock.listen(10)
print 'Socket now listening...'
# backlog : controls the number of incoming connections

def client_thread(conn):
    conn.send('Welcome to the server. Type something and hit enter\n') # send only takes string

    while True:
        # == socket.recv() ==
        # Receive data from the connection
        data = conn.recv(1024)
        # == socket.sendall() ==
        # send reply to the incoming connection
        reply = 'OK...' + data
        if not data:
            break
        conn.sendall(reply)

    conn.close()

while True:
    # == socket.accpet() ==
    conn, addr = sock.accept()
    print 'Connected with %s:%s' % (addr[0], addr[1])

    start_new_thread(client_thread, (conn,))

# == socket.close() ==
sock.close()

