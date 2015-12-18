import os

def someFunc():
    pid = os.getpgid(0)
    import time
    time.sleep(2)
    print '[pid %s] someFunc is called.' % pid

# This doesn't print to STDOUT, cannot know what happened there.
# import thread
# thread.start_new_thread(someFunc, ())

import threading
t1 = threading.Thread(target=someFunc)
t1.start()
t1.join()


class FuncThread(threading.Thread):
    def __init__(self, target, *args, **kwargs):
        self._target = target
        self._args = args
        self._kwargs = kwargs
        super(FuncThread, self).__init__()

    def run(self):
        self._target(*self._args)

def someOtherFunc(msg):
    pid = os.getpgid(0)
    print '[pid %s] someOtherFunc is called. args: %s' % (pid, msg)

t1 = FuncThread(someOtherFunc, 'hello world')
t1.start()
t1.join()


pid = os.getpgid(0)
print '[pid %s] %s program ended:D' % (pid, __name__)
