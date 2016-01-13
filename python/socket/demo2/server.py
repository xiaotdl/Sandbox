# Socket server example in python
# ref: http://www.binarytides.com/python-socket-programming-tutorial/
"""
Socket as a server:
    1. Create a socket
    2. (connect) Connect to remote server
    3. (sendall) Send some data
    4. (recv)    Receive a reply
    5. (close)   Close the socket
"""

import socket   # for sockets
import sys      # for exit


HOST = ''   # Symbolic name meaning all available interfaces
POST = 8888 # Arbitrary non-previleged port

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
# backlog : controls the number of incoming connections
