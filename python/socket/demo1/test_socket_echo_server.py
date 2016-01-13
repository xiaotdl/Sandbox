# TCP/IP Client and Server
# ref: https://pymotw.com/2/socket/tcp.html

# Sockets can be configured to act as a [server] and listen for incoming messages,
# or connect to other applications as a [client].
# After both ends of a TCP/IP socket are connected, communication is bi-directional.

import socket
import sys


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print >>sys.stderr, 'starting up on %s:%s' % server_address # starting up on localhost:10000
# >>>
# $  ~  netstat -an | grep 10000
# tcp4       0      0  127.0.0.1.10000        *.*                    LISTEN

# Note: we can use empty string '' here to listen on all addresses, instead of just localhost
# server_address = ('', 10000)
# print >>sys.stderr, 'starting up on %s:%s' % sock.getsockname() # starting up on 0.0.0.0:0
# >>>
# $  ~  netstat -an | grep 10000
# tcp4       0      0  *.10000                *.*                    LISTEN


sock.bind(server_address)

# Listen for incoming connections
sock.listen(1) # listen() puts the socket into server mode

while True:
    # Wait for a connection
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept() # accept() waits for an incoming connection.
    # connection is actually a different socket on another port (assigned by the kernel).

    try:
        print >>sys.stderr, 'connection from', client_address

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16) # data is read from the connection with recv()
            print >>sys.stderr, 'received "%s"' % data
            if data:
                print >>sys.stderr, 'sending data back to the client'
                connection.sendall(data) # data is transmitted with sendall()
            else:
                print >>sys.stderr, 'no more data from', client_address
                break

    finally:
        # Clean up the connection
        connection.close() # close() socket is closed to free up the port.

# $ python ./socket_echo_server.py

# >>>
# starting up on localhost:10000
# waiting for a connection
# connection from ('127.0.0.1', 51958)
# received "This is the mess"
# sending data back to the client
# received "age.  It will be"
# sending data back to the client
# received " repeated."
# sending data back to the client
# received ""
# no more data from ('127.0.0.1', 51958)
# waiting for a connection
