use strict;
use warnings;

use FindBin;
use lib $FindBin::Bin;

use File;
use Data::Dumper;

my $file = File->new('/a/b/c', '123');
print Dumper($file);

print "end of demo\n";
#die;
#exit -1;

