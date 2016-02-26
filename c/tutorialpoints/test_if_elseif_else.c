#include <stdio.h>

int main() {
    int a = 100;

    if (a == 10) {
        printf("value of a is 10");
    }
    else if (a == 20) {
        printf("value of a is 20");
    }
    else {
        printf("none of the values matched\n");
    }

    printf("value of a: %d\n", a);

    return 0;
}
