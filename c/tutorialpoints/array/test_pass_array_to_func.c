// Way-1
// Formal param as a pointer
// void myFunc(int *param) {
//     ...
// }

// Way-2
// Formal param as a sized/unsized array
// void myFunc(int param[10]) {
//     ...
// }
// void myFunc(int param[]) {
//     ...
// }

// ==> example of Way-2: pass unsized array
// definition:  double getAvg(int arr[], int size) {
// func call:   int arr[5] = {1000, 2, 3, 17, 50};
//              avg = getAvg(arr, 5);

#include <stdio.h>

// func declare
double getAvg(int arr[], int size);

int main() {
    // init array
    int balance[5] = {1000, 2, 3, 17, 50};
    double avg;

    // pass pointer of array as an arg
    avg = getAvg(balance, 5);

    printf("avg value: %f", avg);

    return 0;
}

double getAvg(int arr[], int size) {
    double avg;
    double sum;

    for (int i = 0; i < size; i++) {
        sum += arr[i];
    }

    avg = sum / size;

    return avg;
}
