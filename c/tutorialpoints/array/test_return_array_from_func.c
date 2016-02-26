/* C does not allow return an entire array,
 * however you can return a pointer to an array by specifying the array's name without an index.
 */

// e.g.
// int *array_ref;
// array_ref = getArray();
// printf(*(array_ref + i));

#include <stdio.h>
int * getRandom() {
    static int r[10];

    srand((unsigned)time(NULL));

    for (int i = 0; i < 10; i++) {
        r[i] = rand();
        printf("r[%d] = %d\n", i, r[i]);
    }

    return r;
}

int main() {
   int *ptr; 

   ptr = getRandom();

   for (int i = 0; i < 10; i++) {
       printf("*(ptr+%d) : %d\n", i, *(ptr + i));
   }

   return 0;
}
