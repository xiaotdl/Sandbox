a = set([1, 2, 3])
b = set([2, 3, 4])

print 'all items in a and b:',
print a | b

print 'items in both a and b:',
print a & b

print 'items only in a:',
print a - b

print 'items only in b:', 
print b - a

# >>>
# all items in a and b: set([1, 2, 3, 4])
# items in both a and b: set([2, 3])
# items only in a: set([1])
# items only in b: set([4])