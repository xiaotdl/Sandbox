use strict;
use warnings;

use bytes;

my $KB = 1024;
my $MB = $KB * 1024;

my $s = '';
while (1) {
    $s .= 'x' x $MB;
    print( (bytes::length($s) / $MB) . "\n" );
}

# $ free -hm
#              total       used       free     shared    buffers     cached
# Mem:          993M       181M     **811M**     2.4M       628K        17M
# -/+ buffers/cache:       162M       830M
# Swap:         509M       298M       211M
#
#
# $ perl test_max_string_size.pl
# 1
# 2
# ...
# 890
# 891
# Out of memory!
