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
# class Result(object):

#     def __init__(self, cmd, rc, stdout, stderr):
#         self.cmd= cmd
#         self.rc = rc
#         self.stdout = stdout
#         self.stderr = stderr

#     def __str__(self):
#         cutoff = 128
#         if len(self.stdout) > cutoff:
#             self.stdout = self.stdout[:cutoff] + '...'
#         if len(self.stderr) > cutoff:
#             self.stderr = self.stderr[:cutoff] + '...'

#         return "Result: cmd=%(cmd)s -> " \
#                "rc=%(rc)s, stdout=%(stdout)s, stderr=%(stderr)s" % {k: repr(self.__dict__[k]) for k in self.__dict__}


# def execute(cmd, shell=False, ignore_error=False):
#     rc, out, err = 'n/a', 'n/a', 'n/a'
#     if not shell:
#         if isinstance(cmd, basestring):
#             cmd = cmd.split()
#         print "[INFO] run: '%s' on <localhost>..." % ' '.join(cmd)
#         child = subprocess.Popen(
#             cmd,
#             stdout=subprocess.PIPE,
#             stderr=subprocess.PIPE
#         )
#         out, err = child.communicate()
#         rc = child.returncode
#         r = Result(' '.join(cmd), rc, out, err)
#     else:
#         if type(cmd) is list:
#             cmd = ' '.join(cmd)
#         print "[INFO] run: '%s' on <localhost>..." % cmd
#         try:
#             out = subprocess.check_output(cmd, shell=True)
#         except subprocess.CalledProcessError:
#             rc = -1
#             pass
#         r = Result(cmd, rc, out, err)
#     if r.rc == 'n/a' or ignore_error:
#         pass
#     elif r.rc:
#         print "[WARNING] Non-zero return code!!! %s" % r
#     return r


# r = execute('echo 123')
# print r
# r = execute(['echo', '456'])
# print r
# # use shell when pipe is needed
# r = execute("cal | grep 2016", shell=True)
# print r
# # use shell when cmd includes wildcard *
# r = execute('ls *.py')
# print r
# r = execute('ls *.py', shell=True)
# print r
# r = execute('ls *.py', ignore_error=True)
# print r

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


# == Example 4 ==
# run a cmd and get rc, stdout, stderr

from subprocess import Popen, PIPE, STDOUT

def run(cmd):
    print "== cmd: '%s' ==" % cmd
    child = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE, close_fds=True)
    child.wait()
    rc = child.returncode
    out = child.stdout.read()
    err = child.stderr.read()
    print "rc:\n", rc
    print "out:\n", out
    print "err:\n", err

cmds = (
    'cal | grep 2016',
    'ls *.py',
    'echo 123 456',
)

for cmd in cmds:
    run(cmd)

# == Example 5 ==
# run cmd with timeout
from threading import Thread
class SubprocessTimeoutError(Exception):
    pass

# Ref: http://www.ostricher.com/2015/01/python-subprocess-with-timeout/
def run_command_with_timeout(cmd, timeout_sec):
    """Execute `cmd` in a subprocess and enforce timeout `timeout_sec` seconds.

    Return subprocess exit code on natural completion of the subprocess.
    Raise an exception if timeout expires before subprocess completes."""
    proc = subprocess.Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE, close_fds=True)
    proc_thread = Thread(target=proc.wait)
    proc_thread.start()
    proc_thread.join(timeout_sec)
    if proc_thread.is_alive():
        # Process still running - kill it and raise timeout error
        try:
            proc.kill()
        except OSError, e:
            # The process finished between the `is_alive()` and `kill()`
            return proc.returncode
        # OK, the process was definitely killed
        raise SubprocessTimeoutError('Process #%d killed after %f seconds' % (proc.pid, timeout_sec))
    # Process completed naturally - return exit code
    return proc.returncode

run_command_with_timeout('sleep 5', 2)
# >>>
# Traceback (most recent call last):
#   File "test.py", line 80, in <module>
#     run_command_with_timeout('sleep 5', 2)
#   File "test.py", line 76, in run_command_with_timeout
#     raise SubprocessTimeoutError('Process #%d killed after %f seconds' % (proc.pid, timeout_sec))
# __main__.SubprocessTimeoutError: Process #24858 killed after 2.000000 seconds

# shell returned 1


# == Example 6 ==
# use tempfile.TemporaryFile instead of subprocess.PIPE once stdout/stderr exceeds 64K.
# otherwise the subprocess will be hanging.
# Ref:
# https://thraxil.org/users/anders/posts/2008/03/13/Subprocess-Hanging-PIPE-is-your-enemy/
# import tempfile

# def run(cmd, shell=True, ignore_stdout=False, ignore_stderr=False):
#     logging.info("run: '%s' on <localhost>..." % cmd)

#     # subprocess.PIPE is a fixed size (64K) buffer,
#     # process will be hanging if stdout exceeds this limit.
#     stdout = tempfile.TemporaryFile() if ignore_stdout else subprocess.PIPE
#     stderr = tempfile.TemporaryFile() if ignore_stderr else subprocess.PIPE

#     child = subprocess.Popen(
#         cmd,
#         shell=shell,
#         stdout=stdout,
#         stderr=stderr,
#         close_fds=True
#     )

#     child.wait()

#     rc = child.returncode
#     out, err = 'n/a', 'n/a'
#     if not ignore_stdout:
#         out = child.stdout.read()
#     if not ignore_stderr:
#         err = child.stderr.read()

#     r = Result(rc, out, err, cmd)
#     logging.debug(str(r))
#     if r.rc != 0:
#         logging.warning("Non-zero return code!!! %s" % r)
#         logging.debug(r.stdout)
#         logging.debug(r.stderr)
#     return r

# run("echo 'large stdout and stderr'", ignore_stdout=True, ignore_stderr=True)
