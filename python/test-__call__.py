# x(arguments) is a shorthand for x.__call__(arguments).

class Klass(object):
    def __call__(self, msg):
        print msg
obj = Klass()
obj('hello world')
# >>>
# hello world
