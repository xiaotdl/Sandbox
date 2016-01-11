import subprocess
from time

# wait till commands finished
subprocess.call('echo parent[$$]: going to sleep for 100 secs', shell=True)

# fork a new process to execute
subprocess.Popen('while true; do echo child1[$$]: sleeping; sleep 1; done', shell=True)
subprocess.Popen('while true; do echo child2[$$]: sleeping; sleep 3; done', shell=True)

time.sleep(100)
