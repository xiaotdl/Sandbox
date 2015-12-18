# perlobj - Perl object reference
# Ref: http://perldoc.perl.org/perlobj.html

# There are a few basic principles which define object oriented Perl:
# 1. An object is simply a data structure that knows to which class it belongs.
# 2. A class is simply a package. A class provides methods that expect to operate on objects.
# 3. A method is simply a subroutine that expects a reference to an object (or a package name, for class methods) as the first argument.


# == An Object is Simply a Data Structure ==
# Objects are merely Perl data structures (hashes, arrays, scalars, filehandles, etc.) that have been explicitly associated with a particular class.
# That explicit association is created by the built-in bless function, which is typically used within the constructor subroutine of the class.

# package File;
# 
# sub new {
#     my $class = shift;
# 
#     return bless {}, $class;
# }

# the {} code creates a reference to an empty anonymous hash.
# The bless function then takes that reference and associates the hash with the class in $class. 

# We can also use a variable to store a reference to the data structure that is being blessed as our object:

# sub new {
#     my $class = shift;
#     my $self = {};
#     bless $self, $class;
#     # optional
#     # $self->_initialize();
#     return $self;
# }


# == Objects Are Blessed; Variables Are Not ==
use Scalar::Util 'blessed';
my $foo = {};
my $bar = $foo;
bless $foo, 'Class';
print blessed( $foo );      # prints "Class"
print blessed( $bar );      # prints "Class"
$bar = "some other value";
print blessed( $bar );      # prints undef


# == A Class is Simply a Package ==
# Perl does not provide any special syntax for class definitions.
# A package is simply a namespace containing variables and subroutines.
# The ONLY DIFFERENCE is that in a class, the subroutines may expect a reference to an object or the name of a class as the first argument.
# This is purely a matter of convention.

# Each package contains a special array called @ISA. The @ISA array contains a list of that class's parent classes, if any.
# This array is examined when Perl does method resolution.


# == A Method is Simply a Subroutine ==
# Most methods you write will expect to operate on objects:

# sub save {
#     my $self = shift;
#     open my $fh, '>', $self->path() or die $!;
#     print {$fh} $self->data()       or die $!;
#     close $fh                       or die $!;
# }


# == Method Invocation ==
# Calling a method on an object is written as $object->method .

# my $pod = File->new( 'perlobj.pod', $data );
# $pod->save();

# The -> syntax is also used when dereferencing a reference. It looks like the same operator, but these are two different operations.
# When you call a method, the thing on the left side of the arrow is passed as the first argument to the method.
# That means when we call Critter->new() , the new() method receives the string "Critter" as its first argument. 


# == Inheritance ==

# package File::MP3;
# use parent 'File';    # sets @File::MP3::ISA = ('File');
# my $mp3 = File::MP3->new( 'Andvari.mp3', $data );
# $mp3->save();

# sub save {
#     my $self = shift;
#     say 'Prepare to rock';
#     $self->SUPER::save();
# }


# == Method Resolution Caching ==
# When Perl searches for a method, it caches the lookup so that future calls to the method do not need to search for it again.
# Changing a class's parent class or adding subroutines to a class will invalidate the cache for that class.
# The mro pragma provides some functions for manipulating the method cache directly.


# == Writing Constructors ==
# File.pl
# MP3.pl


# == Method Call Variations ==

# == Method Names as Strings
# my $file = File->new( $path, $data );
# my $method = 'save';
# $file->$method();

# This works exactly like calling $file->save(). This can be very useful for writing dynamic code.
# For example, it allows you to pass a method name to be called as a parameter to another method.

# == Class Names as Strings
# my $class = 'File';
# my $file = $class->new( $path, $data );


# == Invoking Class Methods ==
# my $class = 'Class';
# $class->new();



