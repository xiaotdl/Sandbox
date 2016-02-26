// int *ptr; ptr++; ptr increase from 1000 to 1004 as int is 4 bytes
// char *ptr; ptr++; ptr increase from 1000 to 1001 as char is 1 byte

#include <stdio.h>

const int MAX = 3;

int main() {
    int var[] = {10, 100, 200};
    int i, *ptr;

    // == incrementing a ptr == 
    ptr = var;
    for (i = 0; i < MAX; i++) {
        printf("address of var[%d] = %x\n", i, ptr);
        printf("value of var[%d] = %d\n", i, *ptr);
        ptr++;
    }

    // == decrementing a ptr ==
    ptr = &var[MAX - 1];
    for (i = MAX; i > 0; i--) {
        printf("address of var[%d] = %x\n", i, ptr);
        printf("value of var[%d] = %d\n", i, *ptr);
        ptr--;
    }

    // == ptr comparison ==
    ptr = var;
    i = 0;
    while (ptr <= &var[MAX - 1]) {
        printf("address of var[%d] = %x\n", i, ptr);
        printf("value of var[%d] = %d\n", i, *ptr);
        ptr++;
        i++;
    }

    return 0;
}
