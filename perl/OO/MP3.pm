package File::MP3;

sub new {
    my $class = shift;
    my ( $path, $data ) = @_;

    die "You cannot create a File::MP3 without an mp3 extension\n"
        unless $path =~ /\.mp3\z/;

    return $class->SUPER::new(@_);
}

1;
