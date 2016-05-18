use strict;
use warnings;

use Data::Dumper;
use FindBin;
use lib ("$FindBin::Bin/../lib");

use IPC::LDT;

use IO::Pipe;


my $pipe = IO::Pipe->new();

my $childPid = fork();

if($childPid) {
    # Parent
    $pipe->reader();

    #while(<$pipe>) {
    #    print $_ . "\n";
    #}

    my $ldt = new IPC::LDT(handle=>$pipe, objectMode=>1);
    my @msg = $ldt->receive;
    print "[parent] Received from client : @msg\n" . Dumper(\@msg);
}
else {
    # Child
    $pipe->writer();

    #my $dataRef=[{o=>1, lal=>2, a=>3}, [[qw(4 5 6)], [{oo=>'ps'}, 7, 8, 9]]];
    #print $pipe Dumper($dataRef);

    my $ldt = new IPC::LDT(handle=>$pipe, objectMode=>1);
    my $dataRef=[{o=>1, lal=>2, a=>3}, [[qw(4 5 6)], [{oo=>'ps'}, 7, 8, 9]]];
    $ldt->send($dataRef) or die $ldt->{'msg'};

    exit 0;
}
