use strict;
use warnings;

use Memory::Usage;

my $mu = Memory::Usage->new();
$mu->record('starting work');

# my real code
sub say { print shift . "\n" }
my $x = " " x 1024;
$x .= $x for 1..20;
say length $x;
say "vsz = virtual memory size, rss = resident set size, shared = shared memory size, code = text (aka code or exe) size, data = data and stack size";

$mu->record('after creating variable');

$mu->dump();
