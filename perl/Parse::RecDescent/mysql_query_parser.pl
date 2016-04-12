# Ref: http://www.adp-gmbh.ch/perl/rec_descent.html

use strict;
use warnings;

use Parse::RecDescent;
use Data::TreeDumper;

$::RD_HINT = 1;

my $grammar = q {

expression:     <leftop: term ('+' | '-') term>
                         {
                             my $s = shift @{$item [1]};
                             while (@{$item [1]}) {
                                 my ($op, $t) = splice @{$item [1]}, 0, 2;
                                 if    ($op eq '+') {$s = Mysql::Op::Add->new($s, $t)}
                                 elsif ($op eq '-') {$s = Mysql::Op::Subtract->new($s, $t)}
                             }
                             $return = $s
                         }

term:           <leftop: factor ('*' | '/' | '%') factor>
                         {
                             my $t = shift @{$item [1]};
                             while (@{$item [1]}) {
                                 my ($op, $f) = splice @{$item [1]}, 0, 2;
                                 if    ($op eq '*') {$t = Mysql::Op::Multiply->new($t, $f)}
                                 elsif ($op eq '/') {$t = Mysql::Op::Divide->new($t, $f)}
                                 elsif ($op eq '%') {$t = Mysql::Op::Modulo->new($t, $f)}
                             }
                             $return = $t
                         }

factor:         functioncall
              | number
              | variable
              | '+' factor                   {$return = $item [2]}
              | '-' factor                   {$return = $item [2] * -1}
              | '(' expression ')'           {$return = $item [2]}

functioncall:   m/(?: sum | max | min)/ix '(' expression ')'
                         {
                             if (lc $item[1] eq 'sum') {
                                 $return = Mysql::Function::Sum->new($item[3]);
                             }
                             elsif (lc $item[1] eq 'max') {
                                 $return = Mysql::Function::Max->new($item[3]);
                             }
                             elsif (lc $item[1] eq 'min') {
                                 $return = Mysql::Function::Min->new($item[3]);
                             }
                         }

number:         /\d+/    { $return = Mysql::Value->new($item[1]) }

variable:       /[a-zA-Z_][a-zA-Z0-9_]*/
                         { $return = Mysql::Variable->new($item[1]) }
};

my $parser=Parse::RecDescent->new($grammar);

my $tree;
my $context = {
    variables => {
        column_names => ["name", "sex", "age"],
        rows => [
            {name => 'Tom', sex => 'M',age => 11},
            {name => 'Joe', sex => 'M',age => 22},
            {name => 'Marry', sex => 'F',age => 33},
        ]
    }
};

$tree = $parser->expression("sum(999 + 1 * 1 * 1 + 888 + age) + 1");
print DumpTree($tree);

my $validationError = $tree->validate($context);
die "validationError: " . $validationError . "\n"
    if $validationError;

print $tree->eval($context);

#>>>
# blessed in 'Mysql::Op::Add'
# |- left =  blessed in 'Mysql::Function::Sum'  [OH1]
# |  `- expr =  blessed in 'Mysql::Op::Add'  [OH2]
# |     |- left =  blessed in 'Mysql::Op::Add'  [OH3]
# |     |  |- left =  blessed in 'Mysql::Op::Add'  [OH4]
# |     |  |  |- left =  blessed in 'Mysql::Value'  [OH5]
# |     |  |  |  `- value = 999  [S6]
# |     |  |  `- right =  blessed in 'Mysql::Op::Multiply'  [OH7]
# |     |  |     |- left =  blessed in 'Mysql::Op::Multiply'  [OH8]
# |     |  |     |  |- left =  blessed in 'Mysql::Value'  [OH9]
# |     |  |     |  |  `- value = 1  [S10]
# |     |  |     |  `- right =  blessed in 'Mysql::Value'  [OH11]
# |     |  |     |     `- value = 1  [S12]
# |     |  |     `- right =  blessed in 'Mysql::Value'  [OH13]
# |     |  |        `- value = 1  [S14]
# |     |  `- right =  blessed in 'Mysql::Value'  [OH15]
# |     |     `- value = 888  [S16]
# |     `- right =  blessed in 'Mysql::Variable'  [OH17]
# |        `- name = age  [S18]
# `- right =  blessed in 'Mysql::Value'  [OH19]
#    `- value = 1  [S20]
#    5731


package Mysql::Function::Numeric;

sub new {
    my ($class, $expr) = @_;

    return bless {
        expr => $expr,
    }, $class;
}

sub eval {
    my ($self, $context) = @_;

    return $self->{expr}->eval($context);
}

sub validate {
    my ($self, $context) = @_;

    return $self->{expr}->validate($context);
}


package Mysql::Function::Sum;

use base 'Mysql::Function::Numeric';
use List::Util qw(sum);

sub eval {
    my ($self, $context) = @_;
    my @arr;
    my @rows = @{$context->{variables}->{rows}};
    for my $row (@rows) {
        my $row_context = {
            variables => $row,
        };
        push @arr, $self->SUPER::eval($row_context);
    }

    return sum(@arr);
}

sub validate {
    my ($self, $context) = @_;

    my @error_msg;
    my @rows = @{$context->{variables}->{rows}};
    for my $row (@rows) {
        my $row_context = {
            variables => $row,
        };
        my $err = $self->SUPER::validate($row_context);
        push @error_msg, $err
            if defined $err;
    }
    return @error_msg ?
            join("; ", @error_msg)
        :
            '';
}


package Mysql::Function::Max;

use base 'Mysql::Function::Numeric';
use List::Util qw(max);

sub eval {
    my ($self, $context) = @_;
    my @arr;
    my @rows = @{$context->{variables}->{rows}};
    for my $row (@rows) {
        my $row_context = {
            variables => $row,
        };
        push @arr, $self->SUPER::eval($row_context);
    }

    return max(@arr);
}


package Mysql::Function::Min;

use base 'Mysql::Function::Numeric';
use List::Util qw(min);

sub eval {
    my ($self, $context) = @_;
    my @arr;
    my @rows = @{$context->{variables}->{rows}};
    for my $row (@rows) {
        my $row_context = {
            variables => $row,
        };
        push @arr, $self->SUPER::eval($row_context);
    }

    return min(@arr);
}


package Mysql::Op::Binary;

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


package Mysql::Op::Add;

use base 'Mysql::Op::Binary';

sub eval {
    my ($self, $context) = @_;

    my ($lhs, $rhs) = $self->SUPER::eval($context);
    return $lhs + $rhs;
}


package Mysql::Op::Subtract;

use base 'Mysql::Op::Binary';

sub eval {
    my ($self, $context) = @_;

    my ($lhs, $rhs) = $self->SUPER::eval($context);
    return $lhs - $rhs;
}


package Mysql::Op::Multiply;

use base 'Mysql::Op::Binary';

sub eval {
    my ($self, $context) = @_;

    my ($lhs, $rhs) = $self->SUPER::eval($context);
    return $lhs * $rhs;
}


package Mysql::Op::Divide;

use base 'Mysql::Op::Binary';

sub eval {
    my ($self, $context) = @_;

    my ($lhs, $rhs) = $self->SUPER::eval($context);
    return $lhs / $rhs;
}


package Mysql::Op::Modulo;

use base 'Mysql::Op::Binary';

sub eval {
    my ($self, $context) = @_;

    my ($lhs, $rhs) = $self->SUPER::eval($context);
    return $lhs % $rhs;
}


package Mysql::Variable;

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


package Mysql::Value;

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
