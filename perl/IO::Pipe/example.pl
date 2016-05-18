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
        print $_ . "\n";
    }
}
else {
    # Child
    $pipe->writer();
    my $msg = "hello world";
    my $dataRef=[{o=>1, lal=>2, a=>3}, [[qw(4 5 6)], [{oo=>'ps'}, 7, 8, 9]]];
    print $pipe $msg;
    print $pipe Dumper($dataRef);
    exit 0;
}
