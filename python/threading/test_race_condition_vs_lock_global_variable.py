# Example2: demonstrate race condition with a program and then fix it
# Ref: https://en.wikipedia.org/wiki/Race_condition#Example
from threading import Thread, Lock
#define a global variable
some_var = 0

lock = Lock()

class IncrementThread(Thread):
    def run(self):
        #we want to read a global variable
        #and then increment it
        global some_var
        lock.acquire()
        read_value = some_var
        print "some_var in %s is %d" % (self.name, read_value)
        some_var = read_value + 1
        print "some_var in %s after increment is %d" % (self.name, some_var)
        lock.release()

def use_increment_thread():
    threads = []
    for i in range(50):
        t = IncrementThread()
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print "After 50 modifications, some_var should have become 50"
    print "After 50 modifications, some_var is %d" % (some_var,)

use_increment_thread()
