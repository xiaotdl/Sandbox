# Ref:
# Splice to slice and dice arrays in Perl
# http://perlmaven.com/splice-to-slice-and-dice-arrays-in-perl

# == syntax ==
# splice ARRAY, OFFSET, LENGTH, LIST

# == insert ==
my @others = qw(SnowWhite Humbert);
#               0   1      2     3      4      5     6
my @dwarfs = qw(Doc Grumpy Happy Sleepy Sneezy Dopey Bashful);
splice @dwarfs, 3, 0, @others; # insert "SnowWhite Humbert" starting from index: 3
print "@dwarfs\n";
# >>>
# Doc Grumpy Happy SnowWhite Humbert Sleepy Sneezy Dopey Bashful


# == replace ==
my @others = qw(SnowWhite Humbert);
#               0   1      2     3      4      5     6
my @dwarfs = qw(Doc Grumpy Happy Sleepy Sneezy Dopey Bashful);
splice @dwarfs, 2, 4, @others; # replace "Happy Sleepy Sneezy Dopey" with "SnowWhite Humbert"
print "@dwarfs\n";
# >>>
# Doc Grumpy SnowWhite Humbert Bashful


# == remove an element in the middle of an array ==
#               0   1      2     3      4      5     6
my @dwarfs = qw(Doc Grumpy Happy Sleepy Sneezy Dopey Bashful);
splice @dwarfs, 3, 1; # remove 'Sleepy', index: 3, length: 1
print "@dwarfs\n";
# >>>
# Doc Grumpy Happy Sneezy Dopey Bashful
