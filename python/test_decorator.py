# Ref:
# Understand Python's namespace, closure, and decorator
# http://python.jobbole.com/85056/
# https://en.wikipedia.org/wiki/Closure_(computer_programming)

# == namespace ==
s = "This is a global variable."

def foo(x=1, y=2):
    print locals()

print globals()
foo(3, 4)
# >>>
# {'__builtins__': <module '__builtin__' (built-in)>, '__file__': 'test.py', '__package__': None, 's': 'This is a global variable.', '__name__': '__main__', 'foo': <function foo at 0x1038d8d70>, '__doc__': None}
# {'y': 4, 'x': 3}

print foo.__class__
# >>>
# <type 'function'>


# == function is just an object in Python ==
def outer():
    def inner():
        print "Inside inner"
    print locals()
    return inner
foo = outer()
print globals()['foo'] # >>> {'inner': <function inner at 0x104205578>}
foo() # >>> Inside inner


# == closure ==
print 'closure'
def outer(x=1):
    def inner():
        print x
    return inner
foo = outer()
foo() # >>> 1
# int x not found in globals
print globals()
# int x is wrapped in function's closure related memory
# function can actually save variables from outer namespace, which is called "upvalue"
print foo.func_closure # >>> (<cell at 0x10dad5868: int object at 0x7fbe1940dcc8>,)

print1 = outer(1)
print1() # >>> 1
print2 = outer(2)
print2() # >>> 2


# == decorator ==
print 'decorator'
def outer(func):
    def inner():
        print 'before func'
        ret = func()
        return ret + 1
    return inner

def foo():
    return 1

decorated = outer(foo)
print decorated() # >>> 2
print decorated # >>> <function inner at 0x10f28b140>

# == decorator with @ (syntactic sugar) ==
def logger(func):
    def inner(*args, **kwargs):
        print "== logger start =="
        print "args: %s\nkwargs: %s" % (args, kwargs)
        ret = func(*args, **kwargs)
        print "== logger end =="
        return ret
    return inner

@logger
def doMath(x, y, op='+'):
    return eval(str(x) + op + str(y))
print doMath(1, 2, op='+')
# >>>
# == logger start ==
# args: (1, 2)
# kwargs: {}
# == logger end ==
# 3

class Klass():
    @logger
    def foo(self, a, b, c=3):
        return a, b, c
print Klass().foo(1, 2, c=3)
# >>>
# == logger start ==
# args: (<__main__.Klass instance at 0x1033a0e18>, 1, 2)
# kwargs: {'c': 3}
# == logger end ==
# (1, 2, 3)
