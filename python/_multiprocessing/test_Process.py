from multiprocessing import Process
import os

def info(title):
    print title
    print 'module name:', __name__
    if hasattr(os, 'getppid'): # only available on Unix
        print 'parent process:', os.getppid()
    print 'process id:', os.getpid()

def f(name):
    info('== function f ==')
    print 'hello', name

if __name__ == '__main__':
    info('== function main ==')
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()
