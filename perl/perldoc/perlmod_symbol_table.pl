use strict;
use warnings;

use Data::Dumper;

#my $foo = 123;
our $bar = 456;
{
    local $Data::Dumper::Sortkeys = 1;
    print Dumper(\%main::)
}
{
    no strict 'refs';
    print *{'::bar'};
    print "$bar\n";
}

sub identify_typeglob {
    my $glob = shift;
    print 'You gave me '
        . *{$glob}{PACKAGE} . '::' . *{$glob}{NAME}. "\n";
}
identify_typeglob *foo;
identify_typeglob *bar::baz;
# >>>
# You gave me main::foo
# You gave me bar::baz
#
{
    no strict 'refs';
    #*foo = *bar;
    #*foo = \$bar;
    #print *foo . "\n";
    #print "$bar\n";
}

# Perl has two entirely distinct classes of variables:
# 1) package variables and 2) lexical (aka "my") variables.
# Typeglobs concern the former exclusively, so for the remainder of this post I will completely disregard lexicals.

$main::foobarbaz = 3;
print "== main pkg's symbol table ==\n";
print "$_\n", for sort keys %main::;

# a typeglob is as an aggregate data structure consisting of several independent slots,
# labeled "scalar", "array", "hash", "code" (or subroutine), "filehandle", "dirhandle", "socket", and "format".
# These slots hold the info for the scalar, array, hash, etc. associated with the corresponding symbol.
# In most cases, all the slots but one are empty.
# (Actually, typeglobs have one more slot: a typeglob slot! That's right, typeglobs are self-referential. In the typeglob *foo, for example, there is a slot referring to *foo.)

our $foo = 'hello'; # $main::foo
our @foo = 1..7;    # @main::foo

# $main::foo == ${*main::foo} == ${$main::{foo}}
print "${ *main::foo  }\n";
print "${ $main::{foo} }\n";
print "$main::foo\n";
# @main::foo == @{*main::foo} == @{$main::{foo}}
print "@{ *main::foo }\n";
print "@{ $main::{foo} }\n";
print "@main::foo\n";
# >>>
# hello
# hello
# 1 2 3 4 5 6 7
# 1 2 3 4 5 6 7

# 1. $main::{ foo } and *main::foo refer to the same thing, a typeglob
# 2. this typeglob holds information about both the scalar $main::foo and the array @main::foo,
#    and that we can access this information by enclosing the typeglob in {}
#    and prepending the appropriate sigil (in this case $ or @) to the whole thing.
# 3. (Of course, there is a simpler way to get to the same information: $main::foo and @main::foo.)

# $main::{ foo } and $main::foo are very different things!
# The former is equal to the typeglob *main::foo,
# while the latter refers to the contents of this typeglob's scalar slot.
# It is essential to understand this distinction.
