/* array name is a constant pointer to the first element of the array */
// double balance[50];
// here, balance is a pointer to &balance[0]
//
// double *p;
// double balance[10];
// p = balance;
//
// access array element
// balance[4], *(balance + 4), *(p + 4)

#include <stdio.h>

int main() {
    double balance[5] = {1000.0, 2.0, 3.4, 17.0, 50.0};
    double *p;
    int i;

    p = balance;

    printf("accessing array values using pointers:\n");
    for (i = 0; i < 5; i++) {
        printf("*(p + %d) : %f\n", i, *(p + i));
    }

    printf("accessing array values using balance:\n");
    for (i = 0; i < 5; i++) {
        printf("*(balance + %d) : %f\n", i, *(balance + i));
    }

    return 0;
}
