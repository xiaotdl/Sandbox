# typeglob sigil: *

use strict;
use warnings;

{
    package A;

    sub install {
        my ($pkg, $file, $lineno) = caller;
        {
            no strict 'refs';
            *{"${pkg}::f"} = sub {print "this is a installed sub"}; # install a coderef closure to the caller pkg as a sub
        }
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

A->install();
main::f();
