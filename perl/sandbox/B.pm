package B;

use warnings;
use strict;

use A;

sub import {
    print "B::import\n";
    return &A::import(@_);
}

1;
