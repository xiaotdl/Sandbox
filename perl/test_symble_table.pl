# Ref:
# http://perldoc.perl.org/perlmod.html

use Data::Dumper;

#sub say {print shift . "\n";}

## check Symbol Table
print Dumper(\%::);
#print Dumper(*{'::say'});
print Dumper(\@INC);
print Dumper(\@ISA);
