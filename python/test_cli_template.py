import sys


class Program:
    def __init__(self):
        self.parse_args()
        self.run()

    def parse_args(self):
        pass

    def run(self, task='task1'):
        print 'doing task: %s...' % task
        f = getattr(self, task)
        result = f()
        sys.exit(0)

    def task1(self):
        print 'task1...'

    def task2(self):
        print 'task2...'

main = Program

if __name__ == '__main__':
    main()
