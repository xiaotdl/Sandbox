import re
# == Delete a key in dict ==
# Note: can't remove an item during iteration
# e.g. iteritems, iterkeys, itervalues

def f1(d):
    """iterate twice, copy of keys"""
    to_delete = []
    for k in d:
        if re.match(".*Ref", str(k)):
            to_delete.append(k)
    for k in to_delete:
        del d[k]

def f2(d):
    """a neat way, iterate once using dict.keys(), copy of keys"""
    for k in d.keys():
        if re.match(".*Ref", str(k)):
            del d[k]

def f3(d):
    """delete by value"""
    for k, v in d.items():
        if re.match("x+", str(v)):
            del d[k]

d = {1:'one', 2:'two', 3:'three', 'sigRef1':'xxx', 'sigRef2':'yyy'}
print 'method 1:'
print d; f1(d); print d

d = {1:'one', 2:'two', 3:'three', 'sigRef1':'xxx', 'sigRef2':'yyy'}
print 'method 2:'
print d; f2(d); print d

d = {1:'one', 2:'two', 3:'three', 'sigRef1':'xxx', 'sigRef2':'yyy'}
print 'method 3:'
print d; f3(d); print d



# == build a dictionary ==
given = ['John', 'Eric', 'Terry', 'Michael']
family = ['Cleese', 'Idle', 'Gilliam', 'Palin']
d = dict(zip(given, family))
print d
