# ref: https://docs.python.org/2/library/multiprocessing.html
# == Intro ==
# multiprocessing is a package that supports spawning processes using an API
# similar to the threading module. The multiprocessing package offers both
# local and remote concurrency, effectively side-stepping the Global Interpreter Lock
# by using subprocesses instead of threads. Due to this, the multiprocessing module
# allows the programmer to fully leverage multiple processors on a given machine.

# example: data parallelism
# parallelizing the execution of a function across multiple input values,
# distributing the input data across processes.
from multiprocessing import Pool

def f(x):
    return x*x

if __name__ == '__main__':
    p = Pool(5)
    print p.map(f, [1, 2, 3])
# >>>
# [1, 4, 9]


# == Process class ==
# In multiprocessing, processes are spawned by creating a Process object,
# and then calling its start() method. Process follows the API of threading.Thread
# example: multiprocess program
from multiprocessing import Process

def f(name):
    print 'hello', name

if __name__ == '__main__':
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()
# >>>
# hello bob

# example: show individual process IDs
from multiprocessing import Process
import os

def info(title):
    print title
    print 'module name:', __name__
    if hasattr(os, 'getppid'):  # only available on Unix
        print 'parent process:', os.getppid()
    print 'process id:', os.getpid()

def f(name):
    info('function f')
    print 'hello', name

if __name__ == '__main__':
    info('main line')
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()
# >>>
# main line
# module name: __main__
# parent process: 26081
# process id: 26153
# function f
# module name: __main__
# parent process: 26153
# process id: 26160
# hello bob


# == Exchanging objects between processes ==
# multiprocessing supports two types of communication channel between processes.

# = Queue =
# The Queue class is a near clone of Queue.Queue.
# Queues are thread and process safe.
from multiprocessing import Process, Queue

def f(q):
    q.put([42, None, 'hello'])

if __name__ == '__main__':
    q = Queue()
    p = Process(target=f, args=(q,))
    p.start()
    print q.get()
    p.join()
# >>>
# [42, None, 'hello']

# = Pipes =
# The Pipe() function returns a pair of connection objects connected by a pipe
# which by default is duplex (two-way).
from multiprocessing import Process, Pipe

def f(conn):
    conn.send([42, None, 'hello'])
    conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=f, args=(child_conn,))
    p.start()
    print parent_conn.recv()
    p.join()
# >>>
# [42, None, 'hello']


# == Synchronization between processes ==
# multiprocessing contains equivalents of all the synchronization primitives from threading.
# example: use a lock to ensure that only one process prints to standard output at a time
from multiprocessing import Process, Lock

def f(l, i):
    l.acquire()
    print 'hello world', i
    l.release()

if __name__ == '__main__':
    lock = Lock()

    for num in range(5):
        Process(target=f, args=(lock, num)).start()
# >>>
# hello world 0
# hello world 1
# hello world 2
# hello world 3
# hello world 4


# == Sharing state between processes ==
# Warning:
# When doing concurrent programming, it is usually best to avoid using shared state as far as possible.
# This is particularly true when using multiple processes.

# = Shared memory =
# Data can be stored in a shared memory map using Value or Array.
# These shared objects will be process and thread-safe.
from multiprocessing import Process, Value, Array

def f(n, a):
    n.value = 3.1415927
    for i in range(len(a)):
        a[i] = -a[i]

if __name__ == '__main__':
    num = Value('d', 0.0)
    arr = Array('i', range(10))

    p = Process(target=f, args=(num, arr))
    p.start()
    p.join()

    print num.value
    print arr[:]
# >>>
# 3.1415927
# [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]

# = Server process =
# A manager object returned by Manager() controls a server process which holds Python objects
# and allows other processes to manipulate them using proxies.
# A manager returned by Manager() will support types like:
# list, dict, Namespace, Lock, RLock, Semaphore, BoundedSemaphore, Condition, Event, Queue, Value, and Array.
from multiprocessing import Process, Manager

def f(d, l):
    d[1] = '1'
    d['2'] = 2
    d[0.25] = None
    l.reverse()

def f1(d, l):
    d['new'] = 99
    l.append(99)

if __name__ == '__main__':
    manager = Manager()

    d = manager.dict()
    l = manager.list(range(10))

    p = Process(target=f, args=(d, l))
    p.start()
    p.join()
    print d
    print l
# >>>
# {0.25: None, 1: '1', '2': 2}
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

    p1 = Process(target=f1, args=(d, l))
    p1.start()
    p1.join()
    print d
    print l
# >>>
# {0.25: None, 1: '1', '2': 2, 'new': 99}
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 99]


# == Using a pool of workers ==
# The Pool class represents a pool of worker processes.
# It has methods which allows tasks to be offloaded to the worker processes in a few different ways.

# example: Pool class
# Note that the methods of a pool should only ever be used by the process which created it.
from multiprocessing import Pool

def f(x):
    return x*x

if __name__ == '__main__':
    pool = Pool(processes=4)              # start 4 worker processes
    result = pool.apply_async(f, [10])    # evaluate "f(10)" asynchronously
    print result.get(timeout=1)           # prints "100" unless your computer is *very* slow
    print pool.map(f, range(10))          # prints "[0, 1, 4,..., 81]"
# >>>
# 100
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


# == Reference ==
# The multiprocessing package mostly replicates the API of the threading module.


