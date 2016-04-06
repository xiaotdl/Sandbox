#!/usr/bin/perl
use strict;
use warnings;

use Parse::RecDescent;
use Data::TreeDumper;

my $parser = Parse::RecDescent->new(q{

    EQ:  '='
    OR:  /(?: \|\| | or)/ix
    AND: /(?: &&   | and)/ix
    NOT: /(?: !    | not)/ix

    expression:
        and_expr OR expression
        { $return = Exp::Or->new($item[1], $item[3]) }
      | and_expr

    and_expr:
        not_expr AND and_expr
        { $return = Exp::And->new($item[1], $item[3]) }
      | not_expr

    not_expr:
        NOT brack_expr
        { $return = Exp::Not->new($item[2]) }
      | brack_expr

    brack_expr:
        '(' eq_expr ')'
        { $return = $item[2] }
      | eq_expr
      | term

    eq_expr:
        term EQ term
        { $return = Exp::Eq->new($item[1], $item[3])  }

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

});


# my $tree = $parser->expression("a && b || c");
# my $tree = $parser->expression("a = 1 && b = 2");
my $tree = $parser->expression("result = 'udp' || result = 'tcp'");
# print DumpTree($tree);

my $context = {
    variables => {
        #result => 'icmp',
        result => 'tcp',
    }
};

my $validationError = $tree->validate($context);
print $validationError . "\n";

my $value = $tree->eval($context);
print ($value ? 1 : 0);

package Exp::Binary;

sub new {
    my ($class, $left, $right) = @_;

    return bless {
        left => $left,
        right => $right,
    }, $class;
}

sub eval {
    my ($self, $context) = @_;

    return ($self->{left}->eval($context), $self->{right}->eval($context));
}

sub validate {
    my ($self, $context) = @_;

    return $self->{left}->validate($context) || $self->{right}->validate($context);
}


package Exp::And;

use base 'Exp::Binary';

sub eval {
    my ($self, $context) = @_;

    my ($lhs, $rhs) = $self->SUPER::eval($context);
    return $lhs && $rhs;
}


package Exp::Or;

use base 'Exp::Binary';

sub eval {
    my ($self, $context) = @_;

    my ($lhs, $rhs) = $self->SUPER::eval($context);
    return $lhs || $rhs;
}


package Exp::Not;

sub new {
    my ($class, $exp) = @_;

    return bless {
        exp => $exp,
    }, $class;
}

sub eval {
    my ($self, $context) = @_;

    return !$self->{exp}->eval($context);
}

sub validate {
    my ($self, $context) = @_;

    return $self->{exp}->validate($context);
}

package Exp::Eq;

use base 'Exp::Binary';

use Scalar::Util qw(looks_like_number);

sub eval {
    my ($self, $context) = @_;

    my ($lhs, $rhs) = $self->SUPER::eval($context);
    return
        &looks_like_number($lhs) && &looks_like_number($rhs) ?
            $lhs == $rhs
        :
            $lhs eq $rhs;
}


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
    return exists $variables->{$name} ? ''
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
    return '';
}
