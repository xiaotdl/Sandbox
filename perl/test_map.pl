# map
# Ref: http://perldoc.perl.org/functions/map.html
# map EXPR,LIST

use Data::Dumper;

@numbers = (97..100);
@chars = map(chr, @numbers);
print Dumper(\@chars);

@numbers = (1..5);
@squares = map { $_ * $_ } @numbers;
print Dumper(\@squares);

@numbers = (2..8);
@squares = map { $_ > 5 ? ($_ * $_) : () } @numbers;
print Dumper(\@squares);
@squares = map { $_ * $_ } grep { $_ > 5 } @numbers; # same as above
print Dumper(\@squares);

my @rows = (1, 2, 3);
print Dumper([
    map {
		my $row = $_;
        [$row]
    } @rows
]);
