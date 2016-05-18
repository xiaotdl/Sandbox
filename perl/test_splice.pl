# Ref:
# Splice to slice and dice arrays in Perl
# http://perlmaven.com/splice-to-slice-and-dice-arrays-in-perl

# == syntax ==
# splice ARRAY, OFFSET, LENGTH, LIST

# == insert ==
my @others = qw(SnowWhite Humbert);
my @dwarfs = qw(Doc Grumpy Happy Sleepy Sneezy Dopey Bashful);
splice @dwarfs, 3, 0, @others;
print "@dwarfs";
# >>>
# Doc Grumpy Happy SnowWhite Humbert Sleepy Sneezy Dopey Bashful


# == replace ==
my @others = qw(SnowWhite Humbert);
my @dwarfs = qw(Doc Grumpy Happy Sleepy Sneezy Dopey Bashful);
splice @dwarfs, 2, 4, @others;
print "@dwarfs\n";
# >>>
# Doc Grumpy SnowWhite Humbert Bashful
