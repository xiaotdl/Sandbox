use strict;
use warnings;

use Capture::Tiny ':all';

sub run {
    my $cmd = shift;

    my ($stdout, $stderr, $rc) = capture {
        system($cmd);
    };

    print "==========\n";
    print "cmd: $cmd\n";
    print "stdout: $stdout\n";
    print "stderr: $stderr\n";
    print "rc: $rc\n";

    return ($stdout, $stderr, $rc);
}

my ($stdout, $stderr, $rc);
($stdout, $stderr, $rc) = &run("ps");
($stdout, $stderr, $rc) = &run("cat 123");
