#!/usr/bin/perl
# Parse::RecDescent Tutorial
# Ref: http://www.perl.com/pub/2001/06/13/recdecent.html
use strict;
use warnings;

use Parse::RecDescent;
use Data::TreeDumper;

use vars qw(%VARIABLE);

# Enable warnings within the Parse::RecDescent module.

$::RD_ERRORS = 1; # Make sure the parser dies when it encounters an error
$::RD_WARN   = 1; # Enable warnings. This will warn on unused rules &c.
$::RD_HINT   = 1; # Give out hints to help fix problems.

my $grammar = <<'_EOGRAMMAR_';

  # Terminals (macros that can't expand further)
  #

  # OP       : m([-+*/%])      # Mathematical operators
  # INTEGER  : /[-+]?\d+/      # Signed integers
  # VARIABLE : /[a-zA-Z_]\w*/i # Variable

  # expression : INTEGER OP expression
  #            { return main::expression(@item) }
  #            | VARIABLE OP expression
  #            { return main::expression(@item) }
  #            | INTEGER
  #            | VARIABLE
  #            { return $main::VARIABLE{$item{VARIABLE}} }

  # print_instruction  : /print/i expression
  #                    { print $item{expression}."\n" }
  # assign_instruction : VARIABLE "=" expression
  #                    { $main::VARIABLE{$item{VARIABLE}} = $item{expression} }

  # instruction : print_instruction
  #             | assign_instruction

  # startrule: instruction(s /;/)

    OP1: m([*/%])      # Mathematical operators
    OP2: m([-+])       # Mathematical operators

    calculation:
        add_subtract OP1 calculation
        { $return = $item[2] }
      | add_subtract

    add_subtract:
        term OP2 add_subtract
        { $return = [$item[1], $item[2], $item[3]] }
      | term

    term:
        variable
      | value

    variable:
        /[a-zA-Z_][a-zA-Z0-9_]*/
        { $return = Exp::Var->new($item[1]) }

    value:
        /[0-9]+/
        { $return = Exp::Value->new($item[1]) }
      | "'" /[a-zA-Z0-9_-]+/ "'"
        { $return = Exp::Value->new($item[2]) }
      | '"' /[a-zA-Z0-9_-]+/ '"'
        { $return = Exp::Value->new($item[2]) }


_EOGRAMMAR_

#sub expression {
#  my ($expression, $lhs, $op, $rhs) = @_;
#  $lhs = $VARIABLE{$lhs} if $lhs=~/[^-+0-9]/;
#  return eval "$lhs $op $rhs";
#}

my $parser = Parse::RecDescent->new($grammar);

print DumpTree($parser->term("2"));
print DumpTree($parser->term("a"));
print DumpTree($parser->add_subtract("1 + 2"));
#print "a=2\n";                          $parser->startrule("a=2");
#print "a=1+3\n";                        $parser->startrule("a=1+3");
#print "print 5*7\n";                    $parser->startrule("print 5*7");
#print "print 2/4\n";                    $parser->startrule("print 2/4");
#print "print 2+2/4\n";                  $parser->startrule("print 2+2/4");
#print "print 2/2+4\n";                  $parser->startrule("print 2/2+4");
#print "print 2+-2/4\n";                 $parser->startrule("print 2+-2/4");
#print "aA = 5 ; b = 1; print aA + b\n"; $parser->startrule("aA = 5 ; b = 1; print aA + b");

package Exp::Var;

sub new {
    my ($class, $name) = @_;

    return bless {
        name => $name,
    }, $class;
}

sub eval {
    my ($self, $context) = @_;

    my $name = $self->{name};
    my $variables = $context->{variables};
    return $variables->{$name};
}

sub validate {
    my ($self, $context) = @_;

    my $name = $self->{name};
    my $variables = $context->{variables};
    return exists $variables->{$name} ? undef
        : "Unknown variable: $name";
}


package Exp::Value;

sub new {
    my ($class, $value) = @_;

    return bless {
        value => $value,
    }, $class;
}

sub eval {
    my ($self, $context) = @_;

    return $self->{value};
}

sub validate {
    return undef;
}
