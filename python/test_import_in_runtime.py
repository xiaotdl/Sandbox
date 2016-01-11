import sys

old_paths = list(sys.path)
sys.path.append('lib')
new_paths = list(sys.path)
print [path for path in set(new_paths) if path not in set(old_paths)]
print [set(new_paths) ^ set(old_paths)]
# >>>
# ['lib']
# [set(['lib'])]

from test_module import print_hello
print_hello()
# >>>
# hello
