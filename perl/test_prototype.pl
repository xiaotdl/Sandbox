# Ref:
# perlsub - prototypes
# http://perldoc.perl.org/perlsub.html#Prototypes

sub runFunc(&) {
    my $sub = shift;
    $sub->();
};

runFunc {
    print 123;
};

# >>>
# 123
