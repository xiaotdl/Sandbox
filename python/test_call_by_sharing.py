# Ref: https://en.wikipedia.org/wiki/Evaluation_strategy#Call_by_sharing
# instead of using:
#    call by value
#    call by reference
# Python uses:
#    call by sharing
# which means, function arguments are not visible to the caller
# which means, mutable objects can be mutable, but no assignment can happen
def foo(x):
    x.append(1)
    print id(x)
    x = [2, 3]
    print id(x)

bar = [0]
foo(bar)
print(bar)
