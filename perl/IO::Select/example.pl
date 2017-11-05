use strict;
use warnings;

use IO::Select;
use IO::Socket;

my $sock = new IO::Socket::INET(Listen => 1, LocalPort => 8080);
my $select = new IO::Select( $sock );

print "Waiting for connection to localhost:8080...\n";
my @ready;
while(@ready = $select->can_read) {
    print "ready: @ready\n";
    foreach my $fh (@ready) {
        if($fh == $sock) {
            print "Create a new socket\n";
            my $peerSock = $sock->accept;
            $peerSock->recv(my $buffer, 4096);
            print "Received: $buffer\n";
            $select->add($peerSock);
        }
        else {
            print "Process socket\n";

            print "Maybe we have finished with the socket\n";
            $select->remove($fh);
            $fh->close;
        }
    }
}
