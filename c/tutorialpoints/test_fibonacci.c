#include <stdio.h>

int fibonacci(int i) {
    if (i == 0) {
        return 0;
    } 

    if (i == 1) {
        return 1;
    } 

    return fibonacci(i - 1) + fibonacci(i - 2);
}

int main() {
    for (int i = 0; i < 10; i++) {
        printf("fibonacci(%d): %d\n", i, fibonacci(i));
    }
}
