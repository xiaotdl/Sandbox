import multiprocessing

class MyFancyClass(object):
    def __init__(self, name):
        self.name = name
    def do_sth(self):
        proc_name = multiprocessing.current_process().name
        print 'Doing sth fancy in %s for %s' % (proc_name, self.name)


def worker(q):
    obj = q.get()
    obj.do_sth()


if __name__ == '__main__':
    queue = multiprocessing.Queue()

    p = multiprocessing.Process(target=worker, args=(queue,))
    p.start()

    queue.put(MyFancyClass('Fancy Dan'))

    # wait for worker to finish
    queue.close()
    queue.join_thread()
    p.join()

