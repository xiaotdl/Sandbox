# typeglob sigil: *

use strict;
use warnings;

{
    package A;

    sub p {
        print "in A\n";
        #my ($pkg, $file, $lineno) = caller;
        my @a = caller(0);
        $DB::single = 1; # PERL BREAKPOINT
        no strict 'refs';
        #*{"${pkg}::trace"} = sub {print "$pkg"};
        #sub {my @a = caller(0); }->();

    }

    1;
}

{
    package B;

    sub p {
        print "in B\n";
    }

    1;
}

A->p();
#main::trace();
