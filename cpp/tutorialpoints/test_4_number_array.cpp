#include <iostream>
using namespace std;

#include <iomanip>
using std::setw;

#include <cmath>

#include <ctime>
#include <cstdlib>

double getAverage(int arr[], int size);
int * getRandom();

int main()
{ 
/* == Numbers in C++==
 * primitive data types
 */
    // number definition
    short  s;
    int    i;
    long   l;
    float  f;
    double d;

    // number assignment
    s = 10;
    i = 1000;
    l = 1000000;
    f = 230.47;
    d = 30949.374;

    // number printing
    cout << "short  s  : " << s << endl;
    cout << "int    i  : " << i << endl;
    cout << "long   l  : " << l << endl;
    cout << "float  f  : " << f << endl;
    cout << "double d  : " << d << endl;
    cout << endl;

/* Math Operations in C++
 */
    // mathematical operations
    cout << "sin(d)    :" << sin(d) << endl;
    cout << "abs(i)    :" << abs(i) << endl;
    cout << "floor(d)  :" << floor(d) << endl;
    cout << "sqrt(f)   :" << sqrt(f) << endl;
    cout << "pow(d, 2) :" << pow(d, 2) << endl;
    cout << endl;

/* Random Numbers in C++
 * There are actually two functions you will need to know about random number generation.
 * The first is rand(), this function will only return a pseudo random number.
 * The way to fix this is to first call the srand() function.
 */
    int x, y;

    // set the speed
    srand( (unsigned) time(NULL) );

    // generate 10 random numbers
    for (x = 0; x < 10; x++) {
        // generate actual random number
        y = rand();
        cout << "Random Number : " << y << endl;
    }

/* == C++ Arrays ==
 * C++ provides a data structure, the array, which stores a fixed-size sequential collection
 * of elements of the SAME type.
 * All arrays consist of contiguous memeory locations. The lowest address correspondes to
 * the first element and the highest address to the last element.
 *
 * Declaring Arrays:
 * single-dimension syntax: type arrayName [ arraySize ];
 * e.g.
 * double balance[10];
 *
 * Initializing Arrays:
 * e.g.
 * double balance[5] = {1000.0, 2.0, 3.4, 17.0, 50.0};
 * double balance[] = {1000.0, 2.0}; // auto size, just big enough to hold what's given
 *
 * Acessing Array Elements:
 * e.g.
 * double salary = balance[9];
 */
    int n[10];
    cout << n << endl;

    //init element of array n to 0
    for (int i = 0; i < 10; i++) {
        n[i] = i + 100; // set element at location i to i + 100
    }

    cout << "Element" << setw(13) << "Value" << endl;

    // output each array element's value
    for (int j = 0; j < 10; j++) {
        cout << setw(7) << j << setw(13) << n[j] << endl;
    }

/* C++ Multi-dimensional Arrays
 * syntax: type name[size1][size2]...[sizeN];
 * e.g.
 * int threedim[5][10][4];
 */
    /* Initializing */
    int a[3][4] = {
        {0, 1, 2, 3},
        {4, 5, 6, 7},
        {8, 9, 10, 11}
    };
    // same as >>>
    // int a[3][4] = {0,1,2,3,4,5,6,7,8,9,10,11};
    // <<<

    /* Acessing Array Element */
    int val = a[2][3];

    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 4; j++) {
            cout << "a[" << i << "][" << j << "]: ";
            cout << a[i][j] << endl;
        }
    }

/* C++ Pointer to an Array
 * An array name is a constant pointer to the first element of the array.
 */

    double balance[5] = {1000.0, 2.0, 3.4, 4.0, 555};
    double *p;
    // balance is a pointer to &balance[0]

    p = balance;
    /* &: returns the address of an variable, &var will give the actual address of the var */
    /* *: pointer to a var, *var will pointer to a variable var. */
    cout << "balance : " << balance << endl;
    cout << "&balance: " << &balance << endl;
    cout << "p       : " << p << endl;
    cout << "&p      : " << &p << endl;
    cout << "*p      : " << *p << endl;

    cout << "Array values using pointer " << endl;
    for (int i = 0; i < 5; i++) {
        cout << "*(p + " << i << ") : ";
        cout << *(p + i) << endl;
    }

    cout << "Array values using balance as address" << endl;
    for (int i = 0; i < 5; i++) {
        cout << "*(balance + " << i << ") : ";
        cout << *(balance + i) << endl;
    }

/* C++ Passing arrays to functions
 * C++ doesn't allow to pass an entire array as an argument to a function.
 * However, you can pass a pointer to an array by specifying the array's name
 * without an index.
 */

    /* Way-1: Formal param as a pointer */
    // e.g.
    // void myFunction(int *param) {...};

    /* Way-2: Formal param as a sized array */
    // e.g.
    // void myFunction(int param[10]) {...};

    /* Way-3: Formal param as a unsized array*/
    // e.g.
    // void myFunction(int param[]) {...};

    int array[5] = {1000, 2, 3, 17, 50};
    double avg;

    avg = getAverage(array, 5);

    cout << "Average value is : " << avg << endl;

/* C++ Return array from functions in C++
 * C++ doesn't allow to return an entire array from a function.
 * However, you can return a pointer to an array by specifying the array's name
 * without an index.
 */
    // return a single-dimesnsion array
    // e.g.
    // int * myFunction(...) {...}
    // ==> Note that C++ doesn't advocate to return a address of a local variable
    // to outside of the function. So you would have to define the local var as 'static' var.

    int *ptr;

    ptr = getRandom();
    for (int i = 0; i < 10; i++) {
        cout << "*(ptr + " << i << ") : ";
        cout << *(ptr + i) << endl;
    }
 

    return 0;
}


double getAverage(int arr[], int size) {
    int    i, sum = 0;
    double avg;

    for (i = 0; i < size; i++) {
        sum += arr[i];
    }

    avg = double(sum) / size;

    return avg;
}

int * getRandom() {
    // static var as it will be returned to outside of the function
    static int r[10];

    // set the speed
    srand( (unsigned) time(NULL) );
    for (int i = 0; i < 10; i++) {
        r[i] = rand();
        cout << "Generate random num: " << r[i] << endl;
    }

    return r;
}
