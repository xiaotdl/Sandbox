use strict;
use warnings;

sub say {
    print shift . "\n";
}

my $str = "pkg-abc >= 1.2.3rc4 # comments";

# $str =~ s/#.*//; # truncate end-of-line comment

$str =~
    m/^ \s*
        ( [^<>=\s#]+ ) \s*        # package name
        (?:
            ( <= | = | >= ) \s*   # compare op
            ( [^<>=\s#]+ ) \s*    # package version
        )?
        ([#].*)? \s*              # end-of-line comment
    $/x
or die "Failed to match package version!";

say $1;
say $2;
say $3;
say $4;

# >>>
# pkg-abc
# >=
# 1.2.3rc4
# # comments
