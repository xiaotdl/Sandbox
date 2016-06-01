import time
import sys


for i in range(10):
    print i, # trailing comma removes the trailing empty line
    if i % 2 == 1:
        print '' # stdout is line-buffered until a new line is emitted
    # sys.stdout.flush() # flush will output the current buffer immediately
    time.sleep(0.5)
# >>>
# 0 1
# 2 3
# 4 5
# 6 7
# 8 9
