#include <stdio.h>
#include <stdarg.h>

double getAvg(int num, ...) {
    va_list valist; //declare valist
    double sum;

    // init valist for variable num of args
    va_start(valist, num);

    for (int i = 0; i < num; i++) {
        // access valist using va_arg
        sum += va_arg(valist, int);
    }

    // clean memory reserved for valist using va_end
    va_end(valist);

    return sum / num;
}

int main() {
    printf("avg of 2, 3, 4, 5 = %f\n", getAvg(4, 2, 3, 4, 5));
    printf("avg of 5, 10, 15 = %f\n", getAvg(3, 5, 10, 15));
    return 0;
}
