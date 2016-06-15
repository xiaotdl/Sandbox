# == Test::More ==
# yet another framework for writing test script
# Ref: http://perldoc.perl.org/Test/More.html

# either number of tests or no_plan needs to be specified
#use Test::More tests => 23;
use Test::More qw(no_plan);

# == require_ok ==
require_ok( 'Data::Dump' );
require_ok( 'Some::Module' );
# >>>
# ok 1 - require Data::Dump;
# not ok 2 - require Some::Module;
# #   Failed test 'require Some::Module;'
# #   at test.pl line 12.
# #     Tried to require 'Some::Module'.
# #     Error:  Can't locate Some/Module.pm in @INC (you may need to install the Some::Module module) (@INC contains: /Library/Perl/5.18/darwin-thread-multi-2level /Library/Perl/5.18 /Network/Library/Perl/5.18/darwin-thread-multi-2level /Network/Library/Perl/5.18 /Library/Perl/Updates/5.18.2/darwin-thread-multi-2level /Library/Perl/Updates/5.18.2 /System/Library/Perl/5.18/darwin-thread-multi-2level /System/Library/Perl/5.18 /System/Library/Perl/Extras/5.18/darwin-thread-multi-2level /System/Library/Perl/Extras/5.18 .) at (eval 5) line 2.

my $got, $expected, $test_name;

# == ok ==
$got = 5;
$expected = 5;
$test_name = '5 should eq 5';
ok($got eq $expected, $test_name);
ok($got ne $expected, $test_name);
# >>>
# ok 3 - 5 should eq 5
# not ok 4 - 5 should eq 5
# #   Failed test '5 should eq 5'
# #   at test.pl line 21.


# == is/isnt ==
is   ($got, $expected, $test_name);
isnt ($got, $expected, $test_name);
# >>>
# ok 5 - 5 should eq 5
# not ok 6 - 5 should eq 5
# #   Failed test '5 should eq 5'
# #   #   at test.pl line 37.
# #   #          got: '5'
# #   #     expected: anything else


# == like/unlike ==
like  ($got, qr/\d/, $test_name);
unlike($got, qr/\d/, $test_name);
# >>>
# ok 7 - 5 should eq 5
# not ok 8 - 5 should eq 5
# #   Failed test '5 should eq 5'
# #   #   at test.pl line 51.
# #   #                   '5'
# #   #           matches '(?^:\d)'


# == cmp_ok ==
cmp_ok($got, '==', $expected, $test_name);
cmp_ok($got, '!=', $expected, $test_name);
# >>>
# ok 9 - 5 should eq 5
# not ok 10 - 5 should eq 5
# #   Failed test '5 should eq 5'
# #   at test.pl line 60.
# #          got: 5
# #     expected: anything else


# == is_deeply ==
$test_name = 'compare json using is_deeply()';
my $got_complex_structure = {1 => [2, 3], 4 => [5, 6, 7], 8 => 9};
my $expected_complex_structure = {1 => [2, 3], 4 => [5, 6, 7], 8 => 9};
is_deeply($got_complex_structure, $expected_complex_structure, $test_name);
$expected_complex_structure = {1 => [2, 3], 4 => [5, 6], 8 => 9};
is_deeply($got_complex_structure, $expected_complex_structure, $test_name);
# >>>
# ok 11 - compare json using is_deeply()
# not ok 12 - compare json using is_deeply()
# #   Failed test 'compare json using is_deeply()'
# #   #   at test.pl line 76.
# #   #     Structures begin differing at:
# #   #          $got->{4}[2] = '7'
# #   #     $expected->{4}[2] = Does not exist


# == pass/fail ==
# They are synonyms for ok(1) and ok(0).
# Use these very, very, very sparingly.
$test_name = 'pass/fail';
pass($test_name);
fail($test_name);
# >>>
# ok 13 - pass/fail
# not ok 14 - pass/fail
# #   Failed test 'pass/fail'
# #   #   at test.pl line 90.
