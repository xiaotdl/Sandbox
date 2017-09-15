use strict;
use warnings;

use Data::Dumper;

OUTER: for my $i (0..2) {
    INNER: for my $j (0..2) {
        next OUTER if $i == 1;
        print "($i, $j)";
    }
    print "\n";
}
