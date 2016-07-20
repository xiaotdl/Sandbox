package File;

sub new {
    my $class = shift;
    my ( $path, $data ) = @_;

    my $self = bless {
        path => $path,
        data => $data,
    }, $class;

    return $self;
}

sub DESTROY {
    local $?;
    print 'DESTROYing...';
    exit -1;
}

1;
