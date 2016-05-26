#!/usr/bin/perl

use strict;
use warnings;

use Capture::Tiny qw(:all);

# my $cmd = q[perl -e '$? = 1;'];
# my $cmd = q[perl -e 'exit -1;'];
# my $cmd = q[perl -e 'DESTROY { die "some msg"; }; exit 2;']; # die doesn't print anything inside DESTROY
my $cmd = q[perl -e '1/0;'];

my ($merged_output, $exit_code) = capture_merged { system($cmd) };

my $exit = $exit_code >> 8;
my $core = $exit_code & 128;
my $signal = $exit_code & 127;
print "Error Code: $exit_code (exit=$exit, core=$core, signal=$signal)\n";
print "capture_merged: " . $merged_output;
# >>>
# Error Code: 65280 (exit=255, core=0, signal=0)
# capture_merged: Illegal division by zero at -e line 1.
