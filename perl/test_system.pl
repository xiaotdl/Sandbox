#!/usr/bin/perl

use strict;
use warnings;

my $exit_code = system("python -c 'import sys; sys.exit(-1);'");

my $exit = $exit_code >> 8;
my $core = $exit_code & 128;
my $signal = $exit_code & 127;
print "Error Code: $exit_code (exit=$exit, core=$core, signal=$signal)\n";
# >>>
# Error Code: 65280 (exit=255, core=0, signal=0)
