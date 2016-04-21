import sys
import time
import signal

# common signals to kill a process
# Ctrl + C => SIGINT
# kill     => SIGTERM
# kill 9   => SIGKILL   # kills process directly, which means process can't catch and handle

def handle_signal(singal_num, frame):
    print "you pressed ctrl + c"
    sys.exit(1)

signal.signal(signal.SIGINT, handle_signal)

for i in range(1000):
    print i
    time.sleep(1)


