# Ref:
# http://perlmaven.com/how-to-check-if-a-child-process-is-still-running

use strict;
use warnings;

use POSIX ":sys_wait_h";
use Time::HiRes qw(sleep);

sub say { my @msg = @_; print "@msg\n"; }

my $pid = fork();
die "Could not fork\n"
    unless defined $pid;

if (not $pid) {
    say "In child";
    sleep 1;
    exit 3;
}

say "In parent of $pid";
while (1) {
    my $res = waitpid(-1, WNOHANG);
    say "Res: $res";
    sleep(0.1);

    if ($res == -1) {
        say "Some error occurred ", $? >> 8;
        exit();
    }
    if ($res) {
        say "Child $res ended with ", $? >> 8;
        last;
    }
}

say "about to wait()";
say wait();
say "wait() done";

# >>>
# In parent of 69746
# Res: 0
# In child
# Res: 0
# Res: 0
# Res: 0
# Res: 0
# Res: 0
# Res: 0
# Res: 0
# Res: 0
# Res: 0
# Res: 69746
# Child 69746 ended with  3
# about to wait()
# -1
# wait() done
