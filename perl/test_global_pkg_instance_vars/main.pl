#!/usr/bin/perl

use strict;
use warnings;

use Package;

# == Access global var ==
print "$Package::our_var\n";
print "$Package::my_var\n"; # gives compile error in stderr

# console >>>
# Name "Package::my_var" used only once: possible typo at main.pl line 10.
# our_var
# Use of uninitialized value $Package::my_var in concatenation (.) or string at main.pl line 10.

# $ perl main.pl 2> /dev/null
# stdout >>>
# our_var

# $ perl main.pl > /dev/null
# stderr >>>
# Name "Package::my_var" used only once: possible typo at main.pl line 10.
# Use of uninitialized value $Package::my_var in concatenation (.) or string at main.pl line 10.


# == Acess package var ==
foreach (1..99) {
    Package->new();
}
# Ref:
# https://stackoverflow.com/a/1634716/2989564
# no strict 'refs';
# my $code = &{"${class}::static_method"};
# OR
# my $code = *{"${class}::static_method"}{CODE};
# $code->('Hello','World');
#print $Package::get_instance_cnt();
{
    no strict 'refs';
    print &{"Package::get_instance_cnt"} . "\n";
    # >>>
    # 99
}

# == Access instance var ==
my $pkg = Package->new();
print $pkg->get_var() . "\n";
$pkg->set_var("set_my_var");
print $pkg->get_var() . "\n";
# >>>
# my_var
# set_my_var

1;
