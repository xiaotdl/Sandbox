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


# == Hash Slice ==
# ref: http://www.webquills.net/web-development/perl/perl-5-hash-slices-can-replace.html
my %hash = (one => 1, two => 2, three => 3);
my @keys = qw/one two three/;
# Regular access to scalar key
print "$hash{one}"; # 1
print "\n";
# Hash slice accesses multiple keys. Note the '@'
print "@hash{@keys}"; # 1 2 3
print "\n";

# Hash slice assignment to multiple keys. Note the '@'
@hash{@keys} = (11, 12, 13);
print "@hash{@keys}"; # 11 12 13
print "\n";


my %number_for = (one => 1, two => 2, three => 3);
my $num_for = \%number_for;
my @columns = qw/three one two/;
# Common syntax for dereferencing and getting a scalar index
print $num_for->{one}; # 1
print "\n";
# Alternate syntax, the lazy way:
print $$num_for{two}; # 2
print "\n";
print @$num_for{@columns}; # 312  <= this looks good!
print "\n";
# Alternate syntax, the explicit way
print ${$num_for}{three}; # 3
print "\n";
print @{$num_for}{@columns}; # 312
print "\n";
