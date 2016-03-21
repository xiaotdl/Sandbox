use IPC::Run qw( run timeout  );

my @cmd = ('ps', 'aux');
run \@cmd, \my $in, \my $out, \my $err, timeout(10);
print "\n" . "@cmd: $?" . "\n";
