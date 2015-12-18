"""
Duck typing
Ref: http://www.voidspace.org.uk/python/articles/duck_typing.shtml
"""

##########
# mathmatic operator (syntactic sugar)
print 3 + 3
# same as >>>
print int.__add__(3, 3)
# <<<

# overload '+' operator
class Klass1(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __add__(self, other):
        return self.a - other.b

class Klass2(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __add__(self, other):
        return self.b - other.a

obj1 = Klass1(1, 2)
obj2 = Klass2(10, 20)
print obj1 + obj2
# same as >>>
print obj1.__add__(obj2)
# <<<


##########
# data access for sequence type objects(list, tuple) and mapping type object(dict)
# (syntactic sugar)
a = [0,1,2]
print a[0]
# same as >>>
print list.__getitem__(a, 0)
# <<<

b = {'a':0, 'b':1}
print b['a']
# same as >>>
print dict.__getitem__(b, 'a')
# <<<

##########
# function call
# callable checks where a var has __call__ attr.
def f(arg):
    print arg

f(123)
# >>> 123
# same as >>>
f.__call__(123)
# >>> 123
# <<<
\


# 'Duck typing' happens because when we do var['member'] Python doesn't care what type object var is.
# All it cares is whether the call to its __getitem__ method returns anything sensible. If not - an error will be raised. Something like TypeError: Unsubscriptable object..
# This means you can create your own classes that have their own internal data structures - but are accessed using normal Python syntax. This is awfully convenient.

# isinstance(object, dict) returns True if object is a dictionary - or an instance of a subclass of dict.
# Instead of:
#
#     if isinstance(object, dict):
#         value = object[member]
#
# it is considered more pythonic to do :
#
#     try:
#          value = object[member]
#     except TypeError:
#         # do something else
#
# Our example above could become :
#
#     if hasattr(object, 'keys'):
#          value = object[member]
#
