#!/usr/bin/perl

use strict;
use warnings;


package a;

our $counter = 10;

package b;

$counter++;


package ::main;

$counter++;

print $counter;
# >>>
# 12

1;
