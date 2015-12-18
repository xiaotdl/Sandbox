"""
To understand what 'yield' does, you must first understand what are 'generators'.
And before 'generators' come 'iterables'.
Ref: http://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do-in-python
"""
############
# 'iterable', __iter__(), next()

# mylist is an iterator
mylist = [0,1,2]
for i in mylist:
    print i*i
print type(mylist)
# >>>
# 0
# 1
# 4
# <type 'list'>

# list comprehension
print type([x*x for x in range(3)])
# >>>
# <type 'list'>

# Everything you can use "for... in..." on is an iterable: lists, strings, files...

############
# 'generator'
# 'generators' are 'iterators', but you can only iterate them once.
# because instead of store all values in memory, they generate values on the fly

# It is just the same except you used () instead of [].
# BUT, you can not perform for i in mygenerator a second time since generators can only be used once: they calculate 0, then forget about it and calculate 1, and end calculating 4, one by one.
mygenerator = (x*x for x in range(3))
for i in mygenerator:
    print i
print type(mygenerator)
# >>>
# 0
# 1
# 4
# <type 'generator'>


############
# 'yield'
# 'yield' is a keyword that is used like return, except the function will return a generator.
def createGenerator():
    for i in range(3):
        yield i*i

mygenerator = createGenerator()
print mygenerator
# >>> <generator object createGenerator at 0xb71b7464>
print type(mygenerator)
# >>> <type 'generator'>
for i in mygenerator:
    print i
# >>>
# 0
# 1
# 4


# extend takes generators
# 'duck typing': Python does not care if the argument of a method is a list or not. Python expects iterables so it will work with strings, lists, tuples and generators!
mygenerator = createGenerator()
l = list()
l.extend(mygenerator)
print l
# >>> [0, 1, 4]
print l
# >>> [0, 1, 4]


############
# Controlling a generator exhaustion
class Bank(object):
    crisis = False
    def create_atm(self):
        while not self.crisis:
            yield "$100"
chase = Bank()
corner_street_atm = chase.create_atm()
print corner_street_atm.next()
print corner_street_atm.next()
# >>>
# $100
# $100

chase.crisis = True # crisis is coming, no more money!
try:
    corner_street_atm.next()
except:
    print sys.exc_info()[0]
# >>> <type 'exceptions.StopIteration'>

wall_street_atm = chase.create_atm()
try:
    wall_street_atm.next()
except:
    print sys.exc_info()[0]
# >>> <type 'exceptions.StopIteration'>

chase.crisis = False # trouble is, even post-crisis the ATM remains empty
print 'crisis gone'
print 'corner_street_atm is running out of money'
try:
    print corner_street_atm.next()
except:
    print sys.exc_info()[0]
# >>> <type 'exceptions.StopIteration'>

print 'wall_street_atm still can yield as yield hasn\'t started'
wall_street_atm = chase.create_atm()
try:
    print wall_street_atm.next()
except:
    print sys.exc_info()[0]
# >>> $100

brand_new_atm = chase.create_atm() # build a new one to get back in business
for i in range(5):
    print brand_new_atm.next()



############
# itertools
import itertools

horses = [1, 2, 3]
races = itertools.permutations(horses)
print races
# >>> <itertools.permutations object at 0xb71c638c>
l = list()
l.extend(races)
print l
print l
# >>>
# [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
# [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]


def f123():
    yield 1
    yield 2
    yield 3

mygenerator = f123()
print mygenerator
for item in mygenerator:
    print item
# >>>
# <generator object f123 at 0xb722b5cc>
# 1
# 2
# 3
