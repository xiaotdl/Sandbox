# Encode - character encodings
# Ref: http://perldoc.perl.org/5.8.8/Encode.html
use Encode;
use Data::Dumper;
@list = Encode->encodings();
@all_encodings = Encode->encodings(":all");
print Dumper(\@list);            # Returns available encodings that are loaded.
print Dumper(\@all_encodings);   # Return all available encodings including the ones that are not loaded yet.


# On most platforms the ordinal values of the characters
# (as returned by ord(ch)) is the *"Unicode codepoint"* for the character 
print ord('a') . "\n";
print ord('A') . "\n";


# $octets = encode(ENCODING, $string [, CHECK])
# $string = decode(ENCODING, $octets [, CHECK])
my $string, $octets;
$string = "hello world!";
$octets = encode("iso-8859-1", $string);
$string = decode("iso-8859-1", $octets);


# [$length =] from_to($octets, FROM_ENC, TO_ENC [, CHECK])
from_to($data, "iso-8859-1", "utf8"); #1
$data = decode("iso-8859-1", $data);  #2
$data = encode("utf8", decode("iso-8859-1", $data)); # same as 1
# Both #1 and #2 make $data consist of a completely valid UTF-8 string
# but only #2 turns *utf8 flag* on.


# Perl 5.8 introduced UTF-8 flag.
# This perl notion is like:
#       a byte-oriented mode (utf8 flag off)
#       vs.
#       a character-oriented mode (utf8 flag on).
# 
#  When $octet is...   The utf8 flag in $utf8 is
#  ---------------------------------------------
#  In ASCII only (or EBCDIC only)            OFF <== To make sure old byte-oriented program \
#  In ISO-8859-1                              ON     still work under new  character-oriented data.
#  In any other Encoding                      ON
#  ---------------------------------------------
# 
# peek and poke utf-8 flag:
# is_utf8(STRING [, CHECK])
# _utf8_on(STRING)
# _utf8_off(STRING)



# UTF-8 vs. utf8

# ....We now view strings not as sequences of bytes, but as sequences
#   of numbers in the range 0 .. 2**32-1 (or in the case of 64-bit
#   computers, 0 .. 2**64-1) -- Programming Perl, 3rd ed.
# 
# That has been the perl's notion of UTF-8 but official UTF-8 is more strict; Its ranges is much narrower (0 .. 10FFFF),
# some sequences are not allowed (i.e. Those used in the surrogate pair, 0xFFFE, et al).

# As of Perl 5.8.7, UTF-8 means strict, official UTF-8 while utf8 means liberal, lax, version thereof.
# And Encode version 2.10 or later thus groks the difference between UTF-8 and C"utf8".
#   encode("utf8",  "\x{FFFF_FFFF}", 1); # okay
#   encode("UTF-8", "\x{FFFF_FFFF}", 1); # croaks
