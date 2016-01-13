import cProfile

a=[]
b=[]
NUM = 10000

for i in range(NUM):
    a.append(i)

for i in range(0,NUM,2):
    b.append(i)

cProfile.run('for c in a:\n  if c not in b:\n    pass')
# >>>
#          2 function calls in 0.594 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.594    0.594    0.594    0.594 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('[c for c in a if c not in b]')
# >>>
#          2 function calls in 0.612 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.612    0.612    0.612    0.612 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('set(a) ^ set(b)')
# >>>
#          2 function calls in 0.001 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.001    0.001    0.001    0.001 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
