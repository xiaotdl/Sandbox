use Range qw(value_in_range);

print value_in_range(1, '[1,5]') ? 1 : 0;
print value_in_range(10, '[1,5]') ? 1 : 0;
print value_in_range(10, '[1,]') ? 1 : 0;
