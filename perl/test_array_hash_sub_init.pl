use Data::Dumper;

$array_ref = [1,two,3];
print ref($array_ref);
print Dumper($array_ref);
print $$array_ref[0] . "\n";
print $array_ref->[0] . "\n";
print "@$array_ref\n";
# >>>
# ARRAY$VAR1 = [
#           1,
#           'two',
#           3
#         ];
# 1
# 1 two 3

@array = (1,two,3);
print ref(\@array);
print Dumper(\@array);
print $array[2] . "\n";
# >>>
# ARRAY$VAR1 = [
#           1,
#           'two',
#           3
#         ];
# 3

$hash_ref = {one=>1};
print ref($hash_ref);
print Dumper($hash_ref);
print $$hash_ref{one} . "\n";
print $hash_ref->{one} . "\n";
# >>>
# HASH$VAR1 = {
#           'one' => 1
#         };
# 1
# 1

%hash = (two=>2);
print ref(\%hash);
print Dumper(\%hash);
print $hash{two} . "\n";
# >>>
# HASH$VAR1 = {
#           'two' => 2
#         };
# 2


# e.g.
$op = '=';
$current = {
    name => "name",
    (defined $op ?
            (
                op => $op,
            )
        :
            ()
    ),
};
print ref($current);
print Dumper($current);
# >>>
# HASH$VAR1 = {
#           'name' => 'name',
#           'op' => '='
#         };




sub func {
    $var = shift;
    print ref($var) . "\n"; #CODE
    print $var . "\n";      #CODE(0x886d4b4)
    print 'inside func'. "\n";       #456
    &$var;
}

func(sub {print 'anominous func call as a param';});

# >>>
# CODE
# CODE(0x886d4b4)
# inside func
# anominous func call as a param
