# Ref: http://search.cpan.org/~evo/String-Escape-2010.002/Escape.pm
use String::Escape qw( quote_non_words );
# quote_non_words($value) : $escaped
# As above, but only quotes empty, punctuated, and multiword values;
# simple values consisting of alphanumerics[A-Za-z0-9]without special characters are not quoted.

print quote_non_words("ABCabc123") . "\n";
print quote_non_words("ABCabc123*") . "\n";
print quote_non_words("ABCabc123?") . "\n";

# >>>
# ABCabc123
# "ABCabc123*"
# "ABCabc123?"

use String::Escape qw( backslash unbackslash );
# backslash($value) : $escaped
#   Converts special characters to their backslash-escaped equivalents.
# unbackslash($value) : $escaped
#   Converts backslash escape sequences in a string back to their original characters.
print backslash( "\tNow is the time\nfor all good folks\n" );
print "\n";
print unbackslash( "\tNow is the time\nfor all good folks\n" );
print unbackslash( '\\tNow is the time\\nfor all good folks\\n' );


