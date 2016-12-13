#!/usr/bin/perl

use strict;
use warnings;


package a;

use strict;
use warnings;

sub new () {
    my $class = shift;

    return bless { }, $class;
}

sub _g () {
    `echo 1; exit 10`;
}

sub DESTROY {
    local $?;

    print "DESTROY.1: $?\n";
    &_g;
    print "DESTROY.2: $?\n";
}


package ::main;

my $v = a->new();

exit 3;

1;
