# Ref: http://www.adp-gmbh.ch/perl/rec_descent.html

use strict;
use warnings;

use Parse::RecDescent;

$::RD_HINT = 1;

my $grammar = q {
{use List::MoreUtils;}
{
    my %vars;
    $vars{age} = 3;
    $vars{column_names} = qw(name sex age);
    $vars{rows} = [
        ['Tom', 'M', 11],
        ['Joe', 'M', 22],
        ['Marry', 'F', 33],
    ];
}

start:          statements               {print "$item[1]\n"}

statements:     statement ';' statements
              | statement

statement:      <rightop: variable '=' expression>
                          {my $value = pop @{$item [1]};
                           while (@{$item [1]}) {
                               $vars {shift @{$item [1]}} = $value;
                           }
                           $value
                          }

expression:     <leftop: term ('+' | '-') term>
                         {
                          my $s = shift @{$item [1]};
                          while (@{$item [1]}) {
                              my ($op, $t) = splice @{$item [1]}, 0, 2;
                              if    ($op eq '+') {$s += $t}
                              elsif ($op eq '-') {$s -= $t}
                          }
                          $s
                         }

term:           <leftop: factor ('*' | '/' | '%') factor>
                         {my $t = shift @{$item [1]};
                          while (@{$item [1]}) {
                              my ($op, $f) = splice @{$item [1]}, 0, 2;
                              if    ($op eq '*') {$t *= $f}
                              elsif ($op eq '/') {$t /= $f}
                              elsif ($op eq '%') {$t %= $f}
                          }
                          $t
                         }

factor:         functioncall
              | number
              | variable
              | '+' factor               {$item [2]}
              | '-' factor               {$item [2] * -1}
              | '(' statement ')'        {$item [2]}

number:         /\d+/                    {$item [1]}

variable:       /[a-z]+/i                {$vars {$item [1]} ||= 0}

functioncall:  ('SUM' | 'MAX' | 'MIN') '(' statement ')'
               {
                   my $result = 0;
                   if ($item[1] == 'SUM') {
                       for my $row (@{$vars{rows}}) {
                           $result += $row->[List::MoreUtils::first_index {$_ eq 'age'} @$row ];
                           #$result += $row->[2];
                       }
                   }
                   $return = $result;
                   $return = $item[3];
               }





};

my $parser=Parse::RecDescent->new($grammar);

my $result;
#$result = $parser->start("three=3;six=2*three;eight=three+5;2+eight*six+50");
#$result = $parser->start("1 - 2 * 4 - 3");
#$parser->start("SUM(1 - 2 * 4 - age) + 1");
$parser->start("SUM(age + 1)");

