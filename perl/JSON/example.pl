use strict;
use warnings;

use FindBin;
use lib ("$FindBin::Bin/../lib");

use JSON qw( decode_json );
use Data::Dumper;

my $json = '{
        "name": "Bob",
        "sex": "Male",
        "address": {
                "city": "San Jose",
                "state": "California"
        },
        "friends":
                [
                        {
                                "name": "Alice",
                                "age": "20"
                        },
                        {
                                "name": "Laura",
                                "age": "23"
                        },
                        {
                                "name": "Daniel",
                                "age": "30"
                        }
                ]
}';

my $decoded = decode_json($json);

# This is a Perl example of parsing a JSON object.

print Dumper($decoded);
