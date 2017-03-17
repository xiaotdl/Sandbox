use strict;
use warnings;

use Carp qw<longmess>;
use Data::Dumper;

my $mess = longmess();
print Dumper($mess);

# >>>
# R1 = ' at dump_stack_trace.pl line 3.
# ';
