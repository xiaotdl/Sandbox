import socket
import sys


# # Create a TCP/IP socket
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# # Connect the socket to the port where the server is listening
# server_address = ('localhost', 10000)
# print >>sys.stderr, 'connecting to %s port %s' % server_address
# sock.connect(server_address) # connect() to attach the socket directly to the remote address.

# same as >>>
sock = socket.create_connection(('localhost', 10000))
# <<<

try:
    # Send data
    message = 'This is the message.  It will be repeated.'
    print >>sys.stderr, 'sending "%s"' % message
    sock.sendall(message) # data can be sent through the socket with sendall()

    # Look for the response
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(16) # data can be received with recv()
        amount_received += len(data)
        print >>sys.stderr, 'received "%s"' % data

finally:
    print >>sys.stderr, 'closing socket'
    sock.close() # close() socket is closed to free up the port.

# $ python socket_echo_client.py
# >>>
# connecting to localhost port 10000
# sending "This is the message.  It will be repeated."
# received "This is the mess"
# received "age.  It will be"
# received " repeated."
# closing socket
