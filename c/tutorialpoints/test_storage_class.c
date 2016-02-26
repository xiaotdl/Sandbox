/* storage class: (auto, register, static, extern)
 * defines the scope (visibility) and life-time of var, func.
 */

// auto: default storage class for all local var

// register: define local var to be stored in a register instead of RAM

// static: instructs the compiler to keep a local var in existence

// extern: give reference of a globle var that is visible to ALL program files. 

#include <stdio.h>

void func(void);

static int count = 5;

int main() {
    while (count--) {
        func();
    }

    return 0;
}

void func(void) {
    static int i = 5;
    i++;

    printf("i is %d and count is %d\n", i, count);
}
