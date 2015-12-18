use warnings;
use strict;

use Time::HiRes qw(sleep gettimeofday tv_interval);


# General wait util function
# The function will wait until the condition is meet given the timeout and interval.
# Arguments:
#   \&condition - (required) callback, this function will be called
#                 at each given interval until it returns True before timeout.
#   \@condition_args - condition args, defaults to [].
#   \%condition_kwargs - condition keyword args, defaults to {}.
#   $timeout - (required) timeout in seconds
#   The left args are intuitive...
# Returns: nothing
# Die if condition or timeout parameter is missing.
# Die if condition didn't meet within given timeout.
#
# Example usage:
# my $condition = sub {...};
# &wait( condition => $condition,
#        timeout => 10,
#        condition_args => [arg1, arg2],
#        condition_kwargs => {msg => "hello world!\n"} );
sub wait {
    my %args = @_;
    my $condition        = $args{condition}        || die 'condition parameter is required';
    my $condition_args   = $args{condition_args}   || [];
    my $condition_kwargs = $args{condition_kwargs} || {};
    my $timeout      = $args{timeout}  || die 'timeout parameter is required';
    my $interval     = $args{interval} || 1;
    my $progress_msg = $args{progress_msg} || "progressing...\n";
    my $timeout_msg  = sprintf($args{timeout_msg} || "Condition not meet after %s seconds.\n", $timeout);

    my $startTime = [gettimeofday()];

    while (tv_interval($startTime) < $timeout) {
        print $progress_msg;
        return if $condition->($condition_args, $condition_kwargs);
        sleep $interval;
    }

    die $timeout_msg;
}

sub get_random_num {
    my $random_num = int(rand(10));
    print "Here is random number $random_num."
          . " I need to sleep for a second.\n";
    sleep 1;
    return $random_num;
}

# Note: To avoid warning: Variable "$var" will not stay shared at file...
# This problem can usually be solved by making the inner subroutine anonymous, using the "sub {}" syntax.
# Ref: http://www.perlmonks.org/bare/index.pl/?node_id=137292
my $num_is_bigger_than_5 = sub {
    return &get_random_num() > 5;
};

sub num_is_bigger_than_x {
    my ($aref, $href) = @_;
    my ($x) = @$aref;
    my $msg = $href->{msg};
    print "$msg";
    return &get_random_num() > $x;
}


print "Example: wait until num_is_bigger_than_5 with timeout: 5s, interval: 2s.\n";
&wait( condition => $num_is_bigger_than_5,
       timeout => 5,
       interval => 2,
       timeout_msg => "Wow, you didn't get a number bigger than 5 in %s seconds.\n");

print "Example: wait until num_is_bigger_than_x with args: [50], kwargs: {msg => 'hello wolrd'}, timeout: 10s.\n";
&wait( condition => \&num_is_bigger_than_x,
       timeout => 10,
       condition_args => [50],
       condition_kwargs => {msg => "hello world!\n"} );

# output >>>
# Example: wait until num_is_bigger_than_5 with timeout: 5s, interval: 2s.
# progressing...
# Here is random number 7. I need to sleep for a second.
# Example: wait until num_is_bigger_than_x with args: [50], kwargs: {msg => 'hello wolrd'}, timeout: 10s.
# progressing...
# hello world!
# Here is random number 9. I need to sleep for a second.
# progressing...
# hello world!
# Here is random number 2. I need to sleep for a second.
# progressing...
# hello world!
# Here is random number 8. I need to sleep for a second.
# progressing...
# hello world!
# Here is random number 0. I need to sleep for a second.
# progressing...
# hello world!
# Here is random number 7. I need to sleep for a second.
# Condition not meet after 10 seconds.

# shell returned 60
