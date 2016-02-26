#include <stdio.h>

int main() {
    int var1;
    char var2[10];

    printf("Address of var1: %x\n", &var1);
    printf("Address of var2: %x\n", &var2);

    // -----------------------------------
    int var = 20;
    int *ip;

    ip = &var;

    printf("address of var: %x\n", &var);
    printf("address of var: %x\n", ip);

    printf("value of var: %d\n", var); 
    printf("value of var: %d\n", *ip); 

    // ------------NULL Pointer-------------
    int *ptr = NULL; 

    printf("value of ptr is: %x\n", ptr);

    return 0;
}
