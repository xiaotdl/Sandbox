package Example;

use strict;
use vars qw($VERSION);

# A module that will bind a variable from a script to a password (or whatever) file.

# pull $VERSION from RCS version identifier
($VERSION = substr(q$Revision: 0.7 $, 10)) =~ s/\s+$//;

sub Version {return $VERSION;}

use Carp;

# Create tied hash
# the TIEHASH method is implicitly called when you invoke tie()
sub TIEHASH {
    my $cls = shift;
    my $path = shift;
    my $mode = shift || 'r';

    if (@_) {
        croak ("usage: tie(\%hash, \$file, [mode])");
    }

    my $clobber = ($mode eq 'rw' ? 1 : 0);

    my $node = {
        PATH    => $path,
        CLOBBER => $clobber,
        CURRENT => {}
    };

    open(FH, "$path");
    my @lines = <FH>;
    close FH;

    my ($line, $id, $pass);
    foreach $line (@lines) {
        chomp $line;
        ($id, $pass) = split(/\:/,$line);
        $node->{CURRENT}{$id} = $pass;
    }

    my $self = bless $node => $cls;
    return $self;
}

# Store an entry
# The STORE method is what will handle the actual writting of data to the resource, when a value in the tied hash changes.
# This method will also perform any complex behavior needed to be done before the data should be written, such as encrypting a password.
# This method is called when doing something such as:
#   $hash{FOO} = "bar";
# For good programming measure, we are taking into account the fact that STORE is called after the upcoming method CLEAR finishes.
# When STORE is called via CLEAR there will be no arguments (besides $self, of course). So, STORE will return before writting an entry with no username or password.
sub STORE {
    my $self = shift;
    my $id = shift;
    my $passwd = shift;
    my $passwdFile = $self->{PATH};
    my $return = 0;
    my @cache;
    my $cryptedPass;

    unless ($self->{CLOBBER}) {
        carp ("No write access for $self->{PATH}");
        return;
    }

    if (!$id && !$passwd) {return 1;}

    #if ($passwd eq "") {
    #    $cryptedPass = "";
    #} else {
    #    $cryptedPass = crypt($passwd, $salt);
    #}
    $cryptedPass = $passwd;

    # Warning, possible race condition ahead
    # I need to update this opening a locking!
    if (!open(FH,"<$passwdFile")) {
        carp("Cannot open $passwdFile: $!");
        return;
    }
    flock(FH, 2);

    if (!exists $self->{CURRENT}{$id}) {
        while (<FH>) {
            if ( /^$id\:/ ) {
                push (@cache, "$id\:$cryptedPass\n")
                    unless $cryptedPass eq "";
                $return = 1;
            } else {
                push (@cache, $_);
            }
        }
    }
    close FH;

    if ($return) {
        if (!open(FH, ">$passwdFile")) {
            carp("Cannot open $passwdFile: $!");
            return;
        }
        flock(FH, 2);
        while (@cache) {
            print FH shift (@cache);
        }
    } else {
        if (!open(FH, ">>$passwdFile")) {
            carp("Cannot open $passwdFile: $!");
            return;
        }
        flock(FH, 2);
        print FH "$id\:$cryptedPass\n" unless $cryptedPass eq "";
        #$foo = $hash{FOO};
    }
}

# The FETCH method has a very specific function, to get a value.
# To do this it first checks to see if the username ($id) being looking for exists in the current hash. If so, it returns that value, if not, it returns a message saying it doesn't exist.
sub FETCH {
    my $self = shift;
    my $id = shift;
    if (exists $self->{CURRENT}{$id}) {
        return $self->{CURRENT}{$id};
    } else {
        return "$id doesn't exist";
    }
}

# The DELETE method does just that, it deletes an entry in the hash, and in turn the tied resource. It doesn't delete just the value, but the key/value pair. The DELETE method is only called when the delete() fuction is called. Assigning undef or ``'' to an entry in the hash doesn't delete that entry, so DELETE is not called.

# delete $hash{FOO};

# The above DELETE call will delete all instances of entry FOO
 sub DELETE {
    my $self = shift;
    my $id = shift;
    my $passwdFile = $self->{PATH};
    my @cache;

    unless ($self->{CLOBBER}) {
        carp ("No write access for $self->{PATH}");
        return;
    }

    if (!exists $self->{CURRENT}{$id}) {return 1;}

    delete $self->{CURRENT}{$id};

    if (!open(FH,"<$passwdFile")) {
        carp("Cannot open $passwdFile: $!");
        return;
    }
    flock(FH, 2);
    while (<FH>) {
        if ( /^$id\:/ ) {
            next;
        } else {
            push (@cache, $_);
        }
    }
    close FH;

    if (!open(FH,">$passwdFile")) {
        carp("Cannot open $passwdFile: $!");
        return;
    }
    flock(FH, 2);
    while (@cache) {
        print FH shift (@cache);
    }
    close FH;
    return 1;
}

# CLEAR, will clear the entire hash, as well as clearing all the data out of the tied resource. CLEAR is generally called when you assign an empty list as the value of your tied hash.
# Below illustrates ways in which CLEAR will be invoked.

#    %hash = "";
#    %hash = %newHash;
#    %hash = {};
#    undef %hash;

sub CLEAR {
    my $self = shift;
    my ($passwdFile) = $self->{PATH};

    unless ($self->{CLOBBER}) {
        carp ("No write access for $self->{PATH}");
        return;
    }

    if (!open(FH,">$passwdFile")) {
        carp("Cannot open $passwdFile: $!");
        return;
    }
    close FH;
    $self->{CURRENT} = {};
}

# FIRSTKEY
# This method is invoked when a call is made to iterate through the hash, generally with the keys() or each() functions.
sub FIRSTKEY {
    my $self = shift;
    my $a = keys %{$self->{CURRENT}};
    each %{$self->{CURRENT}};
}

# NEXTKEY
# This method is also invoked during an each() or keys() iteration.
sub NEXTKEY {
    my $self = shift;
    return each %{$self->{CURRENT}};

}

# DESTROY
# This method is invoked when the tied variable is to be destroyed. Unless the return value of tie() has been saved, this can be done with the untie() function. If the tied variable hasn't been untie()'d, DESTROY will be called when the script exits. In general, you don't need to have anything in a DESTROY method, unless you are doing some special debugging, or you possibly have some cleanup that you want to do. In fact, you do not need to have a DESTROY method at all, and our Example.pm will not have this method.
sub DESTROY { unlink "/tmp/tie.txt";}
