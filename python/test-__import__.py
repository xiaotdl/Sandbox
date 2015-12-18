# ref: https://docs.python.org/2/library/functions.html#__import__

# Direct use of __import__() is rare, except in cases where you want to import a module whose name is only known at runtime.

import spam
# results in bytecode resembling the following code >>>
# spam = __import__('spam', globals(), locals(), [], -1)
# <<<

import spam.ham
# results in bytecode resembling the following code >>>
# spam = __import__('spam.ham', globals(), locals(), [], -1)
# <<<

from spam.ham import eggs, sausage as saus
# results in bytecode resembling the following code >>>
# _temp = __import__('spam.ham', globals(), locals(), ['eggs', 'sausage'], -1)
# eggs = _temp.eggs
# saus = _temp.sausage
# <<<


# >>> sys = __import__('sys', globals(), locals(), [], -1)
# >>> type(sys)
# <type 'module'>
