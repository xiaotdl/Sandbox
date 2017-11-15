#!/usr/bin/perl

use strict;
use warnings;

use Data::Dumper;

use PerlIO;

open (my $fh, "perlio_get_layer.pl")
    or die "Couldn't open file!";

# The layers are returned in the order an open() or binmode() call would use them.
# Note that the "default stack" depends on the operating system and on the Perl version, and both the compile-time and runtime configurations of Perl.
my @layers;
@layers = PerlIO::get_layers($fh);
print "input layers: " . join(" > ", @layers) . "\n";

# By default the layers from the input side of the filehandle are returned; to get the output side, use the optional output argument:
@layers = PerlIO::get_layers($fh, output => 1);
print "output layers: " . join(" > ", @layers) . "\n";

close $fh;
# >>>
# input layers: unix > perlio
# output layers:

# The following table summarizes the default layers on UNIX-like and DOS-like platforms and depending on the setting of $ENV{PERLIO} :
# PERLIO     UNIX-like                   DOS-like
# ------     ---------                   --------
# unset / "" unix perlio / stdio [1]     unix crlf
# stdio      unix perlio / stdio [1]     stdio
# perlio     unix perlio                 unix perlio
# # [1] "stdio" if Configure found out how to do "fast stdio" (depends
# # on the stdio implementation) and in Perl 5.8, otherwise "unix perlio"

