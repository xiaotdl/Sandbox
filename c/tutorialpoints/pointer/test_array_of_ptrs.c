#include <stdio.h>

const int MAX = 3;

int main () {
    int var[] = {10, 100, 200};
    int i;

    // -------------without ptr---------------
    for (i = 0; i < MAX; i++) {
        printf("value of var[%d] = %d\n", i, var[i]);
    }

    // -------------with ptr---------------
    int *ptr[MAX];
    for (i = 0; i < MAX; i++) {
        ptr[i] = &var[i]; // assign the addr to ptr
    }
    for (i = 0; i < MAX; i++) {
        printf("value of var[%d] = %d\n", i, *ptr[i]);
    }

    // -------------with ptr---------------
    // store a list of strings
    char *names[] = {
        "Zara Ali",
        "Hina Ali",
        "Nuha Ali",
        "Sara Ali",
    };
    for (i = 0; i < 4; i++) {
        printf("value of names[%d] = %s\n", i, names[i]);
    }

    return 0;
}
