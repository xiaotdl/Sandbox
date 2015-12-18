# This is a handy timer to record execution time of a function/a block of codes
import time
import datetime

class Timer(object):
    def __init__(self, function_name=None, verbose=False):
        self.function_name = function_name
        self.verbose = verbose

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args):
        self.end = time.time()
        self.secs = self.end - self.start
        if self.verbose:
            d = datetime.timedelta(seconds=self.secs)
            print '[elapsed time for %-40s] %ds %dms' % (self.function_name, d.seconds, d.microseconds)

# import timer in other file
# from timer import Timer

def sum1(num):
    return sum([i for i in range(num + 1)])

def sum2(num):
    sum = 0
    for i in range(0, num + 1):
        sum += i
    return sum


with Timer("sleep 2 secs", True) as t:
    print "sleeping%)"
    time.sleep(2)

with Timer("First function executed", True) as t:
    print sum1(100000)

with Timer("Second function executed", True) as t:
    print sum2(100000)

with Timer("Third function executed", True) as t:
    print sum2(1)

