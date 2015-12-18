# High resolution alarm, sleep, gettimeofday, interval timers
use Time::HiRes qw(sleep gettimeofday tv_interval);

my $t0 = [gettimeofday];
# do bunch of stuff here
sleep (0.1);
my $t1 = [gettimeofday];
# do more stuff here
sleep (0.2);
my $t0_t1  = tv_interval $t0, $t1;
my $t0_now = tv_interval $t0;
print $t0_t1, "\n";
print $t0_now, "\n";

my $timeout = 1;
my $startTime = [gettimeofday];
while (tv_interval($startTime) <= $timeout) {
    print "time passed: " . tv_interval($startTime) . "\n";
    sleep(0.1);
}
