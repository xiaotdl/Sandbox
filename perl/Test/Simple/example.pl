# Ref:
# http://search.cpan.org/dist/Test-Simple/lib/Test/Tutorial.pod

use Test::Simple tests => 20;
use Date::ICal;


ok(1 + 1 == 2);
ok(2 + 2 == 5);
# >>>
# 1..2
# ok 1
# not ok 2
# #   Failed test at test.pl line 4.
# # Looks like you failed 1 test of 2.


my $ical = Date::ICal->new( year => 1964, month => 10, day => 16,
                         hour => 16,   min   => 12, sec => 47,
                         tz   => '0530' );

ok( defined $ical,            'new() returned sth' );
ok( $ical->isa('Date::ICal'), '  and it\'s the right class' );
ok( $ical->sec   == 47,       '  sec()'   );
ok( $ical->min   == 12,       '  min()'   );
ok( $ical->hour  == 16,       '  hour()'  );
ok( $ical->day   == 16,       '  day()'   );
ok( $ical->month == 10,       '  month()' );
ok( $ical->year  == 1964,     '  year()'  );


# use Test::More qw(is) to see what we got and what are expected
