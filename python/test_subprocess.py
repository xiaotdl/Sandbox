import subprocess
import time

# == Example 1 ==
# # wait till commands finished
# subprocess.call('echo parent[$$]: going to sleep for 100 secs', shell=True)

# # fork a new process to execute
# subprocess.Popen('while true; do echo child1[$$]: sleeping; sleep 1; done', shell=True)
# subprocess.Popen('while true; do echo child2[$$]: sleeping; sleep 3; done', shell=True)

# time.sleep(100)


# == Example 2 ==
# run a cmd
cmd = ["ls", "-lh"]
out, err = subprocess.Popen(
               cmd,
               stdout=subprocess.PIPE,
               stderr=subprocess.PIPE
           ).communicate()
print out.strip()
if err:
    raise Exception(err)

# == Example 3 ==
# run a cmd
cmd = "ls -lh"
out = subprocess.check_output(cmd, shell=True)
print out.strip()
