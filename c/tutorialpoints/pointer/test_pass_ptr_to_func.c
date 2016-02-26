#include <stdio.h>
#include <time.h>

void getSeconds(unsigned long *par);

double getAvg(int *arr, int size);

int main(){
    // ------------------------------------
    // declare:          type var;
    // pass addr of var: func(&var)
    // take ptr as arg:  void func (*ptr)
    unsigned long sec;

    getSeconds(&sec);

    printf("number of seconds: %ld\n", sec);

    // ------------------------------------
    // declare:          type ptr[];
    // pass ptr to func: func(ptr)
    // take ptr as arg:  void func(*ptr)
    int balance[5] = {1000, 2, 3, 17, 50};
    double avg;

    avg = getAvg(balance, 5);

    printf("avg value is: %f\n", avg);

    return 0;
}

void getSeconds(unsigned long *par) {
    *par = time(NULL);
    return;
}

double getAvg(int *arr, int size) {
    int i, sum = 0;
    double avg;

    for (i = 0; i < size; i++) {
        sum += arr[i];
    }

    avg = (double) sum / size;
    return avg;
}
