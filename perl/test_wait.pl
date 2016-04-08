use warnings;
use strict;

use Time::HiRes qw(sleep gettimeofday tv_interval);
use Data::Dumper;


# General wait util function
# The function will wait till the condition is meet given the timeout and interval.
# Arguments:
#   \&condition - (required) callback, this function will be called
#                 at each given interval till it returns True or
#                 meet \&condition_met_criteria before timeout.
#   \@condition_args - condition args, defaults to [].
#   \&condition_met_criteria - callback, interface to customize condition met criteria
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
#        condition_args => [arg1, arg2, {key1 => "value1\n"}], )
# &wait( condition => $condition,
#        condition_met_criteria =>
#            sub {
#                my $_result = shift;
#                return $_result eq 'what you want';
#            }
#        timeout => 10 )
sub wait {
    my %args = @_;
    my $condition        = $args{condition}        || die 'condition parameter is required';
    my $condition_args   = $args{condition_args}   || [];
    my $condition_met_criteria = $args{condition_met_criteria};
    my $timeout      = $args{timeout}  || die 'timeout parameter is required';
    my $interval     = $args{interval} || 1;
    my $progress_msg = $args{progress_msg} || '';
    my $timeout_msg  = $args{timeout_msg} || "Condition not meet after %s seconds.\n";
    my $success_msg  = $args{success_msg};

    my $startTime = [gettimeofday()];
    my $_result;
    my $success;

    while (tv_interval($startTime) < $timeout) {
        $_result = $condition->($condition_args);

        $progress_msg =
            defined &$progress_msg ? $progress_msg->($_result)
                                   : $progress_msg;
        print $progress_msg;

        $success =
            defined $condition_met_criteria && defined &$condition_met_criteria
            ? $condition_met_criteria->($_result)
            : $_result;
        if ($success) {
            if (defined $success_msg) {
                $success_msg =
                    defined &$success_msg
                    ? $success_msg->(tv_interval($startTime))
                    : $success_msg;
                printf($success_msg, tv_interval($startTime));
            }
            return;
        }

        sleep $interval;
    }

    $timeout_msg =
        defined &$timeout_msg ? $timeout_msg->($timeout, $_result)
                              : $timeout_msg;
    die sprintf($timeout_msg, $timeout, &_dump($_result));
}


# A helper to set Terse and Sortkeys options when running Dumper.
sub _dump () {
    local $Data::Dumper::Terse = 1;
    local $Data::Dumper::Sortkeys = 1;
    return Dumper(@_);
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
    my ($aref) = @_;
    my ($x) = @$aref;
    return &get_random_num() > $x;
}


print "== Example: wait until num_is_bigger_than_5 with timeout: 5s, interval: 2s. ==\n";
&wait( condition => $num_is_bigger_than_5,
       timeout => 5,
       interval => 2,
       timeout_msg => "Wow, you didn't get a number bigger than 5 in %s seconds.\n",
       success_msg => "done in %s seconds.\n");

print "== Example: wait until num_is_bigger_than_x with args: [50], kwargs: {msg => 'hello wolrd'}, timeout: 10s. ==\n";
&wait( condition => \&num_is_bigger_than_x,
       timeout => 10,
       condition_args => [50],
       success_msg => "done in %s seconds.\n");

# output >>>
# Example: wait until num_is_bigger_than_5 with timeout: 5s, interval: 2s.
# Here is random number 5. I need to sleep for a second.
#  done in 1.003984 seconds.

# Example: wait until num_is_bigger_than_x with args: [50], kwargs: {msg => 'hello wolrd'}, timeout: 10s.
# Here is random number 9. I need to sleep for a second.
# Here is random number 9. I need to sleep for a second.
# Here is random number 0. I need to sleep for a second.
# Here is random number 3. I need to sleep for a second.
# Here is random number 9. I need to sleep for a second.
# Condition not meet after 10 seconds.

# shell returned 60
