#!/usr/bin/perl

use strict;
use warnings;

use Global;

print $Global::our_cnt;
print $Global::my_cnt;

# console >>>
# Name "Global::my_cnt" used only once: possible typo at main.pl line 9.
# Use of uninitialized value $Global::my_cnt in print at main.pl line 9.
# 10

# $ perl main.pl 2> /dev/null
# stdout >>>
# 10

# $ perl main.pl > /dev/null
# stderr >>>
# Name "Global::my_cnt" used only once: possible typo at main.pl line 9.
# Use of uninitialized value $Global::my_cnt in print at main.pl line 9.

1;
