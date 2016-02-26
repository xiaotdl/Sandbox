#include <stdio.h>
#include <float.h>


int main() {

    printf("Storage size for int: %d\n", sizeof(int));
    printf("Storage size for char: %d\n", sizeof(char));
    printf("Storage size for short: %d\n", sizeof(short));
    printf("Storage size for long: %d\n", sizeof(long));

    printf("Storage size for float: %d\n", sizeof(float));
    printf("Storage size for double: %d\n", sizeof(double));

    printf("Min float positive size: %E\n", sizeof(FLT_MIN));
    printf("Max float positive size: %E\n", sizeof(FLT_MAX));
    printf("Precision value: %d\n", sizeof(FLT_DIG));



    return 0;
}
