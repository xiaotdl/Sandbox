"""
map()
map(function, iterable, ...)
"""
items = [1,2,3,4,5]
print map(lambda x: x**2, items)
# >>> list(map((lambda x: x **2), items))
# [1, 4, 9, 16, 25]



def square(x):
        return (x**2)
def cube(x):
        return (x**3)

funcs = [square, cube]
for r in range(5):
    print map(lambda x: x(r), funcs)

# >>>
# [0, 0]
# [1, 1]
# [4, 8]
# [9, 27]
# [16, 64]


# >>> pow(3,5)
# 243
# >>> pow(2,10)
# 1024
# >>> pow(3,11)
# 177147
# >>> pow(4,12)
# 16777216
# >>>
# >>> list(map(pow,[2, 3, 4], [10, 11, 12]))
# [1024, 177147, 16777216]


"""
filter() and reduce()
filter(function, iterable)
    filter() extracts each element in the sequence for which the function returns True.
reduce(function, iterable[, initializer])
    reduce() reduces a list to a single value by combining elements via a supplied function.
"""
# def f(x):
#     if x > 0:
#         return True
#     else:
#         return False
f = lambda x: True if (x > 0) else False
print filter(f, range(-5, 5))

print filter((lambda x: x < 0), range(-5, 5))
# >>> list( filter((lambda x: x < 0), range(-5,5)))
# [-5, -4, -3, -2, -1]

print reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])
# >>>
# 15 (eq ((((1+2)+3)+4)+5) )

print reduce(lambda x, y: x+y, [1, 2, 3, 4, 5], 100)
# >>>
# 115 (eq ((((100 + (1+2)+3)+4)+5)) )
