# Ref: http://stackoverflow.com/questions/100003/what-is-a-metaclass-in-python
class Foo(object):
    pass

class Bar(object):
    pass

def choose_class(name):
    if name == 'foo':
        return Foo # return the class, not an instance
    else:
        return Bar

MyClass = choose_class('foo') 
print(MyClass)
print(MyClass())
# >>>
# <class '__main__.Foo'>
# <__main__.Foo object at 0x10b338b10>


# type(name, bases, dict) -> a new type
# type(name of the class, 
#      tuple of the parent class (for inheritance, can be empty), 
#      dictionary containing attributes names and values)

# >>> class Foo(object):
# ...       bar = True
# same as ==>
# >>> Foo = type('Foo', (), {'bar':True})
# <==

MyShinyClass = type('Klass', (), {}) # returns a class object
print(MyShinyClass)
print(MyShinyClass()) # create an instance with the class
# >>>
# <class '__main__.Klass'>
# <__main__.Klass object at 0x100e86f10>



