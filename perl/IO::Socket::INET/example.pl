use strict;
use warnings;

use IO::Socket::INET;

use Data::Dumper;

sub say {
    $_ = shift;
    print $_ . "\n";
}

sub dump () {
    local $Data::Dumper::Terse = 1;
    local $Data::Dumper::Sortkeys = 1;
    return Dumper(@_);
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

        $sock->recv(my $buffer, 4096);
        say "[parent] Received from client : " . &dump($buffer);
    }
} else {
    # child
    my $clientSock = IO::Socket::INET->new(
        PeerHost => $SERVER_IP,
        PeerPort => $PORT,
        Proto => 'tcp',
    ) or die "Failed to create client socket: $!\n";

    say "[child] Connected to server successfully";

    my $data = "DATA from client";
    $clientSock->send($data);
}
