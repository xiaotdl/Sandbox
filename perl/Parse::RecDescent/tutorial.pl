#!/usr/bin/perl
# Parse::RecDescent Tutorial
# Ref: http://www.perl.com/pub/2001/06/13/recdecent.html
use strict;
use warnings;

use Parse::RecDescent;
use Data::Dumper;

use vars qw(%VARIABLE);

# Enable warnings within the Parse::RecDescent module.

$::RD_ERRORS = 1; # Make sure the parser dies when it encounters an error
$::RD_WARN   = 1; # Enable warnings. This will warn on unused rules &c.
$::RD_HINT   = 1; # Give out hints to help fix problems.

my $grammar = <<'_EOGRAMMAR_';

  # Terminals (macros that can't expand further)
  #

  OP       : m([-+*/%])      # Mathematical operators
  INTEGER  : /[-+]?\d+/      # Signed integers
  VARIABLE : /[a-zA-Z_]\w*/i # Variable

  expression : INTEGER OP expression
             { return main::expression(@item) }
             | VARIABLE OP expression
             { return main::expression(@item) }
             | INTEGER
             | VARIABLE
             { return $main::VARIABLE{$item{VARIABLE}} }

  print_instruction  : /print/i expression
                     { print $item{expression}."\n" }
  assign_instruction : VARIABLE "=" expression
                     { $main::VARIABLE{$item{VARIABLE}} = $item{expression} }

  instruction : print_instruction
              | assign_instruction

  startrule: instruction(s /;/)

_EOGRAMMAR_

sub expression {
  my ($expression, $lhs, $op, $rhs) = @_;
  $lhs = $VARIABLE{$lhs} if $lhs=~/[^-+0-9]/;
  return eval "$lhs $op $rhs";
}

my $parser = Parse::RecDescent->new($grammar);

print "a=2\n";                          $parser->startrule("a=2");
print "a=1+3\n";                        $parser->startrule("a=1+3");
print "print 5*7\n";                    $parser->startrule("print 5*7");
print "print 2/4\n";                    $parser->startrule("print 2/4");
print "print 2+2/4\n";                  $parser->startrule("print 2+2/4");
print "print 2/2+4\n";                  $parser->startrule("print 2/2+4");
print "print 2+-2/4\n";                 $parser->startrule("print 2+-2/4");
print "aA = 5 ; b = 1; print aA + b\n"; $parser->startrule("aA = 5 ; b = 1; print aA + b");
