from multiprocessing import Process, Queue
import random

def f(q):
    randint = random.randint(0,100)
    print 'generating randint', randint
    q.put([randint])

if __name__ == '__main__':
    q = Queue()
    for i in range(5):
        p = Process(target=f, args=(q,))
        p.start()
        # print q.get()
        p.join()
    for i in range(5):
        print q.get()
