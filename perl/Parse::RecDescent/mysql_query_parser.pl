# Ref: http://www.adp-gmbh.ch/perl/rec_descent.html

use strict;
use warnings;

use Parse::RecDescent;
use Data::TreeDumper;
use Data::Dumper;

$::RD_HINT = 1;  # show detailed analyses and hints on both errors and warnings.

my $grammar = q {

# MySQL Operator Precedence
# Ref: http://dev.mysql.com/doc/refman/5.7/en/operator-precedence.html
# == highest precedence ==
#    INTERVAL
#    BINARY, COLLATE
#    !
#    - (unary minus), ~ (unary bit inversion)
#    ^
#    *, /, DIV, %, MOD
#    -, +
#    <<, >>
#    &
#    |
#    = (comparison), <=>, >=, >, <=, <, <>, !=, IS, LIKE, REGEXP, IN
#    BETWEEN, CASE, WHEN, THEN, ELSE
#    NOT
#    AND, &&
#    XOR
#    OR, ||
#    = (assignment), :=
# == lowest precedence ==


# == lowest precedence ==

expression:     or_expr

or_expr:        and_expr m/(?: \|\| | or)/ix or_expr
                         { $return = Mysql::Op::Or->new($item[1], $item[3]) }
              | and_expr

and_expr:       not_expr m/(?: && | and)/ix and_expr
                         { $return = Mysql::Op::And->new($item[1], $item[3]) }
              | not_expr

not_expr:       m/(?: ! | not)/ix compare_expr
                         { $return = Mysql::Op::Not->new($item[2]) }
              | compare_expr
              | value
              | variable

compare_expr:   binop_expr ('=' | '!=' | '<' | '>' | '<=' | '>=') binop_expr
                         {
                             my $op = $item[2];
                             if    ($op eq '=' ) {$return = Mysql::Op::Eq->new($item[1], $item[3])}
                             elsif ($op eq '!=') {$return = Mysql::Op::Ne->new($item[1], $item[3])}
                             elsif ($op eq '<' ) {$return = Mysql::Op::Lt->new($item[1], $item[3])}
                             elsif ($op eq '>' ) {$return = Mysql::Op::Gt->new($item[1], $item[3])}
                             elsif ($op eq '<=') {$return = Mysql::Op::Le->new($item[1], $item[3])}
                             elsif ($op eq '>=') {$return = Mysql::Op::Ge->new($item[1], $item[3])}
                         }
              | binop_expr

binop_expr:     <leftop: term ('+' | '-') term>
                         {
                             my $s = shift @{$item[1]};
                             while (@{$item[1]}) {
                                 my ($op, $t) = splice @{$item[1]}, 0, 2;
                                 if    ($op eq '+') {$s = Mysql::Op::Add->new($s, $t)}
                                 elsif ($op eq '-') {$s = Mysql::Op::Subtract->new($s, $t)}
                             }
                             $return = $s
                         }

term:           <leftop: factor ('*' | '/' | '%') factor>
                         {
                             my $t = shift @{$item[1]};
                             while (@{$item[1]}) {
                                 my ($op, $f) = splice @{$item[1]}, 0, 2;
                                 if    ($op eq '*') {$t = Mysql::Op::Multiply->new($t, $f)}
                                 elsif ($op eq '/') {$t = Mysql::Op::Divide->new($t, $f)}
                                 elsif ($op eq '%') {$t = Mysql::Op::Modulo->new($t, $f)}
                             }
                             $return = $t
                         }

factor:         functioncall
              | value
              | variable
              | '+' factor                   {$return = $item[2]}
              | '-' factor                   {$return = $item[2] * -1}
              | '(' expression ')'           {$return = $item[2]}

functioncall:   m/(?: sum | max | min)/ix '(' expression ')'
                         {
                             if    (lc $item[1] eq 'sum') { $return = Mysql::Function::Sum->new($item[3]) }
                             elsif (lc $item[1] eq 'max') { $return = Mysql::Function::Max->new($item[3]) }
                             elsif (lc $item[1] eq 'min') { $return = Mysql::Function::Min->new($item[3]) }
                         }

value:          /\d+/    { $return = Mysql::Value->new($item[1]) }
              | "'" /[a-zA-Z0-9_-]+/ "'"
                         { $return = Mysql::Value->new($item[2]) }
              | '"' /[a-zA-Z0-9_-]+/ '"'
                         { $return = Mysql::Value->new($item[2]) }

variable:       /[a-zA-Z_][a-zA-Z0-9_]*/
                         { $return = Mysql::Variable->new($item[1]) }

# == highest precedence ==
};

my $tree;
my $parser=Parse::RecDescent->new($grammar);
my $context = {
    variables => {
        rows => [
            {name => 'Tom',  sex => 'M',age => 11},
            {name => 'Joe',  sex => 'M',age => 22},
            {name => 'Mary', sex => 'F',age => 33},
        ]
    }
};

# MySQL query e.g.
# mysql> SELECT sum(age + 1 * 2 - 3) + 1 FROM table WHERE name = 'Tom' || name = 'Joe';
# == WHERE parser ==
$tree = $parser->expression("name = 'Tom' || name = 'Joe'");
print DumpTree($tree);

my @rows = @{$context->{variables}->{rows}};
for my $row (@rows) {
    my $row_context = {
        variables => $row,
    };
    my $validationError = $tree->validate($row_context);
    die "validationError: " . $validationError . "\n"
        if $validationError;
    my $selected = $tree->eval($row_context) ? 1 : 0;
    print "'$row->{name}' selected -> $selected\n";
}
# >>>
#     blessed in 'Mysql::Op::Or'
#    |- left =  blessed in 'Mysql::Op::Eq'  [OH1]
#    |  |- left =  blessed in 'Mysql::Variable'  [OH2]
#    |  |  `- name = name  [S3]
#    |  `- right =  blessed in 'Mysql::Value'  [OH4]
#    |     `- value = Tom  [S5]
#    `- right =  blessed in 'Mysql::Op::Eq'  [OH6]
#       |- left =  blessed in 'Mysql::Variable'  [OH7]
#       |  `- name = name  [S8]
#       `- right =  blessed in 'Mysql::Value'  [OH9]
#          `- value = Joe  [S10]
#    'Tom' selected -> 1
#    'Joe' selected -> 1
#    'Marry' selected -> 0


# == SELECT parser ==
$tree = $parser->expression("sum(age + 1 * 2 - 3) + 1 ");
print DumpTree($tree);

my $validationError = $tree->validate($context);
die "validationError: " . $validationError . "\n"
    if $validationError;

print $tree->eval($context);
# >>>
#     blessed in 'Mysql::Op::Add'
#    |- left =  blessed in 'Mysql::Function::Sum'  [OH1]
#    |  `- expr =  blessed in 'Mysql::Op::Subtract'  [OH2]
#    |     |- left =  blessed in 'Mysql::Op::Add'  [OH3]
#    |     |  |- left =  blessed in 'Mysql::Variable'  [OH4]
#    |     |  |  `- name = age  [S5]
#    |     |  `- right =  blessed in 'Mysql::Op::Multiply'  [OH6]
#    |     |     |- left =  blessed in 'Mysql::Value'  [OH7]
#    |     |     |  `- value = 1  [S8]
#    |     |     `- right =  blessed in 'Mysql::Value'  [OH9]
#    |     |        `- value = 2  [S10]
#    |     `- right =  blessed in 'Mysql::Value'  [OH11]
#    |        `- value = 3  [S12]
#    `- right =  blessed in 'Mysql::Value'  [OH13]
#       `- value = 1  [S14]
#    64


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


package Mysql::Op::And;

use base 'Mysql::Op::Binary';

sub eval {
    my ($self, $context) = @_;

    my ($lhs, $rhs) = $self->SUPER::eval($context);
    return $lhs && $rhs;
}


package Mysql::Op::Or;

use base 'Mysql::Op::Binary';

sub eval {
    my ($self, $context) = @_;

    my ($lhs, $rhs) = $self->SUPER::eval($context);
    return $lhs || $rhs;
}


package Mysql::Op::Not;

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


package Mysql::Op::Eq;

use base 'Mysql::Op::Binary';

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


package Mysql::Op::Ne;

use base 'Mysql::Op::Binary';

use Scalar::Util qw(looks_like_number);

sub eval {
    my ($self, $context) = @_;

    my ($lhs, $rhs) = $self->SUPER::eval($context);
    return
        &looks_like_number($lhs) && &looks_like_number($rhs) ?
            $lhs != $rhs
        :
            $lhs ne $rhs;
}


package Mysql::Op::Lt;

use base 'Mysql::Op::Binary';

use Scalar::Util qw(looks_like_number);

sub eval {
    my ($self, $context) = @_;

    my ($lhs, $rhs) = $self->SUPER::eval($context);
    return
        &looks_like_number($lhs) && &looks_like_number($rhs) ?
            $lhs < $rhs
        :
            $lhs lt $rhs;
}


package Mysql::Op::Gt;

use base 'Mysql::Op::Binary';

use Scalar::Util qw(looks_like_number);

sub eval {
    my ($self, $context) = @_;

    my ($lhs, $rhs) = $self->SUPER::eval($context);
    return
        &looks_like_number($lhs) && &looks_like_number($rhs) ?
            $lhs > $rhs
        :
            $lhs gt $rhs;
}


package Mysql::Op::Le;

use base 'Mysql::Op::Binary';

use Scalar::Util qw(looks_like_number);

sub eval {
    my ($self, $context) = @_;

    my ($lhs, $rhs) = $self->SUPER::eval($context);
    return
        &looks_like_number($lhs) && &looks_like_number($rhs) ?
            $lhs <= $rhs
        :
            $lhs le $rhs;
}


package Mysql::Op::Ge;

use base 'Mysql::Op::Binary';

use Scalar::Util qw(looks_like_number);

sub eval {
    my ($self, $context) = @_;

    my ($lhs, $rhs) = $self->SUPER::eval($context);
    return
        &looks_like_number($lhs) && &looks_like_number($rhs) ?
            $lhs >= $rhs
        :
            $lhs ge $rhs;
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
