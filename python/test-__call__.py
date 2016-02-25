# x(arguments) is a shorthand for x.__call__(arguments).
class Parent(object):
    def __init__(self):
        print 'parent init'

class Child(Parent):
    def __init__(self):
        print 'child init'
        super(Child, self).__init__()

Child()

