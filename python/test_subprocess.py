import subprocess

# == Example 1 ==
# # wait till commands finished
# import time
# subprocess.call('echo parent[$$]: going to sleep for 100 secs', shell=True)

# # fork a new process to execute
# subprocess.Popen('while true; do echo child1[$$]: sleeping; sleep 1; done', shell=True)
# subprocess.Popen('while true; do echo child2[$$]: sleeping; sleep 3; done', shell=True)

# time.sleep(100)


# == Example 2 ==
# run a cmd and get rc, stdout, stderr
class Result(object):

    def __init__(self, cmd, rc, stdout, stderr):
        self.cmd= cmd
        self.rc = rc
        self.stdout = stdout
        self.stderr = stderr

    def __str__(self):
        cutoff = 128
        if len(self.stdout) > cutoff:
            self.stdout = self.stdout[:cutoff] + '...'
        if len(self.stderr) > cutoff:
            self.stderr = self.stderr[:cutoff] + '...'

        return "Result: cmd=%(cmd)s -> " \
               "rc=%(rc)s, stdout=%(stdout)s, stderr=%(stderr)s" % {k: repr(self.__dict__[k]) for k in self.__dict__}


def execute(cmd, shell=False, ignore_error=False):
    rc, out, err = 'n/a', 'n/a', 'n/a'
    if not shell:
        if isinstance(cmd, basestring):
            cmd = cmd.split()
        print "[INFO] run: '%s' on <localhost>..." % ' '.join(cmd)
        child = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        out, err = child.communicate()
        rc = child.returncode
        r = Result(' '.join(cmd), rc, out, err)
    else:
        if type(cmd) is list:
            cmd = ' '.join(cmd)
        print "[INFO] run: '%s' on <localhost>..." % cmd
        try:
            out = subprocess.check_output(cmd, shell=True)
        except subprocess.CalledProcessError:
            rc = -1
            pass
        r = Result(cmd, rc, out, err)
    if r.rc != 'n/a' and r.rc != 0 and not ignore_error:
        print "[WARNING] Non-zero return code!!! %s" % r
    return r


r = execute('echo 123')
print r
r = execute(['echo', '456'])
print r
# use shell when pipe is needed
r = execute("cal | grep 2016", shell=True)
print r
# use shell when cmd includes wildcard *
r = execute('ls *.py')
print r
r = execute('ls *.py', shell=True)
print r
r = execute('ls *.py', ignore_error=True)
print r

# >>>
# Result: cmd='echo 123' -> rc=0, stdout='123\n', stderr=''
# Result: cmd='echo 456' -> rc=0, stdout='456\n', stderr=''

# # == Example 3 ==
# # run a cmd
# cmd = "ls -lh"
# out = subprocess.check_output(cmd, shell=True)
# print out
# # run a cmd with pipes
# cmd = "cal | grep 2016"
# out = subprocess.check_output(cmd, shell=True)
# print out
