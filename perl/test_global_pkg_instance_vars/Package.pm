package Package;

use strict;
use warnings;


# == global variable ==
# can be accessed within other package once they import this package
# e.g.
# use Package;
# print $Package::our_var;
our $our_var = 'our_var';

# == package variable ==
# can only be accessed within this package
# other package can only access this through getter method
my $my_var = 'my_var';
# e.g.
my $instance_cnt = 0;

sub new {
    my $class = shift;
# == instance variable ==
    my $self = {
        a => 'a',
        b => 'b',
    };
    bless $self, $class;
    $instance_cnt++;
    return $self;
}

sub get_var {
    return $my_var;
}

sub set_var {
    my ($self, $val) = @_;
    $my_var = $val;
}

sub get_instance_cnt {
    return $instance_cnt;
}

1;
