use strict;
use warnings;

use IO::Socket::INET;

sub get_mgmt_ip {
    my $mgmt_ip;
    eval {
        my $socket = IO::Socket::INET->new(
            Proto       => 'udp',
            PeerAddr    => '8.8.8.8', # Google DNS server
            PeerPort    => '53', # DNS port
        ) or die "Can't bind: $@\n";
        $mgmt_ip = $socket->sockhost;
        close($socket) if $socket;
    };
    return $mgmt_ip;
}

my $mgmt_ip = get_mgmt_ip();

print "$mgmt_ip\n";
