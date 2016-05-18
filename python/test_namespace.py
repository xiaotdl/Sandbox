# Ref:
# Understand Python's namespace, closure, and decorator
# http://python.jobbole.com/85056/
# https://en.wikipedia.org/wiki/Closure_(computer_programming)

import pprint

# == namespace ==
s = "This is a global variable."

print '\n== before func == locals()'
pprint.pprint(locals())
def foo(x=1, y=2):
    print '\n== inside func == globals()'
    pprint.pprint(globals())
    print '\n== inside func, before loop == locals()', locals()
    for i in range(3):
        print '\n== inside func, inside loop == locals()', 'i=%d'%i, locals()
    print '\n== inside func, after loop == locals()', locals()
print '\n== after func == locals()'
pprint.pprint(locals())
print '\n== after func == globals()'
pprint.pprint(globals())

foo(3, 4)
