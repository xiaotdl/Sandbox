// Type casting:
// a way to convert a variable from one data type to another
// syntax: (type_name) expression

// Usual Arithmetic Conversion
// implicitly performed to cast values to a common type
// int -> unsigned int -> long -> unsigned long -> \
// long long -> unsigned long long -> float -> double -> long double

#include <stdio.h>

int main() {
    // ----------------------------------
    int sum = 17, n = 5;
    double mean;

    // type casting has precedence over division
    // sum first converted to type double and then divided by n yielding a double value
    mean = (double) sum / n;
    printf("value of mean: %f\n", mean);

    mean = sum / n;
    printf("value of mean without casting: %f\n", mean);

    // ---------Integer Promotion---------
    int i = 17;
    char c = 'c'; // ascii value is 99

    int res_i;
    res_i = i + c;
    printf("value of sum: %d\n", res_i);

    float res_f;
    res_f = i + c;
    printf("value of sum: %f\n", res_f);

    return 0;
}
