#include <stdio.h>

void swap(int x, int y);

int main() {
    int a = 100;
    int b = 200;

    printf("before swap, a: %d, b: %d\n", a, b);

    swap(a, b);

    printf("after swap, a: %d, b: %d\n", a, b);

    printf("valure didn't change as its func call by value.");

    return 0;
} 

void swap(int x, int y) {
    int tmp;

    tmp = x;
    x = y;
    y = tmp;

    return;
}