# Array operations
# http://perlmaven.com/manipulating-perl-arrays

use Data::Dumper;
use warnings;
use strict;

# pop: remove from right
my @names = ('Foo', 'Bar', 'Moo');
my $last = pop @names;
print "$last\n";     # Moo
print "@names\n";    # Foo Bar

# push: insert from right
my @names = ('Foo', 'Bar');
push @names, 'Moo';
print "@names\n";    # Foo Bar Moo

my @others = ('Darth', 'Vader');
push @names, @others;
print "@names\n";    # Foo Bar Moo Darth Vader


# shift: remove from left
my @names = ('Foo', 'Bar', 'Moo');
my $first = shift @names;
print "$first\n";    # Foo
print "@names\n";    # Bar Moo

# unshift: insert from left
my @names = ('Foo', 'Bar');
unshift @names, 'Moo';
print "@names\n";    # Moo Foo Bar

my @others = ('Darth', 'Vader');
unshift @names, @others;
print "@names\n";    # Darth Vader Moo Foo Bar


# split string into array
my $first_line = "result,count,dfa,asme,dns,ssl,http,ixe,flbl,srdb,ipproto,custom,bytes_in,bytes_out,pkts_in,pkts_out";
my $line = "tcp.http,1,0,0,0,0,1,0,0,0,0,0,372,112,3,2";
my @array = split /,/, $first_line;
print "@array\n";
# convert array into hash
my %hash = map {$_ => 1} @array;
print Dumper(\%hash);
# initialize hash with array
my %row;
@row{@array} = split /,/, $line;
print Dumper(\%row);
my $res = [];
push @$res, \%row;

foreach my $row (@$res) {
    print Dumper($row);
}


my $s = 'tcp.http.google';
my @last = (split(/\./, $s));
print ref(\@last);
print $last[-1];
