use strict;
use warnings;

use IO::Pipe;
use IO::Select;

use Data::Dumper;

my $pipeP2C = IO::Pipe->new();
my $pipeC2P = IO::Pipe->new();

my $childPid = fork();

if($childPid) {
    # Parent
    my $fh_in = $pipeC2P->reader();
    my $fh_out = $pipeP2C->writer();
    # send command: print $fh_out
    # recv response: read $fh_in
    $DB::single = 1; # PERL BREAKPOINT
    print $fh_out 1;
    while (<$fh_in>) {
        print $fh_in->getline();
    }
    print "Parent $$ is exiting...\n";
}
else {
    # Child
    my $fh_in = $pipeP2C->reader();
    my $fh_out = $pipeC2P->writer();

    my $readSelect = new IO::Select;
    $readSelect->add($fh_in);
    my $writeSelect = new IO::Select;
    # $writeSelect->add($fh_out);

    # messageLoop
    while (1) {
        my ($readReady, $writeReady, undef) =
            IO::Select::select($readSelect, $writeSelect, undef, undef);

        for my $fh (@$readReady) {
            my $request = &handleRead($fh);
            &replyToParent($request, $fh_out);
            $readSelect->remove($fh);
            $fh->close;
        }

        for my $fh (@$writeReady) {
            &handleWrite($fh);
            $writeSelect->remove($fh);
            $fh->close;
        }
    }
    #print $pipeC2P "Child $$: ping\n";
    #print $pipeC2P "Child $$ is exiting...\n";
    exit 0;
}

sub handleRead {
    my $fh = shift;
    return $fh->getline();
}

sub handleWrite {
    my $fh = shift;
    print $fh "Parent $$: pong";
}

sub replyToParent {
    my ($request, $fh) = @_;
    my $response = $request == 1 ? "apple\n" :
                   $request == 2 ? "banana\n" :
                                   "unknown\n";
    print $fh $response;
}
