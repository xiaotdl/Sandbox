import socket
import select


CONNECTION_LIST = []
RECV_BUFFER = 4096
PORT = 5000

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_sock.bind(('localhost', PORT))
server_sock.listen(10)

CONNECTION_LIST.append(server_sock)
print 'Chat server started on localhost:%s' % PORT

while True:
    # == select.select ==
    # Get the list sockets which are ready to be read through select.
    # The select function is given the list of connected sockets CONNECTION_LIST.
    # write_sockets and error_sockets are kept empty since we do not need to check
    # any sockets to be writable or having errors.
    read_sockets,write_sockets,error_sockets = select.select(CONNECTION_LIST,[],[])

    for sock in read_sockets:
        # New connection
        if sock == server_sock:
            conn, addr = server_sock.accept()
            CONNECTION_LIST.append(conn)
            print 'Client %s:%s connected' % addr

        # Some incoming message from a client
        else:
            try:
                # In Windows, sometimes when a TCP program closes abruptly,
                # a "Connection reset by peer" exception will be thrown
                data = sock.recv(RECV_BUFFER)
                if data:
                    sock.send('OK ... %s' % data)
            except:
                sock.close()
                CONNECTION_LIST.remove(sock)

server_sock.close()
