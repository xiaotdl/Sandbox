use strict;
use warnings;

use Data::Dumper;
use List::Util qw(max);

our $DEBUG = 0;

sub debug {
    print shift if $DEBUG;
}

sub table_view {
    my $table = shift;

    my $row_length = scalar @{$table};
    my $col_length = scalar @{$table->[0]};
    debug "row_length: $row_length\n";
    debug "col_length: $col_length\n";

    my @max_length_per_col;
    for my $i (0..$col_length - 1) {
        my @curr_col_length;
        for my $j (0..$row_length - 1) {
            push @curr_col_length, length($table->[$j]->[$i]);
        }
        push @max_length_per_col, max(@curr_col_length);
    }

    debug "max_length_per_col:\n" . Dumper(\@max_length_per_col);


    my $new_table = [];
    for my $i (0..$col_length - 1) {
        for my $j (0..$row_length - 1) {
            my $tail_spaces = " " x ($max_length_per_col[$i] - length($table->[$j]->[$i]));
            $new_table->[$j]->[$i] =  $table->[$j]->[$i] . $tail_spaces;
        }
    }

    debug "new_table:\n" . Dumper($new_table);

    my $output = '';
    my $col_name_delimiter = '-';
    my $col_delimiter = ' ';
    my $row_delimiter = "\n";
    for my $i (0..$row_length - 1) {
        if ($i == 1) {
            for my $j (0..$col_length - 1) {
                $output .= $col_name_delimiter x length($new_table->[$i]->[$j]);
                $output .= $col_delimiter;
            }
            $output .= $row_delimiter;
        }
        for my $j (0..$col_length - 1) {
            $output .= $new_table->[$i]->[$j];
            $output .= $col_delimiter;
        }
        $output .=  $row_delimiter;
    }
    print $output;
}

my $table = [
    ['col1', 'col2', 'col3'],
    [1, 2, 3],
    ['4-sfdsfs', 5, 6],
    [7, 8, 9],
    [10, 11, 12],
];

&table_view($table);


# >>>
# col1     col2 col3
# -------- ---- ----
# 1        2    3
# 4-sfdsfs 5    6
# 7        8    9
# 10       11   12
