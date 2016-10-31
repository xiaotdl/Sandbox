package Range;

# Checks value against a range.

use strict;
use warnings;

use base 'Exporter';

our @EXPORT_OK = qw(value_in_range);


sub value_in_range {
    my ($value, $range) = @_;

    $value =~ s/^\s+//;
    $value =~ s/\s+$//;
    $range =~ s/^\s+//;
    $range =~ s/\s+$//;

    return 0
        unless $value =~ /^ \d+ (?: \.\d+ )? $/x;

    if ($range =~ m/^ \[    \s* (\d+ (?: \.\d+ )? ) \s*
                      [,\-] \s* (\d+ (?: \.\d+ )? )? \] $/x) {
        # [ 1.23, 4.56 ]
        my $from = $1;
        my $to = $2;
        return (defined $to ?
            ($value >= $from && $value <= $to) :
            ($value >= $from)
        );
    }
    elsif ($range =~
            #      $1 - base value
            m{^ \[ (\d+ (?: \.\d+ )? ) \s*
            #                     $2 - percentage
                            ~ \s* (\d+) % \s* \]$}x) {
        my $maxDiff = $2 * 0.01 * $1;
        my $from = $1 - $maxDiff;
        my $to = $1 + $maxDiff;
        return ($value >= $from && $value <= $to);
    }
    elsif ($range =~
            #       $1 - base value
            m{^ \s* (\d+(?:\.\d+)?) \s*
            #                     $2 negative part    $3 is percentage?
              ~ \s* \[ \s*  - \s* (\d+(?:\.\d+)?) \s* (%?) \s*
            #                     $4 positive part    $5 is percentage?
                     , \s* \+ \s* (\d+(?:\.\d+)?) \s* (%?) \s* \] \s* $}x
        ) {
        # Asymmetric and percentage ranges
        #  a~[-b%, +c%]
        #  a~[-b, +c]
        #  a~[-b%, +c]
        #  a~[-b, +c%]
        my $from = $1 - $2 * ($3 eq '' ? 1 : 0.01 * $1);
        my $to =   $1 + $4 * ($5 eq '' ? 1 : 0.01 * $1);
        return ($value >= $from && $value <= $to);
    }

    return 0;
}

1;
