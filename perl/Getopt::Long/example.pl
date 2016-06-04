use strict;
use warnings;

use Getopt::Long qw(GetOptions);

sub say { print shift() . "\n"; }

say "\@ARGV(before GetOptions): @ARGV";

my $proto='ip'; # default value

# "=s", ":i":
#     '=' indicates this option requires a value
#     ':' otherwise means the option is optional, if the parse failed it will get default values like "" for string, or 0 for integer.
#     's' indicates the option is an arbitrary string, other types: 'i'=>integer, 'f'=>float
GetOptions(
    'from=s' => \my $src_addr,
    'to=s' => \my $dest_addr,
    'proto=s' => \$proto,
    'num:i' => \my $num,
) or die "Usage: $0 --from NAME\n";

say "\@ARGV(after GetOptions): @ARGV";

say "from: " . $src_addr
    if $src_addr;
say "to: " . $dest_addr
    if $dest_addr;
say "proto: " . $proto
    if $proto;
say "num: " . $num;

# >>>
# $ perl example.pl --from 1.2.3.4 --to 5.6.7.8 --num abc
# @ARGV(before GetOptions): --from 1.2.3.4 --to 5.6.7.8 --num abc
# @ARGV(after GetOptions): abc
# from: 1.2.3.4
# to: 5.6.7.8
# proto: ip
# num: 0 <= expected int, got string in actual, defaults to 0
