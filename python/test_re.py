import re
def callable(matchobject):
    print matchobject
    print matchobject.start()
    print matchobject.pos
    print matchobject.group(0)
    print matchobject.group(1)
    print dir(matchobject)
    print (matchobject.start() > 0 and '_' or '')
    return (matchobject.start() > 0 and '_' or '') + matchobject.group(1).lower()
print re.sub("([A-Z])", callable, "NameLikeThis")
# >>> name_like_this
# one-liner: 
# re.sub("([A-Z])", lambda mo: (mo.start() > 0 and '_' or '') + mo.group(1).lower(), name)

print 2 > 1 and 1 or 0
# same as ==>
# print 1 if 2 > 1 else 0
# <==
