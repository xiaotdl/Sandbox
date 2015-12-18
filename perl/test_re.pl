# perlre
# Ref: http://perldoc.perl.org/perlre.html

# print "Hello World" =~ /(hi|hello)/i;

if ("Hello World" =~ /(hi|hello)/i) {
    print $1;
}

# my $fit_summary = `tail -100 $logfile | tac`;
# my ($ok, $fail, $error);
# ($ok, $fail, $error) = $fit_summary =~ /counts: (\d+) OK, (\d+) FAIL, (\d+) ERROR,/g;
# return 0 unless (defined $ok || defined $fail || defined $error);

# ($support_id) = $response_content =~ /Your support ID is: (\d+)/;


# <Modifier>
# /m
# Treat string as multiple lines. That is, change "^" and "$"
# from matching the start of the string's first line and the
# end of its last line to matching the start and end of each
# line within the string.

# /i
# Case insensitive.

# /x
# Extend your pattern's legibility by permitting whitespace and comments.

# /g
# Match recursively in a string.
# @array = $str =~ m/(stuff)/g;
# $scalar = $str =~ m/(this)/;

# metacharacters: \b, \t, \n etc.

# Ref: http://perldoc.perl.org/functions/quotemeta.html
# \E      end case modification (think vi)
# \Q      quote (disable) pattern metacharacters till \E
# \Q$pattern\E all ASCII characters not matching /[A-Za-z_0-9]/ will be preceded by a backslash in the returned string
# we want to match literal strings with \Q\E

# /e   Evaluate the right side as an expression.
# /ee  Evaluate the right side as a string then eval the result.
# /r   Return substitution and leave the original string untouched.


# Regexp Quote-Like Operators
# Ref: http://perldoc.perl.org/perlop.html#Regexp-Quote-Like-Operators
# $rex = qr/my.STRING/is;
# print $rex;                 # prints (?si-xm:my.STRING)
# s/$rex/foo/;


# Anchors ^ $
# By default regex match is a substring match.
# You want to add anchors to the regex:

#     my $re = qr/^ $testName\.ucs\.(\d+) $/x;