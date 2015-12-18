# Ref: http://stackoverflow.com/questions/25440694/whats-the-purpose-of-dictproxy
class C(object):
    x = None
    def f(self):
        print self.__dict__
        print dir(self)

c = C()
c.f()

#good
C.x = 1
print "C.x", C.x

#bad
#C.__dict__['x'] = 1

#good
m = C()
print "m.x", m.x
m.x = 2
print "m.x", m.x

#also good
m.__dict__['x'] = 3
print "m.__dict__['x']", m.__dict__['x']
