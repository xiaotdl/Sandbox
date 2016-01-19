# chat server does:
# 1. accept multiple incoming connections from clients
# 2. read incoming messages from client and broadcast them to all other connected clients

# == select.select ==
# The select function monitors all the client sockets and the master socket for readable activity.
# If the master socket is readable => it means that the server would accept a new connection;
# If any of the client socket is readable => it means that one of the chat clients has sent a message.

"""Tcp Chat Server"""
import socket
import select


def broadcast_data(sock, msg):
    for socket in CONNECTION_LIST:
        if socket != server_sock and socket != sock:
            try:
                socket.send(msg)
            except:
                socket.close()
                CONNECTION_LIST.remove(socket)

if __name__ == '__main__':
    CONNECTION_LIST = []
    RECV_BUFFER = 4096
    HOST = ''
    PORT = 5000

    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_sock.bind((HOST, PORT))
    server_sock.listen(10)

    CONNECTION_LIST.append(server_sock)
    print 'Chat server started on %s:%s' % (HOST, PORT)

    while True:
        # get a list of sockets which are ready to be read through select
        read_sockets,write_sockets,error_sockets = select.select(CONNECTION_LIST,[],[])

        for sock in read_sockets:
            # new connection
            if sock == server_sock:
                conn, addr = server_sock.accept()
                CONNECTION_LIST.append(conn)
                print 'client %s:%s connected' % addr
                broadcast_data(conn, 'Client [%s:%s] entered room.\n' % addr)
            # some incomig message from a client
            else:
                try:
                    # In Windows, sometimes when a TCP program closes abruptly,
                    # a "Connection reset by peer" exception will be thrown
                    data = sock.recv(RECV_BUFFER)
                    sock.send('msg sent successfully!\n')
                    if data:
                        broadcast_data(sock, '[%s:%s]' % sock.getpeername() +  ' says: ' + data)
                except:
                    print 'client %s:%s goes offline' % addr
                    broadcast_data(sock, 'Client [%s:%s] is offline.\n' % addr)
                    sock.close()
                    CONNECTION_LIST.remove(sock)
    server_sock.close()

# server >>>
# $  ~  python chat_server.py
# Chat server started on localhost:5000
# client 127.0.0.1:60283 connected
# client 127.0.0.1:60288 connected
# client 127.0.0.1:60288 goes offline

# client >>>
# $  ~  telnet localhost 5000
# Trying 127.0.0.1...
# Connected to localhost.
# Escape character is '^]'.
# Client [127.0.0.1:60118] entered room.
# [127.0.0.1:60118] says: hi
# [127.0.0.1:60118] says: how u doing
# [127.0.0.1:60118] says: what up
# Client [127.0.0.1:60288] is offline.
