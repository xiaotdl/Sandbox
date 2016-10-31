package A;

use warnings;
use strict;

use Data::Dumper;

sub import {
    print "A::import\n";
    print Dumper((caller(0))[1]);

    return 1;
}

1;
