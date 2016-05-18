use strict;
use warnings;

use FindBin;
use lib ("$FindBin::Bin/../lib");
use Data::Dumper;

use IPC::LDT;

use IO::Socket::INET;


sub say {
    $_ = shift;
    print $_ . "\n";
}

my $SERVER_IP = 'localhost';
my $PORT = 9999;

my $childPid = fork();

die "Failed to fork a child process: $!"
    unless defined $childPid;

if ($childPid) {
    # parent
    my $serverSock = IO::Socket::INET->new(
        LocalAddr => $SERVER_IP,
        LocalPort => $PORT,
        Proto => 'tcp',
        Listen => 5,
        Reuse => 1,
    ) or die "Failed to create server socket: $!\n";

    say "[parent] Server waiting for client connection on port $PORT";
    while (1) {
        my $sock = $serverSock->accept();

        my $peerAddress = $sock->peerhost();
        my $peerPort = $sock->peerport();

        say "[parent] Accepted new client connection from $peerAddress:$peerPort";

        # $sock->recv(my $buffer, 4096);
        # say "[parent] Received from client : " . Dumper($buffer);

        my $ldt = new IPC::LDT(handle=>$sock, objectMode=>1);
        my @msg = $ldt->receive;
        print "[parent] Received from client : @msg\n" . Dumper(\@msg);
    }
} else {
    # child
    my $clientSock = IO::Socket::INET->new(
        PeerHost => $SERVER_IP,
        PeerPort => $PORT,
        Proto => 'tcp',
    ) or die "Failed to create client socket: $!\n";

    say "[child] Connected to server successfully";

    # my $data = "DATA from client";
    # $clientSock->send($data);

    my $ldt = new IPC::LDT(handle=>$clientSock, objectMode=>1);
    my $dataRef=[{o=>1, lal=>2, a=>3}, [[qw(4 5 6)], [{oo=>'ps'}, 7, 8, 9]]];
    $ldt->send($dataRef) or die $ldt->{'msg'};

    exit 0;
}
