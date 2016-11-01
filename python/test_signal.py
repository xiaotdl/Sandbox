import os
import sys
import time
import signal

# common signals to kill a process
# Ctrl + C => SIGINT
# kill     => SIGTERM
# kill 9   => SIGKILL   # NOTE: SIGKILL kills process directly, which means process can't be caught and handled

def handle_sigint(singal_num, frame):
    print "Caught SIGINT - you pressed ctrl + c"
    sys.exit(1)

def handle_sigterm(singal_num, frame):
    print "Caught SIGTERM - progarm was killed"
    sys.exit(1)

signal.signal(signal.SIGINT, handle_sigint)
signal.signal(signal.SIGTERM, handle_sigterm)

# os.kill(os.getpid(), signal.SIGTERM)

for i in range(1000):
    print i
    time.sleep(1)


