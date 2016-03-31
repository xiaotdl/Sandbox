# Ref: http://billauer.co.il/blog/2013/03/fork-wait-and-the-return-values-in-perl-in-different-scenarios/
use strict;
use warnings;

my $child = fork();
die("Failed to fork!\n")
    unless defined $child;

if ($child) {
    # parent
    my $pid;
    $pid = wait;
    my $status = $?;

    die("No child process!\n")
        if $pid < 0;

    die("Child process = $child but process $pid was reaped!\n")
        unless $child == $pid;

    my $exit = $status >> 8;
    my $core = $status & 128;
    my $signal = $status & 127;
    print "Full status = $status (exit=$exit, core=$core, signal=$signal)\n";
} else {
    # child
    die("Bye bye cruel world!\n");
}
