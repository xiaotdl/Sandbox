/* array:
 * a data structure that can store a fixed-sized sequential collection of elements of the same type.
 */

// Declare array
// syntax: type arrayName [arraySize]
// e.g.: double balance[10];

// Init array
// e.g.: double balance[5] = {1000.0, 2.0, 3.4, 7.0, 50.0};
// if you omit the size of the array, an array just big enough to hold the init values will be created.

// Access array element
// e.g.: double salary = balance[9];

#include <stdio.h>

int main() {
    int arr[5];

    // init array
    for (int i = 0; i < 5; i++) {
        arr[i] = i + 100;
    }

    // access array element
    for (int j = 0; j < 5; j++) {
        printf("Element[%d] = %d\n", j, arr[j]);
    }

    return 0;
}
