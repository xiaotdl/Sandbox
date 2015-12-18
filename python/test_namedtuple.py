from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'], verbose=True)
p = Point(x=11, y=22)
print p.x, p.y
# >>>
# 11 22

attrs = ['name', 'age', 'height']
Person = namedtuple('Person', attrs)
person1 = Person('James', '26', '185')
person2 = Person('Sarah', '24', '170')
for person in (person1, person2):
    print person
    for i, attr in enumerate(attrs):
        print "%-7s: %s" % (attr, person[i])
# Person(name='James', age='26', height='185')
# name   : James
# age    : 26
# height : 185
# Person(name='Sarah', age='24', height='170')
# name   : Sarah
# age    : 24
# height : 170
