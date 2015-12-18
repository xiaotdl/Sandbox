# Ref: http://stackoverflow.com/questions/100003/what-is-a-metaclass-in-python
# metaclasses are especially useful to do black magic, and therefore complicated stuff. But by themselves, they are simple:
#   - intercept a class creation
#   - modify the class
#   - return the modified class

# __metaclass__ is deprecated in python 3.4, instead use: class ClassName(metaclass=MetaClass)

# Python metaclass
# ref: http://eli.thegreenplace.net/2011/08/14/python-metaclasses-by-example/

class MyMeta(type):
    def __new__(meta, name, bases, dct):
        print '-----------------------------------'
        print "Allocating memory for class", name
        print meta
        print bases
        print dct
        return super(MyMeta, meta).__new__(meta, name, bases, dct)
    def __init__(cls, name, bases, dct):
        print '-----------------------------------'
        print "Initializing class", name
        print cls
        print bases
        print dct
        super(MyMeta, cls).__init__(name, bases, dct)


class MyKlass(object):
    __metaclass__ = MyMeta

    def foo(self, param):
        pass

    barattr = 2

#######################
# use case 1: change attributs to upper case; add short function at module level
#######################
class UpperAttrMetaclass(type):
    def __new__(cls, name, bases, attrs):
        uppercase_attr = {}
        for name, val in attrs.items():
            if not name.startswith('__'):
                uppercase_attr[name.upper()] = val
            else:
                uppercase_attr[name] = val
        klass = super(UpperAttrMetaclass, cls).__new__(cls, name, bases, uppercase_attr)

        import sys
        module = sys.modules[attrs['__module__']]
        def stub(*args, **kwargs):
            print "call klass.run()"
        setattr(module, 'cmd_run', stub)
        
        return klass

class Foo(object):
    __metaclass__ = UpperAttrMetaclass
    attr1 = 'bar'

cmd_run()
# >>> call klass.run()
print(hasattr(Foo, 'attr1'))
# >>> False
print(hasattr(Foo, 'ATTR1'))
# >>> True

#######################
# use case 2: singleton
#######################
class MetaSingleton(type):
    instance = None
    def __call__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls.instance

class Foo(object):
    __metaclass__ = MetaSingleton

a = Foo()
b = Foo()
print a is b
# >>> True

#######################
# use case 3: record order of class definition
#######################
class MyMeta(type):
    counter = 0
    def __init__(cls, name, bases, dic):
        type.__init__(cls, name, bases, dic)
        cls._order = MyMeta.counter
        MyMeta.counter += 1

class MyType(object):
    __metaclass__ = MyMeta

class MyTypeChild1(MyType): pass
class MyTypeChild2(MyType): pass
class MyTypeChild3(MyType): pass

print MyTypeChild1._order
print MyTypeChild2._order
print MyTypeChild3._order
# >>>
# 1
# 2
# 3
