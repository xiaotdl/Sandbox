# client does:
# 1. listen for incoming messages from the server
# 2. check user input, if the user types in a message then send it to the server

import socket
import select
import string
import sys


def prompt():
    sys.stdout.write('[You] say: ')
    sys.stdout.flush()

if __name__ == '__main__':
    if (len(sys.argv) < 3):
        print 'Usage: python telnet.py hostname port'
        sys.exit(1)

    host = sys.argv[1]
    port = int(sys.argv[2])

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)

    try:
        sock.connect((host, port))
    except:
        print 'unable to connect'
        sys.exit()

    print 'Connected to remote host. Start sending messages.'
    prompt()

    while True:
        socket_list = [sys.stdin, sock]
        read_sockets, write_sockets, error_sockets = select.select(socket_list , [], [])

        for socket in read_sockets:
            # incoming msg from remote server
            if socket == sock:
                data = socket.recv(4096)
                if not data:
                    print '\nDisconnected from chat server.'
                    sys.exit()
                else:
                    sys.stdout.write(' '*50 + '\r')
                    sys.stdout.flush()
                    sys.stdout.write(data)
                    sys.stdout.flush()
                    prompt()
            # user entered a message into sys.stdin
            else:
                msg = sys.stdin.readline()
                sock.send(msg)
                prompt()

# >>>
# $ ~ python chat_client.py localhost 5000
# Connected to remote host. Start sending messages.
# Client [127.0.0.1:65038] entered room.
# [You] say: hi
# [127.0.0.1:65038] says: hey
# [127.0.0.1:65038] says: how are you
# [You] say: what up
# [127.0.0.1:65038] says: i'm good buddy
# [You] say:
