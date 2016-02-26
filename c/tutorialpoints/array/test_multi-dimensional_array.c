// declare:
// type arrayName [x][y];

// init:
// int a[3][4] = {
//     {0, 1, 2, 3},
//     {4, 5, 6, 7},
//     {8, 9, 10, 11}
// };

// access:
// int val = a[2][3];

#include <stdio.h>

int main() {
    int a[5][2] = {{0,1}, {2,3}, {4,5}, {6,7}, {8,9}};

    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 2; j++) {
            printf("a[%d][%d] = %d\n", i, j, a[i][j]);
        }
    }

    return 0;
}
