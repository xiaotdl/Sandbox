/* constant:
 * fixted value that the program may not alter during execution.
 * aka literal
 */


#include <stdio.h>

// == #define identifier value ==
#define LENGTH 10
#define WIDTH 5
#define NEWLINE '\n'

int main() {
    int area = LENGTH * WIDTH;
    printf("value of area: %d", area);
    printf("%c", NEWLINE);

    // == const type variable = value; ==
    const int L = 10;
    const int W = 5;
    const char N = '\n';

    int A = L * W;
    printf("value of area: %d", A);
    printf("%c", N);

    return 0;
}

