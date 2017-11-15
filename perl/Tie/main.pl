#!/usr/bin/perl

# This is a quick command line program to test this module out. Try adding, deleting, and getting passwords.

use Example;

tie(%hash, "Example", "example", "rw") || die "Can't tie : $!";

&ask;

sub ask {
    print "(A)dd, (D)elete, or (G)et user:";
    $ans = <STDIN>;
    if ($ans =~ /a/i) { &add; }
    elsif ($ans =~ /d/i) { &delete;}
    elsif ($ans =~ /g/i) {&get;}
    else { print "Try again\n"; &ask;}
}

sub add {
    print "User Name:";
    $name = <STDIN>;
    print "\nPassword:";
    $pass = <STDIN>;
    chop $name;
    chop $pass;
    $DB::single = 1; # PERL BREAKPOINT
    $hash{$name} = $pass;
    print "\nAdded\nAgain (Y/N)?";
    $again = <STDIN>;
    if ($again !~ /y/i) { untie %hash; exit;}else{&ask;}

}

sub delete {
    print "User Name:";
    $name = <STDIN>;
    chop $name;
    delete $hash{$name};
    print "\nDeleted\nAgain (Y/N)?";
    $again = <STDIN>;
    if ($again !~ /y/i) { untie %hash; exit;}else{&ask;}

}

sub get {
    print "User Name:";
    $name = <STDIN>;
    chop $name;
    if (!exists $hash{$name}) {
        print "$name isn't valid";
    } else {
        print "$name\'s encrypted password is " . $hash{$name};
    }
    print "\nAgain (Y/N)?";
    $again = <STDIN>;
    if ($again !~ /y/i) { untie %hash; exit;}else{&ask;}

}

