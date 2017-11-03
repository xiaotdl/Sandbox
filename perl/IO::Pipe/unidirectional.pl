use strict;
use warnings;

use IO::Pipe;

use Data::Dumper;

my $pipe = IO::Pipe->new();

my $childPid = fork();

if($childPid) {
    # Parent
    $pipe->reader();
    while(<$pipe>) {
        print $_;
    }
    print "Parent $$ exiting...\n";
}
else {
    # Child
    $pipe->writer();
    my $msg = "from child $$: ping\n";
    print $pipe $msg;
    my $dataRef=[{o=>1, lal=>2, a=>3}, [[qw(4 5 6)], [{oo=>'ps'}, 7, 8, 9]]];
    print $pipe Dumper($dataRef);
    print $pipe "Child $$ exiting...\n";
    exit 0;
}
