//   ptr         ptr       variable
// +------+    +------+    +-----+
// | addr | -> | addr | -> | val |
// +------+    +------+    +-----+


// declare: a ptr to a ptr of type int
// int **var;

#include <stdio.h>

int main() {
    int var;
    int *ptr;
    int **pptr;

    var = 3000;

    ptr = &var;
    pptr = &ptr;

    printf("value of var = %d\n", var);
    printf("value of *ptr = %d\n", *ptr);
    printf("value of **pptr = %d\n", **pptr);
}
