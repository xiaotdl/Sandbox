use strict;
use warnings;

use Data::Dumper;

#$me  = whoami();
#$him = whowasi();

sub currSub  { (caller(1))[3]  }
sub callerSub { (caller(2))[3]  }


sub f2 {
    my $ctx = {};
    @$ctx{qw(package filename line subroutine hasargs
            wantarray evaltext is_require hints bitmask hinthash)} = caller(0);
    print Dumper($ctx);
    print "currSub: " . &currSub . "\n";
    print "callerSub: " . &callerSub . "\n";
}

sub f1 {
    print "callerPkg: " . caller . "\n";
    &f2;
}

&f1;

# >>>
# $VAR1 = {
#           'subroutine' => 'main::f2',
#           'wantarray' => undef,
#           'filename' => 'caller.pl',
#           'hasargs' => '',
#           'bitmask' => 'UUUUUUUUUUUUUU',
#           'hints' => 1762,
#           'line' => 23,
#           'hinthash' => undef,
#           'evaltext' => undef,
#           'package' => 'main',
#           'is_require' => undef
#         };
# currSub: main::f2
# callerSub: main::f1
