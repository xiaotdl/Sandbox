import sys

old_paths = list(sys.path)
sys.path.append('lib')
new_paths = list(sys.path)
print [path for path in new_paths if path not in old_paths]
# >>>
# ['lib']

from test_module import print_hello
print_hello()
# >>>
# hello
