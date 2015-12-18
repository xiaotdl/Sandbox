class Klass(object):
    def __repr__(self):
        return "(repr)This is empty Klass."
    def __str__(self):
        return "(str)This is empty Klass."
    pass
obj = Klass()
print obj.__repr__ # to be unambiguous, will overwrite __str__ if not exist, not vice versa
print obj.__str__  # to be human readable
print repr(obj)
print str(obj)
print obj # print str(obj)

print obj.__class__
print obj.__class__.__name__

# >>>
# <bound method Klass.__repr__ of (repr)This is empty Klass.>
# <bound method Klass.__str__ of (repr)This is empty Klass.>
# (repr)This is empty Klass.
# (str)This is empty Klass.
# (str)This is empty Klass.
# <class '__main__.Klass'>
# Klass
