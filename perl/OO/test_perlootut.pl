# perlootut
# Ref: http://perldoc.perl.org/perlootut.html
# class, object, attribute, method
#                = noun     = verb
# Perl -- class-based OO

# == Class ==
package File;

# == Constructor
# In Perl, no special keyword for constructing an object.
# However, most OO modules in CPAN use a method named new() to do it.
my $hostname = File->new(
    path          => '/etc/hostname',
    content       => "foo\n",
    last_mod_time => 1304974868,
);

# == Blessing
# Most Perl objects are hashes, but an object can be
# an instance of any Perl type (scalar, array, etc.)
# Turning a plain data structure into an object is done by "blessing"
# that data structure user Perl's bless.
use Scalar::Util 'blessed';
print blessed($hash);      # undef
print blessed($hostname);  # File


# == Methods ==
# The arrow operator (->) tells Perl that we are calling a method.
# When we make a method call, Perl arranges for the method's invocant
# to be passed as the first argument. Invocant is a fancy name for
# the thing on the left side of the arrow. The invocant can either be
# a class name or an object. We can also pass additional arguments to
# the method:
sub print_info {
    my $self   = shift;
    my $prefix = shift // "This file is at ";
    print $prefix, ", ", $self->path, "\n";
}
$file->print_info("The file is located at ");
#>>> The file is located at /etc/hostname


# == Polymorphism ==
# File->print_content();
# WebPage->print_content();


# == Inheritance ==
# package File::MP3;
# use parent 'File';

# == overriding methods
# package File::MP3;
# use parent 'File';

# sub print_info {
#     my $self = shift;
#     $self->SUPER::print_info();
#     print "Its title is ", $self->title, "\n";
# }


# == Encapsulation ==
# When another developer uses your class, they don't need to know
# how it is implemented, they just need to know what it does.


# == Compostion ==
# reference other objects in class, or a has-a relationship.


# == Roles ==

# == Mixin == 

# == Perl OO system ==
# example: Moose
