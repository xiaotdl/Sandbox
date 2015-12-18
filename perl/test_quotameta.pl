# Ref: http://perldoc.perl.org/functions/quotemeta.html
# quotemeta or \Q...\E
# Returns the value of EXPR with all the ASCII non-"word" characters backslashed.
# (That is, all ASCII characters not matching /[A-Za-z_0-9]/ will be preceded by a backslash
# in the returned string, regardless of any locale settings.)

$sentence = 'The quick brown fox jumped over the lazy dog';
$substring = 'quick.*?fox';
$sentence =~ s{$substring}{big bad wolf};
print $sentence . "\n";

$sentence = "The quick brown fox jumped over the lazy dog";
$substring = 'quick.*?fox';
$substring = 'quick.*?\sfox';
$sentence =~ s{\Q$substring\E}{big bad wolf};
print $sentence . "\n";

$sentence = "The quick.*?fox jumped over the lazy dog";
$substring = 'quick.*?\sfox';
$sentence =~ s{\Q$substring\E}{big bad wolf};
print $sentence . "\n";

print quotemeta 'quick.*?\sfox';
