# ref: http://www.cnblogs.com/lustralisk/p/pythonProgressBar.html

# -*- coding:utf-8 -*-

# Copyright: Lustralisk
# Author: Cedric Liu
# Date: 2015-11-08

import sys, time

class ProgressBar:
    def __init__(self, count = 0, total = 0, width = 50):
        self.count = count
        self.total = total
        self.width = width
    def move(self):
        self.count += 1
    def log(self, s):
        sys.stdout.write(' ' * (self.width + 9) + '\r')
        sys.stdout.flush()
        print s
        progress = self.width * self.count / self.total
        sys.stdout.write('{0:3}/{1:3}: '.format(self.count, self.total))
        sys.stdout.write('#' * progress + '-' * (self.width - progress) + '\r')
        if progress == self.width:
            sys.stdout.write('\n')
        sys.stdout.flush()

bar = ProgressBar(total = 10)
for i in range(10):
    bar.move()
    bar.log('We have arrived at: ' + str(i + 1))
    time.sleep(1)


# how it goes all the way.
# import sys, time

# for i in range(5):
    # first try
    # sys.stdout.write('{0}/5r'.format(i + 1))

    # second try
    # sys.stdout.write(str(i) * (5 - i) + '\r')

    # third try
    # sys.stdout.write(' ' * 10 + '\r')
    # sys.stdout.flush()
    # sys.stdout.write(str(i) * (5 - i) + '\r')

    # fourth try
    # sys.stdout.write(' ' * 10 + '\r')
    # sys.stdout.flush()
    # print i
    # sys.stdout.write(str(i) * (5 - i) + '\r')
    # sys.stdout.flush()
    # time.sleep(1)

    # sys.stdout.flush()
    # time.sleep(1)

