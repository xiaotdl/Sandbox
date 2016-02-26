// int * func() {
//  ...
// }

// it's not a good idea to return the address of a local var outside the func,
// so you would have to define the local var as static var

#include <stdio.h>
#include <time.h>

int * getRandom() {
    static int r[10];

    srand((unsigned)time(NULL));

    for (int i = 0; i < 10; i++) {
        r[i] = rand();
        printf("%d\n", r[i]);
    }

    return r;
}

int main() {
    int *p;
    int i;

    p = getRandom();

    for (i = 0; i < 10; i++) {
        printf("*(p+[%d]):%d\n", i, *(p+i));
    }

    return 0;
}
