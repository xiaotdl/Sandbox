/* sizeof() - returns size of a variable
 * & (get addr)  - returns address of a variable
 * * (get value) - pointer to a variable
 * ?: - conditional expression
 */

#include <stdio.h>

int main() {
    int a = 4;
    short b;
    double c;
    int *ptr;

    // == sizeof() ==
    printf("size of var a = %d\n", sizeof(a));
    printf("size of var b = %d\n", sizeof(b));
    printf("size of var c = %d\n", sizeof(c));

    // == &, * ==
    ptr = &a; // 'ptr' now contains the address of var 'a'
    printf("value of var a: %d\n", a);
    printf("*ptr: %d\n", *ptr);
    printf("ptr: %d\n", ptr);

    // == ?: ternary ==
    a = 10;
    b = (a == 1) ? 20 : 30;
    printf("value of b should be 30: %d\n", b);

    return 0;
}
