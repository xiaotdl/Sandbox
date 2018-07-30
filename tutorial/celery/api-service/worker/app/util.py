import logging
import subprocess


class CommandErrorException(Exception):
    pass


class Result(object):
    def __init__(self, rc, stdout, stderr, cmd):
        self.rc = rc
        self.stdout = stdout
        self.stderr = stderr
        self.cmd = cmd

    def __str__(self):
        cutoff = 1024
        if len(self.stdout) > cutoff:
            self.stdout = self.stdout[:cutoff] + '...'
        if len(self.stderr) > cutoff:
            self.stderr = self.stderr[:cutoff] + '...'

        return "Result: cmd=%(cmd)s -> " \
               "rc=%(rc)s, stdout=%(stdout)s, stderr=%(stderr)s" \
               % {k: repr(self.__dict__[k]) for k in self.__dict__}


def run(cmd, shell=True):
    logging.debug("run: '%s' on <localhost>..." % cmd)

    child = subprocess.Popen(
        cmd,
        shell=shell,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    out, err = child.communicate()
    rc = child.returncode

    r = Result(rc, out, err, cmd)
    logging.debug(str(r))
    if r.rc != 0:
        logging.warning("Non-zero return code!!! %s" % r)
        logging.debug(r.stdout)
        logging.debug(r.stderr)
    return r


def cmd_info(cmd, r):
    return {
        'cmd': cmd,
        'result': {
            'rc': r.rc,
            'stdout': r.stdout,
            'stderr': r.stderr
        }
    }


if __name__ == '__main__':
    print run('hostname')
    print run('whoami')
