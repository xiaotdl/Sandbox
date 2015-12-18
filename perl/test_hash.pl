# Printing hash
my %hash = (1..10);
foreach (sort keys %hash) {
    print "$_ => $hash{$_}\n";
}


# print Dumper(\%hash)
use Data::Dumper;
my %hash = (
    key1 => 'value1',
    key2 => 'value2'
);
print Dumper(%hash);  # okay, but not great
print "or\n";
print Dumper(\%hash); # much better


# Some hash utils
# sudo cpan; install Hash::MostUtils
use Hash::MostUtils qw(hashgrep);
my %hash = (1..10);
my %dump =
        # != for numerical and nq for string comparison
        hashgrep { $a != 1 && $b != 4 }
        %hash;
print Dumper(\%dump);
