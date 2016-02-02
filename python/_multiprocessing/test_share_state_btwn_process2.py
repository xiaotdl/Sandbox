from multiprocessing import Process, Value, Array
from ctypes import Structure, c_char_p, c_int, c_bool
import socket
import time
import os

SERVER_POOL = [('127.0.0.1', 8888), ('127.0.0.1', 9999)]

class Server(Structure):
    _fields_ = [('ip', c_char_p), ('port', c_int), ('active', c_int)]

def get_active_servers(servers):
    while True:
        active = []
        for server in servers:
            if server.active:
                active.append((server.ip, server.port))
        print 'active servers:', active
        time.sleep(1)

def health_monitor_server(servers):
    while True:
        for server in servers:
            # check if port is open, and update its active status
            rc1 = os.system('netstat -an | grep \*.%s > /dev/null' % (server.port,))
            rc2 = os.system('netstat -an | grep %s.%s > /dev/null' % (server.ip, server.port))
            server.active = (rc1 == 0 or rc2 == 0)
        time.sleep(1)


if __name__ == '__main__':
    servers = Array(Server, [(server[0], server[1], True) for server in SERVER_POOL])

    ps = []
    p = Process(target=get_active_servers, args=(servers,))
    ps.append(p)
    p = Process(target=health_monitor_server, args=(servers,))
    ps.append(p)

    for p in ps:
        p.start()
    for p in ps:
        p.join()
