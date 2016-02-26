/* variable:
 * a name given to a storage area that our program manipulates.
 * each variable has a specific type, which determines the size and layout of the varialbe's memeory.
 * type(init val): char('\0'), int(0), float(0), double(0), pointer(NULL), void --> absence of type
 */

#include <stdio.h>

/* var declaration */
extern int a, b;
extern int c;
extern float f;

/* function declaration */
int func();

int main() {
    /* var definition */
    int a, b;
    int c;
    float f;

    /* var init */
    a = 10;
    b = 20;

    c = a + b;
    printf("value of c: %d\n", c);

    f = 70.0/3.0;
    printf("value of f: %f\n", f);


    /* function call */
    int i = func();
    printf("rv of func(): %d\n", i);

    return 0;
}

int func() {
    return 0;
}



