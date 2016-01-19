import socket


HOST = ''   # Symbolic name meaning all available interfaces
PORT = 5000
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))
print 'waiting on port %s' % PORT

while True:
    # == sock.recvfrom ==
    data, addr = sock.recvfrom(1024)
    reply = 'OK ...' + data
    # == sock.sendto ==
    sock.sendto(reply, addr)
    print 'Received message from %s:%s' % addr + ' - ' + data

s.close()

# >>>
# $  ~  nc -u localhost 5000
# hey
# OK ...hey
# what's up
# OK ...what's up
